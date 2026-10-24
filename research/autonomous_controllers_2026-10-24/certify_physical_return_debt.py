#!/usr/bin/env python3
"""Exact physical short-return charges, a specified OPEN debt interface,
and prepared finite controls. Not a complete gap transfer or controller.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
from partial_drift31_graph import graph,quotient31
from certify_drift31_read_minimum import returns_to
R=Path(__file__).resolve().parent
D=((0,1),(1,0),(0,-1),(-1,0))
STR=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW','NNSNSSSS','WWWEWW','SNSSSN','WEEEEEEWWEEEWEWE','SSNNNSNSSSSSSSSSSS']

def replay(word,B,p=(0,0),h=0):
 initial=sorted(B);B=set(B);ev=[]
 for t,c in enumerate(word):
  actual='L'if p in B else'R';assert actual==c
  ev.append({'time':t,'position':p,'incoming_heading':h,'turn':c});B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return{'word':word,'initial_black':initial,'events':ev,'final_black':sorted(B),'final_position':p,'final_heading':h}

def diamond(n):
 assert n>=2
 moves=([1,0]*n)+([1,2]*n)+([3,2]*n)+([3,0]*n)
 p=(0,0);h=0;seen=set();B=set();word='';points=[]
 for hh in moves:
  assert p not in seen;seen.add(p);points.append(p);s=(hh-h)%4;assert s in(1,3);c='R'if s==1 else'L';word+=c
  if c=='L':B.add(p)
  h=hh;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert p==(0,0)and h==0 and len(seen)==8*n and len(B)==4*n-2
 z=replay(word+'L',B);assert len(z['final_black'])==4*n+1
 assert z['events'][0]['position']==z['events'][-1]['position']==(0,0)
 assert z['events'][0]['incoming_heading']==z['events'][-1]['incoming_heading']==0
 z['n']=n;z['first_return_duration']=8*n;z['scope']='Prepared finite factor; initial BLACK support grows as4n-2. Not a WHITE complete front or repeatable module.'
 return z

def interface():
 H={t:tuple('NESW'.index(c)for c in s)for t,s in enumerate(STR)}|{-3:(),-2:(),-1:()};stages=[]
 for target in(11,12,13):
  levels=sorted(t for t in H if t<target);hs=[H[t]for t in levels];kind,G=graph(hs,levels);assert kind=='open'
  _,paths=returns_to(hs,G,target);cross=[]
  for ch in G['chains']:
   (i,j),a=ch[0];t=levels[i];h=H[t][j];ps=(-t-D[h][0],-D[h][1]);qs,ks=quotient31(ps)
   (i,j),b=ch[-1];t=levels[i];ho=(H[t][j]+(1 if j%2==0 else-1))%4;pd=(-t+3*b+D[ho][0],b+D[ho][1]);qd,kd=quotient31(pd)
   cross.append({'source_level':-qs[0],'target_level':-qd[0],'voltage':kd-ks,'outside_read_distance':len(ch)+1,'chain':ch})
  assert sum(c['outside_read_distance']for c in cross)==G['event_count']+len(cross)
  stages.append({'target_level':target,'named_histories':{t:H[t]for t in levels},'open_graph':G,'same_physical_returns':paths,'all_boundary_chains':cross})
 assert [p['duration']for p in stages[0]['same_physical_returns']]==[4]
 assert sorted(p['duration']for p in stages[1]['same_physical_returns'])==[4,8]
 assert not stages[2]['same_physical_returns']
 assert stages[2]['open_graph']['event_count']==79 and len(stages[2]['all_boundary_chains'])==18
 C=Counter((z['source_level'],z['target_level'])for z in stages[2]['all_boundary_chains']);assert C=={(13,14):4,(15,13):7,(15,14):7}
 assert sorted(z['outside_read_distance']for z in stages[2]['all_boundary_chains'])[-1]==36
 return stages

def main():
 local=[]
 for v in range(4):
  for alpha in(-1,1):
   u=(v+alpha)%4
   for sigma in(-1,1):
    # Source incoming solves turn sigma -> departure u. Target incoming v.
    hin=(u-sigma)%4;turns=[sigma]+[alpha]*3+[-sigma]
    p=(0,0);h=hin;ev=[]
    for t,s in enumerate(turns):
     ev.append((p,h,s));h=(h+s)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
    assert ev[4][0]==(0,0)and ev[4][1]==v
    charged=0 if sigma==alpha else 4
    assert ev[charged][1]==v and ev[charged][2]==alpha
    local.append({'incoming_return_heading':v,'loop_orientation':alpha,'departure_heading':u,'source_turn':sigma,'charged_endpoint':charged,'events':ev})
 assert len(local)==16
 sharp=replay('RLLLL',{(0,-1),(1,-1),(1,0)},h=1);assert not sharp['final_black']
 result={'scope':__doc__,'sixteen_rotated_endpoint_charge_cases':local,'sharp_five_read_prepared_control':sharp,'arbitrary_length_prepared_first_return_controls':[diamond(n)for n in(2,3,5,20)],'specified_open_debt_interface':interface(),'limits':'The79-event object is a complete-history necessary OPEN graph only, with outside classes UNKNOWN. No actual finite factor, complete phase clock, full period or growth8 completion is asserted. Its separate fixed-period positive clock probe is UNKNOWN. Prepared finite controls do not refute a WHITE growth8-specific debt theorem.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['partial_drift31_graph.py','certify_drift31_read_minimum.py','DRIFT31_EVEN_GAP_CHAIN_MASS_ADDENDUM.md']}}
 (R/'physical_return_debt_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('PASS16 charge cases, full prepared5 and diamond controls; supplied OPEN79 debt1->2->0 retains18 chains')
if __name__=='__main__':main()
