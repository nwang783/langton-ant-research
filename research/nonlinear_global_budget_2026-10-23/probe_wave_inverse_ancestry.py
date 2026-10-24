#!/usr/bin/env python3
from pathlib import Path
import json,runpy,hashlib
ROOT=Path(__file__).parent;C=runpy.run_path(str(ROOT/'certify_prepared_travelling_wave.py'));E=C['E'];N=json.loads((ROOT/'prepared_wave_five_band_normal_form.json').read_text());B={tuple(j)for j in N['full_black_orbit_profiles']};F={tuple(q)for q in N['finite_XOR_cap']};p=tuple(N['pose'][0]);h=N['pose'][1];V=E['V'];p=(p[0]-V[h][0],p[1]-V[h][1]);h=(h+2)%4;I=''.join('L'if c=='R'else'R'for c in E['H'][::-1]);rot={I[i:]+I[:i]for i in range(104)}
def color(q,rows,F):return ((q[0]-q[1],q[0]%2)in B)^(q in F)
C['cert_parallel'].__globals__['color']=color;recent='';out=[];samples=[];result=None
for t in range(100001):
 if t%10000==0:samples.append([t,list(p),h,len(F)])
 if t>=208 and recent[:104]==recent[104:]and recent[104:]in rot:
  w=recent[104:]
  try:cert=C['cert_parallel']({},F,p,h,w)
  except AssertionError:cert=None
  if cert:result={'entry':t,'pose':[list(p),h],'inverse_H_word':w,'certificate':cert,'finite_XOR_mass':len(F)};break
 if t==100000:break
 ch='L'if color(p,{},F)else'R';out.append(ch);recent=(recent+ch)[-208:];E['toggle'](F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
word=''.join(out);tail=word[-min(20000,len(word)):];pi=[0]*len(tail)
for i in range(1,len(tail)):
 j=pi[i-1]
 while j and tail[i]!=tail[j]:j=pi[j-1]
 if tail[i]==tail[j]:j+=1
 pi[i]=j
period=len(tail)-pi[-1]if tail else None
report={'scope':'Deterministicpast of one supplied five-full-band/two-toggle state via exact time-reversal conjugacy; not a no-launch theorem.','standard_H_ancestry':result,'sampled_steps':len(word),'samples':samples,'suffix_candidate_period':period,'last_pose':[list(p),h]};(ROOT/'wave_inverse_ancestry_probe.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
