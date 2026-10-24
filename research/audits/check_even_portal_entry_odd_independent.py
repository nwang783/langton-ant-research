from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files={'even_LL_portal_entry_forces_a_LEFT_and_an_odd_output.md':'fad3fa8eb29cfa9933f876d2c3b913ed380ac2a47a9270a4da6ed66d72ad92f0','check_even_portal_entry_incidence.py':'8af03d25','check_even_portal_entry_incidence.json':'b3e564ca','even_portal_entry_incidence_is_cap_free_at_the_reader.md':'5b7a0101385d02780728a82026b794ad54ae841abf843e8c54c26ddedfbea563','check_even_portal_uncapped_reader.py':'d6e05acc','check_even_portal_uncapped_reader.json':'66f8dd07'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_even_portal_entry_incidence.json').read_text());U=json.loads((D/'check_even_portal_uncapped_reader.json').read_text());H='NESW';V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];out=lambda w,r:H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
def analyze(root,q,c,row):
 hs={1+1j:'SN',1j:root,0j:'NNSS',1+0j:'EE',1+2j:q,2j:c};su={};bad=[]
 for p,w in hs.items():
  for h,d in zip(H,V):
   if p+d not in hs:continue
   ss=[r for r in range(len(w))if out(w,r)==h];tt=[r for r,hh in enumerate(hs[p+d])if hh==h]
   if len(ss)!=len(tt):bad.append((p,h,p+d,ss,tt))
   else:su.update({(p,r):(p+d,s)for r,s in zip(ss,tt)})
 if bad:
  assert row['result']=='port';cert=row['certificate'];assert any(cert==dict(source=xy(p),direction=h,source_ranks=ss,target=xy(v),target_ranks=tt)for p,h,v,ss,tt in bad);return 'port'
 wrong=[]
 for p,w in hs.items():
  for r in range(len(w)):
   cur=(p,r);seen={cur};path=[cur]
   while cur in su:
    cur=su[cur];path.append(cur)
    if cur[0]==p:
     if cur[1]!=r+1:wrong.append(path)
     break
    assert cur not in seen
    seen.add(cur)
 if wrong:
  assert row['result']=='rank';path=[(complex(*p),r)for p,r in row['certificate']['path']];assert path in wrong and row['certificate']['start_rank']==path[0][1]and row['certificate']['returned_rank']==path[-1][1];return'rank'
 assert row['result']=='open';assert{((complex(*a[0]),a[1]),(complex(*b[0]),b[1]))for a,b in row['certificate']['successor_edges']}==set(su.items());assert c.startswith('SS')and out(c,0)=='W'
 # Forced first physical ports, not arbitrary selected indices.
 firstE=next(r for r in range(len(c))if out(c,r)=='E');firstN=c.index('N');assert firstE==1 and firstN>=2
 assert su[(2j,1)]==(1+2j,0)and su[(1+2j,0)]==(1+1j,0)and su[(1+1j,0)]==(1j,1)
 assert su[(1j,2)]==(2j,firstN)
 return'open'
words=[''.join(z)for n in range(5)for z in product('NS',repeat=n)];rows={(r['root'],r['q'],r['C']):r for r in J['rows']};cnt=Counter()
for root,q,c in product(['EWW','EWWE'],['E','EE','EEW','EEWE'],words):cnt[analyze(root,q,c,rows[root,q,c])]+=1
assert len(rows)==248 and cnt==J['summary']==dict(port=225,rank=18,open=5)
# Fresh complete-domain generator using positions of N among even/odd indices.
from itertools import combinations
urows={(r['root'],r['q'],r['C']):r for r in U['rows']};keys=set();uc=Counter();opens=[]
for root,q in product(['EWW','EWWE'],['E','EE','EEW','EEWE']):
 k=sum(out(root,r)=='N'for r in range(len(root)));l=q.count('E')
 for eps in(0,1):
  for a in range(k+1):
   b=k-a;t=l-a;s=k+l-3*a+eps
   if min(b,t,s)<0:continue
   n=a+b+s+t;assert n==2*(k+l-2*a)+eps<=11
   if n<=0:continue
   for rn in combinations(range(0,n,2),a):
    for ln in combinations(range(1,n,2),b):
     nn=set(rn)|set(ln);c=''.join('N'if i in nn else'S'for i in range(n));assert sum(out(c,r)=='E'for r in range(n))==l
     key=(root,q,c);assert key not in keys;keys.add(key);row=urows[key];assert(row['Nin'],row['Eout'],row['length'],row['R_S_minus_R_N'])==(k,l,n,s-a)
     why=analyze(root,q,c,row);uc[why]+=1
     if why=='open':opens.append((*key,s-a))
assert keys==set(urows)and len(keys)==131 and uc==U['summary']==dict(rank=119,open=12);assert sorted(opens)==sorted(tuple(r)for r in U['open_profiles'])
assert sum(ca==0 for root,q,c,ca in opens)==5 and all(ca>=1 for root,q,c,ca in opens if len(c)>=5)
assert{c for root,q,c,ca in opens if root=='EWWE'and q=='EEWE'}=={'SSNNSS','SSNSSN','SSNNSSS','SSNSSNS'}
# Exact all-read algebra: even-root/even-q C counts k2,l3, first S gives c>=1.
for eps in(0,1):
 for a in range(3):
  c=5-3*a+eps
  if c>=1:assert a<=1 and c-a>=1
# Quarter-rotated physical inverse recovery; two history types remain disjoint.
for h in range(4):
 rot=(-1j)**h
 for shift in[0j,7-3j,-5+11j]:
  B=(1+1j)*rot+shift;Y=1j*rot+shift;q=(1+2j)*rot+shift
  assert Y+V[(1+h)%4]==B and q+V[(2+h)%4]==B
  ry=''.join(H[(H.index(c)+h)%4]for c in'EWW');rq=''.join(H[(H.index(c)+h)%4]for c in'EEW');assert(H.index(ry[1])-H.index(ry[0]))%4==2 and rq[0]==rq[1]
O=dict(status='PASS exact even-portal LEFT entry and nonadditive odd-output injection; separate cap-free-reader/global-M extension',files={f:sha(D/f)for f in files},script=sha(S),cap4_counts=cnt,derived_domain_counts=uc,uncapped_open_profiles=sorted(opens),analytic_review=[
'The 248 complete six-cell cap4 products and every physical ordinal witness were independently rebuilt. Complete q Sout1 words are E,EE,EEW,EEWE. Five opens all force C firstR S departingW. A RIGHT q would require C firstR to departE into it, impossible even across full quotient lifts. LEFT q preserves one-use flow, leaving the stated three profiles.',
'The uncapped argument is stronger than the cover: q.R0->B.R0->Y.L1 and C firstEout->q.R0, whereas Y.R2 supplies C firstNin. Thus first Eout precedes first Nin, and complete-WHITE C must start SS with its first Eout at L1. The same missing b predecessor excludes RIGHT q at arbitrary q/C multiplicity, without a maximum or critical premise.',
'For the separate GLOBAL-M portal premise, the equal Y C sectors identify q first-R SW sector and C opposite SE sector with M. Only THEN the independently qualified cap-free Sout1 maximum domain limits q to4 reads. No universal all-cap first-R maximum is imported. EvenY/evenq would require NinC2/EoutC3; R_S=5-3R_N+epsilon and firstS force R_S-R_N>=1, making C first-R NW sector exceed M.',
'The entire count-derived C domain n<=2(k+l)+1<=11 is generated independently by even/odd N-position subsets, not a guessed cap. All131 histories and119 literal rank failures match. The four6/7-read higher-C shields are retained outside GLOBAL M and are not actual-factor claims.',
'Odd Y EWW has opposite R0/L1 headings; odd q EEW has same headings, so mixed orientations cannot alias types. Each full-quotient witness recovers its unique portalB by its incomingR0 vector or outgoingR0 vector respectively. This yields a nonadditive output reservation only; no original-fuel charge or addition to overlapping reservations.',
'Prepared F49 has BLACK-first C and only finite q prefix, so does not satisfy this complete-WHITE kernel. No arbitrary boundary coverage, wholly-one-use circle, controller exclusion or capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(cnt,uc);print(sha(S.with_suffix('.json')))
