"""Discovery: literal-profile producer-label CEGAR with checkable no-hit artifacts.
Every round is a newly generated conservative abstraction. H remains conditional.
Default watched cell is the protected token (uninformative, but harmless).
Only complete-context-protected in-patch lineage events guide label selection.
"""
from pathlib import Path
import argparse,json,subprocess,os,time
from resource_profile import load_profile
p=argparse.ArgumentParser();p.add_argument('--profile',required=True);p.add_argument('--hypotheses',required=True);p.add_argument('--signed',required=True);p.add_argument('--row',nargs=7,type=int,required=True);p.add_argument('--prefix',required=True);p.add_argument('--rounds',type=int,default=8);p.add_argument('--cap',type=int,default=1500000);p.add_argument('--mode',default='source');p.add_argument('--watch',default='');p.add_argument('--scope');p.add_argument('--expand',action='store_true');A=p.parse_args()
ROOT=Path(__file__).resolve().parent;prefix=Path(A.prefix).resolve();prefix.parent.mkdir(parents=True,exist_ok=True);profile,data,pm=load_profile(A.profile);G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in Path(A.signed).read_text().splitlines()if l.strip()};H={tuple(map(int,l.split()[:7]))for l in Path(A.hypotheses).read_text().splitlines()if l.strip()};row=A.row;D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,z):return p[0]+z[0],p[1]+z[1]
def trace(w):
 p=(0,0);h=0;req={};odd=set()
 for c in w:req.setdefault(p,c=='L');odd.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h])
 return req,odd
R=[trace(m['word']+m['end_marker'])[0]for m in M];O=[trace(m['word'])[1]for m in M]
def run(cmd,out):
 z=subprocess.run(list(map(str,cmd)),cwd=ROOT,text=True,capture_output=True,env={**os.environ,'PRODUCER_LABEL_ALLOW_WIDE':'1'});Path(str(out)+'.txt').write_text(z.stdout);Path(str(out)+'.log').write_text(z.stderr)
 if z.returncode and not z.stdout.startswith('status CAP_OR_ERROR'):raise RuntimeError(' '.join(map(str,cmd))+'\n'+z.stderr[-3000:])
 return z.stdout
watched=[tuple(map(int,c.split(',')))for c in A.watch.split(';')if c]or[tuple(row[-2:])];extras=set();results=[]
def save():Path(str(prefix)+'_summary.json').write_text(json.dumps({'scope':'Conditional discovery only; H is not a signed relation','args':vars(A),'results':results},indent=2))
for rnd in range(A.rounds):
 t=time.time();pr=Path(str(prefix)+f'_r{rnd:02d}');b=Path(str(pr)+'_base');e=Path(str(pr)+'_exact');q=Path(str(pr)+'_quotient');mode=A.mode
 if extras:
  assert mode in ('source','both');pf=Path(str(pr)+'_extra.json');pf.write_text(json.dumps(sorted(extras)));mode+='plus:'+str(pf)
 run(['python',ROOT/'generate_resource_transfer_patch.py',A.profile,*row,b,mode],str(b)+'_gen')
 run(['python',ROOT/'add_resource_producer_labels.py',A.profile,str(b)+'.json',e,A.hypotheses,';'.join(','.join(map(str,c))for c in watched),A.signed],str(e)+'_gen')
 if A.scope:run(['python',ROOT/'quotient_resource_scoped_producers.py',str(e)+'.json',q,A.scope],str(q)+'_gen')
 else:run(['python',ROOT/'quotient_resource_producer_labels.py',str(e)+'.json',q],str(q)+'_gen')
 J=json.loads(Path(str(q)+'.json').read_text());res=run([ROOT/'protected_patch_bdd_labels_witness_v2',str(q)+'.dat',A.cap,str(q)+'.bdd'],q);entry={'round':rnd,'extra_points':sorted(extras),'watched':watched.copy(),'variables':J['n'],'result':res.splitlines()[0]if res else'NO_OUTPUT','prefix':str(q),'seconds':round(time.time()-t,3)};results.append(entry);save();print(row,entry,flush=True)
 if 'CAP_OR_ERROR'in res:
  res=run([ROOT/'protected_patch_bdd_labels',str(q)+'.dat',A.cap,str(q)+'.bdd'],str(q)+'_closure');entry['closure_result']=res.strip();save()
 if 'EXHAUSTED_NO_HIT'in res:
  entry['verification']=run(['python',ROOT/'verify_protected_patch_bdd_labels.py',str(q)+'.dat',str(q)+'.bdd'],str(q)+'_verify').strip();save();break
 if 'WITNESS 'not in res:entry['stop']='no reconstructed witness';save();break
 path=[]
 for line in res.splitlines():
  if line.startswith('WITNESS '):
   pos,col,a=map(int,line.split()[1:]);path.append({'pose':J['poses'][pos]if pos<J['out']else None,'color':col,'packet_id':a})
 Path(str(q)+'_witness.json').write_text(json.dumps(path,indent=2));patch={tuple(c)for c in J['points']};labels={tuple(c):(row[0],slot,(0,0),0,-1)for slot,c in enumerate(G[row[0]]['outputs'])if tuple(c)in patch};events=[]
 for step,st in enumerate(path):
  if st['pose']is None:continue # OUT cannot touch ANY patch cell.
  x,y,h=st['pose'];p0=(x,y);a=st['packet_id'];world=lambda c:add(p0,rot(c,h))
  for slot,c in enumerate(G[a]['inputs']):
   cell=world(c)
   if cell in labels:
    aa,ss,pp,hh,born=labels[cell];rel=rot((x-pp[0],y-pp[1]),-hh);r=(aa,a,*rel,(h-hh)%4,*G[aa]['outputs'][ss]);signed=r[:5]in F or r in FP;hyp=r in H and not(born==-1 and step==len(path)-1)
    if signed or hyp:events.append({'cell':cell,'step':step,'source_step':born,'row':r,'signed':signed,'kind':'lineage'})
  context={world(c)for c in R[a]};labels={c:l for c,l in labels.items()if c not in context}
  for slot,c in enumerate(G[a]['outputs']):
   cell=world(c)
   if cell in patch:labels[cell]=(a,slot,p0,h,step)
 entry['events']=events;eligible=[ev for ev in events if tuple(ev['cell'])not in watched];eligible.sort(key=lambda ev:(not ev['signed'],ev['step'],ev['source_step']))
 if eligible:
  chosen=eligible[0];watched.append(tuple(chosen['cell']));entry['chosen']=chosen
 elif A.expand and A.mode in ('source','both'):
  # Outside-color suggestions are purely geometric. No outside provenance is trusted.
  goalcells={add(tuple(row[2:4]),rot(c,row[4]))for c in G[row[1]]['inputs']};new=goalcells-patch
  if not new:entry['stop']='no eligible internal lineage or new target-input cell';save();break
  extras|=new;entry['expanded_target_inputs']=sorted(new)
 else:entry['stop']='no eligible internal lineage cell';save();break
 save()
