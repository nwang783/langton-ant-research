from pathlib import Path
SELF=Path(__file__).resolve();src=SELF.with_name('check_U_recycled_q_return_independent.py').read_text().split('rows=[]')[0].replace('U_recycled_q_return_frozen_20261023_1939','U_arm_return_frozen_20261023_1943');n={'__file__':str(SELF)};exec(compile(src,str(SELF),'exec'),n)
globals().update({k:v for k,v in n.items()if not k.startswith('__')})
arm=1+2j;bridge=[1+5j,3+3j,1+1j,-1+3j];W=bridge[-1];X=bridge[0]
def edge(p):return {2*p+v,2*p-v}if(v:=1+1j if sum(xy(p))%2==0 else 1-1j)else None
for cell,a,b in zip((arm,1+1j,1j),bridge,bridge[1:]):assert edge(cell)=={a,b}
rows=[]
for s in(7,8,9):
 for h in range(4):
  for slot,i in enumerate(sorted(G[s][0],key=xy)):
   p=arm-rotation(i,h);start=2*p+rotation(-1-1j,h);end=start+rotation(8j,h)
   if(sum(xy(p))+h)%2:r='wrong_sector'
   elif{p+rotation(z,h)for z in G[s][2]}&star:r='permanent_source_L_star_context'
   elif meet((start,end),source):r='consumer_base_contacts_source_U'
   else:
    assert(s,p,h,i)==(7,6j,2,-1+4j)and end==X
    for j,(a,b)in enumerate(zip(bridge,bridge[1:])):
     got=meet((start,end),(a,b));assert got==((Fraction(1),Fraction(0),(Fraction(1),Fraction(5)))if j==0 else None)
    r='Jordan_Cgap6_plus_retired_upper_deadline'
   rows.append(dict(consumer=s,head=(*xy(p),h),input_slot=slot,reason=r))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=30,permanent_source_L_star_context=26,consumer_base_contacts_source_U=3,Jordan_Cgap6_plus_retired_upper_deadline=1)
ref=json.loads((B/'02_U_arm_return.json').read_text());assert{(r['consumer'],r['head'],r['input_slot'],r['reason'])for r in rows}=={(r['consumer'],tuple(r['head']),r['input_slot'],r['reason'])for r in ref['all_60_consumer_alignments']}
C=raws[1][len(raws[0]):];prefix=[]
for s in(7,8,9):
 assert arm in G[s][1]and 3j in G[s][0]and 3j not in G[s][1]
 e,h,_,_=walk(raws[7]);P=2*e+rotation(-1-1j,h)
 for j,(a,b)in enumerate(zip(bridge,bridge[1:])):assert meet((W,P),(a,b))==((Fraction(0),Fraction(1),(Fraction(-1),Fraction(3)))if j==2 else None)
 for _ in range(s-7):
  old=P;ep,dh,_,_=walk(C);e+=rotation(ep,h);h=(h+dh)%4;P=2*e+rotation(-1-1j,h);assert all(meet((old,P),(a,b))is None for a,b in zip(bridge,bridge[1:]))
 prefix.append(dict(source=s,full_exit=(*xy(e),h),C_count=s-7))
joins=[1,-2,-2,-1];assert [n for n in range(20) if 2*n+sum(joins)in(-8,8)]==[6]
endpoints=[];outputs=[]
for s in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={q for q,b in req.items()if b};out=(black^flip)-{e+rotation(q,h)for q in K}
 assert min(o.imag for o in out)>=0 and min(o.real+o.imag for o in out)>=0
 outputs.append(dict(source=s,min_y=int(min(o.imag for o in out)),min_W_H=int(min(o.real+o.imag for o in out))))
 if s in(0,4,7):assert h==0 and e.imag>0 and e.imag-e.real>=0 and (rotation(e,3).imag-rotation(e,3).real)>=0
 if s in(1,5,8):assert h==3 and e.imag-e.real>=1
 endpoints.append(dict(source=s,exit=(*xy(e),h)))
out=dict(status='PASS protected U arm Jordan and genuine upper birth deadline',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),rows=rows,bridge=list(map(xy,bridge)),source_interfaces=prefix,endpoints=endpoints,all_output_bounds=outputs,forced_C_age=6,latest_other_upper_producer_clock=1,proof='Old d0,3 is consumed by source and absent from every full source output, so replacement must be later-produced. UCC exitsclock2 too late. UC exitsW atH5. Plain U exitsN at y4: clock0 heads/outputs cannot decrease y; one-C transition has H gain>=1 after nonnegative N gains, then all W zero-clock heads and full outputs have nonnegative H gains. No producer startclock<=1 reachesH3.',scope='Genuine earlier U-family output1,2 cannot feed any later U-family input in same actual complete-eight factor. D/V retirement remains allowed; no record, historical merger or capture claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],dict(counts))
