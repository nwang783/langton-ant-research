#!/usr/bin/env python3
"""Author-only finite and complete-white controls for additive port-type lemma."""
import json,random
from pathlib import Path
from check_extremal_read_coupling import ROOT,event_word,quotient,cycles,finite_control,D

def analyze(w,h):
 ev,d,hend=event_word(w,h);P=len(w);H={}
 for e in ev:
  r,k=quotient(e['p'],d);H.setdefault(r,[]).append(dict(e,stable=e['t']-k*P))
 for es in H.values():es.sort(key=lambda e:e['stable'])
 types={}
 for r,es in H.items():
  assert ''.join(e['c'] for e in es)==''.join('R' if i%2==0 else 'L' for i in range(len(es)))
  types[r]='singleton' if len(es)==1 else ('odd' if len(es)%2 else 'even')+('_same' if es[0]['hi']==es[-1]['hi'] else '_opposite')
 E={}
 for r,es in H.items():
  a=es[0];n=(r[0]+D[a['ho']][0],r[1]+D[a['ho']][1]);nr,k=quotient(n,d)
  if a['stable']+1!=H[nr][-1]['stable']+k*P:continue
  E[r]=(nr,k)
  assert types[r] in ('singleton','odd_opposite','even_same')
  assert types[nr] in ('singleton','odd_opposite','even_opposite')
 n={t:list(types.values()).count(t) for t in ('singleton','odd_opposite','odd_same','even_same','even_opposite')}
 A=n['singleton']+n['odd_opposite'];assert len(E)<=A+min(n['even_same'],n['even_opposite'])
 for cyc in cycles(E):
  tt=[types[r] for r in cyc['cells']];assert tt.count('singleton')==tt.count('odd_opposite')==len(tt)//2
 return {'period':P,'drift':d,'types':n,'edges':len(E),'cycles':cycles(E)}

def main():
 s=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());complete=[]
 for m in (1,2,3):
  for h in range(4):complete.append(analyze(s['word']*m,h))
 rng=random.Random(20261024);checked=0;exceptions=[]
 for i in range(120):
  pts=[(x,y) for x in range(-3,4) for y in range(-3,4)]
  B=set(rng.sample(pts,rng.randrange(15))) if i else set()
  _,_,_,tr,H,_=finite_control(B,(0,0),i%4,3000)
  for u,es in H.items():
   f,z=es[0],es[-1]
   if f['c']!='R' or f['t']==2999:continue
   v=tr[f['t']+1]['p'];fv,zv=H[v][0],H[v][-1]
   if zv['t']!=f['t']+1:continue
   if len(H[v])>1:
    if fv['t']==0:exceptions.append(['target_initial',i,u,v])
    else:assert fv['hi']!=zv['hi']
   if len(es)>1:
    if z['t']==2999:exceptions.append(['source_final',i,u,v])
    else:assert (f['hi']==z['hi'])==(z['c']=='L')
   checked+=1
 # Sharp minimal8 origin age. The finite seed is derived/replayed explicitly.
 w='RRRRLRRRR';ev,_,_=event_word(w);bits={};seed=set()
 for e in ev:
  q=e['p'];c=e['c']
  if q not in bits:
   bits[q]=c
   if c=='L':seed.add(q)
  else:assert bits[q]!=c;bits[q]=c
 tr=[];B=set(seed);p=(0,0);h=0
 for t,c in enumerate(w):
  assert ('L' if p in B else 'R')==c
  tr.append([t,list(p),h,c]);B.symmetric_difference_update((p,));h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 origin=[e for e in tr if e[1]==[0,0]];assert [e[3] for e in origin]==list('RLR');assert origin[-1][0]==8 and origin[0][2]==0 and origin[-1][2]==2
 result={'scope':'Author-only port-type controls, not independent audit.','complete_white':complete,'finite_factors':120,'marked_finite_edges_checked':checked,'boundary_exceptions':exceptions,'sharp_origin_age8':{'word':w,'seed':sorted(seed),'trace':tr,'final_black':sorted(B)}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'controls':len(complete),'finite_edges':checked,'exceptions':len(exceptions),'sharp_seed':sorted(seed)},indent=2))
if __name__=='__main__':main()
