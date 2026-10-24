#!/usr/bin/env python3
"""Author controls for all-cap extremal-read coupling. Not independent audit."""
import json,random,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'computability'))
from check_rigid_reachability import State,forward,D
from periodic_tail_checker import first_mismatch

def quotient(q,d):
 j=0 if d[0] else 1
 k=q[j]//abs(d[j]);k=k if d[j]>0 else -k
 return (q[0]-k*d[0],q[1]-k*d[1]),k

def event_word(w,h=0,p=(0,0)):
 ev=[];start=p
 for t,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R' else -1))%4
  ev.append(dict(t=t,p=p,hi=hi,ho=h,c=c));p=(p[0]+D[h][0],p[1]+D[h][1])
 return ev,(p[0]-start[0],p[1]-start[1]),h

def cycles(G):
 out=[];seen=set()
 for start in G:
  at=start;path=[];ind={}
  while at in G and at not in ind and at not in seen:
   ind[at]=len(path);path.append(at);at=G[at][0]
  if at in ind:
   c=path[ind[at]:];out.append({'cells':c,'winding':sum(G[x][1] for x in c)})
  seen.update(path)
 return out

def front(w,h=0):
 ev,d,hend=event_word(w,h);assert hend==h and d!=(0,0);P=len(w)
 H={}
 for e in ev:
  r,k=quotient(e['p'],d);H.setdefault(r,[]).append(dict(e,stable=e['t']-k*P,k=k))
 for es in H.values():es.sort(key=lambda e:e['stable'])
 bad=[];blackfirst=[]
 for r,es in H.items():
  if any(e['c']==f['c'] for e,f in zip(es,es[1:])):bad.append({'cell':r,'word':''.join(e['c'] for e in es)})
  if es[0]['c']=='L':blackfirst.append(r)
 F={};K={};E={};EL={};types={}
 for r,es in H.items():
  a,z=es[0],es[-1]
  n=(r[0]+D[a['ho']][0],r[1]+D[a['ho']][1]);nr,k=quotient(n,d);F[r]=(nr,k)
  if z['c']=='L':
   n=(r[0]-D[z['hi']][0],r[1]-D[z['hi']][1]);K[r]=quotient(n,d)
  if a['stable']+1==H[nr][-1]['stable']+k*P:
   E[r]=(nr,k)
   if H[nr][-1]['c']=='L':EL[r]=(nr,k)
  types[r]='singleton' if len(es)==1 else ('odd_opposite' if len(es)%2 and a['hi']!=z['hi'] else ('odd_same' if len(es)%2 else 'even'))
 white=not bad and not blackfirst
 if white:
  assert all(c['winding']==-1 for c in cycles(F))
  assert all(c['winding']==1 for c in cycles(K))
  assert not any(v[0] in EL for v in EL.values())
  incoming={v[0] for v in E.values()}
  for r in E:
   if r in incoming:assert types[r] in ('singleton','odd_opposite')
  A=sum(v in ('singleton','odd_opposite') for v in types.values());N=len(H)
  assert 2*len(E)<=2*A+(N-A)
  cf=cycles(F);ck=cycles(K)
  chosen=[]
  # Each item is a physical source-event phase in the supplied event period.
  for cyc in cf:
   for r in cyc['cells']:chosen.append((H[r][0]['t'],0))
  for cyc in ck:
   for target in cyc['cells']:chosen.append(((H[target][-1]['t']-1)%P,1))
  tags={}
  for phase,tag in chosen:tags.setdefault(phase,set()).add(tag)
  overlaps=[phase for phase,s in tags.items() if len(s)==2]
  CH=sum(ev[t]['ho']%2 for t in overlaps);CV=len(overlaps)-CH
  Ex=sum(D[ev[t]['ho']][0] for t in overlaps);Ey=sum(D[ev[t]['ho']][1] for t in overlaps)
  LF=sum(len(c['cells']) for c in cf);LL=sum(len(c['cells']) for c in ck);kk=len(cf)+len(ck)
  delta=CH-CV;X=(1+kk)*d[0]+Ex;Y=(1+kk)*d[1]+Ey
  assert P>=LF+LL-len(overlaps)+max(2*abs(X)-delta,2*abs(Y)+delta)
  assert 2*len(overlaps)<=min(LF,LL)
  for cyc in cycles(E):
   assert cyc['winding']==-1
   assert all(types[r] in ('singleton','odd_opposite') for r in cyc['cells'])
   assert any(types[r]=='odd_opposite' for r in cyc['cells'])
   assert sum(H[r][-1]['stable']-H[r][0]['stable'] for r in cyc['cells'])==P+len(cyc['cells'])
 return {'period':P,'drift':d,'growth':w.count('R')-w.count('L'),'classes':len(H),'complete_white':white,'bad_alternation':bad,'black_first_classes':blackfirst,'types':{v:list(types.values()).count(v) for v in sorted(set(types.values()))},'first_cycles':cycles(F),'last_L_reverse_cycles':cycles(K),'first_last_edges':[{'source':r,'target':v[0],'voltage':v[1]} for r,v in E.items()],'first_last_L_edges':[{'source':r,'target':v[0],'voltage':v[1]} for r,v in EL.items()]}

def finite_control(B,p,h,T):
 trace=[]
 for t in range(T):
  c='L' if p in B else 'R';hi=h;h=(h+(1 if c=='R' else -1))%4
  trace.append(dict(t=t,p=p,hi=hi,ho=h,c=c));B.symmetric_difference_update((p,));p=(p[0]+D[h][0],p[1]+D[h][1])
 H={}
 for e in trace:H.setdefault(e['p'],[]).append(e)
 E={};EL={}
 for r,es in H.items():
  a=es[0]
  if a['c']!='R' or a['t']==T-1:continue
  n=trace[a['t']+1]['p'];z=H[n][-1]
  if z['t']==a['t']+1:
   E[r]=n
   if z['c']=='L':EL[r]=n
 incoming=set(E.values());exceptions=[]
 for r,n in E.items():
  if r not in incoming:continue
  es=H[r];a,z=es[0],es[-1]
  if a['t']==0 or z['t']==T-1:exceptions.append(r);continue
  assert len(es)==1 or (z['c']=='R' and a['hi']!=z['hi'])
 for r,n in EL.items():
  if n in EL:
   a,z=H[n][0],H[n][-1]
   assert a['t']==0 or z['t']==T-1
 return len(E),len(EL),exceptions,trace,H,EL

def main():
 standard=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
 controls=[]
 for mult in (1,2,3):
  for rot in range(4):controls.append(front(standard['word']*mult,(standard['heading']+rot)%4))
 rng=random.Random(20261024);finite=0;boundary=0;literal=None
 for i in range(120):
  pts=[(x,y) for x in range(-3,4) for y in range(-3,4)]
  B=set(rng.sample(pts,rng.randrange(15))) if i else set()
  e,el,ex,tr,H,EL=finite_control(B,(0,0),i%4,3000)
  finite+=1;boundary+=len(ex)
  if i==0:
   for u,v in EL.items():
    if H[u][0]['t']>0 and H[v][-1]['t']<2999:
     literal={'initial_black':[],'initial_pose':[[0,0],0],'source':u,'target':v,'source_first_time':H[u][0]['t'],'target_last_time_within_3000':H[v][-1]['t'],'source_first_heading':H[u][0]['hi'],'target_last_heading':H[v][-1]['hi'],'limitation':'Last means within the actual 3000-read finite factor, not all future time.'};break
 D102=json.loads((ROOT/'K1_pipeline_detours_2026-10-23/prepared_D102_black_helper_connected_control.json').read_text())
 inv=''.join('L' if c=='R' else 'R' for c in D102['word'][::-1])
 candidates={'D102':front(D102['word']),'inverse_D102':front(inv,2)}
 result={'scope':'Author-only controls; no classification or capture theorem.','standard_controls':controls,'finite_factor_controls':finite,'finite_reads':finite*3000,'boundary_exceptions_retained':boundary,'finite_positive_marked_edge':literal,'D102_diagnostics':candidates}
 dest=Path(__file__).with_suffix('.json');dest.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'standard_control_count':len(controls),'finite_controls':finite,'boundary_exceptions':boundary,'finite_positive':literal,'D102':{k:{x:v[x] for x in ('period','drift','growth','complete_white','bad_alternation','black_first_classes')} for k,v in candidates.items()}},indent=2))
if __name__=='__main__':main()
