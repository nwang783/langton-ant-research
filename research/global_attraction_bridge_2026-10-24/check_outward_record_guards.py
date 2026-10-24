"""Exact outward H104 record phases, all-old-side minimal guards, and real record controls."""
import json
from pathlib import Path
from check_fresh_record_trap_bridge import geometry,verify_tail,replay,D
P=Path(__file__).parent
A=json.loads((P/'TERMINAL_TRAP_CERTIFICATE.json').read_text());H=A['period'];C=A['fixed_continuation'][46:];I={(0,2),(0,3),(1,1),(2,4),(3,2),(3,3)}
B0,p0,h0,prefix=replay(I,(0,0),2,C)
Q,pe,he=geometry((0,0),2,H);d=pe;assert d==(2,-2)and he==2
heads=[];h=2
for a in H:heads.append(h);h=(h+(1 if a=='R'else-1))%4
out=[]
for n in [(1,0),(0,-1),(1,-1)]:
 f=lambda x:sum(a*b for a,b in zip(n,x));delta=f(d);M=max(map(f,Q));past=M-delta;records=[]
 prior=max(f(tuple(e[1]))for e in prefix+[[0,list(x),0,'?']for x in I]);K0=max(1,(prior-f(p0)-M+delta-1)//delta+1)
 # Exact established prefix plus K0 full cycles lets every returned phase be checked on the complete actual board.
 BK,pK,hK,_=replay(B0,p0,h0,H*K0)
 states=[];bk=set(BK);pk=pK;hk=hK
 for a in H:
  states.append((set(bk),pk,hk));bk,pk,hk,_=replay(bk,pk,hk,a)
 for i,q in enumerate(Q):
  if f(q)>past:
   W=H[i:]+H[:i];V,vp,vh=geometry((0,0),heads[i],W);assert vp==d and vh==heads[i]
   G=set();epochmax=0
   for v in V:
    last=(-1-f(v))//delta
    for k in range(max(0,last+1)):G.add(tuple(v[j]+k*d[j]for j in range(2)));epochmax=max(epochmax,k)
   first={}
   for k in range(epochmax+1):
    for j,v in enumerate(V):
     x=tuple(v[u]+k*d[u]for u in range(2))
     if x in G and x not in first:first[x]=[k*104+j,W[j]]
   assert set(first)==G
   J={x for x,(t,a)in first.items()if a=='L'};_,dd,tests=verify_tail(J,(0,0),heads[i],W);assert dd==d
   current,head,hh=states[i];assert hh==heads[i] and all(f(x)<f(head)for x in current)
   normalized={tuple(x[u]-head[u]for u in range(2))for x in current};assert normalized&G==J
   # Previous prefix, all prior cycles and earlier phases are strictly below this record.
   assert f(head)>prior and f(q)>max([M-delta]+[f(x)for x in Q[:i]])
   rec=dict(phase=i,normalized_heading=heads[i],canonical_relative_pose=q,guard_size=len(G),black_size=len(J),white_size=len(G-J),required_black=sorted(J),required_white=sorted(G-J),old_guard=sorted(G),guard_first_reads=[[x,*first[x]]for x in sorted(G)],max_old_read_time=max(t for t,a in first.values()),cycle_word=W,ray_threshold_tests=tests,actual_control_epoch=K0,actual_control_pose=[head,hh],full_actual_control_board=sorted(current))
   if n==(1,-1)and i in(45,55):
    start=(-1,1);sponsor=(-1,0);z=(0,1);duration=8 if i==45 else 12
    assert start in J and sponsor not in J and ((z in J)==(i==45))
    pre=(J-{start})|{sponsor};RW='RL'+W[:duration-2]
    _,pend,hend,ev=replay(pre,start,1,RW)
    assert pend==start and hend==3 and all(tuple(e[1])!=start for e in ev[1:])
    assert max(f(x)for x in pre)==-1 and all(f(tuple(e[1]))<=1 for e in ev)
    assert sum(f(tuple(e[1]))==1 for e in ev)==(1 if i==45 else 2)
    oldread={tuple(e[1])for e in ev if f(tuple(e[1]))<0};assert oldread=={start,sponsor,z}
    free=G-oldread;controls=[]
    for x in sorted(free):
     perturbed=pre^{x};_,p2,h2,ev2=replay(perturbed,start,1,RW);assert ev2==ev and(p2,h2)==(pend,hend)
     t,a=first[x];assert t>=duration-2
     b,ph,hh,_=replay(J^{x},(0,0),heads[i],(W*(t//104+1))[:t])
     assert ph==x and (ph in b)!=(a=='L')
     controls.append(dict(flip_cell=x,required_black=x in J,first_disagreement_from_record_cut=t))
    rec['fresh_first_return_comparison']=dict(initial_pose=[start,1],base_initial_black=sorted(pre),record_word=RW,first_return_duration=duration,first_return_pose=[pend,hend],top_visits=1 if i==45 else 2,forced_guard_black=sorted(J&oldread),forced_guard_white=sorted(oldread-J),unconstrained_required_black=len(J&free),unconstrained_required_white=len(free-J),one_bit_controls=controls)
   records.append(rec)
  past=max(past,f(q))
 expected={(1,0):[61,71],(0,-1):[14,28],(1,-1):[45,46,55,56]}[n];assert [x['phase']for x in records]==expected
 out.append(dict(outward_normal=n,period_advance=delta,complete_strict_record_phases=expected,valid_from_epoch=K0,prior_support_and_history_max=prior,records=records))
result=dict(status='AUTHOR exact eight outward standard104 record guards; independent audit pending',canonical_period=H,canonical_heading=2,canonical_drift=d,normal_catalog=out)
(P/'OUTWARD_RECORD_GUARDS_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print([(x['outward_normal'],[(r['phase'],r['guard_size'],r['black_size'])for r in x['records']])for x in out])
