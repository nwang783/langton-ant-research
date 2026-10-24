from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';ns={'__file__':str(SELF.parent/'check_canonical_birth_rank3_balance_independent.py')};exec(Path(ns['__file__']).read_text().split('expected=')[0],ns);base=ns['rows'];outs=ns['departures'];H='NESW';vec={'N':1j,'E':1,'S':-1j,'W':-1};cp={'A':1,'Z':0,'Y':1j,'B':1+1j};op={'A':1-1j,'Z':-1-1j,'Y':-1+1j,'B':1+1j}
def locate(row,ll,q):
 cell=lambda p:ll+(1+1j)/2+(p-(1+1j)/2)*1j**q
 hh={cell(p):''.join(H[(H.index(h)-q)%4]for h in hist)for p,hist in zip(cp.values(),row[0])};heights={ll:0,ll+op['A']*1j**q:0}
 for v,h in zip('ZYB',row[1]):heights[ll+op[v]*1j**q]=0 if h=='M'else-int(h[2:])
 entry=cell(1);bd=[(cell(cp[v]),H[(H.index(d)-q)%4])for v,d in[('A','W'),('Z','N'),('Y','E'),('B','S')]]
 return hh,heights,entry,bd

def close(packages):
 hh={};ht={};births=[]
 for row,ll,q in packages:
  hs,he,e,bd=locate(row,ll,q)
  if any(p in hh and hh[p]!=h for p,h in hs.items())or any(p in ht and ht[p]!=h for p,h in he.items()):return None
  hh.update(hs);ht.update(he);births.append((e,bd))
 nodes=[(p,r)for p,h in hh.items()for r in range(len(h))];edges=[];oo={p:outs(h)for p,h in hh.items()}
 for p,h in hh.items():edges.extend(((p,r),(p,r+1),4)for r in range(len(h)-1))
 for p,h in hh.items():
  for d in'EW'if h[0]in'NS'else'NS':
   q=p+vec[d]
   if q not in hh:continue
   aa=[(p,r)for r,c in enumerate(oo[p])if c==d];bb=[(q,r)for r,c in enumerate(hh[q])if c==d]
   if len(aa)!=len(bb):return None
   for u,v in zip(aa,bb):edges.extend([(u,v,1),(v,u,-1)])
 for e,bd in births:
  for p,d in bd:
   if d not in oo[p]:return None
   v=(p,oo[p].index(d))
   if v!=(e,1):edges.append(((e,1),v,1))
 dist={n:0 for n in nodes}
 for _ in nodes:
  changed=False
  for u,v,k in edges:
   if dist[v]<dist[u]+k:dist[v]=dist[u]+k;changed=True
  if not changed:return hh,ht
 return None

def find(t):return next(r for r in base if r[0]==t)
F=find(('NNSN','WWEW','NSSS','EEWE'));I=find(('NNSN','WWWE','NSNN','WEEE'))
q1=next(r for r in base if locate(r,-3+1j,3)[0]=={-2+1j:'NSSS',-2+2j:'EWEE',-3+1j:'EEWE',-3+2j:'NNNS'})
fixed=[(F,0,0),(F,-2,0),(I,-1+1j,3),(q1,-3+1j,3)]
priors=[]
for J,G in product([row for row in base if all(len(h)%2==0 for h in row[0])],repeat=2):
 packs=fixed+[(J,-1-1j,1),(G,1+1j,3)];z=close(packs)
 if z is not None:priors.append((packs,z))
assert len(priors)==12
even=[r for r in base if r[0][0]=='NNSN'and all(len(h)%2==0 for h in r[0])];assert len(even)==7
results=[];candidates=0
for packs,(oldhs,ht)in priors:
 for rr,qq,rotation in product(even,even,(0,2,3)):
  rh,_,_,_=locate(rr,-3-1j,1);qh,_,_,_=locate(qq,-4,rotation)
  if rh.get(-2)!='WWEW'or outs(rh[-2-1j]).count('E')!=oldhs[-1-1j].count('E')or rh[-3].count('S')!=1:continue
  if qh.get(-3+1j)!='EEWE'or qh.get(-3)!=rh[-3]:continue
  candidates+=1;z=close(packs+[(rr,-3-1j,1),(qq,-4,rotation)])
  if z is not None:results.append((z,rr,qq,rotation))
assert(candidates,len(results))==(120,18)
summary=Counter()
for(hh,ht),rr,qq,q in results:
 assert hh[-1-1j]=='WWWE'and hh[-2-1j]=='SSSN';assert(hh[-3-1j],hh[-3])in[('WWWE','NNSN'),('WEWW','SNNN')]
 summary[(hh[-3-1j],hh[-3],q,qq[0])]+=1
assert len(summary)==6
# Half-turn selected Q2 is the rotated canonical positive duplicator.
half=locate(F,-4,2)[0];assert half=={-4+1j:'SSNS',-3+1j:'EEWE',-3:'SNNN',-4:'WWEW'}
# Exhaust literal boundary side transitions, all complete ranks.
cross=lambda z,w:(z.conjugate()*w).imag
crossings=[]
for name,hist,d in[('Z','WWEW',-1-1j),('e','NNSN',-1+1j),('x','WWEW',-1-1j),('m','SNNN',-1+1j)]:
 os=outs(hist);events=[]
 for r,(inn,out)in enumerate(zip(hist,os)):
  side0=cross(d,-vec[inn]);side1=cross(d,vec[out]);assert side0 and side1;event='entry'if side0<0<side1 else'exit'if side1<0<side0 else'left_stay'if side0>0 else'right_stay';events.append(event)
 assert events==(['exit','left_stay','entry','left_stay']if name!='m'else['entry','left_stay','exit','left_stay']);crossings.append((name,events))
notes={}
for name,pref in [('zero_output_activated_child_repeat_or_half_turn_gate.md','4670f374'),('half_turn_supplier_cannot_return_to_same_Gamma_v2.md','7ef1fd92')]:
 sh=hashlib.sha256((D/name).read_bytes()).hexdigest();assert sh.startswith(pref);notes[name]=sh
out={'status':'PASS zero-output Q2 repeat-or-half-turn closure and conditional same-Gamma cursor-ear exclusion','notes':notes,'prior_rows':12,'new_candidates':120,'necessary_rows':18,'six_profiles':[{'s':k[0],'m':k[1],'rotation':k[2],'Q2':k[3],'count':v}for k,v in summary.items()],'complete_chord_crossings':crossings,'analytic':['Independently reconstruct all110 canonical histories and merge all literal shared ordinal ports, equal neighbor heights, same-cell >=4 gaps and canonical first-boundary minima. The old fixed six-face closure has12 rows; adding both even flag1 squares gives120 candidates and18 survivors in six profiles. No off-curve K1 clock order is imported.','Q2 has a genuine flag1 child Q1, so zero output rules out incoming flag0: it would have positive q and hence one of the excluded odd O profiles. This justifies the seven-even-flag1 inventory, rather than assuming Q2 is a duplicator.','WWWE/NNSN gives the actual repeated canonical path P0->R->Q2->Q1, four possible Q2 histories. WEWW/SNNN makes R a flag1 leaf; saturation then forces the half-turned actual Q2 duplicator, selecting WWEW rather than its preliminary EWWW alternative. Its parent is upper-left, not R. No off-Gamma status or repetition follows solely from this local table.','For the ear theorem, exact ports give u.L1=beta-4, g.L1=beta-5, f.R0=beta-6, j.R0=beta-7, k.L1=beta-8, and Q2 birth=k.R0-1<=beta-13. If Q2 lies on the same physical Gamma, increasing selected births force it before consecutive D,G. The physical displacement4 requires at least4 contacts to D.','D->J->P0->R->Q2 is an embedded zigzag, interior disjoint from Gamma because the first three faces are actual off-cycle descendants. C-contact edges cannot cross another C edge except by sharing its endpoint/contact. The chord approaches the LEFT side at both endpoints; together with the forward Gamma arc it bounds a finite LEFT ear.','Every physical crossing is at a listed primal contact; open face-interior joins contain no cursor path. Direct side computation gives exit/stay/entry/stay at the three negative contacts and entry/stay/exit/stay at positive m. Every rank and optional L3 is retained.','K1 orders the first two Gamma R0 exits before its first R2 entry and before alpha=B(D). All three canonical-chord R2 entries occur after alpha, by genuine child birth order. Only m.R0 can enter earlier. Translation by nonzero drift puts the cursor outside this bounded physical ear at sufficiently negative time. Two exits with at most one prior entry are impossible. Thus Q2 cannot lie on SAME Gamma and remains LEFT by the final unused contact.'],'scope':'Exact zero-output half-turn local mode and K1 same selected curve only. No cross-Gamma transfer exclusion, ancestry iteration, original-fuel charge or general K1/capture conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(candidates,len(results))
