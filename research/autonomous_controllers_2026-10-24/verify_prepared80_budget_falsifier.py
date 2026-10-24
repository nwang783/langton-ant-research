#!/usr/bin/env python3
"""Fresh vector-heading verification of the auditor's literal80 budget falsifier.
No retained ant/quotient/lifetime implementation is imported.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parent
W='RRRRLLLLRLRRRRLLLLRLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLRRRRLLLLRLLRRL'
P=80;D=(4,4);CAP={(-1,-1),(-1,0)};INPUT={(0,1),(3,2)}
def shift(p,n):return(p[0]+4*n,p[1]+4*n)
def qclass(p):
 k=p[0]//4;return(p[0]-4*k,p[1]-4*k),k

def replay(B,steps,expect=True):
 B=set(B);p=(0,0);v=(0,1);trace=[];owner={q:('initial',q)for q in B}
 for t in range(steps):
  turn='L'if p in B else'R'
  if expect:assert turn==W[t%P],(t,p,turn,W[t%P])
  row={'time':t,'position':p,'incoming_vector':v,'turn':turn}
  if turn=='L':row['consumed_owner']=owner.pop(p);B.remove(p);v=(-v[1],v[0])
  else:assert p not in owner;owner[p]=('R',t);B.add(p);v=(v[1],-v[0])
  trace.append(row);p=(p[0]+v[0],p[1]+v[1])
 return B,p,v,trace,owner

def main():
 assert len(W)==P
 final,p,v,E,owners=replay(CAP|INPUT,P);assert p==D and v==(0,1)
 out=final-{shift(c,1)for c in CAP};assert len(out)==14 and len(final)==16
 assert owners[(3,4)]==('R',29)and owners[(3,3)]==('R',78)
 # Complete actual physical histories, with no primitive-direction collapse.
 H=defaultdict(list);K={}
 for e in E:
  q,k=qclass(e['position']);i=e['time'];K[i]=k;H[q].append((i-P*k,i))
 A={};I=[];O=[];LIVES=[]
 for q,es in H.items():
  es.sort();cs=[E[i]['turn']for tau,i in es];assert all(c!=d for c,d in zip(cs,cs[1:]))
  if cs[0]=='L':I.append(es[0][1])
  if cs[-1]=='R':O.append(es[-1][1])
  for (ta,i),(tb,j)in zip(es,es[1:]):
   if E[i]['turn']=='R':
    vv=K[i]-K[j];age=j+vv*P-i;assert age==tb-ta and age>0 and age%4==0
    assert shift(E[j]['position'],vv)==tuple(E[i]['position'])
    A[i]=(j,vv);A[j]=(i,-vv);LIVES.append({'R':i,'L':j,'voltage':vv,'age':age})
 assert len(H)==31 and sorted(I)==[15,21]and len(O)==14 and len(LIVES)==32
 assert max(z['age']for z in LIVES)==56<P
 # Fresh expanded-circuit graph: alpha, actual conjugate beta, root sigma.
 edges=[]
 for z in LIVES:
  i,j,vv=z['R'],z['L'],z['voltage'];edges.append((i,j,vv,'alpha',i));edges.append(((i+1)%P,(j+1)%P,vv+(j==P-1)-(i==P-1),'beta',i))
 for i in I+O:edges.append((i,(i+1)%P,int(i==P-1),'input'if i in I else'output',i))
 adj=defaultdict(list)
 for n,(i,j,*_)in enumerate(edges):adj[i].append((n,1));adj[j].append((n,-1))
 assert set(adj)==set(range(P))and all(len(x)==2 for x in adj.values())
 seen=set();circuits=[]
 for st in range(P):
  if st in seen:continue
  at=st;prev=None;wind=0;seq=[]
  while True:
   seen.add(at);n,s=next(z for z in adj[at]if z[0]!=prev);i,j,vv,typ,own=edges[n];seq.append((n,s));wind+=s*vv;at=j if s==1 else i;prev=n
   if at==st:break
  roots=[edges[n]for n,s in seq if edges[n][3]in['input','output']]
  circuits.append({'full_winding':wind,'event_count':len(seq),'input_count':sum(e[3]=='input'for e in roots),'output_count':sum(e[3]=='output'for e in roots),'oriented_edge_indices':seq})
 assert sorted((abs(c['full_winding']),c['input_count'],c['output_count'])for c in circuits)==[(0,1,1),(3,1,13)]
 S=sum(abs(c['full_winding'])for c in circuits);assert S==3 and 4*(S-1)>2*min(len(I),len(O))
 # Exact all-N induction premises. Old output copies and later input copies
 # do not meet the one-period read footprint. This tests every possible lift
 # analytically via the full quotient, not a sampled shift cutoff.
 positions={tuple(e['position'])for e in E};disjoint_witness=[]
 for typ,cells,forbidden in [('old_output',out,lambda k:k<0),('future_input',INPUT,lambda k:k>0)]:
  for z in sorted(cells):
   shifts=[]
   for pp in positions:
    if qclass(pp)[0]==qclass(z)[0]:
     k=(pp[0]-z[0])//4;assert shift(z,k)==pp;assert not forbidden(k),(typ,z,k);shifts.append(k)
   disjoint_witness.append({'type':typ,'cell':z,'all_read_footprint_lifts':sorted(set(shifts))})
 controls=[]
 for N in [1,2,5,17]:
  seed=CAP|{shift(z,k)for z in INPUT for k in range(N)};bb,pp,vv,tt,oo=replay(seed,P*N)
  target={shift(z,N)for z in CAP}|{shift(z,k)for z in out for k in range(N)};assert bb==target and pp==shift((0,0),N)and vv==(0,1)
  # Rerun N periods plus16 reads; the first disagreement is exactly15 later.
  _,_,_,tail,_=replay(seed,P*N+16,False);mism=[t for t,e in enumerate(tail)if e['turn']!=W[t%P]];assert mism and mism[0]==P*N+15
  controls.append({'N':N,'full_initial_black':sorted(seed),'full_final_black':sorted(bb),'first_word_deviation':P*N+15})
 module_rows=[]
 for t in range(P-9):
  if W[t:t+10]=='RRRRLLLLRL':module_rows.append({'start':t,'literal_pose':[E[t]['position'],E[t]['incoming_vector']],'fuel_read':E[t+5],'active_cap_read':E[t+6]})
 assert [z['start']for z in module_rows]==[0,10,27,42,66]
 assert [E[t]['consumed_owner']for t in[32,47,71]]==[('R',20),('R',35),('R',59)]
 result={'status':'FRESH INDEPENDENT VERIFICATION PASS OF LITERAL PREPARED COUNTERCONTROL','scope':'Refutes m*(S-1)<=2min(I,O). Does not refute any WHITE-only claim, finite-seed attraction, or uniqueness. Repeating forever needs both infinite prelaid input rays.','word':W,'P':P,'full_drift':D,'full_initial_cap':sorted(CAP),'input_ray_starts':sorted(INPUT),'literal_one_period_trace':E,'one_period_full_output':sorted(final),'per_period_permanent_outputs':sorted(out),'complete_stable_histories':[{'representative':q,'events':es}for q,es in sorted(H.items())],'input_phases':sorted(I),'output_phases':sorted(O),'owned_lifetimes':LIVES,'expanded_edges':edges,'expanded_circuits':circuits,'candidate':{'m':4,'S':S,'I':len(I),'O':len(O),'left':8,'right':4,'status':'FALSE'},'all_N_noninterference_witness':disjoint_witness,'finite_complete_controls':controls,'five_literal_ten_modules':module_rows,'cap_regeneration_R_owners':{'translated_minus1_minus1':78,'translated_minus1_0':29},'feature':'Three later nominal ten-module fuel inputs are R20/R35/R59 births; active cap is regenerated. Stable input atphase21 is restored R77 to permanent BLACK. All32 owned ages<P.'}
 (R/'prepared80_budget_falsifier_independent_confirmation.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS80:31 complete classes,I2,O14,S3; exact all-N fields; recycled module fuel and regenerated cap')
if __name__=='__main__':main()
