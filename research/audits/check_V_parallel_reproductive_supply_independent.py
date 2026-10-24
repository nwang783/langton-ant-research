from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','meet','pt','edge','walk','raws','mark','K')})
BUNDLE=ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036';manifest=json.loads((BUNDLE/'manifest.json').read_text())
for p,h in manifest['files'].items():assert hashlib.sha256((BUNDLE/p).read_bytes()).hexdigest()==h
selected={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};r=0j;A=1j;B=1;C=2+1j
rows=[];gates=[];srows=[];sgates=[];adjacent=[]
def bad(s,a,p,h):
 sc=chords(s);cc=chords(a,p,h)
 for j,x in enumerate(sc):
  for k,y in enumerate(cc):
   hit=meet(*x,*y)
   if hit:
    allow=(j==len(sc)-1 and k==0 and(p,h)==(G[s]['end'],G[s]['h'])and hit=={pt(x[1])})
    if allow:adjacent.append([s,a,*xy(p),h,j,k])
    else:return True
 return False
for s in(4,5,6):
 assert{r,A,B,C}<=G[s]['O']
 for a in IDS:
  req0=walk(raws[a]+mark)[2]
  for h in range(4):
   for slot in G[a]['I']:
    p=-rotation(slot,h);record=dict(source=s,consumer=a,head=[*xy(p),h])
    if(sum(xy(p))+h)%2:why='wrong_sector'
    elif bad(s,a,p,h):why='past_source_chord_contact'
    else:
     why='r_retirement_requires_both_A_and_B_already_absent';req={p+rotation(q,h):v for q,v in req0.items()};ins={p+rotation(q,h)for q in G[a]['I']};core={p+rotation(q,h)for q in K}
     assert(a,p,h)in((0,1,3),(4,3,3),(7,4+1j,3));assert req[A]is False and A not in ins and B not in ins and (req[B]is False or B in core)
     gates.append(record)
    record['reason']=why;rows.append(record)
 for q in(A,B):
  for a in IDS:
   for h in(0,2):
    p=q-rotation(selected[a],h);ctx={p+rotation(z,h)for z in G[a]['ctx']};record=dict(source=s,source_output=xy(q),consumer=a,head=[*xy(p),h])
    if(sum(xy(p))+h)%2:why='wrong_sector'
    elif r in ctx:why='causally_held_r_in_context'
    elif bad(s,a,p,h):why='past_source_chord_contact'
    else:
     why='B_to_D_or_DC_only_exact_age4';assert(q,a,p,h)in((B,0,1-1j,0),(B,1,1-1j,0));sgates.append(record)
    record['reason']=why;srows.append(record)
ref=json.loads((BUNDLE/'V_parallel_reproductive_supply.json').read_text());key=lambda x:(x['source'],x['consumer'],tuple(x['head']))
assert{key(x):x['reason']for x in rows}=={key(x):x['reason']for x in ref['r_retirement_rows']}
skey=lambda x:(key(x),tuple(x['source_output']))
assert{skey(x):x['reason']for x in srows}=={skey(x):x['reason']for x in ref['selected_rows']}
rc=Counter(x['reason']for x in rows);sc=Counter(x['reason']for x in srows);assert rc=={'wrong_sector':138,'past_source_chord_contact':129,'r_retirement_requires_both_A_and_B_already_absent':9};assert sc=={'causally_held_r_in_context':84,'past_source_chord_contact':6,'B_to_D_or_DC_only_exact_age4':6}
E=-1-1j;L=1+1j;Z=3-1j;assert set(edge(r))=={E,L}and set(edge(B))=={Z,L}
for g in gates:
 s,a=g['source'],g['consumer'];p=complex(*g['head'][:2]);h=g['head'][2];cc=chords(a,p,h)[0];assert cc[1]==L and meet(*cc,L,E)=={pt(L)}
 for j,ch in enumerate(chords(s)):assert meet(*ch,L,E)==({pt(E)}if j==0 else set())
for g in sgates:
 s,a=g['source'],g['consumer'];cc=chords(a,1-1j,0)[0];assert cc[1]==Z
 for i,(u,v)in enumerate(zip([Z,L,E],[L,E])):
  assert meet(*cc,u,v)==({pt(Z)}if i==0 else set())
  for j,ch in enumerate(chords(s)):assert meet(*ch,u,v)==({pt(E)}if i==1 and j==0 else set())
# Exact symbolic alpha_V in (1,2) units of pi/4. Tests both interval endpoints
# to certify all principal branches, then sums affine expressions identically.
def turns(angles):
 out=[]
 for (a,b),(c,d)in zip(angles,angles[1:]):
  coef=c-a;off=d-b
  while coef*Fraction(3,2)+off<=-4:off+=8
  while coef*Fraction(3,2)+off>=4:off-=8
  assert all(-4<=coef*x+off<=4 for x in(1,2)) and -4<coef*Fraction(3,2)+off<4
  out.append((coef,off))
 return out,(sum(x for x,y in out),sum(y for x,y in out))
rootturns={}
for a,alpha in[(0,(0,1)),(4,(1,0)),(7,(0,2))]:
 t,total=turns([(alpha[0],alpha[1]+2),(0,5),(1,0)])
 assert total==(1-alpha[0],-alpha[1]-2);rootturns[a]=t
bt,btotal=turns([(0,1),(0,3),(0,5),(1,0)]);assert btotal==(1,-1)
assert[n for n in range(20)if 2*(n-1)in(-8,8)]==[5];assert[n for n in range(20)if 2*n in(-8,8)]==[4]
out=dict(status='PASS V-base one parallel reproductive distinguished identity',manifest_sha256=hashlib.sha256((BUNDLE/'manifest.json').read_bytes()).hexdigest(),root_counts=dict(rc),selected_counts=dict(sc),root_rows=rows,selected_rows=srows,root_gates=gates,B_gates=sgates,adjacency_exceptions=adjacent,root_closing_turns=rootturns,B_closing_turns=bt,forced_r_age=5,forced_B_age=4,analytic='Literal classification makes original r survive while either A or B survives, also excluding simultaneous retirement. Held-r context removes all parallel reproductive A/B roles. Actual once-only C spending gives coefficient one. Exact held physical edge bridges, literal source C tails, final base contact, live-edge barrier and assumed center simplicity establish Jordan clocks5/4. No whole-cohort first-touch assumption.',scope='Simple-center complete-eight factor only, automatically a U-entry suffix. C-tail outputs separate. No V count bound, reproduction attainment, or capture theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(rc);print(sc)
