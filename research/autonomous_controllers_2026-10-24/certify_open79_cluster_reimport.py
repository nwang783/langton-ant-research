#!/usr/bin/env python3
"""All-length first-contact implication and two genuine finite prepared controls.
No all-gap stock sign, factor repetition or controller is claimed.
"""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0))
X=(2,1);U=(0,1);Q=(1,1);A=(1,0);B=(0,0);C=(-1,0);Z=(2,0);CL={X,U,Q,A};T=lambda p:3*p[1]-p[0]+11
H9='WWWEWW';H10='SNSSSN';H11='WEEEEEEWWEEEWEWE';H12='SSNNNSNSSSSSSSSSSS'
def replay(f):
 black=set(map(tuple,f['initial_black']));p=tuple(f['initial_position']);h=f['initial_heading'];ev=[];last={}
 for t,c in enumerate(f['word']):
  assert c==('L'if p in black else'R');ev.append({'time':t,'position':p,'incoming_heading':h,'turn':c});last[p]=t;black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 contact=tuple(f['contact_position']);assert ev[-1]['position']==contact and ev[-1]['incoming_heading']==2
 assert all(e['position']not in CL and T(e['position'])>=13 for e in ev[7:-1])
 assert all(e['position']!=C for e in ev[7:]);assert ev[6]['position']==C
 assert ev[-1]['turn']==('R'if contact==U else'L')
 if contact==U:assert [e['turn']for e in ev if e['position']==U]==['L','R']
 if contact==X:assert [e['incoming_heading']for e in ev if e['position']==X]==[2,2]and[e['turn']for e in ev if e['position']==X]==['R','L']
 return {**f,'events':ev,'complete_final_black':sorted(black),'final_position':p,'final_heading':h}
def main():
 assert H11[9]=='E'and H10[3]=='S'and H12[1]=='S'
 assert [j for j,h in enumerate(H9)if h=='E']==[3]
 # Assuming no prior cluster reimport, every following turn is forced.
 tail=[(C,2,'L'),(B,1,'L'),(U,0,'R'),(Q,1,'R'),(A,2,'L'),(Z,1,'L'),(X,0,'L')]
 for(p,h,c),(pp,hh,cc)in zip(tail,tail[1:]):
  out=(h+(1 if c=='R'else-1))%4;assert out==hh and pp==(p[0]+D[out][0],p[1]+D[out][1])
 assert tail[-1][1]!=2
 first_contacts=[{'cell':'U','incoming_heading':'S','turn':'R','immediate_source':(0,2),'source_normal_level':17,'meaning':'Restores the guide erased by its prior L. This read creates BLACK; it is not BLACK input consumption.'}, {'cell':'X','incoming_heading':'S','turn':'L','immediate_source':(2,2),'source_normal_level':15,'meaning':'Consumes the actual BLACK lifetime born at the owned first R at X.'}]
 raw=json.load(open(R/'open79_cluster_reimport_discovery.json'));controls=[replay(f)for f in raw['found']];assert sorted(len(f['word'])for f in controls)==[17,21];assert sorted(len(f['initial_black'])for f in controls)==[6,8]
 # Exact subsequent continuations of just these frozen seeds are diagnostics,
 # not failures of every possible exterior completion.
 continuations=[]
 for f in controls:
  black=set(map(tuple,f['initial_black']));p=X;h=2;reads=[];Ctimes=[]
  for t in range(200):
   c='L'if p in black else'R';reads.append((t,p,h,c))
   if p==C:Ctimes.append((t,h,c))
   if len(Ctimes)==2:break
   black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
  assert len(Ctimes)==2
  if tuple(f['contact_position'])==U:
   assert Ctimes[-1]==(142,0,'L');fail={'time':142,'cell':C,'actual_incoming':'N','required_next_incoming':'S','owned_rank':9}
  else:
   xr=[e for e in reads if e[1]==X];assert xr[3]==(32,X,2,'L');fail={'time':32,'cell':X,'actual_incoming':'S','required_next_incoming':'N','owned_rank':3}
  continuations.append({'contact_branch':f['contact_position'],'next_C_return':Ctimes[-1],'specific_supplied_history_failure':fail,'scope':'These particular finite seeds only. Changing unprescribed exterior fields is not excluded.'})
 out={'scope':__doc__,'cluster':sorted(CL),'barrier_cell':B,'next_B_incoming':'E from C','possible_first_contacts':first_contacts,'forced_tail_if_cluster_avoided':tail,'positive_finite_controls':controls,'specific_seed_continuation_diagnostics':continuations,'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_SHORT_GAP_FORCES_PREPARATION_AGE.md','physical_return_debt_certificate.json']},'limits':'During the next C first-return excursion, first cluster reimport has one of two north-entry ports. No stock increase/decrease sign or repeated-block growth follows. Controls end at first reimport; neither is a regenerative controller or a completed supplied interface.'}
 (R/'open79_cluster_reimport_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS exact all-length two-port logic, full prepared17/21 fields and scoped seed continuation failures')
if __name__=='__main__':main()
