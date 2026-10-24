"""Exact mature-profile test of the THREE supplied words on15324 output.
Two COMPLETE source backgrounds: the three useful-band output, and the actual
five-band producer output retaining both untouched exterior helper profiles.
Only repetition of these supplied words is tested; no changing schedule is covered.
No new words, cap search or field cropping.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd
import json,hashlib
from check_prepared1564_router_geometry import trace
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'
R=json.loads((P/'prepared4352_output_return_wave.json').read_text());NF=json.loads((P/'prepared15324_return_normal_form.json').read_text())

def profile(word,p,h):
 rows=list(trace(word,p,h));d=rows[-1][1][0]-p[0];assert rows[-1][1][1]-p[1]==d and rows[-1][2]==h and d
 s=abs(d);groups=defaultdict(list)
 for i,q,hh,c in rows[:-1]:groups[q[0]-q[1],q[0]%s].append(((q[0]-q[0]%s)//d,i,c))
 for g in groups.values():g.sort(key=lambda a:(-a[0],a[1]));assert all(a[2]!=b[2]for a,b in zip(g,g[1:]))
 return {'stride':s,'groups':groups,'black':{j for j,g in groups.items()if g[0][2]=='L'},'word_sha256':hashlib.sha256(word.encode()).hexdigest()}
C={1564:profile(json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],(-6,-6),0),4352:profile(json.loads((G/'second_prepared_wave_certificate.json').read_text())['word'],(-2,3),3),15324:profile(R['word'],(13,7),0)}
whole_input={(t,a)for t,b in NF['bulk_mod26']for a in range(b,78,26)}
core_input={j for j in whole_input if -28<=j[0]<=46};T={j for j,g in C[15324]['groups'].items()if len(g)%2}
assert len(core_input)==1956 and C[15324]['black']==core_input&C[15324]['groups'].keys()
sources={'complete_three_band_15324_output':core_input^T,'actual_five_band_15324_output':whole_input^T};assert[len(s)for s in sources.values()]==[2364,3300]
results=[]
for name,S in sources.items():
 loS=min(t for t,a in S);hiS=max(t for t,a in S)
 for target,c in C.items():
  g=gcd(78,c['stride']);orientations=[]; ordered=sorted(c['groups'].items())
  for rot in(0,2):
   sign=1 if rot==0 else-1;lo=loS-min(sign*t for t,a in c['black']);hi=hiS-max(sign*t for t,a in c['black']);records=[];matches=[]
   for dt in range(lo,hi+1):
    if dt%2:continue
    for dx in range(g):
     witness=None
     for(t,a),rows in ordered:
      want=rows[0][2]=='L';tt=sign*t+dt;aa=(sign*a+dx)%g
      wrong=next((x for x in range(aa,78,g)if((tt,x)in S)!=want),None)
      if wrong is not None:witness={'consumer_class':[t,a],'first_slot':rows[0][1],'required':'L'if want else'R','source_class':[tt,wrong],'source_black':(tt,wrong)in S};break
     if witness is None:matches.append([dt,dx])
     else:records.append({'translation_t':dt,'translation_x_mod_gcd':dx,'witness':witness})
   orientations.append({'proper_rotation_quarters':rot,'necessary_t_interval':[lo,hi],'tested_alignments':len(records)+len(matches),'matches':matches,'rejections':records})
  results.append({'source':name,'target_word_period':target,'common_gcd':g,'parallel_orientations':orientations,'perpendicular_reason':'Each supplied target has nonempty initial-black read rays, which escape any finite normal hull under perpendicular drift; finite edits cannot repair infinitely many.'})
out={'scope':__doc__,'sources':{name:{'full_black_classes':len(S),'normal_hull':[min(t for t,a in S),max(t for t,a in S)],'complete_output_profiles':sorted(S)}for name,S in sources.items()},'consumers':{n:{'stride':c['stride'],'read_classes':len(c['groups']),'first_black_classes':len(c['black']),'word_sha256':c['word_sha256']}for n,c in C.items()},'results':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared15324_known_output_consumers.json').write_text(json.dumps(out,indent=2)+'\n')
for r in results:print(r['source'],r['target_word_period'],[(o['tested_alignments'],o['matches'])for o in r['parallel_orientations']])
