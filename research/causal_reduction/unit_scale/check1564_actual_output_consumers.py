"""Two supplied-wave consumer tests on the ACTUAL producer's mature bulk.
Keep both untouched exterior helper rails, and separately add the actual
endpoint's emitted standard lane. No new word/cap/period synthesis.
"""
from pathlib import Path
from collections import defaultdict,Counter
from math import gcd
import json,hashlib
from check1564_noncrossing_producer import setup,H,W,V
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'

def profile(word,p,h):
 rr=list(trace(word,p,h));d=rr[-1][1][0]-p[0],rr[-1][1][1]-p[1];assert d[0]==d[1]and d[0]>0 and rr[-1][2]==h
 s=d[0];groups=defaultdict(list)
 for i,q,hh,c in rr[:-1]:
  a=q[0]%s;groups[q[0]-q[1],a].append(((q[0]-a)//s,i,c))
 for row in groups.values():row.sort(key=lambda z:(-z[0],z[1]));assert all(a[2]!=b[2]for a,b in zip(row,row[1:]))
 return {'word':word,'pose':[p,h],'stride':s,'read':groups,'black':{j for j,row in groups.items()if row[0][2]=='L'},'toggle':{j for j,row in groups.items()if len(row)%2}}
A=profile(W,(-6,-6),0)
J=json.loads((G/'second_prepared_wave_certificate.json').read_text());N=json.loads((G/'three_standard_band_wave_normal_form.json').read_text());B=profile(J['word'],tuple(N['pose'][0]),N['pose'][1])
normal=json.loads((G/'prepared_wave_five_band_normal_form.json').read_text());initial={(t,a)for t,b in normal['full_black_orbit_profiles']for a in range(b,14,2)}
assert len(initial)==420
five_out=initial^A['toggle'];assert len(five_out)==524
_,_,ss,_=setup(100,0);flights=[s for s in ss if s['kind']=='H'];helpers=set();helper_records=[]
for i in [1,3]:
 s=flights[i];p,h=s['start'];counts=Counter((q[0]-q[1],q[0]%2)for _,q,hh,c in list(trace(H,p,h))[:-1]);black={j for j,n in counts.items()if n%2};lift={(t,a)for t,b in black for a in range(b,14,2)}
 assert not helpers&lift;helpers|=lift
 helper_records.append({'flight':i+1,'black_mod2':sorted(black),'full_read_normal_hull':[min(t for t,a in counts),max(t for t,a in counts)]})
assert len(helpers)==168 and not helpers&five_out
end=json.loads((P/'prepared1564_source_endpoint_family.json').read_text());tp=(-104,-24);th=0;tail=end['capture_word'];counts=Counter((q[0]-q[1],q[0]%2)for _,q,hh,c in list(trace(tail,tp,th))[:-1]);tail_black={j for j,n in counts.items()if n%2};tail_lift={(t,a)for t,b in tail_black for a in range(b,14,2)}
assert len(tail_lift)==84 and not tail_lift&(helpers|five_out)
backgrounds={'seven_writer_output':five_out|helpers,'seven_writer_output_plus_endpoint_lane':five_out|helpers|tail_lift};reports=[]
for name,out in backgrounds.items():
 for C in[A,B]:
  q=14;p=C['stride'];g=gcd(p,q);loout=min(t for t,a in out);hiout=max(t for t,a in out);rotations=[];matches=[]
  for rot in[0,2]:
   sign=1 if rot==0 else-1;lo=loout-min(sign*t for t,a in C['black']);hi=hiout-max(sign*t for t,a in C['black']);align=[]
   for dt in range(lo,hi+1):
    if dt%2:continue
    for dx in range(g):
     bad=[]
     for(t,a),row in sorted(C['read'].items()):
      tt=sign*t+dt;aa=(sign*a+dx)%g;want=row[0][2]=='L';wrong=[r for r in range(aa,q,g)if((tt,r)in out)!=want]
      if wrong:bad.append({'read_class':[t,a],'output_normal':tt,'wrong_output_residues':wrong,'required_black':want,'first_slot':row[0][1]})
     rec={'dt':dt,'dx_mod_gcd':dx,'wrong_read_classes':len(bad),'wrong_full_cycle_cells':sum(len(z['wrong_output_residues'])for z in bad),'witness':bad[0]if bad else None};align.append(rec)
     if not bad:matches.append({'rotation':rot,'dt':dt,'dx':dx})
   rotations.append({'rotation':rot,'normal_translation_interval':[lo,hi],'candidates':align,'count':len(align),'min_wrong_classes':min((e['wrong_read_classes']for e in align),default=None),'min_wrong_full_cycle_cells':min((e['wrong_full_cycle_cells']for e in align),default=None)})
  reports.append({'background':name,'consumer_period':len(C['word']),'consumer_stride':p,'background_cycle_copies':q//g,'parallel_rotations':rotations,'matches':matches,'perpendicular_scope':'Every required-black ray eventually leaves the finite normal support; no finite XOR edits can repair it.'})
  print(name,'->',len(C['word']),'matches',matches,'counts/min',[(r['count'],r['min_wrong_classes'])for r in rotations],flush=True)
out={'scope':__doc__,'status':'NO supplied-wave mature consumer'if all(not r['matches']for r in reports)else'MATCHES REQUIRE PHYSICAL CHRONOLOGY',
 'helper_records':helper_records,'endpoint_lane_black_mod2':sorted(tail_black),'backgrounds':{name:{'black_mod14':sorted(out),'black_count':len(out),'normal_hull':[min(t for t,a in out),max(t for t,a in out)]}for name,out in backgrounds.items()},'reports':reports,
 'phase_scope':'Exact cyclic phase poses preserve mature first-color orbit requirements. Same-sector translations have even normal shift.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared1564_actual_output_consumers.json').write_text(json.dumps(out,indent=2)+'\n')
