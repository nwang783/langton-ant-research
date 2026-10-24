"""Intersect a forward patch/producer graph with backward suffix-avoidance flags.
CLI FORWARD.json PREFIX H.tsv SIGNED.tsv. Nine-field guarded-XOR-reset output.
Flag1 means every later strict complete context avoids its cell. Starts unknown,
ends1; a touching packet requires before0 and permits after0/1 unless forbidden.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
inp=Path(sys.argv[1]);out=Path(sys.argv[2]);hyp=Path(sys.argv[3]);signed=Path(sys.argv[4]);J=json.loads(inp.read_text());profile,data,profile_meta=load_profile(J['resource_profile_file']);assert all(J.get(k)==v for k,v in profile_meta.items());G=data['geometry']['geometry'];M=data['macro_words']['macro_words'];F=data['ordinary'];FP=data['protected']|{tuple(map(int,l.split()[:7]))for l in signed.read_text().splitlines()if l.strip()};H={tuple(map(int,l.split()[:7]))for l in hyp.read_text().splitlines()if l.strip()};D=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def trace(w):
 p=(0,0);h=0;seen=set()
 for c in w:
  seen.add(p);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return seen
C=[trace(m['word']+m['end_marker'])for m in M];tx,ty,th=J['target_pose'];target=J['target'];n=J['n'];Q=[]
for z in G[target]['inputs']:
 zz=rot(z,th);q=(tx+zz[0],ty+zz[1])
 if list(q)!=J['protected_q']:Q.append(q)
assert all(list(q)in J['points']for q in Q);assert n+len(Q)<=50;flags=((1<<len(Q))-1)<<n;T=[];branches=[]
for ti,t in enumerate(J['transitions']):
 if len(t)==7:sid,to,k,v,f,goal,a=t;clear=reset=0
 elif len(t)==8:sid,to,k,v,f,clear,goal,a=t;reset=0
 else:sid,to,k,v,f,clear,reset,goal,a=t
 if goal:T.append([sid,to,k|flags,v|flags,f,clear,reset,goal,a]);branches.append({'forward_transition':ti,'outer_goal':True,'after_flags':{}});continue
 x,y,h=J['poses'][sid];rel=rot((tx-x,ty-y),-h);parts=[(k,v,clear,reset,{})]
 for j,q in enumerate(Q):
  bit=1<<(n+j);qp=rot((q[0]-x,q[1]-y),-h);row=(a,target,*rel,(th-h)%4,*qp);forbid=row[:5]in F or row in FP or row in H;touch=qp in C[a];nparts=[]
  for kk,vv,cc,rr,meta in parts:
   if touch:
    for value in([0]if forbid else[0,1]):nparts.append((kk|bit,vv,cc|bit,rr|(value*bit),{**meta,str(j):value}))
   else:nparts.append((kk|bit if forbid else kk,vv,cc,rr,meta))
  parts=nparts
 for kk,vv,cc,rr,meta in parts:T.append([sid,to,kk,vv,f,cc,rr,goal,a]);branches.append({'forward_transition':ti,'outer_goal':False,'after_flags':meta})
new=dict(J);new.update(n=n+len(Q),transitions=T,format='guarded_xor_reset_producer_prophecy_product_v1',prophecy_cells=Q,prophecy_offset=n,prophecy_branches=branches,forward_model_file=str(inp),forward_model_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),prophecy_signed_file=str(signed),prophecy_signed_sha256=hashlib.sha256(signed.read_bytes()).hexdigest(),prophecy_hypothesis_file=str(hyp),prophecy_hypothesis_sha256=hashlib.sha256(hyp.read_bytes()).hexdigest(),prophecy_hypotheses=[list(r)for r in sorted(H)],candidate_hypotheses=[list(r)for r in sorted(H|{tuple(r)for r in J.get('candidate_hypotheses',[])})]);out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{new['n']} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,J['start']))+'\n')
 for row in T:f.write(' '.join(map(str,row))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':new['n'],'prophecy_cells':Q,'transitions':len(T),'hypotheses':len(new['candidate_hypotheses'])}))
