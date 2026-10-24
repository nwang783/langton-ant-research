from pathlib import Path
from collections import defaultdict
import hashlib,json,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'kernel_cycle_lift_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'INTERLEAVING_SPATIAL_ARCHIVE_LEDGER.md';assert sha(note)=='eafb84d4ca6e271b368fa07ea63d1df36dec052c692d8c9e2c61e73309d9a8d8';rf=json.loads((D/'interleaving_spatial_archive_ledger_certificate.json').read_text())
ns={'__file__':str(S.with_name('check_cycle_birth_finite_fuel_independent.py'))};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns);ends,wvertex=ns['ends'],ns['wvertex'];V=(1j,1,-1j,-1);cx=lambda q:complex(*q);xy=lambda q:(int(q.real),int(q.imag))
def control(B0,p,h,b,d,stop,reference):
 B=set(B0);G=defaultdict(dict);lat=int(wvertex(p,h).real+wvertex(p,h).imag)%4;born={q:None for q in B};retired=[];old=set();M=0;Mfull=0;shots={}
 def edit(q,add):
  a,z=ends(q,lat)
  if add:G[a][z]=q;G[z][a]=q
  else:del G[a][z];del G[z][a]
 def comp(v):
  seen={v};todo=[v];E=set()
  for a in todo:
   for z,q in G[a].items():
    E.add(q)
    if z not in seen:seen.add(z);todo.append(z)
  return E
 for q in B:edit(q,True)
 for t in range(stop+1):
  C=comp(wvertex(p,h));Mfull=max(Mfull,len(C))
  if b<=t<=d:M=max(M,len(C))
  if t==b:assert p not in B;base=set(B);cohort=dict(born);old=set(B);origin=p
  if stop<=60:shots[t]=(set(B),p,h,dict(born),set(C))
  if t==d:
   assert B=={cx(q)for q in reference['cut_full_black']}and set(C)=={cx(q)for q in reference['cut_active']};assert [*xy(p)]==reference['cut_pose'][0]and h==reference['cut_pose'][1];assert born=={cx(q):v for q,v in reference['cut_births']};assert base=={cx(q)for q in reference['base_black']}
   axis=0 if abs(p.real-origin.real)>=abs(p.imag-origin.imag)else 1;coord=lambda q:int(q.real if axis==0 else q.imag);L=abs(coord(p)-coord(origin));lines=range(min(coord(p),coord(origin))+1,max(coord(p),coord(origin)));fresh={q for q in B if born[q]is not None and born[q]>=b};K=0
   for line in lines:
    diff={q for q in B^base if coord(q)==line};fr={q for q in fresh if coord(q)==line};rr=[z for z in retired if coord(z[1])==line];K+=len(rr)
    charge=sum((1 if q in B else-1)*(-1)**int(q.imag if axis==0 else q.real)for q in diff);assert charge%4==2 and len(diff)>=2 and len(fr)+len(rr)>=2
    ar=next(z for z in reference['per_line']if z['line']==line);assert diff=={cx(q)for q in ar['discrepancy']}and fr=={cx(q)for q in ar['fresh']};assert {(z[0],xy(z[1]),z[2])for z in rr}=={(z['update'],tuple(z['cell']),z['birth_at_b'])for z in ar['retired']}
   todo=set(B);components=[]
   while todo:
    q=next(iter(todo));A=comp(ends(q,lat)[0]);components.append(A);todo-=A
   dorm=[A for A in components if A!=C and A&fresh];assert all(len(A)<=M-1 for A in dorm);bound=(max(0,2*len(lines)-K-M)+M-2)//(M-1);assert len(dorm)>=bound
   fields={(frozenset(A),frozenset(A&fresh))for A in dorm};assert fields=={(frozenset(cx(q)for q in z['edges']),frozenset(cx(q)for q in z['fresh']))for z in reference['dormant_fresh_component_fields']}
   summary={'b':b,'d':d,'distance':L,'M':M,'old_retirements_on_lines':K,'fresh_mass':len(fresh),'active_fresh_mass':len(C&fresh),'dormant_fresh_components':len(dorm),'lower_bound_dormant_fresh_components':bound}
   for k,v in summary.items():assert v==reference[k]
  if t==stop:break
  q=p;ch='L'if q in B else'R'
  if ch=='L':
   if q in old:retired.append((t,q,cohort[q]));old.remove(q)
   B.remove(q);born.pop(q);edit(q,False)
  else:B.add(q);born[q]=t;edit(q,True)
  h=(h+(1 if ch=='R'else-1))%4;p+=V[h]
 return summary,shots,Mfull,retired
blank,shots,mfull,ret=control(set(),0j,0,1,18,60,rf['controls'][0]);assert blank['M']==10 and max(len(shots[t][4])for t in range(60))==11
helper=1+0j;parent=1j
assert helper in shots[16][4]and helper not in shots[17][4]and parent in shots[17][4]and parent not in shots[18][4]
assert shots[53][1]==helper and shots[53][3][helper]==1 and helper not in shots[54][0];assert shots[59][1]==parent and shots[59][3][parent]==7 and parent not in shots[60][0]
assert ret==[(4,0j,0)]
for k,z in rf['controls'][0]['completed_interleaving']['full_special_cuts'].items():
 B,p,h,born,C=shots[int(k)];assert B=={cx(q)for q in z['black']}and C=={cx(q)for q in z['active']}and [list(xy(p)),h]==z['pose']and born=={cx(q):v for q,v in z['births']}
n=400;g={-1j,1+1j,2+2j,1+3j};poses=[(0j,1),(complex(n-1,n),0),(complex(-n,3*n-4),3),(complex(-5*n+5,-n),2),(complex(-3*n,-3*n+8),1)];seed={p+q*(-1j)**((h-1)%4)for p,h in poses for q in g};assert len(seed)==20 and seed=={cx(q)for q in rf['controls'][1]['initial_black']}
feedback,_,_,_=control(seed,0j,1,60,20627,20627,rf['controls'][1]);assert feedback['M']==42 and feedback['distance']==399 and feedback['old_retirements_on_lines']==11 and feedback['fresh_mass']==2396 and feedback['dormant_fresh_components']==199 and feedback['lower_bound_dormant_fresh_components']==19
bindings={p:sha(R/p)for p in ['global_capture_bridge_2026-10-23/live_cursor_transport_debt.md','active_w_archive_itinerary_2026-10-23/ACTIVE_EPISODES.md','active_w_archive_itinerary_2026-10-23/TWENTY_CELL_SUSTAINED_CAP.md']}
out={'status':'PASS retained axial-charge specialization to current fresh complete archives, plus two named full-field controls','author_note':sha(note),'author_controls':sha(D/'interleaving_spatial_archive_ledger_certificate.json'),'dependencies':bindings,'blank_control':blank,'blank_full_interval_cap_0_through59':11,'long_checkpoint_control':feedback,'analytic_review':[
'Retained axial charge with comparisonboardB_b and zeroheight gives alternating signed discrepancy2mod4 on EVERY strict separating row/column. Every initialBLACK-to-WHITE discrepancy consumes one actual cut-b cohort lifetime; every initialWHITE-to-BLACK discrepancy has a CURRENT R-born lifetime afterb. Thus K_r+F_r>=2. Consumed-and-reborn initial cells can count in both ledgers but not discrepancy, only strengthening this inequality.',
'Summing distinctstrictlines gives currentfresh mass>=2(L-1)-K. At mostMfresh cells are active atd. Any dormant complete component containing a currentfresh lifetime had that lifetimeactive immediately afterbirth and a LAST active-to-dormant transition in[b,d]. It is bridgeL: one oldactiveedge isdeleted and surviving departedcomponent has<=M-1 edges.',
'This FULL component stays frozen untilcheckpoint: a future read or Rattachment would activate the wholecomponent and its marked fresh lifetime, contradicting lastdeparture. Passive/passive merges without active import cannot occur. Hence each relevant dormantcomponentcontainsatmostM-1 totaledges, even with oldcells/cycles, giving the stated ceilingbound. Arbitrary oldarchives are not deleted.',
'The activecap is required on the EARLIER interval[b,d], separately from a parentfeedback cap[d-1,c]. b is BEFORE the helperRbirth, so the cut-b cohort excludes thatnewhelper and counts eacholdlifetimeonce. Checkpointfresh labels use currentbirth, not historicalRcounts.',
'Blank actual17<18<53<59 interleaving is fullyexecuted throughbothconsumptions with originalR1/R7 labels. Interval[1,18] cap10 is correct; fullcuts[0,59] require11, not10. OnlyolderR0 diedat4, so no older-than-helper consumption occurs during17..59. This is short-range only.',
'Named n400 complete20-cell orbit is replayed only throughactualcheckpoint20627 with allremoteports/blackfields retained. Everylinecharge, birthlabel and fullfresh dormantcomponent matches; M42,L399,K11,currentfresh2396,dormant199,bound19. Laterconsumption248084 is a retained-source fact, NOT independently replayed here; checkpoint is NOT certified as another completed parentdeparture.',
'This is a spatial CHECKPOINT alternative, not a new invariant, globallydecreasing potential, uniquecharge, stack/LIFO rule or obstruction to legalrecycling. Standard transport itself producesfresharchives; no capture theorem follows.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(blank,feedback)
