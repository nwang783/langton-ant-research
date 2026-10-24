from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'terminal_LL_portal_upper_side_has_a_physical_completion_collision.md':'65df766ad347da82d569f873d715394f864da4a5403a1c8495f2ed590f1dab38','check_terminal_LL_upper_side_collision.py':'3de0f206cc1fd18528eb8c0547081978e78a46636bb9c6cc1105e403739ce3f6','check_terminal_LL_upper_side_collision.json':'b91b04927db71a44ca64e7d8455320773633df4985345d7f0fa9a2dfbec16d84'}
for f,h in files.items():assert sha(D/f)==h
ref=json.loads((D/'check_terminal_LL_upper_side_collision.json').read_text());lib=S.with_name('check_global_max_flow2_staircase_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('rows=[];stats=Counter()')[0],ns);cv,string,V,out,NS,EW,test=[ns[k]for k in('cv','string','V','out','NS','EW','test')]
mapres={'skipped':'rank','global_max':'higher_C'}
def physical(hs):
 su={};edges=set()
 for p,w in hs.items():
  for j in range(len(w)-1):edges.add(((p,j),(p,j+1),4,'same_cell'))
  for h,v in enumerate(V):
   if p+v not in hs:continue
   aa=[j for j in range(len(w))if out(w,j)==h];bb=[j for j,x in enumerate(hs[p+v])if x==h];assert len(aa)==len(bb)
   for i,j in zip(aa,bb):
    a,b=(p,i),(p+v,j);su[a]=b;edges.add((a,b,1,'actual'));edges.add((b,a,-1,'actual_reverse'))
 return su,edges
def ev(z):return(complex(*z[0]),z[1])
def verify_cert(hs,row):
 su,edges=physical(hs);c=row['certificate'];typ=row['result']
 if typ=='rank':
  p=list(map(ev,c['path']));assert all(su[a]==b for a,b in zip(p,p[1:]));assert p[-1][0]==p[0][0]and p[-1][1]!=p[0][1]+1;return len(p)-1
 if typ=='clock':
  cy=[(ev(a),ev(b),w,label)for a,b,w,label in c['cycle']];assert all(e in edges for e in cy)and all(a[1]==b[0]for a,b in zip(cy,cy[1:]+cy[:1]));assert sum(e[2]for e in cy)==c['total']>0;return c['total']
 return None
ct1=Counter();tops=[];rows1={};wits1=[]
r1={(r['R'],r['U'],r['W']):r for r in ref['Q_square_nonport_rows']}
for rr,uu,ww in product(map(cv,['SNN','SNNS']),NS,EW):
 hs={-1j:cv('WWEE'),1-1j:rr,0j:uu,1+0j:ww};ans,wit=test(hs);typ=mapres.get(ans,ans);ct1[typ]+=1;key=tuple(map(string,(rr,uu,ww)))
 if typ!='port':
  assert key in r1 and r1[key]['result']==typ;verify_cert(hs,r1[key]);rows1[key]=typ
 if typ=='higher_C':wits1.append((key,wit))
 if typ=='open':tops.append((rr,uu,ww))
assert dict(ct1)==ref['Q_square_counts']and set(rows1)==set(r1);assert list(map(lambda z:list(map(string,z)),tops))==ref['Q_square_modes']
ct2=Counter();rows2={};lengths=Counter();weights=Counter();permode={};r2={(r['R'],r['U'],r['W'],r['L'],r['K']):r for r in ref['upper_eight_nonport_rows']}
for rr,uu,ww in tops:
 per=Counter();pairs=[]
 for ll,kk in product(EW,NS):
  hs={-2-1j:cv('EEWW'),-1-1j:cv('SNNS'),-1j:cv('WWEE'),1-1j:rr,0j:uu,1+0j:ww,-1+0j:ll,-2+0j:kk};ans,wit=test(hs);typ=mapres.get(ans,ans);ct2[typ]+=1;per[typ]+=1;key=tuple(map(string,(rr,uu,ww,ll,kk)))
  if typ!='port':
   assert key in r2 and r2[key]['result']==typ;val=verify_cert(hs,r2[key]);rows2[key]=typ;pairs.append([string(ll),string(kk)])
   if typ=='rank':assert len(wit)-1 in[4,8];lengths[val]+=1
   elif typ=='clock':weights[val]+=1
   else:raise AssertionError(typ)
 assert len(pairs)==22;permode[str(tuple(map(string,(rr,uu,ww))))]=dict(counts=dict(per),complete_count_pairs=pairs)
assert dict(ct2)==ref['upper_eight_counts']and set(rows2)==set(r2)and ct2==dict(port=4695,rank=100,clock=10)
# The already signed terminal cover supplies fixed four words in all18 modes.
prior=json.loads((D/'check_terminal_LL_even_portal_suppliers.json').read_text());import ast
selected=[]
for row in prior['rows']:
 if row['result']!='open':continue
 hs={complex(*ast.literal_eval(p)):w for p,w in row['histories'].items()};assert hs[-1+2j]=='EEWW'and hs[2j]=='SNNS'and hs[1+2j]=='WWEE'and hs[2+2j]in['SNN','SNNS'];selected.append(hs[2+2j])
assert len(selected)==18
# Q=(1,2) is the opposite C sector of WWEE from the portal's M sector(0,1).
# R_W=R_E=1 makes the opposite C heights equal, independently of unknown readers.
assert sum(cv('WWEE')[i]==1 for i in[0,2])==sum(cv('WWEE')[i]==3 for i in[0,2])==1
outreport=dict(status='PASS scoped terminal LL even-portal upper-side physical completion obstruction',bindings=files,Q_square_counts=dict(ct1),five_modes=list(map(lambda z:list(map(string,z)),tops)),independent_higher_C_witnesses=wits1,upper_eight_counts=dict(ct2),physical_rank_path_lengths=dict(lengths),positive_clock_weights=dict(weights),all_mode_count_domains=permode,bound_prior_open_profiles=len(selected),analytic_review=[
'Each missing reader ranges over EVERY complete WHITE empty or1..4-read history in its actual incoming axis. The1922 and4805 products are count-derived finite local domains, not word-depth or period scans. Used and zero port counts are retained.',
'The physical shift(-1,-3) preserves axis parity and places maximal Q at the independently solved face anchor(0,-1). In the terminal portal application, C=WWEE has balanced R_W/R_E, transporting the known opposite portal M sector to Q. No unknown reader first-R maximum is presumed.',
'All53 first-square non-port products independently classify as43 literal same-physical next-rank failures,1 positive clock,4 higher-C,5 necessary modes. Every stored rank/clock witness is separately replayed against actual ordinal successor/equality edges, not just matched counts.',
'Each of the five modes has exactly22 complete L/K count-compatible pairs. All110 have a physical rejection:100 same-cell wrong-next-rank paths of4/8edges or10 exact positive cycles with actual +/-1 equalities and same-cell >=4. No further global height or chronology bound is used in this final stage.',
'Any full-drift quotient realization supplies these physical eight-cell histories, so identification of translated classes cannot remove a same-PHYSICAL-cell return or positive actual-time cycle. Older stock and optionalL3 remain within the complete histories.',
'Only the specified complete-WHITE cap4 terminal LL entry into this even-root portal is excluded. The prior18 local networks remain valid weaker data without these four completed readers; prepared F84/F85 and changed-role/higher-multiplicity joins are not excluded. No whole-front or general one-use classification follows.'
],dependencies={'prior_independent_report':sha(S.with_name('check_terminal_LL_portal_suppliers_independent.json'))})
S.with_suffix('.json').write_text(json.dumps(outreport,indent=2)+'\n');print(outreport['status']);print(sha(S.with_suffix('.json')));print(ct1,ct2,lengths,weights)
