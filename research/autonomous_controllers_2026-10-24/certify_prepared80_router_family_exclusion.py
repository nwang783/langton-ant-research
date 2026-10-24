#!/usr/bin/env python3
"""Proof-producing complete-WHITE exclusion for one UNBOUNDED macro family.
The finite box is derived from full-drift growth and checker charges in the note.
No guessed period, width, visit-count, or seed-size bound is used.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parent
M='RRRRLLLLRL';G=['RLRRRRL','RRRRL','RRRRLRLRLRRRRL','LRRL']
V=[(0,1),(1,0),(0,-1),(-1,0)]
def trace(w,h=0):
 p=(0,0);E=[]
 for t,c in enumerate(w):
  E.append({'t':t,'p':p,'h':h,'turn':c});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 return E,p,h

def quotient(p,d):
 j=0 if d[0] else 1;k=p[j]//d[j]
 return (p[0]-k*d[0],p[1]-k*d[1]),k

def check(a,b,c,e):
 w=''.join(M*n+g for n,g in zip([a,b,c,e],G));E,d,h=trace(w);P=len(w)
 assert h==0 and P==30+10*(a+b+c+e)
 assert d==(3+a-b-c+e,1+a+b-c+e)
 charges=[sum((1 if z['turn']=='R'else-1)for z in E if sum(z['p'])%2==par)for par in[0,1]]
 assert charges==[5+a-b+c+e,7-a+b-c-e]and sum(charges)==12
 base={'parameters':[a,b,c,e],'P':P,'full_drift':d,'checker_charges':charges,'word_sha256':hashlib.sha256(w.encode()).hexdigest()}
 if d==(0,0):return dict(base,status='NOT_TRANSLATING')
 H=defaultdict(list)
 for z in E:
  q,k=quotient(z['p'],d);H[q].append({'phase':z['t'],'lift':k,'canonical_time':z['t']-P*k,'turn':z['turn'],'actual_position':z['p']})
 for es in H.values():es.sort(key=lambda z:z['canonical_time'])
 for q,es in sorted(H.items()):
  for x,y in zip(es,es[1:]):
   if x['turn']==y['turn']:
    return dict(base,status='NONALTERNATING_ON_ANY_PREPARED_BOARD',witness={'representative':q,'complete_class_history':es,'same_turn_consecutive_phases':[x['phase'],y['phase']]})
 roots=[(q,es)for q,es in sorted(H.items())if es[0]['turn']=='L']
 assert roots,('WHITE CANDIDATE',a,b,c,e)
 q,es=roots[0]
 return dict(base,status='STABLE_BUT_BLACK_INPUT_REQUIRED',input_count=len(roots),output_count=sum(es[-1]['turn']=='R'for es in H.values()),witness={'representative':q,'complete_class_history':es,'BLACK_first_phase':es[0]['phase']})

def main():
 # These local vectors and charges are the finite ingredients of the symbolic
 # formulas, not sampled parameter extrapolation.
 heading=0;parity=0;routers=[];modules=[]
 for i,g in enumerate(G):
  E,d,h=trace(M,heading);assert h==heading
  delta=[sum((1 if z['turn']=='R'else-1)for z in E if (z['t']+parity)%2==j)for j in[0,1]]
  modules.append({'run':i,'incoming_heading':heading,'incoming_checker_parity':parity,'module_word':M,'module_drift':d,'checker_charge':delta})
  E,d,hh=trace(g,heading)
  routers.append({'router':i,'word':g,'incoming_heading':heading,'outgoing_heading':hh,'drift':d,'checker_charge':[sum((1 if z['turn']=='R'else-1)for z in E if(z['t']+parity)%2==j)for j in[0,1]],'full_local_geometry':E})
  heading=hh;parity=(parity+len(g))%2
 assert heading==parity==0
 assert [r['module_drift']for r in modules]==[(1,1),(-1,1),(-1,-1),(1,1)]
 assert [r['checker_charge']for r in modules]==[[1,-1],[-1,1],[1,-1],[1,-1]]
 assert [sum(r['drift'][i]for r in routers)for i in[0,1]]==[3,1]
 assert [sum(r['checker_charge'][i]for r in routers)for i in[0,1]]==[5,7]
 rows=[check(a,b,c,e)for a in range(7)for e in range(7-a)for b in range(8)for c in range(9)]
 assert len(rows)==2016
 counts=Counter(x['status']for x in rows);stable=[x for x in rows if x['status']=='STABLE_BUT_BLACK_INPUT_REQUIRED']
 source=R.parent/'sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md'
 J={'status':'AUTHOR ALL-PARAMETER FAMILY EXCLUSION; independent audit pending','family':'M^a A M^b B M^c C M^e D, all four exponents independently nonnegative integers','M':M,'routers':G,'derived_parameter_box':'a+e<=6, b<=7, c<=8; no arbitrary cap','scope':'Excludes a complete WHITE translating front only in this exact fixed-router family. Prepared waves survive. No general winding or controller classification.','growth_bound_dependency':{'path':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'section':'2.3 residue monodromy: g>=2max(abs(dx),abs(dy))'},'module_geometry':modules,'router_geometry':routers,'symbolic_identities':{'P':'30+10(a+b+c+e)','X':'3+a-b-c+e','Y':'1+a+b-c+e','g_even':'5+a-b+c+e','g_odd':'7-a+b-c-e','growth':12,'bound_equalities':['2(a+e)=Y-g_odd+6','2b=Y-X+2','2c=10-X-g_odd']},'counts':dict(counts),'all_derived_box_cases':rows,'stable_prepared_cases':stable}
 (R/'prepared80_router_family_exclusion_certificate.json').write_text(json.dumps(J,indent=2)+'\n')
 print('PASS derived2016 cover',dict(counts));print('stable prepared',[(z['parameters'],z['P'],z['full_drift'],z['input_count'])for z in stable])
if __name__=='__main__':main()
