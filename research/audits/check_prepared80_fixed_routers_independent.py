from pathlib import Path
from collections import Counter,defaultdict
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=D/'PREPARED80_FIXED_ROUTERS_ALL_EXPONENTS_EXCLUSION.md';assert sha(proof).startswith('e3812742')
assert sha(D/'certify_prepared80_router_family_exclusion.py')=='7ed476d26bc7279da767b1d4fde9bb1d36cc1439e78d098d5c103020149b7cf5'
F=D/'prepared80_router_family_exclusion_certificate.json';assert sha(F)=='ccef3e0da42260660a71b745edd23aa2ac8393dd2270c880f1704ab4b240576b';J=json.loads(F.read_text());src=Path(J['growth_bound_dependency']['path']);assert sha(src)=='bd3e74c5a2a87c4431fe4c777b9eeaa7010e42600ab9eb9bea6198e9ca249db7'
M='RRRRLLLLRL';routers=['RLRRRRL','RRRRL','RRRRLRLRLRRRRL','LRRL'];assert M==J['M']and routers==J['routers'];xy=lambda p:[int(p.real),int(p.imag)]
def trace(w,v=1j):
 p=0j;E=[]
 for t,c in enumerate(w):E.append((t,p,v,c));v*=(-1j if c=='R'else 1j);p+=v
 return E,p,v
v=1j;par=0;ds=[];gs=[]
for i,g in enumerate(routers):
 E,d,e=trace(M,v);assert e==v;charges=[sum(1 if c=='R'else-1 for t,p,h,c in E if(t+par)%2==j)for j in(0,1)];row=J['module_geometry'][i];assert xy(d)==row['module_drift']and charges==row['checker_charge']and row['incoming_checker_parity']==par
 E,d,e=trace(g,v);rr=J['router_geometry'][i];assert xy(d)==rr['drift'];charge=[sum(1 if c=='R'else-1 for t,p,h,c in E if(t+par)%2==j)for j in(0,1)];assert charge==rr['checker_charge'];ds.append(d);gs.append(charge);v=e;par=(par+len(g))%2
assert(v,par)==(1j,0)and sum(ds)==3+1j and [sum(x[i]for x in gs)for i in(0,1)]==[5,7]
# Local concatenation proves formulas for all nonnegative exponents. The full
# vector has even checker parity; WHITE complete classes contribute0or1.
# g=12 and the signed full-residue drift theorem give |X|,|Y|<=6, q>=0.
for X in range(-6,7):
 for Y in range(-6,7):
  for q in range(13):
   assert Y-q+6<=12 and Y-X+2<=14 and 10-X-q<=16
expected={(a,b,c,e)for a in range(7)for e in range(7-a)for b in range(8)for c in range(9)};rows={tuple(r['parameters']):r for r in J['all_derived_box_cases']};assert len(rows)==len(J['all_derived_box_cases'])==2016 and set(rows)==expected
counts=Counter();stable=[]
for (a,b,c,e),row in rows.items():
 w=''.join(M*n+r for n,r in zip((a,b,c,e),routers));E,d,v=trace(w);P=len(w);assert v==1j and P==30+10*(a+b+c+e)==row['P']and xy(d)==[3+a-b-c+e,1+a+b-c+e]==row['full_drift']and hashlib.sha256(w.encode()).hexdigest()==row['word_sha256']
 ch=[sum(1 if c0=='R'else-1 for t,p,h,c0 in E if int(p.real+p.imag)%2==j)for j in(0,1)];assert ch==[5+a-b+c+e,7-a+b-c-e]==row['checker_charges'];X,Y=map(int,(d.real,d.imag));q=ch[1];assert 2*(a+e)==Y-q+6 and 2*b==Y-X+2 and 2*c==10-X-q
 if d==0:assert row['status']=='NOT_TRANSLATING';counts['zero']+=1;continue
 # Independent full-vector equivalence, quotient by the actual d (not gcd).
 H=defaultdict(list)
 for t,p,h,c0 in E:
  k=int(p.real)//int(d.real)if d.real else int(p.imag)//int(d.imag);r=p-k*d;H[r].append((t-k*P,t,k,c0,p))
 for z in H.values():z.sort()
 bad=[(r,x,y)for r,z in H.items()for x,y in zip(z,z[1:])if x[3]==y[3]]
 witness=row['witness'];r=complex(*witness['representative']);actual=H[r]
 assert [dict(phase=t,lift=k,canonical_time=ct,turn=c0,actual_position=xy(p))for ct,t,k,c0,p in actual]==witness['complete_class_history']
 if bad:
  assert row['status']=='NONALTERNATING_ON_ANY_PREPARED_BOARD';t1,t2=witness['same_turn_consecutive_phases'];i=next(i for i,z in enumerate(actual)if z[1]==t1);assert actual[i+1][1]==t2 and actual[i][3]==actual[i+1][3];counts['nonalternating']+=1
 else:
  roots=[r for r,z in H.items()if z[0][3]=='L'];assert roots and row['status']=='STABLE_BUT_BLACK_INPUT_REQUIRED'and len(roots)==row['input_count']and actual[0][3]=='L'and actual[0][1]==witness['BLACK_first_phase'];assert sum(z[-1][3]=='R'for z in H.values())==row['output_count'];counts['prepared']+=1;stable.append([a,b,c,e,P,xy(d),len(roots)])
assert counts==dict(zero=28,nonalternating=1984,prepared=4)and stable==[[a,1,1,1,60+10*a,[a+2,a+2],a]for a in range(2,6)]
out=dict(status='PASS all nonnegative exponent fixed-router family exclusion',proof=sha(proof),certificate=sha(F),script=sha(S),source_growth_bound=sha(src),counts=dict(counts),stable_prepared=stable,analytic_review=['Literal local module/router geometry and checker charges prove the symbolic formulas for every exponent. In a complete WHITE front every complete physical class contributes nonnegative checker charge; full d has even checker parity, including axis drifts. Together with g>=2max(|X|,|Y|), the three exact linear identities derive a+e<=6,b<=7,c<=8. No guessed period or visit cap is imposed.','All2016 tuples are reconstructed from literal turns and actual full-drift classes, ordered by phase-P*lift. Every nonalternation witness is checked in its complete class. The four alternating cases require genuine BLACK-first input classes; they are not rejected as physically impossible prepared waves.','For nonzero drift, sufficiently far repeated physical copies lie outside every finite initial BLACK support and therefore must begin R. Thus this exact fixed-router family cannot repeat forever from a finite seed. Changing routers, mixed member concatenations, extra runs and all other WHITE fronts remain outside the theorem. The prior prepared80 actual counterexample and its active peak11 are preserved.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
