"""Two exact construction attempts, not a seed scan or route theorem.
1.Remove remote old ports from the signed20-cell feedback architecture.
2.Try one explicit outward four-turn S/T lap schema; keep its exact failure.
"""
from pathlib import Path
import json,sys,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
sys.path.insert(0,str(ROOT/'computability'))
from active_flight import DIR,rot,cursor,ends,comp,step
from periodic_tail_checker import first_mismatch,State
STD=ROOT/'recovered_bundle/ant_global/root/standard.json';H=json.loads(STD.read_text())['word']
G={(0,-1),(1,1),(2,2),(1,3)};B=set(G);p=(0,0);h=1;born={q:None for q in B};prefix=[]
for t in range(182):
 q=p;c='L'if q in B else'R';prefix.append(dict(update=t,cell=q,turn=c))
 if c=='R':born[q]=t
 else:born.pop(q)
 p,h=step(B,p,h)
assert(p,h)==((5,1),1)and born[(0,2)]==60
assert first_mismatch(State(frozenset(B),p,h),H)is None
P=[];pp=p;hh=h
for c in H:P.append(pp);hh=(hh+(1 if c=='R'else-1))%4;pp=(pp[0]+DIR[hh][0],pp[1]+DIR[hh][1])
assert(pp[0]-p[0],pp[1]-p[1])==(2,2)and min(q[0]for q in P)==4
port_deletion=dict(initial_black=sorted(G),initial_mass=4,initial_pose=[(0,0),1],prefix182=prefix,cut182_field=sorted(B),cut182_pose=[p,h],exact_H104_forever=True,H_phase_x_range=[min(q[0]for q in P),max(q[0]for q in P)],H_drift=(2,2),marked_R60_cell=(0,2),marked_lifetime_never_read_again=True,all_n_unused_ports_x_maxima=dict(port2='-n',port3='-5n+8',port4='-3n+2'),scope='Deleting the first remote turning port from the20-cell family leaves a literal H tail. All other remote ports have negative x for n>=20 and remain unread; they can be retained or removed initially. This failed return construction does NOT rule out different compact-source mechanisms.')
S='RRRRLRLRL';T='RRRRLLLLRLRL';word='';addresses=[]
for n in range(2):
 for b,(w,num)in enumerate([(T,n+1),(S,1),(T,n+1),(S,1),(T,n+2),(S,1),(T,n+2),(S,1)]):
  for j in range(num):
   for r,c in enumerate(w):word+=c;addresses.append((n,b,j,r))
p=(0,0);h=0;last={};seed=set();reads=[];bad=None
for t,c in enumerate(word):
 if p in last and last[p]['turn']==c:
  bad=dict(update=t,address=addresses[t],cell=p,turn=c,previous=last[p]);break
 if p not in last and c=='L':seed.add(p)
 last[p]=dict(update=t,address=addresses[t],turn=c);reads.append((p,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
assert bad and bad['cell']==(2,1)and bad['previous']['update']==15 and bad['update']==139
B=set(seed);p=(0,0);h=0;mx=0;trace=[]
for t,(q,c)in enumerate(reads):
 assert p==q and c==('L'if p in B else'R');C=comp(B,1,cursor(p,h));mx=max(mx,len(C));trace.append(dict(update=t,pose=[p,h],full_black=sorted(B),active_w=sorted(C)));p,h=step(B,p,h)
assert p==bad['cell']and p in B
spiral=dict(schema='lap n = T^(n+1) S T^(n+1) S T^(n+2) S T^(n+2) S',initial_heading=0,lap_heading_restored=True,lap_displacement=(0,-4),finite_test_laps=2,conflict=bad,minimal_seed_for_valid_prefix=sorted(seed),initial_mass=len(seed),valid_prefix_updates=len(reads),prefix_peak_active_w=mx,valid_prefix_trace=trace,scope='R/R same-cell contradiction at139 rejects this specific full lap program for EVERY initial board, even an infinite one. It is a failed construction, not a universal spatial obstruction or an RH16/4 test.')
out=dict(status='AUTHOR exact failed compact self-return adaptations',remote_port_deletion=port_deletion,one_ST_spiral=spiral,source_sha256={str(STD.relative_to(ROOT)):hashlib.sha256(STD.read_bytes()).hexdigest()},scope='No random scan or larger cap enumeration. Both proposed mechanisms fail to supply a completed compact self-made far return; neither proves the conjectural route bound or excludes other constructions.')
(OUT/'compact_self_return_attempts_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'port_deletion':{'seed_mass':4,'tail':'exact H104 forever','marked_target_consumed':False},'spiral':{k:spiral[k]for k in['schema','conflict','initial_mass','valid_prefix_updates','prefix_peak_active_w']}},indent=2))
