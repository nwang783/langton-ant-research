from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'EXPLICIT_RECORD_CLOCK_MANIFEST.json';assert sha(mf)=='1df0229443dc04764efa17f890339bbd8a085e4aecbee9f8a0f1cdf458dc6e8e'
m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(D/f)==h
J=json.loads((D/'EXPLICIT_RECORD_CLOCK_CHECKED.json').read_text());source=json.loads((D/'JOINT_RECORD_DROUGHT_CHECKED.json').read_text());V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];norm=lambda p:[int(p.imag),int(p.real),-int(p.imag),-int(p.real)];fieldhash=lambda B:hashlib.sha256(json.dumps(sorted(map(xy,B)),separators=(',',':')).encode()).hexdigest()
# Independent predictor reconstructs FORWARD from the inferred initial heading,
# unlike the author's backward-coincidence search.
def predict(h,history):
 h0=(h-sum(1 if c=='R'else-1 for c in history))%4;p=0j;seen={}
 for c in history:
  seen[p]=c;h0=(h0+(1 if c=='R'else-1))%4;p+=V[h0]
 assert h0==h
 return 'L'if seen.get(p)=='R'else'R'
regs=[]
for ar in J['truncated_prediction_regressions']:
 B={complex(*q):-1 for q in ar['seed']};p=0j;h=0;hist=[];counts={a:0 for a in(1,4,16,64)}
 for t in range(1200):
  c='L'if p in B else'R'
  for g in counts:
   if t>=g and predict(h,hist[-g:])!=c:
    assert c=='L'and B[p]<t-g;counts[g]+=1
  if c=='L':B.pop(p)
  else:B[p]=t
  h=(h+(1 if c=='R'else-1))%4;p+=V[h];hist.append(c)
 assert {str(k):v for k,v in counts.items()}==ar['only_old_BLACK_prediction_failures'];regs.append(dict(seed=ar['seed'],mismatch_counts=counts))
def parity(B,Q,d,w):
 axis=lambda p:int(p.real)if d.real else int(p.imag);dd=axis(d)
 def mul(v):
  if axis(v)%dd:return None
  k=axis(v)//dd;return k if k*d==v else None
 crits=[];maxhit=-1;maxover=0;tests=0
 for i,q in enumerate(Q):
  hits={k for z in B if(k:=mul(z-q))is not None and k>=0};over=[k for j,z in enumerate(Q)if(k:=mul(z-q))is not None and(k>0 or k==0 and j<i)]
  crit={0}|set(over)|hits|{k+1 for k in hits}
  for k in crit:assert((k in hits)^bool(sum(m<=k for m in over)%2))==(w[i]=='L');tests+=1
  crits.append(sorted(crit));maxhit=max([maxhit]+list(hits));maxover=max([maxover]+over)
 return crits,maxhit,maxover,tests
controls=[]
for au in J['full_repeat_certificate_controls']:
 n=au['n'];sc=next(c for c in source['controls']if c['name']==f'MT_{n}');cut=88368+208*n;ss=sc['named_full_snapshots'][str(cut)];B={complex(*q)for q,i in ss['full_field']};p=complex(*ss['pose'][0]);h=ss['pose'][1];ext=list(ss['hull']);history=[]
 for t in range(208):
  ext=[max(a,b)for a,b in zip(ext,norm(p))];c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];history.append(c)
 ext=[max(a,b)for a,b in zip(ext,norm(p))];B0=set(B);p0=p;h0=h;M0=list(ext);memory=(h,history[-208:]);w=[];Q=[];records=[];last=0;P=104;H=104;K=2*P+H+2
 assert fieldhash(B)==au['initial_full_sha256']and len(B)==au['initial_full_mass']and[*[xy(p),h]]==au['loop_pose']and M0==au['old_full_hull']
 for t in range(P*K):
  for a,v in enumerate(norm(p)):
   if v>ext[a]:assert v==ext[a]+1;ext[a]=v;records.append((t,a));last=t
  assert t-last<H;c='L'if p in B else'R'
  if t<3*P:assert predict(h,history[-208:])==c
  if t<P:w.append(c);Q.append(p)
  else:assert c==w[t%P]
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];history.append(c)
  if t+1==P:assert(h,history[-208:])==memory;d=p-p0;assert h==h0
 w=''.join(w);assert w==au['word']and xy(d)==au['drift']and d!=0
 rr,normal=next((t,a)for t,a in records if P<t<=P+H);assert[rr,normal]==au['positive_record']and norm(d)[normal]>=1 and M0[normal]<=norm(p0)[normal]+P+H
 assert min(norm(q)[normal]for q in Q)>=norm(p0)[normal]-P
 crits,hit,over,tests=parity(B0,Q,d,w);assert crits==au['all_critical_indices']and hit==au['initial_ray_hit_max']and over==au['self_overlap_max']and hit<=2*P+H and over<=P and max(map(max,crits))<=K-1
 assert len(B)==au['terminal_full_mass']and fieldhash(B)==au['terminal_full_sha256']
 # Whole final field gets an additional independent infinite-tail parity check.
 Qend=[q+(p-p0)for q in Q];_,endhit,endover,endtests=parity(B,Qend,d,w)
 controls.append(dict(n=n,source_cut=cut,reads=208+P*K,initial_full_mass=len(B0),initial_hash=fieldhash(B0),terminal_full_mass=len(B),terminal_hash=fieldhash(B),record=[rr,normal],period=P,drift=xy(d),observed_copies=K,complete_field_hit_max=hit,self_overlap_max=over,initial_tests=tests,terminal_tests=endtests))
small=[]
for H in (1,2):
 G=H*(H+1)**4;S0=4*(2**G);F=G+1+2*S0*S0+(H+3)*S0;small.append(dict(H=H,G=G,S=str(S0),F_star=str(F)))
assert small==J['small_formula_regressions']and sum(z['reads']for z in controls)==98592
O=dict(status='PASS explicit finite-record-clock forcing bound',manifest=sha(mf),proof=m['files']['EXPLICIT_FINITE_RECORD_CLOCK_BOUND.md'],script=sha(S),formula='G=H(H+1)^4; S=4*2^G; F*=G+1+2*S^2+(H+3)*S',small_arithmetic=small,predictor_controls=regs,whole_field_controls=controls,analytic_review=[
'For every subinterval inside the finite H-clock window, endpoint-inclusive event gaps are<=H; the signed last-normal lemma bounds any visit back into its earlier augmented rectangle byG. No asymptotic/global clock assumption is needed.',
'At t>=G+1 an originalBLACK read would lie inR0 too late. An R-bornBLACK with no read in[t-G,t) hasbirthb<t-G and forbidden age>G (equivalently lies inR_(t-G-1)). The most recent retained same-cell turn determinescolor exactly; if no retained visit exists, it mustbeWHITE. An oldL never causes a falseBLACK prediction.',
'Currentheading plus lastGturns reconstructs relativepositions and gives one deterministic memory transition while the finite clock holds. There are<=4*2^G states. The S+1 cuts G+1..G+1+S give a repeated state and period1<=P<=S, with s+P<=G+1+S. The actual observed word repeats until the end of the window; this is not a finite-state claim about the whole physical board.',
'K=2P+H+2 copies fit beforeF* by s+PK<=G+1+S+S(2S+H+2). The H-clock gives a strict unionrecord r in(s+P,s+P+H], within those copies. Its earlier identical phase r-P>=s was visited, so the record normal has a·d>0. In particular d!=0 and the repeated heading is explicit.',
'Every cell of COMPLETE B_s is inside the actual augmented hull. Strictrecordr and unit speed give M_a(s)<=a·p_s+P+H. Every phase read is >=a·p_s-P in thatnormal. Thus any hit on initialB_s has periodindexk<=2P+H. This uses every original/written oldBLACK, not a recent crop or active subset.',
'For self-overlaps Q_j-Q_i=m d, a nonzero integer coordinate ofd and the within-period unit-walk diameter give positive m<=P. Each phasecolor is determined by finitelymany threshold flips and initial-field hit spikes. All changes, including last-hit successors, occur byK-1. The K physically observed copies verify them all, so exact parity induction proves the FULL original board has this tail forever froms.',
'This supplies explicit period<=S and onset<=G+1+S under the finite clock premise, strengthening the signed compactness existence theorem without using its cover search. The same EVERY-interval nontranslator drought consequence now has explicit F*. No numerical simulation at F* scale was performed.',
'Bounded controls retain full MT old fields,98592 physical updates, all initial-field ray hits and an extra full final-field infinite parity verification. The4800 tiny-history tests use an independent forward-position predictor; they confirm its only possible error outside the clock premise is an oldBLACK input. These are interfaces, not a finite exhaustion proof of the analytic bound.'
],scope='Complete finite initial seed and its entire augmented hull. A pristine finite H-dense union-record window of lengthF* forces eventual translating turns/poses, not full-board equality. No universal forcing-window occurrence, canonical104 uniqueness, practical runtime, or finite-prefix certificate against undisclosed remoteBLACK.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
