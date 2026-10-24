from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'three_read_LRL_entries_cannot_feed_the_even_LL_portal.md';A=D/'check_three_read_LRL_entry_to_even_portal.json'
assert sha(P)=='6025a78992596a8f8eb84591b73b8e8c8c1871ad37d57e8697b4c75905ba2c54';assert sha(A).startswith('6956066a');assert sha(D/'check_three_read_LRL_entry_to_even_portal.py').startswith('d1a194a6');J=json.loads(A.read_text())
H='NESW';V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)]
def out(w,r,b=False):return H[(H.index(w[r])+(1 if(r%2==0)!=b else-1))%4]
def net(hs,black):
 ans={}
 for p,w in hs.items():
  for h,v in zip(H,V):
   if p+v not in hs:continue
   a=[r for r in range(len(w))if out(w,r,p in black)==h];b=[r for r,c in enumerate(hs[p+v])if c==h]
   assert len(a)==len(b),(p,h,w,hs[p+v]);ans.update({(p,r):(p+v,s)for r,s in zip(a,b)})
 return ans
Z=3j;rows=[];counts=Counter()
for root,reader in [('EWW','SSN'),('EWWE','SSNN')]:
 fixed={1+1j:'SN',1j:root,0j:'NNSS',1+0j:'EE',1+2j:'EEW',2j:reader,1+3j:'NNSS',2+3j:'EEW',2+2j:'S'}
 for black in[False,True]:
  generated=set()
  for a in range(3):
   for n in({4*a,4*a+1}if black else{4*a,4*a-1}):
    if n<=0:continue
    for letters in product('EW',repeat=n):
     w=''.join(letters)
     if w.count('W')!=2 or sum(out(w,r,black)=='S'for r in range(n))!=2:continue
     assert w not in generated;generated.add(w)
     re=sum(w[r]=='E'for r in range(n)if(r%2==0)!=black);rw=sum(w[r]=='W'for r in range(n)if(r%2==0)!=black);assert re==rw==a
     su=net(fixed|{Z:w},{Z}if black else set());i=[r for r in range(n)if out(w,r,black)=='S'][1];j=w.index('W');path=[(Z,i)];u=path[0]
     while len(path)==1 or u[0]!=Z:
      assert u in su;u=su[u];assert u[0]==Z or u not in path;path.append(u)
     target=[(Z,i),(2j,1),(1+2j,0),(1+1j,0),(1j,1),(0j,3),(1+0j,1),(1+1j,1),(1j,2),(2j,2),(1+2j,1),(1+3j,0),(2+3j,0),(2+2j,0),(1+2j,2),(1+3j,1),(Z,j)]
     assert path==target and j!=i+1
     actual=next(z for z in J['rows']if z['portal_root']==root and z['reader_starts_BLACK']==black and z['D']==w)
     assert actual['actual16_channel']==[[xy(p),r]for p,r in path];assert(actual['second_S_rank'],actual['first_W_rank'])==(i,j)
     why='backward'if j<=i else'skipped';counts[(root,black,why).__repr__()]+=1;rows.append(dict(root=root,BLACK=black,word=w,source=i,target=j,result=why,path=[[xy(p),r]for p,r in path]))
  assert len(generated)==(22 if black else 18)
assert len(rows)==80 and len(J['rows'])==80
files=['check_one_use_L3_transport_independent.json','check_three_read_one_use_staircase_independent.json']
deps={x:sha(R/'audits'/x)for x in files};assert deps[files[0]]=='ad205d481891b627c1fa783be2f185a112ae784eca5768149867cf68f004069e';assert deps[files[1]]=='8fd1d92b752e25f17151bac74664fd748543a16f606160f5cf0acefa73385c8d'
# Locate the already signed combined immediate-stock/entry/link report by its exact hash.
links=[p for p in (R/'audits').glob('*.json')if sha(p)=='7bfa9ef03abd4be5dbbdbb5f9e7007f2ac9c397616cd7e8e435c448e09e90df1'];assert len(links)==1;deps[links[0].name]=sha(links[0])
O=dict(status='PASS exact three-read LRL entry collision and qualified all-length nonalternation consequence',proof=sha(P),author_certificate=sha(A),script=sha(S),dependencies=deps,all80_actual_channels=rows,counts=dict(counts),analytic_review=[
'All named histories are complete WHITE, including t EEW,r S,q EEW, with u NNSS supplied by the signed rotated 00 GLOBAL-M case. The root EWW versus EWWE changes C SSN versus SSNN but not the sixteen-event return. All directed internal ports, including zero ports, match exactly.',
'The second south departure of D supplies C.L1 and the first west arrival is supplied by u.L1. Independent physical ordinal tracing gives the sixteen steps stated, with no intermediate physical D read. Quotient identifications cannot repair a literal backward or skipped return at this same physical D.',
'If the final first-W arrival were the next D read, all prior arrivals were E. Its second south departure therefore was R_E, leaving BLACK; next L_W would depart south a third time. This uses neither an initial-color assumption nor a multiplicity cap at D.',
'W_in=2=S_out gives R_E=R_W=a<=2. Alternation derives WHITE n=4a or4a-1 and BLACK n=4a or4a+1. Thus the independent complete domain is exactly18 WHITE and22 BLACK words; both supplied root choices give80 actual rank failures, not a guessed bounded scan.',
'For the stated RR1-to3-to1 stock-to-EVEN EWWE portal maximal one-use link, the initial and final internal vertices must LEFT. If wholly alternating, no-fall transport and final q bit0 make every LEFT bit0. The three-LEFT staircase obstruction permits at most two LEFTs. One is the already signed immediate stock join; two end in precisely the present forbidden L0-R-L0. This is a nonalternation obligation only, not a length, fuel or front exclusion.',
'Odd-root q=EEWE, changed source or sink words, prepared BLACK named histories and longer nonalternating links remain outside. The odd-root local return is separately valid only with the explicitly supplied three-read q branch.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(counts);print(sha(S.with_suffix('.json')))
