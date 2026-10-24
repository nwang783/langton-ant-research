from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];A=R/'terminal_DCC_ordinary_owner_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(A/'manifest.json')=='366d13a96532e69277168e25e2c48b52862660994acc476ebe4bbb078add8a89'
man=json.loads((A/'manifest.json').read_text())
for f,h in man['files'].items():assert sha(A/f)==h
for f,h in man['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,rot,xy,center,meet=[ns[k]for k in ('W','M','K','tr','rot','xy','center','meet')]
J=json.loads((A/'terminal_DCC.json').read_text());G={a:tr(W[a])for a in 'DCVUFQB'}
assert [(G[a]['p'],G[a]['h'])for a in 'DCVU']==[(1+1j,0),(1j,3),(1+3j,0),(4j,0)]
# Bind literal signs explicitly; all subsequent N/E x cones are sound.
assert all((rot(h)*G[a]['p']).real>=0 for h in (0,1)for a in 'DVU')
assert all((rot(3)*G[a]['p']).real<0 for a in 'DVU')
assert all(G[a]['p'].imag>=1 for a in 'DVU')
contexts={a:tr(W[a]+M)for a in G};I={a:{q for q,b in contexts[a]['req'].items()if b and q not in K}for a in G}
assert not I['C'] and sum(len(I[a])for a in 'DVU')==8
# C has no imported residual input: all exits in its core are fixed literal R writes.
ce=G['C']['p'];ch=G['C']['h'];cek={ce+rot(ch)*q for q in K}
assert all(q in G['C']['last']and G['C']['last'][q][0]=='R'for q in cek)
def chord(a,p=0j,h=0):return center(p,h),center(p+rot(h)*G[a]['p'],(h+G[a]['h'])%4)
def pose(p,h):return [*xy(p),h]
def contact(a,b):return meet(*a,*b)
win=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
geo=[]
for src in 'DCVU':
 ks=next(z['allowed_C_counts_before_contact_ENTRY']for z in win if z['source_class']=='postFOREIGN_ordinary'and z['source_atom']==src and z['contact_atom']=='C')
 assert ks==([3,4,5]if src in 'DC'else[3,4,5,6])
 aa,bb=chord(src)
 for k in ks:
  h=(-k)%4;c,d=chord('C',0j,h)
  verts=[(u-v)/2 for u in (aa,bb)for v in (c,d)]
  for x in range(math.ceil(min(z.real for z in verts)),math.floor(max(z.real for z in verts))+1):
   for y in range(math.ceil(min(z.imag for z in verts)),math.floor(max(z.imag for z in verts))+1):
    if(x+y+h)%2:continue
    p=complex(x,y);co=meet(aa,bb,c+2*p,d+2*p)
    if co is None:continue
    if ns['cross'](bb-aa,d-c)==0:
     axis=(lambda v:int(v.real))if(d-c).real else(lambda v:int(v.imag))
     old=Fraction(0);new=Fraction(axis(aa-c-2*p),axis(d-c))
     if not(0<new<=1):continue
     assert c+2*p+new*(d-c)==aa
    else:old,new=co
    if not(0<=old<1 and 0<new<=1):continue
    hd=(h+1)%4;pd=p-rot(hd)*(1+2j);p1=pd+rot(hd)*G['D']['p']
    assert p1+rot(hd)*G['C']['p']==p and(hd+3)%4==h
    cd=contact(chord(src),chord('D',pd,hd));cc=contact(chord(src),chord('C',p1,hd))
    geo.append((src,k,pose(p,h),str(old),str(new),pose(pd,hd),pose(p1,hd),cd,cc))
assert len(geo)==20
key=lambda z:(z[0],z[1],tuple(z[2]))
AG={ (z['source_RAW'],z['SOURCE_ENTRY_to_terminal_C2_ENTRY_C_clock'],tuple(z['terminal_C2_ENTRY'])):z for z in J['all20_exact_ordinary_source_terminal_C2_geometry_rows']}
assert {key(z)for z in geo}==AG.keys()
for z in geo:
 a=AG[key(z)];assert z[3:7]==(a['old_source_parameter'],a['new_C2_parameter'],a['actual_last_D_ENTRY'],a['actual_C1_ENTRY'])
 assert bool(z[7])==bool(a['actual_source_D_contact_with_last_D'])and bool(z[8])==bool(a['actual_source_contact_with_C1'])
beta=1-1j;births=[]
for a in 'DCVUFQB':
 q=G[a]['p']+rot(G[a]['h'])*beta;assert G[a]['last'][q]==('R',len(W[a])-2)
 ek={G[a]['p']+rot(G[a]['h'])*v for v in K};assert q not in ek
 births.append((a,xy(q),len(W[a])-2))
assert births==[(z['actual_previous_RAW'],z['actual_beta_cell'],z['last_R_tick0'])for z in J['all7_genuine_previous_RAW_beta_births']]
for a in 'DC':assert beta not in contexts[a]['req']and(beta-G[a]['p'])/rot(G[a]['h'])not in K
# Source-D common at age<3 is only used on a genuine BASE-ending G8 factor,
# never by pretending terminal DCC is a completed packet. Bind the exact signed query report.
common=json.loads((R/'audits/check_atomic_common_four_C_independent.json').read_text());assert common['shifted_clock_queries']==184
rows=[];cl=Counter();TAIL=W['D']+W['C']*2;tt=tr(TAIL+M);assert tt['bad']is None
AR={(z['source_RAW'],z['candidate_K'],z['consumer_ENTRY_C_clock'],z['consumer'],tuple(z['input'])):z for z in J['all192_D_C_source_beta_first_loss_before_actual_last_D_roles']}
for z in geo:
 src,k,cp,_,_,dp,p1,_,_=z
 if src not in 'DC':continue
 target=complex(*dp[:2]);th=dp[2]
 for n in range(k):
  h=(-n)%4
  for a in 'DVU':
   for inp in I[a]:
    p=beta-rot(h)*inp;end=p+rot(h)*G[a]['p'];ak=(src,k,n,a,tuple(xy(inp)));au=AR[ak]
    assert pose(p,h)==au['pose']and pose(end,h)==au['RAW_EXIT']
    if(int(p.real+p.imag)+h)%2:why='sector'
    elif src=='C'and n==0:why='source unfinished'
    elif n==0:assert p.imag<1;why='N0 head too low'
    elif n==1:assert p.imag<1;why='W1 head too low'
    elif n==2:
     if src=='C':assert a=='U'and p.real>=0;why='C S2 x cone'
     elif contact(chord(src),chord(a,p,h)):
      assert a=='U'and p==0;why='nonadjacent source exit repeat'
     else:
      assert a=='U'and p==1+1j and(2-p)/rot(h)in I[a];why='genuine sourceD common min3'
    elif n==3:
     if contact(chord(src),chord(a,p,h)):why='earlier source contact'
     else:
      assert end in(1-2j,3-2j)
      if k==4:assert end.real>target.real;why='E x monotone'
      else:
       assert k==5 and target==-1-3j and end.real+1>target.real
       # Literal N V=(+1,+3), so original x proof is valid.
       assert min(G[b]['p'].real for b in 'DVU')==0
       # Independent alternative sum/y inequalities also close the endpoint.
       assert end.real+end.imag+1>target.real+target.imag
       why='E then C then N x and sum cones'
    else:
     assert k==5 and n==4 and end in(1+1j,2+2j)and end.real>target.real and end.imag>target.imag;why='N x and y cones'
    rows.append((ak,pose(p,h),pose(end,h),why));cl[why]+=1
 q=(beta-target)/rot(th);first=next((i,c)for i,(p,h,c)in enumerate(tt['reads'])if p==q)
 assert first==({3:38,4:33,5:16}[k],'R')and first[0]<40
assert len(rows)==192 and{z[0]for z in rows}==AR.keys()
STAR={0j,1j,1+0j,1+1j};ledger=Counter();vguards=[]
vr=json.loads((R/'fresh_RAW_V_U_early_donor_guards_2026-10-24/fresh_r.json').read_text())['all3_marker_loss_Jordan_interfaces']
assert len(vr)==3 and all(z['actual_RAW_EXIT']==[0,1,3]for z in vr)
for z in geo:
 src,k,cp,_,_,dp,_,cd,cc=z;p=complex(*cp[:2]);h=cp[2];pd=complex(*dp[:2]);hd=dp[2]
 if src=='U':
  bad=[q for q in STAR if(q-p)/rot(h)in K or contexts['C']['req'].get((q-p)/rot(h))is False]
  assert bad and any((q-p)/rot(h)in K or any(pos==(q-p)/rot(h)and c=='R'for pos,_,c in G['C']['reads'])for q in bad)
 if cd or cc:assert k-1>=2;ledger['earlier actual precursor contact']+=1
 elif src=='U':ledger['fresh U star']+=1
 elif src in 'DC':ledger['preceding beta']+=1
 else:
  assert src=='V'and k in (4,5,6)
  if k==6:
   assert pd==2-1j and hd==3 and all((rot(3)*G[a]['p']).real<0 for a in 'DVU')
  q=-pd/rot(hd);first=next((i,c)for i,(pos,hh,c)in enumerate(tt['reads'])if pos==q)
  assert first==({4:31,5:22,6:21}[k],'R');vguards.append((k,dp,first));ledger['fresh V r']+=1
assert ledger=={'earlier actual precursor contact':6,'fresh U star':5,'preceding beta':6,'fresh V r':3}
# Local terminal tail only joins adjacent chords. No source with gap0/1 omitted.
assert contact(chord('D'),chord('C',1+2j,3))is None
assert contact(chord('C',1+1j,0),chord('C',1+2j,3))==(1,0)
controls=[]
for au in J['all2_actual_prepared_positive_terminal_words']:
 seq=au['word'];raw=''.join(W[a]for a in seq);z=tr(raw+M);assert z['bad']is None
 seed={q for q,b in z['req'].items()if b};assert sorted(map(xy,seed))==au['complete_black_seed']
 board=set(seed);p=0j;h=0
 for t,(q,hh,c)in enumerate(z['reads']):
  assert(p,h)==(q,hh)and(p in board)==(c=='L')
  rr=au['all_RAW_plus_given_M11_physical_reads'][t];assert rr['cell']==xy(p)and rr['turn']==c
  board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 ps=ns['pieces'](seq)
 for i,a in enumerate(ps):
  for j in range(i+1,len(ps)):
   co=contact(a,ps[j])
   if co is None:continue
   assert j==i+1 and a[1]==ps[j][0]and co==(1,0)
 controls.append(dict(word=seq,seed=sorted(map(xy,seed)),final=sorted(map(xy,board)),reads=len(raw+M),pose=pose(p,h)))
assert len(TAIL+M)==51 and tt['p']==1j and tt['last'][1j]==('L',11)
extra=tr(TAIL+W['D']+M);assert extra['bad'][:2]==(51,11)and extra['bad'][3]=='L'
out=dict(status='PASS independent terminal-DCC ordinary-owner closure',manifest_sha256=sha(A/'manifest.json'),literal_base_N_displacements={a:xy(G[a]['p'])for a in 'DVU'},geometry_count=20,geometry=[dict(source=z[0],clock=z[1],C2=z[2],lastD=z[5],C1=z[6],earlier_D=bool(z[7]),earlier_C1=bool(z[8]))for z in geo],beta_role_count=len(rows),beta_counts=cl,actual_beta_births=births,beta_roles=rows,source_ledger=ledger,V_tail_first_reads=vguards,complete_controls=controls,marker='DCC+M51 legal; ungiven turn51 isR, not a completed nextD+ownM',analytical_qualification='SourceD minimum3 invoked only at hypothetical earlier actual BASE consumer in genuine G8; standaloneC uses coordinate cones. CURRENT-to-CORE loss retained. Global-first stopping supplies simplicity only before contact. No completed nextG7 or fictitious DCC packet.',auditor_correction='Earlier challenge recalled N V as(-1,+3); literal is(+1,+3). Original N x cones are valid; no source result withdrawn.',scope='Only postFOREIGN ordinary outgoing owners at GLOBAL first contact in actual terminalDCC secondC. LeadingC allowed. PreFOREIGN/originalFOREIGN owners and arbitrary-tail simplicity remain separate.')
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')),dict(ledger))
