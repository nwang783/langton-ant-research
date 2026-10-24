"""Two literal four-read controls for a narrowly specified potential class."""
import json
from pathlib import Path
from blank_collision_operator import next_collision,materialize,D
from blank_collision_absorber import standard_certificate
P=Path(__file__).parent
controls=[]
for h,input_cell,expected_h,expected_p,expected_B in [
 (1,(-1,0),3,(-2,0),{(0,0),(0,-1),(-1,-1)}),
 (3,(1,0),1,(2,0),{(0,0),(0,1),(1,1)})]:
 B={input_cell};p=(0,0);hh=h;log=[]
 assert standard_certificate([(input_cell,(0,0),1)],p,h) is None
 for t,a in enumerate('RRRL'):
  assert(p in B)==(a=='L')
  log.append(dict(t=t,p=p,h=hh,read=a,board=sorted(B)))
  B^={p};hh=(hh+(1 if a=='R' else -1))%4;p=(p[0]+D[hh][0],p[1]+D[hh][1])
 assert(B,p,hh)==(expected_B,expected_p,expected_h)
 z=next_collision([(input_cell,(0,0),1)],(0,0),h)
 assert z['blank_duration']==3 and z['total_duration']==4
 assert materialize(z['new_terms'])==B
 assert standard_certificate([(q,(0,0),1)for q in B],p,hh) is None
 controls.append(dict(initial_board=[input_cell],initial_pose=[(0,0),h],word='RRRL',reads=log,
                      final_board=sorted(B),final_pose=[p,hh],first_old_contact_time=3,
                      initial_and_final_exact_standard=False))
report=dict(status='AUTHOR CHECKED; independent audit required',controls=controls,
 potential='sum_{(x,y) in B} f(y) + C_h(p_y), with f(-1)+f(1)>0',
 changes=['2 f(-1) + C_W(0) - C_E(0)','2 f(1) + C_E(0) - C_W(0)'],
 contradiction='The sum of two required nonpositive changes is 2(f(-1)+f(1)) > 0.',
 scope='Fixed absolute axis layers and tangentially translation-invariant heading correction only; no diagonal, recentered, guard-defect, or record-to-record claim.')
(P/'AXIS_BLACK_MASS_OBSTRUCTION_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print('Checked two literal four-read, full-field, nonabsorbed singleton controls.')
