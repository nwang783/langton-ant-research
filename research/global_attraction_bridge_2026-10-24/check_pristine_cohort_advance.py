"""Complete unrestricted no-old-input cover, with sharp pristine coordinate/diagonal advance."""
import json
from pathlib import Path
from check_fresh_record_trap_bridge import verify_tail,replay,D
P=Path(__file__).parent
B=set();born={};p=(0,0);h=0;events=[];records={str(n):[]for n in[(0,1),(1,1),(-1,1)]};maxima={key:-1 for key in records};states={};word=''
for t in range(10081):
 if t==9977:states['tail']=dict(black=sorted(B),pose=[p,h])
 for n in [(0,1),(1,1),(-1,1)]:
  key=str(n);v=sum(n[j]*p[j]for j in range(2))
  if v>maxima[key]:
   maxima[key]=v;records[key].append(dict(time=t,head=p,heading=h,height=v,preceding_event=events[-1]if events else None))
 c='L'if p in B else'R';e=dict(time=t,cell=p,incoming=h,turn=c,consumed_birth=born.get(p));events.append(e);word+=c
 if c=='L':B.remove(p);born.pop(p);h=(h-1)%4
 else:B.add(p);born[p]=t;h=(h+1)%4
 p=(p[0]+D[h][0],p[1]+D[h][1])
H=word[9977:];TB=set(map(tuple,states['tail']['black']));tp,th=states['tail']['pose'];Q,d,tests=verify_tail(TB,tuple(tp),th,H);assert d==(-2,-2)and len(TB)==715
bounds=[]
for n,want in [((0,1),22),((1,1),35),((-1,1),34)]:
 f=lambda q:sum(n[j]*q[j]for j in range(2));pref=max(f(e['cell'])for e in events[:9977]);tail=max(map(f,Q));advance=f(d);assert advance<=0 and max(pref,tail)==want
 bounds.append(dict(normal=n,sharp_blank_advance=want,prefix_maximum=pref,tail_maximum=tail,tail_projection_advance=advance,all_strict_blank_records=records[str(n)]))
axis=records[str((0,1))];caps=[r for r in records[str((1,1))]if r['height']%2==0];assert len(axis)==23 and axis[-1]['time']==9460 and len(caps)==18
sponsors=[]
for r in caps[1:]:
 e=r['preceding_event'];assert e['turn']=='L'and e['consumed_birth']is not None and e['consumed_birth']>=0
 x,y=e['cell'];assert x+y==r['height']-1>=1 and r['heading']==0
 sponsors.append(dict(new_cap_first_level=r['height'],record_time=r['time'],record_pose=[r['head'],r['heading']],sponsor_cell=e['cell'],sponsor_birth=e['consumed_birth'],sponsor_consumption=e['time'],entire_lifetime_initially_in_virgin_halfplane=True))
# These are genuine record cuts, not artificial empty-board initials.
a,pa,ha,ea=replay({(0,-1)},(0,-1),1,'L');assert(a,pa,ha)==(set(),(0,0),0)
b,pb,hb,eb=replay({(-1,-1),(0,-1)},(-1,-1),2,'LL');assert(b,pb,hb)==(set(),(0,0),0)
result=dict(status='AUTHOR unrestricted cohort-coupling advance lemma and sharp controls; independent audit pending',initial_pose=[(0,0),0],blank_prefix_length=9977,blank_prefix=word[:9977],blank_tail_word=H,blank_tail_state=states['tail'],blank_tail_drift=d,infinite_ray_tests=tests,distinct_prefix_read_cells=len({e['cell']for e in events[:9977]}),bounds=bounds,first_phase_diagonal_cap_sponsors=sponsors,sharp_genuine_record_preparations=dict(coordinate=dict(initial_black=[(0,-1)],pose=[(0,-1),1],word='L',events=ea),diagonal_first_phase=dict(initial_black=[(-1,-1),(0,-1)],pose=[(-1,-1),2],word='LL',events=eb)),full_blank_prefix_events=events[:9977])
(P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print(dict(bounds=[(z['normal'],z['sharp_blank_advance'])for z in bounds],fresh_side_sponsors=len(sponsors),sponsor_cells=[z['sponsor_cell']for z in sponsors],blank_tail_pose=states['tail']['pose'],tailmass=len(TB),raychecks=tests))
