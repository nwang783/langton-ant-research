"""Exact old-D age-one second-contact slice; endpoint exhaustion, not a depth cap."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from collections import Counter
import importlib.util,json,hashlib
H=Path(__file__).resolve().parent
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(p,q):return(p[0]+q[0],p[1]+q[1])
def sub(p,q):return(p[0]-q[0],p[1]-q[1])
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q=p[:2];h=p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return(*q,h)
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def floor(q):return q.numerator//q.denominator
def ceil(q):return-((-q.numerator)//q.denominator)
a,b=chord('D',(0,0,0));u=sub(b,a);boxes=[];geo=[];typed=[];solutions=[];words={};counts=Counter()
for b1 in'DCVU':
 N=1+(b1=='C');h=(2-N)%4
 for b2 in'DCVU':
  c,d=chord(b2,(0,0,h));v=sub(d,c);den=det(u,v);corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)];bounds=[(floor(min(p[k]for p in corners)),ceil(max(p[k]for p in corners)))for k in(0,1)]
  boxes.append(dict(first=b1,second=b2,effective_N=N,exact_corners=[[[q.numerator,q.denominator]for q in p]for p in corners],exact_integer_bounds=bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y-N)%2:continue
    zz=sub(add(c,(2*x,2*y)),a)
    if den:
     ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
     if not(0<=ss<1 and 0<tt<=1):continue
    else:
     if det(zz,u):continue
     k=0 if u[0] else 1;st=Q(zz[k],u[k]);mul=Q(v[k],u[k]);assert mul>0
     if st>=0:continue
     tt=-st/mul;ss=Q(0)
     if not(0<tt<=1):continue
    p2=(x,y,h);geo.append((b1,b2,p2,ss,tt))
    for A in'FQB':
     dp=after(W[A]+W[b1],(0,0,3));pa=(x-dp[0],y-dp[1],3);raw=W[A]+W[b1]+W[b2];tr=l.trace(raw+l.M);reason='keep'
     if not tr['feasible']:reason='local_conflict'
     else:
      for guard in[(2,0),(1,-1)]:
       loc=l.rot(sub(guard,pa[:2]),-pa[2]);f=tr['first'].get(loc)
       if loc in l.K:reason='guardian_in_A_K';break
       if f and f[0]=='R':reason='guardian_before_WHITE';break
     typed.append((A,b1,b2,pa,p2,reason));counts[reason]+=1
     if reason!='keep':continue
     if pa[1]<2:counts['no_endpoint_y']+=1;continue
     nsol=0
     for dn in range(pa[1]-1):
      for vn in range((pa[1]-2-dn)//3+1):
       for un in range((pa[1]-2-dn-3*vn)//4+1):
        rem=pa[1]-2-dn-3*vn-4*un
        for dw in range(rem+1):
         vw=rem-dw;num=1+dn+vn-dw-3*vw-pa[0]
         if num<0 or num%4:continue
         uw=num//4
         if dw+vw+uw==0:continue
         nsol+=1;solutions.append((A,b1,b2,pa,p2,dn,vn,un,dw,vw,uw))
         for X in sorted(set(permutations('D'*dn+'V'*vn+'U'*un))):
          for Y in sorted(set(permutations('D'*dw+'V'*vw+'U'*uw))):
           if Y[-1]not in('VU'if A in'FQ'else'U'):continue
           T='D'+''.join(X)+'C'+''.join(Y)+A+b1+b2
           if T in words:continue
           rawold=''.join(W[z]for z in T[:-(len(A+b1+b2))]);old=l.trace(rawold)
           if not old['feasible']:r='old_literal_conflict'
           else:
            # exact young-current guards before A, physical RAW reads only
            # use full path actual global positions rather than restarted chart
            p=(0,0);hh=0;bad=False
            for tick,c0 in enumerate(rawold):
             if tick>=10 and p in[(2,0),(1,-1)]:bad=True
             hh=(hh+(1 if c0=='R'else-1))%4;p=add(p,l.DIRS[hh])
            if bad:r='young_guard_old_RAW_read'
            else:
             full=l.trace(''.join(W[z]for z in T)+l.M)
             r='FULL_FEASIBLE_PREPARED_D_ENTRY'if full['feasible']else'full_literal_conflict'
           words[T]=r
     if nsol==0:counts['no_endpoint_counts']+=1

# The source D is a BASE, so its actual preceding full packet contributes
# one of eight FINAL atomic roles, not an unsupported internal C prefix.
previous_roles=[]
for P in ('D','DC','V','VC','VCC','U','UC','UCC'):
    w=''.join(W[z]for z in P);ep=after(w);g=l.literal_geometry(w)
    beta=add(ep[:2],l.rot((1,-1),ep[2]));tr=l.trace(w)
    assert tr['last'][beta]==('R',len(w)-2) and list(beta)in g['outputs']
    c=P.count('C')
    previous_roles.append(dict(previous_full=P,ownCs=c,previous_full_entry_clock=-c,
        full_source_age_at_FOREIGN=1+c,actual_post_EXIT_age_at_FOREIGN=1,
        original_beta_full_output=beta,actual_last_R_tick0=len(w)-2))

assert len(boxes)==16 and len(geo)==23 and len(typed)==69 and len(solutions)==142
assert Counter(r[-1]for r in typed)=={'keep':45,'guardian_before_WHITE':18,'local_conflict':6}
assert len(words)==347 and Counter(words.values())=={
    'old_literal_conflict':145,'full_literal_conflict':160,'FULL_FEASIBLE_PREPARED_D_ENTRY':42}
positive_tokens=sorted(T for T,c in words.items()if c=='FULL_FEASIBLE_PREPARED_D_ENTRY')
assert Counter('DC'if T.startswith('DC')else'D'for T in positive_tokens)=={'DC':22,'D':20}
assert sum('U'in T for T in positive_tokens)==36

def physical_owner(T,tick):
    lo=0
    for i,z in enumerate(T):
        if tick<lo+len(W[z]):
            return dict(actual_atom_index0=i,actual_atom=z,atom_start_tick0=lo,
                        canonical=o.describe(z,tick-lo))
        lo+=len(W[z])
    j=tick-lo;assert 0<=j<len(l.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,next_word_read_number1=j+1,turn=l.M[j])

def control(T,prepared_beta=False):
    body=''.join(W[z]for z in T);tr=l.trace(body+l.M);assert tr['feasible']
    seed={q for q,(c,t)in tr['first'].items()if c=='L'}
    if prepared_beta:
        assert tr['first'].get((1,-1),('L',0))[0]!='R';seed.add((1,-1))
    B=set(seed);p=(0,0);h=0;cut=None
    for tick,c in enumerate(body+l.M):
        assert(p in B)==(c=='L')
        if c=='L':B.remove(p)
        else:B.add(p)
        h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
        if tick+1==len(body):cut=dict(head=(*p,h),complete_black=sorted(B),mass=len(B))
    return dict(tokens=list(T),RAW_length=len(body),physical_reads=len(body)+len(l.M),
        complete_initial_black=sorted(seed),all_unlisted_initial_cells_WHITE=True,initial_mass=len(seed),
        incoming_beta_is_prepared_initial_not_genuine_U_ancestry=prepared_beta,
        RAW_exit=cut,actual_M11_exit=dict(head=(*p,h),complete_black=sorted(B),mass=len(B)))

word_records=[]
for T,classification in sorted(words.items()):
    Aindex=next(i for i,z in enumerate(T)if z in'FQB');Cindex=T.index('C')
    X,Y=T[1:Cindex],T[Cindex+1:Aindex];tr=l.trace(''.join(W[z]for z in T)+l.M)
    assert tr['feasible']==(classification=='FULL_FEASIBLE_PREPARED_D_ENTRY')
    r=dict(tokens=list(T),classification=classification,selected_source_full='DC'if not X else'D',
           source_C1_atom_index0=Cindex,old_N_run=list(X),old_W_run=list(Y),
           foreign_entry=after(''.join(W[z]for z in T[:Aindex])))
    if not tr['feasible']:
        r.update(immutable_conflict=tr,previous_actual_owner=physical_owner(T,tr['previous_read']),
                 failing_actual_owner=physical_owner(T,tr['conflict_read']))
    word_records.append(r)

controls=[control(T,True)for T in positive_tokens]
Dcontrols=[control('D'+T)for T in positive_tokens]
nodes=[(T,T)for T in positive_tokens]+[('D+'+T,'D'+T)for T in positive_tokens]
assert len({T for label,T in nodes})==84
reverse=[]
for label,T in nodes:
    for P in'DCVUFQB':
        trial=P+T;tr=l.trace(''.join(W[z]for z in trial)+l.M)
        assert tr['feasible']==(not label.startswith('D+')and P=='D')
        r=dict(suffix_node=label,predecessor=P,feasible=tr['feasible'])
        if not tr['feasible']:
            r.update(immutable_conflict=tr,previous_actual_owner=physical_owner(trial,tr['previous_read']),
                     failing_actual_owner=physical_owner(trial,tr['conflict_read']))
        reverse.append(r)
assert len(reverse)==588 and sum(r['feasible']for r in reverse)==42

paths=[R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
       R/'audits/check_second_ordinary_small_interface_independent.json',
       R/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',
       R/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
       R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
       R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_OLD_D_AGE1_SECOND_CONTACT_PENDING_REVIEW',
    scope='Only outgoing oldD BASE inside original U-entry complete-eight prefix, true source-entry-to-FIRSTforeign C age1, chronological FIRST new SECOND ordinary RAW contact, actual b1+b2+finalM11. No other age/source or second simplicity.',
    all8_actual_previous_full_FINAL_bud_roles=previous_roles,
    guardians_current_at_FOREIGN=[dict(cell=(2,0),genuine_source_D_R8=True),dict(cell=(1,-1),genuine_actual_previous_atomic_EXIT_bud=True,post_EXIT_age=1)],
    all16_exact_contact_parallelograms=boxes,
    all23_b1_typed_contact_poses=[dict(first=b1,second=b2,second_pose=p2,old_s=[ss.numerator,ss.denominator],new_t=[tt.numerator,tt.denominator])for b1,b2,p2,ss,tt in geo],
    all69_foreign_alignments=[dict(foreign=A,first=b1,second=b2,foreign_pose=pa,second_pose=p2,classification=why)for A,b1,b2,pa,p2,why in typed],
    exact142_endpoint_count_solutions=[dict(foreign=A,first=b1,second=b2,foreign_pose=pa,second_pose=p2,dN=dn,vN=vn,uN=un,dW=dw,vW=vw,uW=uw)for A,b1,b2,pa,p2,dn,vn,un,dw,vw,uw in solutions],
    endpoint_identity='xA=1+dN+vN-dW-3vW-4uW; yA=2+dN+3vN+4uN+dW+vW. All counts nonnegative; W run nonempty and lastV/U(orU forB). This forces finite counts; no path-depth bound.',
    all347_exact_whole_words=word_records,word_classification=dict(Counter(words.values())),
    all42_complete_prepared_D_entry_controls=controls,all42_complete_D_prepend_controls=Dcontrols,
    all588_closed_seven_atom_reverse_queries=reverse,
    reverse_closure='Each42 base positive has ONLY rawD parent. Each D-prepended positive has NO seven-atom parent.84 nodes/42 edges; relation naturally closed, not truncated.',
    conclusion='No selected oldD at true preforeign age1 inside a prior U-entry factor realizes the stipulated FIRST SECOND-contact. Exact one-C endpoints exhaust all body histories, so the reverse closure applies to the complete scoped slice.',
    later_internal_U_warning='36 positives contain laterU. Those genuine U-entry subfactors do NOT contain the selected first D chord. Only U ancestry BEFORE selected oldD is excluded and required.',
    source_clock_warning='Previous full source withc ownCs starts at clock-c; atFOREIGN full age1+c while actual postEXIT age is1. Signed1325 applies postEXIT1; no false full-source clock reset. Only eight FINAL roles precede a D base.',
    no_postforeign_maturity_or_exterior_reset=True,no_general_second_simplicity=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'D_age1_first_contact.json').write_text(json.dumps(out,indent=2)+'\n')
print('23 b1-typed poses/69 A types ->45; exact142 endpoint counts ->347 words,305 immutable failures+42 prepared positives.')
print('84-node/588-query reverse closure: only D parents once, then none; no U BEFORE selectedD. Later internalUs remain explicit.')
