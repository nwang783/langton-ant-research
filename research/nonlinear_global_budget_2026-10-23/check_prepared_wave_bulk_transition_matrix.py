#!/usr/bin/env python3
"""Exact all-phase/proper-rotation/translation mature-output compatibility
between the TWO already certified positive-fuel words. No cap/word search.
Complete output includes untouched black classes outside the word's read set.
"""
from pathlib import Path
from collections import defaultdict
from math import gcd
import json,hashlib
P=Path(__file__).parent;V=((0,1),(1,0),(0,-1),(-1,0))
def make(nf,cf,bkey):
 N=json.loads((P/nf).read_text());J=json.loads((P/cf).read_text());w=J['word'];p=tuple(N['pose'][0]);h=N['pose'][1];s=N['drift'][0];G=defaultdict(list)
 for i,c in enumerate(w):
  x,y=p;a=x%s;G[x-y,a].append(((x-a)//s,i,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=x+v[0],y+v[1]
 assert p==(N['pose'][0][0]+s,N['pose'][0][1]+s)and h==N['pose'][1]
 for g in G.values():g.sort(key=lambda z:(-z[0],z[1]));assert all(a[2]!=b[2]for a,b in zip(g,g[1:]))
 B={(t,a)for t,b in N[bkey]for a in range(b,s,2)};BB={j for j,g in G.items()if g[0][2]=='L'};T={j for j,g in G.items()if len(g)%2};O=B^T
 assert BB==B&G.keys()
 return {'period':len(w),'stride':s,'read':G,'need_black':BB,'input':B,'output':O,'normal_hull':[min(t for t,a in O),max(t for t,a in O)],'word_sha256':hashlib.sha256(w.encode()).hexdigest()}
A=make('prepared_wave_five_band_normal_form.json','prepared_travelling_wave_certificate.json','full_black_orbit_profiles')
B=make('three_standard_band_wave_normal_form.json','second_prepared_wave_certificate.json','full_black_profiles')
allwaves={1564:A,4352:B};results=[]
for source,S in allwaves.items():
 for target,C in allwaves.items():
  q,p=S['stride'],C['stride'];g=gcd(p,q);out=S['output'];outlo,outhi=S['normal_hull'];rs=[]
  for r in(0,2):
   sign=1 if r==0 else-1;lo=outlo-min(sign*t for t,a in C['need_black']);hi=outhi-max(sign*t for t,a in C['need_black']);poses=[]
   for dt in range(lo,hi+1):
    if dt%2:continue
    for dx in range(g):
     mism=[]
     for(t,a),G in sorted(C['read'].items()):
      tt=sign*t+dt;aa=(sign*a+dx)%g;want=G[0][2]=='L'
      bad=[x for x in range(aa,q,g)if((tt,x)in out)!=want]
      if bad:mism.append({'consumer_profile':[t,a],'output_normal':tt,'required_color':'L'if want else'R','output_residues_wrong':bad,'first_slot':G[0][1]})
     assert mism,('compatible consumer',source,target,r,dt,dx)
     poses.append({'translation_t':dt,'translation_x_mod_gcd_stride':dx,'conflicting_consumer_classes':len(mism),'mismatches_per_full_background_cycle':sum(len(z['output_residues_wrong'])for z in mism),'first_witness':mism[0]})
   rs.append({'clockwise_quarter_rotation':r,'necessary_translation_t_interval':[lo,hi],'tested_alignments':len(poses),'minimum_conflicting_read_classes':min((m['conflicting_consumer_classes']for m in poses),default=None),'background_period_in_consumer_copies':q//g,'minimum_XOR_repairs_per_background_cycle':min((m['mismatches_per_full_background_cycle']for m in poses),default=None),'alignments':poses})
  results.append({'producer_word_period':source,'consumer_word_period':target,'common_residue_gcd':g,'parallel_rotations':rs,'perpendicular_rotations':'impossible: nonempty required-black rays eventually leave bounded output normal support','compatible_mature_bulk_alignments':0})
out={'scope':__doc__,'status':'All four mature-output/consumer pairs fail for every physical same-sector proper rotation, translation, cyclicphase and finite cap',
 'waves':{k:{'stride':v['stride'],'read_classes':len(v['read']),'input_full_black_classes':len(v['input']),'output_black_on_read':len(v['output']&v['read'].keys()),'untouched_black_classes':len(v['input']-v['read'].keys()),'output_full_black_classes':len(v['output']),'complete_output_profiles':sorted(v['output']),'normal_hull':v['normal_hull'],'word_sha256':v['word_sha256']}for k,v in allwaves.items()},
 'matrix':results,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared_wave_bulk_transition_matrix.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all four bulk transitions fail')
for r in results:print(r['producer_word_period'],'->',r['consumer_word_period'],[(z['tested_alignments'],z['minimum_conflicting_read_classes'])for z in r['parallel_rotations']])
