"""Discovery only: add individual witness-conflicting color/lineage cells.
An OUT excursion may invalidate every untracked fact; proposed cells are therefore
only heuristics, never proof premises. Every result comes from a freshly built sound model.
CLI source target x y h qx qy prefix rounds
"""
from pathlib import Path
import json,sys,subprocess,os
ROOT=Path(__file__).resolve().parent; W=ROOT.parent/'word_stabilization'
row=tuple(map(int,sys.argv[1:8]));prefix=Path(sys.argv[8]); rounds=int(sys.argv[9]);prefix.parent.mkdir(parents=True,exist_ok=True)
Hfile=ROOT/'producer_labels_hypothesis_202.tsv';Sfile=W/'dcv_anchored_signed102.tsv'
H={tuple(map(int,l.split()))for l in Hfile.read_text().splitlines()};F={tuple(map(int,l.split()[:5]))for l in(W/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for p in [W/'dcv_protected_patch2_kernel.tsv',Sfile]for l in p.read_text().splitlines()}
G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];M=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words'];D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,z):return p[0]+z[0],p[1]+z[1]
def trace(w):
 p=(0,0);h=0;req={};odd=set()
 for c in w:
  req.setdefault(p,c=='L');odd.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h])
 return req,odd
R=[trace(m['word']+m['end_marker'])[0]for m in M];O=[trace(m['word'])[1]for m in M]
def run(cmd,out):
 z=subprocess.run(list(map(str,cmd)),cwd=ROOT,text=True,capture_output=True,env={**os.environ,'PRODUCER_LABEL_ALLOW_WIDE':'1'});Path(str(out)+'.txt').write_text(z.stdout);Path(str(out)+'.log').write_text(z.stderr)
 return z.stdout
points=set();watched=[(-1,-1)];results=[]
for rnd in range(rounds):
 p=Path(str(prefix)+f'_r{rnd:02d}');pf=Path(str(p)+'_points.json');pf.write_text(json.dumps(sorted(points)));b=Path(str(p)+'_base');e=Path(str(p)+'_exact');q=Path(str(p)+'_quotient')
 run(['python','generate_protected_transfer_patch_custom.py',*row,b,'sourceplus:'+str(pf)],str(b)+'_gen')
 run(['python','add_protected_producer_labels.py',str(b)+'.json',e,Hfile,';'.join(','.join(map(str,c))for c in watched),Sfile],str(e)+'_gen')
 run(['python','quotient_protected_producer_labels.py',str(e)+'.json',q],str(q)+'_gen')
 J=json.loads(Path(str(q)+'.json').read_text());res=run(['./protected_patch_bdd_labels',str(q)+'.dat',3000000,str(q)+'.bdd'],q);entry={'round':rnd,'points':sorted(points),'watched':watched.copy(),'variables':J['n'],'result':res.strip(),'prefix':str(q)};results.append(entry);Path(str(prefix)+'_summary.json').write_text(json.dumps(results,indent=2));print(entry,flush=True)
 if 'EXHAUSTED_NO_HIT'in res:
  entry['verification']=run(['python','verify_protected_patch_bdd_labels.py',str(q)+'.dat',str(q)+'.bdd'],str(q)+'_verify').strip();break
 if 'ABSTRACT_WITNESS'not in res:break
 wr=run(['./protected_patch_bdd_labels_witness_v2',str(q)+'.dat',3000000],str(q)+'_witness');path=[]
 for line in wr.splitlines():
  if line.startswith('WITNESS '):
   pos,col,a=map(int,line.split()[1:]);path.append({'pose':J['poses'][pos]if pos<J['out']else None,'color':col,'packet_id':a})
 if not path:entry['stop']='witness reconstruction failed';break
 Path(str(q)+'_witness.json').write_text(json.dumps(path,indent=2));patch={tuple(c)for c in J['points']};labels={tuple(c):(row[0],slot,(0,0),0,-1)for slot,c in enumerate(G[row[0]]['outputs'])};known={c:int(v^(c in O[row[0]]))for c,v in R[row[0]].items()};events=[];conflicts=[]
 for step,st in enumerate(path):
  if st['pose']is None:continue
  x,y,h=st['pose'];p0=(x,y);a=st['packet_id'];world=lambda c:add(p0,rot(c,h))
  for c,v in R[a].items():
   cell=world(c)
   if cell in known and known[cell]!=v:conflicts.append({'cell':cell,'step':step,'kind':'color'})
  for slot,c in enumerate(G[a]['inputs']):
   cell=world(c)
   if cell in labels:
    aa,ss,pp,hh,born=labels[cell];rel=rot((x-pp[0],y-pp[1]),-hh);r=(aa,a,*rel,(h-hh)%4,*G[aa]['outputs'][ss]);signed=r[:5]in F or r in FP;hyp=r in H and not(born==-1 and step==len(path)-1)
    if signed or hyp:events.append({'cell':cell,'step':step,'source_step':born,'row':r,'signed':signed,'kind':'lineage'})
  context={world(c)for c in R[a]};labels={c:l for c,l in labels.items()if c not in context}
  for slot,c in enumerate(G[a]['outputs']):labels[world(c)]=(a,slot,p0,h,step)
  for c,v in R[a].items():known[world(c)]=v
  for c in O[a]:known[world(c)]^=1
 entry['events']=events;entry['conflicts']=conflicts
 eligible=[ev for ev in events if tuple(ev['cell'])not in watched]; eligible.sort(key=lambda ev:(not ev['signed'],ev['step']))
 if eligible:
  chosen=eligible[0];cell=tuple(chosen['cell']);watched.append(cell);points.add(cell);entry['chosen']=chosen
 else:
  eligible=[ev for ev in conflicts if tuple(ev['cell'])not in patch];eligible.sort(key=lambda ev:(ev['step'],sum(abs(z)for z in ev['cell'])))
  if not eligible:entry['stop']='no new individual cell';break
  chosen=eligible[0];points.add(tuple(chosen['cell']));entry['chosen']=chosen
 Path(str(prefix)+'_summary.json').write_text(json.dumps(results,indent=2))
Path(str(prefix)+'_summary.json').write_text(json.dumps(results,indent=2))
