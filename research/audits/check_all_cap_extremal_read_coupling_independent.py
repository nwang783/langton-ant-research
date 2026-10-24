from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib,random
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();V=(1j,1,-1j,-1)
for l in (D/'SHA256SUMS').read_text().splitlines():h,p=l.split(None,1);assert sha(R/p)==h
ref=json.loads((D/'check_extremal_read_coupling.json').read_text())
def trace(word,h=0):
 p=0j;out=[]
 for t,c in enumerate(word):hh=(h+(1 if c=='R'else-1))%4;out.append((t,p,h,hh,c));p+=V[hh];h=hh
 return out,p,h
def key(q,d):
 ax=0 if d.real else 1;dd=int(d.real if ax==0 else d.imag);coord=int(q.real if ax==0 else q.imag);k=coord//abs(dd)*(1 if dd>0 else-1);return q-k*d,k
def loops(G):
 seen=set();ans=[]
 for a in G:
  walk=[];local={};v=a
  while v in G and v not in seen and v not in local:local[v]=len(walk);walk.append(v);v=G[v][0]
  if v in local:
   cyc=walk[local[v]:];ans.append((cyc,sum(G[q][1]for q in cyc)))
  seen.update(walk)
 return ans
def build(word,h):
 ev,d,hh=trace(word,h);assert hh==h and d;P=len(word);H={}
 for t,q,hi,ho,c in ev:
  a,k=key(q,d);H.setdefault(a,[]).append((t-k*P,hi,ho,c,t))
 for a in H:H[a].sort()
 bad=[(a,''.join(v[3]for v in es))for a,es in H.items()if any(x[3]==y[3]for x,y in zip(es,es[1:]))];white=not bad and all(es[0][3]=='R'for es in H.values());b={};kk={};E={};EL={};types={}
 for a,es in H.items():
  f,l=es[0],es[-1];n,k=key(a+V[f[2]],d);b[a]=(n,k)
  if l[3]=='L':kk[a]=key(a-V[l[1]],d)
  if H[n][-1][0]+k*P==f[0]+1:
   E[a]=(n,k)
   if H[n][-1][3]=='L':EL[a]=(n,k)
  types[a]='single'if len(es)==1 else 'even'if len(es)%2==0 else'odd_same'if f[1]==l[1]else'odd_opposite'
 if white:
  bc,kc,ec=loops(b),loops(kk),loops(E);assert all(w==-1 for c,w in bc)and all(w==1 for c,w in kc)
  assert len(set(v[0]for v in E.values()))==len(E)
  assert not(set(EL)&{v[0]for v in EL.values()});inc={v[0]for v in E.values()}
  assert all(types[a]in ['single','odd_opposite']for a in set(E)&inc)
  A=sum(v in ['single','odd_opposite']for v in types.values());assert 2*len(E)<=len(H)+A
  for c,w in ec:
   assert w==-1 and all(types[a]in ['single','odd_opposite']for a in c)and any(types[a]=='odd_opposite'for a in c)
   assert sum(H[a][-1][0]-H[a][0][0]for a in c)==P+len(c)
  g=sum(len(es)%2 for es in H.values());assert g>=sum(len(c)for c,w in ec)>=2*max(abs(d.real),abs(d.imag))*len(ec)
  # Every subset of actual b/k cycle families, not just the all-cycle choice.
  for mask in range(1<<(len(bc)+len(kc))):
   bs=[c for i,(c,w)in enumerate(bc)if mask>>i&1];ks=[c for i,(c,w)in enumerate(kc,len(bc))if mask>>i&1]
   fsel={H[a][0][4]for c in bs for a in c};lsel={(H[a][-1][4]-1)%P for c in ks for a in c};ov=fsel&lsel;LF=sum(map(len,bs));LL=sum(map(len,ks));C=len(ov)
   assert len(fsel)==LF and len(lsel)==LL and 2*C<=min(LF,LL,sum(v=='even'for v in types.values()))
   delta=sum(1 if ev[t][3]%2 else-1 for t in ov);e=sum((V[ev[t][3]]for t in ov),0j);k=len(bs)+len(ks);z=(1+k)*d+e
   bound=LF+LL-C+max(2*abs(z.real)-delta,2*abs(z.imag)+delta);assert P>=bound
 return dict(P=P,d=[int(d.real),int(d.imag)],classes=len(H),white=white,bad=[([int(a.real),int(a.imag)],w)for a,w in bad],type_counts=dict(Counter(types.values())),bcycles=[(len(c),w)for c,w in loops(b)],kcycles=[(len(c),w)for c,w in loops(kk)],E=len(E),EL=len(EL))
std=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text());controls=[]
for mult in [1,2,3]:
 for rot in range(4):controls.append(build(std['word']*mult,(std['heading']+rot)%4))
for x,y in zip(controls,ref['standard_controls']):assert x['white']==y['complete_white']and x['classes']==y['classes'] and x['E']==len(y['first_last_edges'])and x['EL']==len(y['first_last_L_edges'])
# Exhaust the only small clockwise contractible candidates left by ell<=8,
# retaining vertex simplicity and mandatory quarter-turn at EVERY step.
small={}
for n in [4,8]:
 good=[]
 for ww in product('RL',repeat=n):
  ev,ep,eh=trace(''.join(ww));pts=[z[1]for z in ev]
  if ep==0 and eh==0 and len(set(pts))==n:good.append(''.join(ww))
 small[n]=good
assert set(small[4])=={'RRRR','LLLL'}and small[8]==[]
# Independent actual finite-factor controls retain initial/final exceptions.
rng=random.Random(20261024);boundaries=0;literal=None
for i in range(120):
 pts=[complex(x,y)for x in range(-3,4)for y in range(-3,4)];B=set(rng.sample(pts,rng.randrange(15)))if i else set();p=0j;h=i%4;H={};tr=[]
 for t in range(3000):
  c='L'if p in B else'R';ho=(h+(1 if c=='R'else-1))%4;ev=(t,p,h,ho,c);tr.append(ev);H.setdefault(p,[]).append(ev);B.symmetric_difference_update({p});p+=V[ho];h=ho
 E={};EL={}
 for a,es in H.items():
  f=es[0]
  if f[4]!='R' or f[0]==2999:continue
  q=tr[f[0]+1][1]
  if H[q][-1][0]==f[0]+1:
   E[a]=q
   if H[q][-1][4]=='L':EL[a]=q
 for a in set(E)&set(E.values()):
  f,l=H[a][0],H[a][-1]
  if f[0]==0 or l[0]==2999:boundaries+=1;continue
  assert len(H[a])==1 or(l[4]=='R'and f[2]!=l[2])
 for a,q in EL.items():
  if q in EL:assert H[q][0][0]==0 or H[q][-1][0]==2999
 if i==0:
  es=[(H[a][0][0],H[q][-1][0],a,q)for a,q in EL.items()if H[a][0][0]>0 and H[q][-1][0]<2999];literal=min(es)
assert boundaries==ref['boundary_exceptions_retained']==8 and literal[:2]==(1723,1724)
d102=json.loads((R/'K1_pipeline_detours_2026-10-23/prepared_D102_black_helper_connected_control.json').read_text())['word'];inv=''.join('L'if c=='R'else'R'for c in d102[::-1]);diag={n:build(w,h)for n,w,h in [('D102',d102,0),('inverse_D102',inv,2)]};assert all(len(v['bad'])==8 for v in diag.values())
out={'status':'PASS cap-free prepared reverse boundary dichotomy, first-to-last matching, exact overlap-corrected counterflow','author_note_sha256':sha(D/'ALL_CAP_EXTREMAL_READ_COUPLING.md'),'standard_controls':controls,'finite_factor_controls':120,'actual_fine_reads':360000,'retained_boundary_exceptions':boundaries,'finite_EL_example_times':literal[:2],'small_contractible_quarter_turn_polygons':small,'D102_and_inverse_repetition_diagnostics':diag,'analytic_review':[
'Reverse k keeps all odd-output classes as BLACK terminals. Every cycle consists solely of WHITE reverse first-R vertices, so the exact same-port first-time rule holds even when arbitrary off-cycle input is BLACK: at right corners increment1, at left increment1-4q with q>=1. Each physical closed return length is divisible by4 because successive axes alternate and horizontal/vertical signed sums vanish.',
'An essential quotient cycle is embedded and primitive, has equal left/right corners, and therefore negative first-time winding relative to reverse drift, giving +1 original winding. A contractible CCW cycle violates ell=4Q>=2ell+8. Clockwise gives ell<=8: length4 allR has impossible positive total time, length8 would need6R/2L; avoiding premature RRRR forces(RRRL)^2, which repeats a vertex. Length6 is impossible by the same axis parity. Thus finite partial-functional components contain exactly one terminal or one essential cycle, not necessarily terminal-rooted trees only.',
'For u→v→w coincidence edges, if nonsingleton v last incoming equals its first incoming, its earlier first arrival would require a read of u before u firstR. Hence headings are opposite. If v last turn wereL its last outgoing equals its firstR outgoing, giving a later visit to w after w last, impossible. Thus every internal E vertex is singleton or opposite-heading odd; E_L has no internal vertex and is an undirected matching after full-drift quotient, with no omitted initial-head exception in the complete front.',
'Indegree/outdegree bounds give2|E|<=2A+B. E cycles are subsets of b cycles, all odd, and cannot be entirely singleton because their winding is-1. Summing actual H(v)=F(u)+1 gives P=sum(H-F)-length. Distinct cycle vertices give both odd and opposite-heading capacity claims without overlap.',
'Selected first-R and reversed last-L cycles may share GEOMETRY but only common actual event classes reduce inventory. These coincidences lie in E_L and both endpoints are even k-cycle vertices, explaining2C<=min(LF,LL,n_even), not the false analogous claim for arbitrary E_L edges. Subtracting unique selected events leaves a nonnegative UNBALANCED inventory with displacement(1+k)d+e and horizontal-minus-vertical countdelta. Separate horizontal/vertical capacities yield the displayed max bound. No autonomous residual trace is claimed.',
'The D102 and inverse diagnostics each have eight complete stable translation classes with nonalternating letters, excluding those repeated words on ANY initial board. This does not invalidate the signed finite prepared D102 control or provide a new global periodic classification. Retained positive growth g>=max(8,2||d||infinity) is an attributed prior theorem under the complete-WHITE/finite-overlap bridge.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
