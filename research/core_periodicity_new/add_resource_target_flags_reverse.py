"""Reverse exact patch graph, then track suffix-untouched target input cells.
CLI BASE.json PREFIX H.tsv [SIGNED.tsv]. Hypotheses never filter outer-source goal.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
base=Path(sys.argv[1]);out=Path(sys.argv[2]);hyp=Path(sys.argv[3]);extra=Path(sys.argv[4]);J=json.loads(base.read_text());profile,data,profile_meta=load_profile(J['resource_profile_file']);assert all(J.get(k)==v for k,v in profile_meta.items());G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in extra.read_text().splitlines()if l.strip()};H={tuple(map(int,l.split()[:7]))for l in hyp.read_text().splitlines()if l.strip()};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];tx,ty,th=J['target_pose'];b=J['target'];n=J['n'];Q=[]
for z in G[b]['inputs']:
 r=rot(z,th);q=(tx+r[0],ty+r[1])
 if list(q)!=J['protected_q']:Q.append(q)
assert all(list(q)in J['points']for q in Q)
T=[];goal=None;stats={'signed_filtered_flags':0,'hypothesis_filtered_flags':0}
for sid,to,k,v,flip,g,a in J['transitions']:
 if g:assert goal is None;goal=(sid,k,v);continue
 x,y,h=J['poses'][sid];vv=v^(flip&k);clear=0;rel=rot((tx-x,ty-y),-h)
 for j,q in enumerate(Q):
  bit=1<<(n+j);local=rot((q[0]-x,q[1]-y),-h);row=(a,b,*rel,(th-h)%4,*local)
  if row in FP or row in H:k|=bit;stats['signed_filtered_flags'if row in FP else'hypothesis_filtered_flags']+=1
  if local in C[a]:clear|=bit
 T.append([to,sid,k,vv,flip,clear,0,a])
for r in J['reentry']:T.append([r,J['out'],0,0,0,0,0,99])
sp,sk,sv=J['start'];T.append([sp,sp,sk,sv,0,0,1,100]);assert goal is not None;gp,gk,gv=goal;flags=((1<<len(Q))-1)<<n;start=[gp,gk|flags,gv|flags]
new=dict(J);new.update(n=n+len(Q),base_n=n,target_flag_cells=Q,start=start,transitions=T,format='guarded_xor_clear_reverse_target_v1',out=J['out']+1,reentry=[],base_model_file=str(base),base_model_sha256=hashlib.sha256(base.read_bytes()).hexdigest(),extra_guard_file=str(extra),extra_guard_sha256=hashlib.sha256(extra.read_bytes()).hexdigest(),candidate_hypothesis_file=str(hyp),candidate_hypothesis_sha256=hashlib.sha256(hyp.read_bytes()).hexdigest(),candidate_hypotheses=[list(r)for r in sorted(H)],target_flag_stats=stats)
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{new['n']} {new['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,start))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write('\n')
print(json.dumps({'variables':new['n'],'target_flags':Q,'positions':new['out']+1,'transitions':len(T),'stats':stats,'hypotheses':len(H)}))
