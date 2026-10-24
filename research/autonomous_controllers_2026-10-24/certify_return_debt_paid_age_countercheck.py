#!/usr/bin/env python3
"""Replay one explicit79-event partial clock calendar and its geometric-only filling.
The filled word is rejected by physical color chronology. This is not a controller.
"""
from pathlib import Path
import json,hashlib
from check_extremal_read_coupling import event_word,front
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0));T=lambda p:3*p[1]-p[0]
def turn(h,hh):
 a=(hh-h)%4;assert a in(1,3);return'R'if a==1 else'L'
def safe(p,h):
 for s in(1,-1):
  pp=p;hh=h;ok=True
  for _ in range(4):hh=(hh+s)%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1]);ok &= T(pp)>=13
  if ok:return s
 return None

def main():
 q=json.load(open(R/'return_debt_paid_age_clock_result.json'));P=q['period'];lev=q['levels'];H={int(t):h for t,h in q['source_histories'].items()};C=q['chains'];X=q['canonical_chain_starts'];S=q['phases'];Z=q['reduced_lifts'];order=q['fixed_order'];A=[];clocks={}
 for c,ch in enumerate(C):
  assert X[c]==S[c]+P*Z[c]
  for a,((i,j),k)in enumerate(ch):
   t=lev[i];clock=X[c]+a-k*P;phase=clock%P;lap=clock//P;p=(-t-3*lap,-lap);clocks[t,j]=clock
   assert clock%4==t%2;assert phase==S[c]+a
   A.append({'phase':phase,'position':p,'heading':H[t][j],'turn':'R'if j%2==0 else'L','T':t,'rank':j,'canonical_clock':clock})
 assert len(A)==79 and len({a['phase']for a in A})==79
 for t,hs in H.items():
  for j in range(len(hs)-1):assert clocks[t,j+1]-clocks[t,j]>=4 and(clocks[t,j+1]-clocks[t,j])%4==0
 for c,ch in enumerate(C):
  for((i,j),k),((ii,jj),kk)in zip(ch,ch[1:]):assert clocks[lev[i],j]+1==clocks[lev[ii],jj]+(kk-k)*P
 gap_records=[];W=''
 for c,b,o in zip(order,order[1:]+order[:1],q['travel_obligations']):
  assert(c,b)==(o['source_chain'],o['target_chain']);ch=C[c]
  W+=''.join('R'if j%2==0 else'L'for(i,j),k in ch)
  path=[(tuple(p),h)for p,h,flag in o['geometric_unknown_region_path']];assert all(T(p)>=13 for p,h in path)
  for(p,h),(pp,hh)in zip(path,path[1:]):assert pp==(p[0]+D[hh][0],p[1]+D[hh][1]);turn(h,hh)
  m=o['actual_distance'];extra=m-(len(path)+1);assert extra>=0 and extra%4==0
  pad=next((i for i,(p,h)in enumerate(path)if safe(p,h)is not None),None);sg=safe(*path[pad])if pad is not None else None;assert extra==0 or pad is not None;gap=''
  for a,(p,h)in enumerate(path):
   if a==pad:gap+=('R'if sg==1 else'L')*extra
   if a+1<len(path):gap+=turn(h,path[a+1][1])
   else:
    (ii,jj),kk=C[b][0];gap+=turn(h,H[lev[ii]][jj])
  assert len(gap)==m-1;W+=gap;gap_records.append({'from':c,'to':b,'duration':m,'unknown_read_count':m-1,'base_path':path,'padding_at':pad,'padding_turn_sign':sg,'padding_steps':extra})
 assert len(W)==P
 A.sort(key=lambda a:a['phase']);start=A[0]['position'];heading=A[0]['heading'];ev,d,hend=event_word(W,heading,start);assert d==(3,1)and hend==heading
 for a in A:
  e=ev[a['phase']];assert e['p']==a['position']and e['hi']==a['heading']and e['c']==a['turn']
 for e in ev:
  if e['t']not in{a['phase']for a in A}:assert T(e['p'])>=13
 prev={};conflict=None;first_black=set()
 for e in ev:
  p=e['p']
  if p not in prev:
   if e['c']=='L':first_black.add(p)
  elif prev[p]['c']==e['c'] and conflict is None:conflict={'earlier':prev[p],'later':e,'reason':'Consecutive physical reads require the same turn; impossible on ANY initial coloring.'}
  prev[p]=e
 assert conflict is not None
 summary=front(W,heading);assert not summary['complete_white']
 result={'scope':__doc__,'period_parameter':P,'specified_named_read_count':79,'unassigned_read_count':P-79,'full_drift':d,'canonical_chain_starts':X,'chain_phases':S,'chain_lifts':Z,'named_events':A,'gaps':gap_records,'geometric_filled_word':W,'initial_position':start,'initial_heading':heading,'first_actual_color_conflict':conflict,'retained_complete_front_check':summary,'warning':'Every gap has a geometric alternating-axis path entirely in unknown T>=13, but the displayed filling is NOT a legal finite factor on any initial board. No full-odd inventory or autonomous controller is claimed. The underlying79-event interface remains OPEN because other fillings have not been exhausted.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['return_debt_paid_age_clock_result.json','partial_drift31_graph.py','check_extremal_read_coupling.py','physical_return_debt_certificate.json']}}
 (R/'return_debt_paid_age_countercheck_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('PASS79 explicit phase clocks;18 geometric unknown-region gaps; filling rejected at',conflict['earlier']['t'],conflict['later']['t'],conflict['later']['p'])
if __name__=='__main__':main()
