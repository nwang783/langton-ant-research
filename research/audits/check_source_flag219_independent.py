from pathlib import Path
import json,hashlib,sys
from check_protected_patch_model_independent import main as check_base,walk,raws,mark,rotation,xy
P=Path(__file__).resolve().parents[1];W=P/'word_stabilization';A=P/'audits';R=A/'source_flag_replays';R.mkdir(exist_ok=True)
cases=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers']
accepted=[6,8,9,10,11,13,25,29,32,37,38,57,58,59,60,61,63,64,65,66,67,68,*range(45,57),69,27,34]
def tup(c):return(c['source_packet'],c['target_packet'],*c['target_pose'],*c['source_output'])
offlist=(1,0,2,2,0,2,3);signed38={tup(cases[i-1])for i in accepted}|{offlist};assert len(signed38)==38
signed36=signed38-{tup(cases[i-1])for i in [27,34]}
def readrel(path):return{tuple(map(int,l.split()[:7]))for l in path.read_text().splitlines()}
assert readrel(W/'dcv_anchored_signed38.tsv')==signed38
assert readrel(W/'dcv_anchored_signed36.tsv')==signed36
baseprotected=readrel(W/'dcv_protected_patch2_kernel.tsv');signed40=signed38|{tup(cases[i-1])for i in [26,30]};assert readrel(W/'dcv_anchored_signed40.tsv')==signed40;prior=baseprotected|signed36
results=[]
for case in [219]:
 src=W/'dcv_direct_source_flags40/candidate219.json';data=json.loads(src.read_text());n=data['base_n'];mask=(1<<n)-1
 assert(data['source'],data['target'],*data['target_pose'],*data['protected_q'])==(6,4,-3,0,1,0,0);assert (6,4,-3,0,1,0,0)not in {tup(c)for c in cases}
 s=data['source'];end,dh,first,flips=walk(raws[s]);context=walk(raws[s]+mark)[2];core={p for p,b in walk(mark)[2].items()if b};entry={p for p,b in context.items()if b};outputs=(entry^flips)-{end+rotation(p,dh)for p in core}
 q=complex(*data['protected_q']);Q=sorted(outputs-{q},key=xy);assert data['source_flag_cells']==[list(xy(p))for p in Q]
 assert all(list(xy(p))in data['points']for p in Q) and data['n']==n+len(Q)
 extra=Path(data['extra_guard_file']);hyp=Path(data['candidate_hypothesis_file']);hyp=hyp if hyp.is_absolute()else P/hyp
 assert readrel(extra)==signed36 and readrel(hyp)==signed40
 for field,path in [('extra_guard_sha256',extra),('candidate_hypothesis_sha256',hyp)]:assert data[field]==hashlib.sha256(path.read_bytes()).hexdigest()
 flags=((1<<len(Q))-1)<<n;sp,sk,sv=data['start'];assert sk&flags==flags and sv&flags==flags
 original=dict(data,n=n,start=[sp,sk&mask,sv&mask]);orig=[]
 for sid,to,k,v,f,clear,g,a in data['transitions']:
  x,y,h=data['poses'][sid];ctx=walk(raws[a]+mark)[2];wantk=k&mask;wantclear=0
  for j,p in enumerate(Q):
   flag=1<<(n+j);key=(s,a,x,y,h,*xy(p))
   if key in prior or(not g and key in signed40):wantk|=flag
   if rotation(p-complex(x,y),-h)in ctx:wantclear|=flag
  assert k==wantk and clear==wantclear and v&~mask==0 and f&~mask==0
  orig.append([sid,to,k&mask,v,f,g,a])
 original['transitions']=orig
 b=R/f'case{case}_base.json';b.write_text(json.dumps(original))
 lines=[f"{n} {data['out']+1} {len(orig)} {len(data['reentry'])}",' '.join(map(str,original['start']))]+[' '.join(map(str,t))for t in orig]+[' '.join(map(str,data['reentry']))]
 b.with_suffix('.dat').write_text('\n'.join(lines)+'\n');check_base(b)
 # Exact integer flag graph serialization.
 lines=[f"{data['n']} {data['out']+1} {len(orig)} {len(data['reentry'])}",' '.join(map(str,data['start']))]+[' '.join(map(str,t))for t in data['transitions']]+[' '.join(map(str,data['reentry']))]
 assert src.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 results.append({'case':case,'status':'PASS independent literal base and source-output flag reconstruction','flags':[list(xy(p))for p in Q],'variables':data['n'],'invariant':json.loads((A/'protected_patch_replays/candidate219_signed40.invariant_check.json').read_text()),'sha256':{str(src.with_suffix(s).relative_to(P)):hashlib.sha256(src.with_suffix(s).read_bytes()).hexdigest()for s in ['.json','.dat']}})
out={'status':'PASS signed-premise source flags; no mutual hypotheses needed','cases':results,'controls':json.loads((A/'bdd_clear_checker_controls_independent.json').read_text())}
(A/'source_flags219_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
