from pathlib import Path
from itertools import product
from collections import defaultdict,deque
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'four_read_one_use_alternation_has_a_lower_terrace_supplier.md';JF=D/'check_four_read_one_use_lower_terrace.json';assert sha(P)=='dcaec6e702346d51e48d87955b69537f7850bfe3046a2d242ce1c05982466d47'and sha(JF).startswith('1677c73c')and sha(D/'check_four_read_one_use_lower_terrace.py').startswith('99aa595f');J=json.loads(JF.read_text());H='NESW';V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];out=lambda w,r:H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
ns={'__file__':str(S.with_name('check_global_max_flow2_staircase_independent.py'))};exec(Path(ns['__file__']).read_text().split('rows=[];stats=Counter()')[0],ns);test=ns['test'];cv=ns['cv']
def net(hs):
 su={}
 for p,w in hs.items():
  for h,d in zip(H,V):
   if p+d not in hs:continue
   aa=[r for r in range(len(w))if out(w,r)==h];bb=[r for r,hh in enumerate(hs[p+d])if hh==h];assert len(aa)==len(bb),(p,h,aa,bb)
   su.update({(p,r):(p+d,s)for r,s in zip(aa,bb)})
 return su
fixed={-1j:'WWEW',0j:'N',1+0j:'WWEW',1+1j:'N',2+1j:'WWEW',1-1j:'SSSN',2+0j:'SSSN'};E=2-1j;domain=[]
# Ein=Nout=1 yields re=rw=a<=1; WHITE n4a or4a-1.
for a in range(2):
 for n in{4*a,4*a-1}:
  if n<=0:continue
  for xs in product('EW',repeat=n):
   w=''.join(xs)
   if w.count('E')==1 and sum(out(w,r)=='N'for r in range(n))==1:domain.append(w)
assert sorted(domain)==['EWW','EWWW','WWE','WWEW'];rows=[]
for row in J['rows']:
 w=row['reader'];hs=fixed|{E:w};su=net(hs);ans,wit=test({p:cv(s)for p,s in hs.items()});assert ans==('open'if w.startswith('E')else'clock');nrank=next(r for r in range(len(w))if out(w,r)=='N');erank=w.index('E');pathN=[(E,nrank),(2+0j,3),(1+0j,3),(1-1j,2)];pathE=[(1-1j,1),(E,erank)];assert all(su[a]==b for path in[pathN,pathE]for a,b in zip(path,path[1:]))
 if not w.startswith('E'):
  assert(nrank,erank)==(0,2);rows.append(dict(reader=w,result='positive_clock',cycle=[[xy(a[0]),a[1],xy(b[0]),b[1],k]for a,b,k in wit]));continue
 assert(nrank,erank)==(2,0);paths=[[(1+0j,2),(1-1j,1),(E,0)],[(E,2),(2+0j,3),(1+0j,3)]];assert all(su[a]==b for path in paths for a,b in zip(path,path[1:]));assert[[[xy(p),r]for p,r in path]for path in paths]==row['exact_paths']
 tt={(complex(*ast.literal_eval(e)[0]),ast.literal_eval(e)[1]):t for e,t in row['distinct_mod4_calendar'].items()};ev={(p,r)for p,hh in hs.items()for r in range(len(hh))};assert set(tt)==ev and len(ev)==len(set(tt.values()))==row['events']
 for a,b in su.items():assert tt[b]==tt[a]+1
 for p,hh in hs.items():
  x,y=map(int,(p.real,p.imag));phase=2*(x%2)if(x+y)%2==0 else 3-2*(x%2)
  for r in range(len(hh)):
   assert tt[p,r]%4==phase
   if r:assert tt[p,r]-tt[p,r-1]>=4
 # Full components partition named events, with genuinely disjoint calendars.
 incoming=set(su.values());comps=[];seen=set()
 for start in sorted(ev-incoming,key=lambda e:(e[0].real,e[0].imag,e[1])):
  u=start;cc=[]
  while True:
   assert u not in seen;seen.add(u);cc.append(u)
   if u not in su:break
   u=su[u]
  comps.append(cc)
 assert seen==ev;assert[[[xy(p),r]for p,r in cc]for cc in comps]==row['components'];order=row['component_order'];assert sorted(order)==list(range(len(comps)))and all(tt[comps[a][-1]]<tt[comps[b][0]]for a,b in zip(order,order[1:]))
 # Reconstruct unrestricted curl on ALL incident radial ports including zeros.
 adj=defaultdict(list)
 for p,hh in hs.items():
  for h,d in zip(H,V):
   right=p+d/2-1j*d/2;left=p+d/2+1j*d/2;flux=sum(out(hh,r)==h for r in range(len(hh)))-hh.count(H[(H.index(h)+2)%4]);adj[left].append((right,flux));adj[right].append((left,-flux))
 vals={.5-.5j:0};todo=deque(vals)
 while todo:
  p=todo.popleft()
  for q,k in adj[p]:
   if q in vals:assert vals[q]==vals[p]+k
   else:vals[q]=vals[p]+k;todo.append(q)
 assert set(vals)==set(adj);assert vals[1.5-1.5j]==vals[2.5-.5j]==-2 and vals[1.5-.5j]==-3 and vals[2.5-1.5j]==(-4 if w=='EWW'else-5)
 rows.append(dict(reader=w,result='necessary_open_calendar',events=len(ev),C_levels=[vals[1.5-1.5j],vals[2.5-.5j]],L_levels=[vals[1.5-.5j],vals[2.5-1.5j]],exact_nested_paths=[[[xy(p),r]for p,r in path]for path in paths]))
# Literal all-index channel and full-drift sign in the explicitly EVEN branch.
fn={'A':lambda i:complex(i+1,i),'R':lambda i:complex(i+1,i+1),'D':lambda i:complex(i+2,i),'E':lambda i:complex(i+2,i-1)};ww={'A':'WWEW','R':'N','D':'SSSN','E':'EWW'}
ch=[('E',0,2),('D',0,3),('A',0,3),('D',-1,2),('A',-1,1),('D',-2,0),('A',-2,0),('R',-2,0),('A',-1,2),('D',-2,1),('E',-1,0)];assert[list(x)for x in ch]==J['circular_channel_family_index_rank'];hs={f(i):ww[a]for a,f in fn.items()for i in range(-4,5)};su=net(hs);phys=[(fn[a](i),r)for a,i,r in ch];assert all(su[a]==b for a,b in zip(phys,phys[1:]));roles=defaultdict(list)
for a,i,r in ch[:-1]:roles[a].append((i,r))
assert {a:sorted(r for i,r in rs)for a,rs in roles.items()}=={'E':[2],'D':[0,1,2,3],'A':[0,1,2,3],'R':[0]}
assert {int(fn[a](0).real-fn[a](0).imag)for a in fn}=={0,1,2,3}
# All n: each fixed (family,rank) occurs once, and i+j modn is a bijection;
# no short quotient can alias distinct families/ranks. E_(i-n)=E_i+d.
for n in range(1,9):
 use=[(a,(i+j)%n,r)for i in range(n)for a,j,r in ch[:-1]];assert len(use)==len(set(use))==10*n;assert fn['E'](-n)-fn['E'](0)==complex(-n,-n)
dep=R/'audits/check_one_use_L3_transport_independent.json';assert sha(dep)=='ad205d481891b627c1fa783be2f185a112ae784eca5768149867cf68f004069e';old=json.loads(dep.read_text());assert sorted(r[2]for r in old['necessary_profiles']if r[:2]==[1,1])==['SSNNS','SSSN','SSSNN']
O=dict(status='PASS local four-read one-use lower-terrace supplier; whole-circle equation ONLY with every shared D_i=SSSN explicitly supplied',proof=sha(P),certificate=sha(JF),script=sha(S),signed_uncapped_dependency=sha(dep),exact_cap_free_outer_domain=sorted(domain),four_reader_controls=rows,all_index_ten_step_channel=ch,source_interior_roles=dict(roles),analytic_review=[
'The signed uncapped11 LRL case retains SSSN,SSNNS,SSSNN. An oddfive-read sharedreader is a genuine alternative, not a distinctoutput payment. The local evenbranch explicitly supplies BOTH U/V=SSSN, automatic under a completecap4 premise.',
'Ein1=Nout1 gives R_E=R_W=1 with noL_E and exact n3/4, yielding fourcompleteWHITE words. Physical E.N->V3->B3->U2 and U1->E.E give tN=U2-3>=U1+1=tE; equalitycannotuseoneE L event. WWE/WWEW putN beforeE and failclock. EWW/EWWW remainnecessary.',
'Exact B2->U1->E0 and E2->V3->B3 give Bspan23=Espan02+4>=12 and strict interval nesting. OptionalE.L3 stayspresent. Everylocalport andcalendar is rebuilt; these25/26eventnetworks have no supplied exteriorphysicalconnectors.',
'Independent fullradialcurl places both E Csectors atM-2, northLsideM-3,southLsideM-4/M-5. This reader is not anothermaximalcurve, and noindependentfuel/root payment follows.',
'The optionalwholecircle claim requires the ENTIRE EVEN sharedreader branch D_i=SSSN, not only boundaryLEFT4/RIGHT1. Uncappedoddsharedreaders reset it. Subject tothis explicit premise, everyarrow of the tenstepphysicalchannel is checked; familyx-y offsets distinguish allshortquotients and each(family,rank)role is usedonce withbijective indexshift.',
'Actual T0(E_(i-1))=T2(E_i)+10, while E_(i-n)=E_i+d forfull d=(-n,-n) andtime+P. Telescoping gives P=10n+sumDelta02E. Allpositive terms implyeachspan<P andP>=18n. This isoneexactconditionaloccurrencepartition, not anadditivefuelbudget or anattainedcircle.',
'No globalallcapfirstR maximum, arbitraryone-use runbound, higherclockreset, physicalfactor, controllerclassification, WHITE S1 or universalcapture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
