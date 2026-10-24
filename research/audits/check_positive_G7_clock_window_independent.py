from pathlib import Path
from itertools import product
from fractions import Fraction
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'actual_G7_positive_clock_contact_window_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((D/'manifest.json').read_text());assert sha(D/'manifest.json')=='e8bcc46e3bca45eeec199b7fe89339da239af4485c3cba20977dd6a432343671'
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
q=R/'audits/check_one_foreign_contact_C_window_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('def inside')[0],ns)
W,M,walk,center,xy,principal,plus,minus=[ns[k]for k in('W','M','walk','center','xy','principal','plus','minus')]
J=json.loads((D/'positive_clock_window.json').read_text());clock={'D':0,'C':1,'V':0,'U':0,'F':2,'Q':2,'B':2};head=[]
for a in clock:
 z=walk(W[a]);assert z['feasible']and z['h']==(-clock[a])%4;head.append(dict(atom=a,clock_increment=clock[a],actual_RAW_EXIT_headingCW=z['h']))
assert head==J['all7_actual_heading_clock_interfaces']
# Reconstruct every adjacent principal turn as a pair of exact pi/4,beta coefficients.
alpha={'D':(1,0),'C':(1,0),'V':(2,-1),'U':(2,0),'F':(4,1),'TQ':(2,0),'TB':(2,1)}
last={'Q':'TQ','B':'TB'};rot=lambda h:(-1j)**h
actual={}
for a in'DCVUFQB':
 z=walk(W[a]);pts=[center(0j,0)]
 if a in'QB':f=walk(W['F']);pts.append(center(f['p'],f['h']))
 pts.append(center(z['p'],z['h']));actual[a]=(z['h'],[v-u for u,v in zip(pts,pts[1:])])
turns=[]
for a,b in product('DCVUFQB',repeat=2):
 x=last.get(a,a);y='F'if b in'QB'else b;omega=2 if x=='C' else 4 if x=='F' else 0
 coef=plus((omega-8*int(a=='C'and b in'FQB'),0),minus(alpha[y],alpha[x]));ha,va=actual[a];hb,vb=actual[b]
 if x==y=='F':assert coef==(4,0)and not walk(W[a]+W[b])['feasible']
 else:principal(xy(va[-1]),xy(vb[0]*rot(ha)),coef)
 turns.append(dict(before=a,after=b,coefficient=coef,CFwrap=(a=='C'and b in'FQB')))
# Intrinsic source offsets are direct algebra from terminal target alpha and remaining source pieces.
a={'D':(1,0),'C':(1,0),'V':(0,1),'U':(0,0)}
def form(src,tgt,L):
 if src in a:return plus((2*L,0),minus(a[src],a[tgt]))
 return minus(plus((2*L,0),{'F_prefix':(2,-1),'Q_tail':(0,0),'B_tail':(0,-1)}[src]),a[tgt])
def inside(c):
 lo,hi=sorted([c[0],sum(c)])
 if lo>=4 and hi<=12 and not(c[1]==0 and c[0]in(4,12)):return True
 assert hi<=4 or lo>=12
 return False
rows=[]
for src,tgt in product(['D','C','V','U','F_prefix','Q_tail','B_tail'],'DCVU'):
 off=form(src,tgt,0);assert min(off[0],sum(off))>=-2 and not(off[1]==0 and off[0]<=-2)
 allowed=[L for L in range(8)if inside(form(src,tgt,L))];assert min(form(src,tgt,8)[0],sum(form(src,tgt,8)))>12
 pairs=[dict(effective_L=L,actual_C_count_K=L-2*f,intervening_complete_foreigns_f=f,max_ordinary_monotone_epochs=L-f+1)for L in allowed for f in range(L//2+1)if src!='C'or L-2*f>=1]
 au=next(z for z in J['all28_source_ordinary_actor_windows']if(z['source'],z['ordinary_contact_actor'])==(src,tgt));assert allowed==au['allowed_effective_L']and pairs==au['all_necessary_K_f_pairs']
 for r in au['all8_exact_angle_bounds']:
  assert tuple([r['T_coeff_pi_over4'],r['T_coeff_beta']])==form(src,tgt,r['effective_clock'])and r['strict_Jordan_window']==inside(form(src,tgt,r['effective_clock']))
 assert max(z['intervening_complete_foreigns_f']for z in pairs)<=3 and max(z['max_ordinary_monotone_epochs']for z in pairs)<=7
 rows.append(dict(source=src,target=tgt,offset=off,allowed_L=allowed,K_f_pairs=pairs))
cf=walk(W['C']+W['F']+M);assert cf['feasible'];assert next(z for z in turns if(z['before'],z['after'])==('C','F'))['coefficient']==(-3,1)
review=[
'The independently signed generic foreign-interval grammar removes every actual adjacent C-toFOREIGN boundary in the stipulated U-start G7 factor, including before its firstFOREIGN. EmptyQF/BF do not reintroduce aC wrap. All raw CF/CQ/CB prepared positives remain outside this implication.',
'Fresh actual endpoint/tangent reconstruction checks all49 adjacent turns. The exact open-turn sum telescopes for arbitrary word length, with endpoint corrections terminalC and terminal standaloneF only; Q/B tails remain real separate pieces. No repeated application of a oneFOREIGN geometric theorem is used. An F-piece followed by another F-prefix is the only formal reversing join; literalFF fails, excluding macroFF/FQ/FB alike.',
'For an ordinary old source, K includes its ownC if applicable and excludes a targetC interval; f counts complete FOREIGNs between source and target entries. For an F-prefix source its OWN FOREIGN contributes the retained+pi/2-beta correction, not an extra f. Q/Btail sources use their own fixed tangent corrections and count only subsequentFOREIGNs. These yield the four displayed source-turn forms exactly.',
'At GLOBAL-first contact, the earlier full repaired proxy is simple. Choose earliest positive onset and the outgoing old piece at a vertex/kink. The old subarc plus new partial ordinary chord is a Jordan curve. Opposite closing tangents would overlap earlier; same-direction collinear onset is retained with zero closing turn. Thus -pi<delta<pi. Every source form is>-pi/2 even atK=f=0, so total turning cannot be-2pi and must be+2pi, giving pi<T<3pi.',
'Exact beta/(pi/4) in(0,1) coefficient bounds yield all28 windows without numerical angle tolerance or word-depth cap. L>=8 exceeds the upper bound by a derived uniform inequality. All nonnegativeK,f decompositions retain sourceC K>=1; f<=3, F-prefixf<=2 and K+f+1<=7 follow arithmetically.',
'The at-most-seven ordinary monotone epochs have unbounded lengths and state. Foreign-actor first contacts, all source lifetime maturity, color survival through FOREIGN, contact exclusion, arbitrary-language entry and global capture remain outside. A source tail may touch its own foreign PLUS three later complete foreign words.'
]
out=dict(status='PASS exact positive actual-G7 clock and necessary multi-FOREIGN ordinary-contact windows',manifest=sha(D/'manifest.json'),dependencies=m['dependencies'],headings=head,all49_principal_interfaces=turns,all28_windows=rows,analytic_review=review,scope=m['scope'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
