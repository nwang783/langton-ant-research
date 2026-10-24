import json
from collections import Counter,defaultdict
from check_extremal_read_coupling import ROOT,event_word,quotient,cycles,D
G=ROOT/'nonlinear_global_budget_2026-10-23'
s=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());S=s['word'];P=json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'];Q=json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']
def mask(q):return q[0]%2==0 and sum(q)%28==20
def info(w):
 ev,d,h=event_word(w);H=defaultdict(list);delta=0
 for e in ev:
  r,k=quotient(e['p'],d);H[r].append(dict(e,clock=e['t']-k*len(w)))
  if mask(e['p']):delta+=1 if e['c']=='R' else -1
 for es in H.values():es.sort(key=lambda e:e['clock']);assert all(x['c']!=y['c'] for x,y in zip(es,es[1:]))
 first={};last={};nin=nout=selectedin=selectedout=0
 for r,es in H.items():
  a,z=es[0],es[-1]
  if a['c']=='R':n=(r[0]+D[a['ho']][0],r[1]+D[a['ho']][1]);first[r]=quotient(n,d)
  else:nin+=1;selectedin+=mask(r)
  if z['c']=='L':n=(r[0]-D[z['hi']][0],r[1]-D[z['hi']][1]);last[r]=quotient(n,d)
  else:nout+=1;selectedout+=mask(r)
 f=cycles(first);l=cycles(last)
 return {'period':len(w),'drift':d,'input_black_roots':nin,'output_black_roots':nout,'first_cycles':[(len(c['cells']),c['winding']) for c in f],'last_cycles':[(len(c['cells']),c['winding']) for c in l],'selected_input':selectedin,'selected_output':selectedout,'delta':delta}
for n,w in [('S',S),('P',P),('Q',Q)]:print(n,info(w))
for fn,bkey,stride,start,h in [('prepared_wave_five_band_normal_form.json','full_black_orbit_profiles',14,(-6,-6),0),('three_standard_band_wave_normal_form.json','full_black_profiles',26,(68,73),3)]:
 nf=json.loads((G/fn).read_text());w=P if stride==14 else Q;ev,d,hh=event_word(w,h,start);groups=defaultdict(list)
 for e in ev:
  x,y=e['p'];groups[(x-y,x%stride)].append((e['t']-len(w)*((x-x%stride)//stride),e['c']))
 for es in groups.values():es.sort()
 B={(t,a)for t,b in nf[bkey] for a in range(b,stride,2)};O=B^{k for k,v in groups.items() if len(v)%2}
 def select(k):
  t,a=k;x=a;y=a-t;x-=start[0];y-=start[1]
  for _ in range((-h)%4):x,y=y,-x
  return mask((x,y))
 print(fn, 'full_in',sum(map(select,B)),'full_out',sum(map(select,O)),'unread',sum(select(k)for k in B-groups.keys()))
ph=[]
for j in range(104):
 w=S[j:]+S[:j];ev,d,h=event_word(w);de=sum((1 if e['c']=='R' else -1)for e in ev if mask(e['p']))
 if d==(-2,2) and de>0:ph.append((j,de))
print('same_drift_positive_standard_phases',ph)
