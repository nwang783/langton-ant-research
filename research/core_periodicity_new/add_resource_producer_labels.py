"""Add conservative producer labels at selected fixed patch cells.
CLI BASE.json PREFIX H.tsv 'x,y;x,y' [SIGNED.tsv].
H is an UNPROVED mutual-induction hypothesis, used only at smaller gaps.
Edge format: from,to,guardmask,guardvalue,xor,resetmask,resetvalue,goal,packet.
"""
from pathlib import Path
import hashlib,json,sys,itertools,os
from resource_profile import load_profile
profile,data,profile_meta=load_profile(sys.argv.pop(1));base=Path(sys.argv[1]);out=Path(sys.argv[2]);hyp=Path(sys.argv[3]);Q=[tuple(map(int,t.split(',')))for t in sys.argv[4].split(';')];extra=Path(sys.argv[5]);J=json.loads(base.read_text());assert all(J.get(k)==v for k,v in profile_meta.items());G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in extra.read_text().splitlines()if l.strip()};H={tuple(map(int,l.split()[:7]))for l in hyp.read_text().splitlines()if l.strip()};assert len(set(Q))==len(Q) and all(list(q)in J['points']for q in Q)
D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,z):return p[0]+z[0],p[1]+z[1]
def sub(p,z):return p[0]-z[0],p[1]-z[1]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=add(p,D[h])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];source=J['source'];n=J['n'];maps=[];start=list(J['start']);stats={'signed_rejected_codes':0,'hypothesis_rejected_codes':0,'goal_hypothesis_rejected_codes':0};labels=[]
for q in Q:
 # A code has an exact producer pose recovered geometrically from this fixed cell.
 L=[None];code={}
 for a in J['keep']:
  for slot,z in enumerate(G[a]['outputs']):
   for h in range(4):
    p=sub(q,rot(z,h))
    if(sum(p)+h)%2:continue
    code[a,slot,h]=len(L);L.append({'packet':a,'slot':slot,'heading':h,'pose':[*p,h],'outer_origin':False})
 outer=0
 if list(q)in G[source]['outputs']:
  outer=len(L);L.append({'packet':source,'slot':G[source]['outputs'].index(list(q)),'heading':0,'pose':[0,0,0],'outer_origin':True})
 bits=(len(L)-1).bit_length();mask=((1<<bits)-1)<<n;start[1]|=mask;start[2]|=outer<<n
 labels.append({'cell':q,'offset':n,'bits':bits,'codes':L,'outer_code':outer});maps.append(code);n+=bits
assert n<=50 or os.environ.get("PRODUCER_LABEL_ALLOW_WIDE")=="1", "Use explicit wide preparation only before quotienting; the exact engine has a 50-variable cap"

def complement_cubes(bad,bits):
 # Disjoint cubes partition ALL bit patterns except the prohibited exact codes.
 def rec(i,k,v,bs):
  if not bs:return[(k,v)]
  if i==bits:return[]
  bit=1<<i
  return rec(i+1,k|bit,v,[x for x in bs if not x&bit])+rec(i+1,k|bit,v|bit,[x for x in bs if x&bit])
 return rec(0,0,0,list(bad))
T=[]
for sid,to,k,v,f,goal,a in J['transitions']:
 x,y,h=J['poses'][sid];p=(x,y);cubes=[(k,v)];resetmask=resetvalue=0
 for j,q in enumerate(Q):
  L=labels[j];off=L['offset'];bits=L['bits'];z=rot(sub(q,p),-h);bad=set()
  if list(z)in G[a]['inputs']:
   for code,lab in enumerate(L['codes']):
    if not code:continue
    pp=lab['pose'][:2];hh=lab['heading'];rel=rot(sub(p,pp),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']]);signed=row[:5]in F or row in FP;induct=row in H and(not goal or not lab['outer_origin'])
    if signed or induct:
     bad.add(code);stats['signed_rejected_codes'if signed else'hypothesis_rejected_codes']+=1
     if induct and goal:stats['goal_hypothesis_rejected_codes']+=1
  if bad:
   cs=complement_cubes(bad,bits);cubes=[(kk|(ck<<off),vv|(cv<<off))for kk,vv in cubes for ck,cv in cs]
  if z in C[a]:resetmask|=((1<<bits)-1)<<off
  if list(z)in G[a]['outputs']:
   resetmask|=((1<<bits)-1)<<off;resetvalue|=maps[j][a,G[a]['outputs'].index(list(z)),h]<<off
 for kk,vv in cubes:T.append([sid,to,kk,vv,f,resetmask,resetvalue,goal,a])
new=dict(J);new.update(n=n,base_n=J['n'],producer_labels=labels,start=start,transitions=T,format='guarded_xor_reset_v1',base_model_file=str(base),base_model_sha256=hashlib.sha256(base.read_bytes()).hexdigest(),extra_guard_file=str(extra),extra_guard_sha256=hashlib.sha256(extra.read_bytes()).hexdigest(),candidate_hypothesis_file=str(hyp),candidate_hypothesis_sha256=hashlib.sha256(hyp.read_bytes()).hexdigest(),candidate_hypotheses=[list(r)for r in sorted(H)],producer_label_stats=stats)
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':n,'label_cells':Q,'positions':J['out']+1,'transitions':len(T),'stats':stats,'hypotheses':len(H)}))
