#!/usr/bin/env python3
"""Complete mature output of the supplied1564 wave, and exact self-consumer
profile test under every proper rotation and translation. No cap search.
An all-future bulk mismatch cannot be fixed by finitely many eligibility edits.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
P=Path(__file__).parent
N=json.loads((P/'prepared_wave_five_band_normal_form.json').read_text())
J=json.loads((P/'prepared_travelling_wave_certificate.json').read_text())
w=J['word'];p=tuple(N['pose'][0]);h=N['pose'][1];V=((0,1),(1,0),(0,-1),(-1,0));g=defaultdict(list)
for i,c in enumerate(w):
 x,y=p;t=x-y;a=x%14;k=(x-a)//14;g[t,a].append((k,i,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=x+v[0],y+v[1]
assert p==(8,8)and h==0
for G in g.values():
 G.sort(key=lambda z:(-z[0],z[1]));assert all(a[2]!=b[2]for a,b in zip(G,G[1:]))
required_black={j for j,G in g.items()if G[0][2]=='L'}
toggle={j for j,G in g.items()if len(G)%2}
input_full={(t,a)for t,b in N['full_black_orbit_profiles']for a in range(b,14,2)}
assert len(input_full)==420 and required_black==input_full&g.keys()
output_full=input_full^toggle
output_black_on_read={j for j,G in g.items()if G[-1][2]=='R'}
assert output_full&g.keys()==output_black_on_read
assert(len(g),len(required_black),len(output_black_on_read),len(toggle),len(output_full-g.keys()),len(output_full))==(557,197,301,358,223,524)
# Candidate translations must fit EVERY required-black normal level into the
# full output normal hull. Those integer bounds are necessary for all others.
outlo=min(t for t,a in output_full);outhi=max(t for t,a in output_full)
results=[];counts={};total=0
for r in(0,2):
 s=1 if r==0 else-1
 lo=outlo-min(s*t for t,a in required_black);hi=outhi-max(s*t for t,a in required_black)
 entries=[]
 for dt in range(lo,hi+1):
  if dt%2:continue # same physical conserved sector
  for dx in range(14):
   mism=[]
   for(t,a),G in sorted(g.items()):
    q=(s*t+dt,(s*a+dx)%14);want=G[0][2]=='L';actual=q in output_full
    if want!=actual:mism.append({'read_profile':[t,a],'target_profile':q,'required':'black'if want else'white','actual':'black'if actual else'white','first_word_slot':G[0][1]})
   assert mism,(r,dt,dx,'unexpected self-consumer')
   entries.append({'translation_t':dt,'translation_x_mod14':dx,'mismatch_count':len(mism),'first_witness':mism[0]});total+=1
 results.append({'clockwise_quarter_rotation':r,'required_black_translation_t_interval':[lo,hi],'sector_even_t_required':True,'candidates':entries,'minimum_mismatches':min((e['mismatch_count']for e in entries),default=None)})
# Perpendicular copies have a required-black ray with drift normal +/-28;
# the COMPLETE output has bounded normal support. Hence infinitely many
# required first-L sites are white, regardless of finite cap, translation or phase.
assert len(required_black)>0
out={'scope':__doc__,'status':'No exact1564 self-consumer on complete mature output, for any proper rotation/translation/phase or finite cap',
 'input_full_black_profiles':sorted(input_full),'output_full_black_profiles':sorted(output_full),
 'read_profiles':557,'input_black_on_read':197,'output_black_on_read':301,
 'untouched_black_profiles':sorted(input_full-g.keys()),'untouched_black_count':223,
 'output_full_black_count':524,'output_t_hull':[outlo,outhi],'odd_toggle_profiles':sorted(toggle),
 'parallel_tests':results,'parallel_candidates_checked':total,
 'perpendicular_exclusion':'197 required-black infinite drift rays eventually leave the bounded normal support; finite edits cannot repair infinitely many white sites',
 'phase_scope':'Cyclic phase shifts with their exact physical phase poses leave the mature first-color ray profile invariant: i-1564*k changes only by a common time-origin constant',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared1564_complete_output_self_consumer.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS output full524=301 read+223 untouched; no self-consumer among',total,'parallel poses or any perpendicular pose')
print([(r['clockwise_quarter_rotation'],r['required_black_translation_t_interval'],r['minimum_mismatches'])for r in results])
