"""Verify a whole frozen companion-source family before signing any member.
Independent literal geometry uses the audit-side builder; invariants use a separate C++ implementation.
"""
from pathlib import Path
import json,hashlib,subprocess
from check_protected_patch_model_independent import main as check_base,walk,raws,mark,rotation,xy
P=Path(__file__).resolve().parents[1];W=P/'word_stabilization';A=P/'audits';R=A/'mutual_source_flag_replays';R.mkdir(exist_ok=True)
family=W/'dcv_mutual_family';summary=json.loads((family/'summary.json').read_text());assert summary.get('stable') is True,'No stable family: nothing is proved by this driver.'
last=summary['stages'][-1];stage=family/f"stage{last['stage']:02}";hp=stage/'hypotheses.tsv'
def rel(p):return{tuple(map(int,l.split()[:7]))for l in p.read_text().splitlines()}
H=rel(hp);assert len(H)==last['active_count']==last['supported_count'];hdigest=hashlib.sha256(hp.read_bytes()).hexdigest();assert hdigest==last['hypotheses_sha256']
cases=json.loads((W/'dcv_conditional_confinement_optimized.json').read_text())['unproved_bad_transfers']
def tup(c):return(c['source_packet'],c['target_packet'],*c['target_pose'],*c['source_output'])
ids=[6,8,9,10,11,13,25,29,32,37,38,57,58,59,60,61,63,64,65,66,67,68,*range(45,57),69,27,34]
S={tup(cases[i-1])for i in ids}|{(1,0,2,2,0,2,3)};assert len(S)==38 and S<=H
S36=S-{tup(cases[i-1])for i in [27,34]};assert rel(W/'dcv_anchored_signed36.tsv')==S36
base=rel(W/'dcv_protected_patch2_kernel.tsv');prior=base|S36
assert hashlib.sha256((W/'dcv_protected_patch2_kernel.tsv').read_bytes()).hexdigest()=='395d31eb25954760bbf42520398eb18f510ab97fbee085da683fc9d6374f71ce'
assert hashlib.sha256((W/'seven_sub_dcv_star4_kernel.tsv').read_bytes()).hexdigest()=='51979b66632b81c04b1dd9dbcfa85bf6a6f759db953252e32040ba4605d80146'
rows={tuple(r['tuple']):r for r in last['results']};assert len(rows)==len(last['results']) and set(rows)==H-S
results=[]
for key,entry in sorted(rows.items()):
 assert entry['status']=='EXHAUSTED_NO_HIT';i=entry['candidate_index'];src=stage/f'candidate{i:03}.json';data=json.loads(src.read_text());n=data['base_n'];mask=(1<<n)-1
 assert(data['source'],data['target'],*data['target_pose'],*data['protected_q'])==key
 assert data['candidate_hypothesis_sha256']==hdigest and Path(data['candidate_hypothesis_file']).resolve()==hp.resolve()
 extra=Path(data['extra_guard_file']);assert rel(extra)==S36 and data['extra_guard_sha256']==hashlib.sha256(extra.read_bytes()).hexdigest()
 s=data['source'];end,dh,first,flips=walk(raws[s]);context=walk(raws[s]+mark)[2];core={p for p,b in walk(mark)[2].items()if b};entryblack={p for p,b in context.items()if b};outputs=(entryblack^flips)-{end+rotation(p,dh)for p in core}
 q=complex(*data['protected_q']);Q=sorted(outputs-{q},key=xy);assert data['source_flag_cells']==[list(xy(p))for p in Q]
 assert q in outputs and all(list(xy(p))in data['points']for p in outputs) and data['n']==n+len(Q)
 flags=((1<<len(Q))-1)<<n;sp,sk,sv=data['start'];assert sk&flags==flags and sv&flags==flags
 original=dict(data,n=n,start=[sp,sk&mask,sv&mask]);orig=[]
 for sid,to,k,v,f,clear,g,a in data['transitions']:
  x,y,h=data['poses'][sid];ctx=walk(raws[a]+mark)[2];wantk=k&mask;wantclear=0
  for j,p in enumerate(Q):
   bit=1<<(n+j);query=(s,a,x,y,h,*xy(p))
   if query in prior or(not g and query in H):wantk|=bit
   if rotation(p-complex(x,y),-h)in ctx:wantclear|=bit
  assert k==wantk and clear==wantclear and v&~mask==0 and f&~mask==0
  orig.append([sid,to,k&mask,v,f,g,a])
 original['transitions']=orig;b=R/f'candidate{i:03}_base.json';b.write_text(json.dumps(original))
 lines=[f"{n} {data['out']+1} {len(orig)} {len(data['reentry'])}",' '.join(map(str,original['start']))]+[' '.join(map(str,t))for t in orig]+[' '.join(map(str,data['reentry']))]
 b.with_suffix('.dat').write_text('\n'.join(lines)+'\n');check_base(b)
 lines=[f"{data['n']} {data['out']+1} {len(orig)} {len(data['reentry'])}",' '.join(map(str,data['start']))]+[' '.join(map(str,t))for t in data['transitions']]+[' '.join(map(str,data['reentry']))]
 assert src.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 cert=src.with_suffix('.bdd');out=R/f'candidate{i:03}.invariant_check.json'
 subprocess.run([str(A/'check_guarded_clear_bdd64_invariant_independent'),str(src.with_suffix('.dat')),str(cert),str(out)],check=True)
 results.append({'candidate_index':i,'tuple':key,'invariant_check':json.loads(out.read_text()),'sha256':{str(src.with_suffix(s).relative_to(P)):hashlib.sha256(src.with_suffix(s).read_bytes()).hexdigest()for s in ['.json','.dat','.bdd']}})
 onlist=[i for i,c in enumerate(cases,1)if tup(c)in H|{tup(cases[j-1])for j in [26,30]}];out={'status':'PARTIAL_NOT_SIGNED','stage':last['stage'],'hypotheses':len(H),'already_signed':len(S),'independently_checked_certificates':len(results),'previously_unsigned_clauses':len(H-(S|{tup(cases[j-1])for j in [26,30]}|{(6,4,-3,0,1,0,0)})),'on_original69_indices':onlist,'original69_not_excluded':69-len(onlist),'hypothesis_sha256':hdigest,'results':results}
 (A/'mutual_source_flag_family_independent.partial.json').write_text(json.dumps(out,indent=2))
out['status']='PASS entire simultaneous least-gap family'
(A/'mutual_source_flag_family_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='results'}))
