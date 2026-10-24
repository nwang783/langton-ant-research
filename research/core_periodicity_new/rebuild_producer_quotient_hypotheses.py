"""Keep a frozen producer partition, weaken its predicates to a new H family.
CLI QUOTIENT.json PREFIX H.tsv. Reject a class only when EVERY member is forbidden.
"""
from pathlib import Path
import json,sys,hashlib
inp=Path(sys.argv[1]);out=Path(sys.argv[2]);hyp=Path(sys.argv[3]);J=json.loads(inp.read_text());B=json.loads(Path(J['base_model_file']).read_text());W=Path('/workspace/shared/langton/word_stabilization');G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];M=json.loads((W/'seven_sub_dcv_port_quotient.json').read_text())['macro_words'];F={tuple(map(int,l.split()[:5]))for l in(W/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for p in[W/'dcv_protected_patch2_kernel.tsv',Path(J['extra_guard_file'])]for l in p.read_text().splitlines()};H={tuple(map(int,l.split()))for l in hyp.read_text().splitlines()};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];labels=J['producer_label_classes'];n=J['n'];start=J['start']
for L in labels:
 q=L['cell']
 for cl in L['classes']:
  sig=[]
  if all(lab is not None for lab in cl['members']):
   for ii,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
    x,y,h=B['poses'][sid];z=rot((q[0]-x,q[1]-y),-h)
    if list(z)not in G[a]['inputs']:continue
    forbids=[]
    for lab in cl['members']:
     px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']]);forbids.append(row[:5]in F or row in FP or(row in H and(not goal or not lab['outer_origin'])))
    if all(forbids):sig.append(ii)
  cl['rejected_transitions']=sig

def complement_cubes(bad,bits):
 def rec(i,k,v,bs):
  if not bs:return[(k,v)]
  if i==bits:return[]
  bit=1<<i;return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
T=[]
for ti,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
 x,y,h=B['poses'][sid];cubes=[(k,v)];resetmask=resetvalue=0
 for L in labels:
  q=L['cell'];off=L['offset'];bits=L['bits'];z=rot((q[0]-x,q[1]-y),-h);bad={ci for ci,cl in enumerate(L['classes'])if ti in cl['rejected_transitions']}
  if bad:cubes=[(kk|(ck<<off),vv|(cv<<off))for kk,vv in cubes for ck,cv in complement_cubes(bad,bits)]
  if z in C[a]:resetmask|=((1<<bits)-1)<<off
  if list(z)in G[a]['outputs']:
   matches=[i for i,lab in enumerate(L['exact_codes'])if i and not lab['outer_origin']and lab['packet']==a and lab['slot']==G[a]['outputs'].index(list(z))and lab['pose']==[x,y,h]];assert len(matches)==1;val=L['exact_codes_to_class'][matches[0]];resetmask|=((1<<bits)-1)<<off;resetvalue|=val<<off
 for kk,vv in cubes:T.append([sid,to,kk,vv,f,resetmask,resetvalue,goal,a])
new=dict(J);new.update(transitions=T,producer_label_classes=labels,partition_source_file=str(inp),partition_source_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),candidate_hypothesis_file=str(hyp),candidate_hypothesis_sha256=hashlib.sha256(hyp.read_bytes()).hexdigest(),candidate_hypotheses=[list(r)for r in sorted(H)]);out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {B['out']+1} {len(T)} {len(B['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,B['reentry']))+'\n')
print(json.dumps({'variables':n,'hypotheses':len(H),'transitions':len(T)}))
