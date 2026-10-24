from pathlib import Path
import hashlib,itertools,json,collections
S=Path(__file__).resolve();R=S.parents[1];A=R/'autonomous_controllers_2026-10-24'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note=A/'EXTREMAL_CYCLE_RESIDUE_CHARGE.md'
assert sha(note)=='8716dd224fb915b1548d652eb58f3ab0fb9fc658fee98cc20d0315411db4b6f7'
res=R/'sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md'; drift=R/'periodic_classification_new/minimal_full_drift_corollary.md'
assert sha(res)=='bd3e74c5a2a87c4431fe4c777b9eeaa7010e42600ab9eb9bea6198e9ca249db7'
assert sha(drift)=='e6580bdb07dfd6c378c086640f777596ea74d17f4d1a77bc593e22cd312ae3ad'
controls=[]
# Geometric controls only. Enumerate all alternating-axis paths through length10,
# retaining simple full-drift quotient circuits, never replacing full by primitive.
for ell in (4,6,8,10):
 count=0
 for axis in (0,1):
  for signs in itertools.product((-1,1),repeat=ell):
   pts=[(0,0)]
   for i,s in enumerate(signs):
    q=list(pts[-1]);q[(axis+i)%2]+=s;pts.append(tuple(q))
   a,b=(-pts[-1][0],-pts[-1][1])
   if (a,b)==(0,0):continue
   def key(q):
    x,y=q
    if a:
     rx=x%abs(a);k=(x-rx)//a;return rx,y-k*b
    ry=y%abs(b);k=(y-ry)//b;return x-k*a,ry
   if len({key(q) for q in pts[:-1]})!=ell:continue
   assert (a+b)%2==0 and ell>=2*max(abs(a),abs(b))
   for coord,d in ((0,a),(1,b)):
    sums=collections.Counter()
    for x,y in pts[:-1]:
     r=(x,y)[coord];r=r%abs(d) if d else r;sums[r]+=(-1)**(x+y)
    assert all(v==0 for v in sums.values())
   count+=1
 controls.append(dict(length=ell,simple_full_drift_geometric_circuits=count))
# Four remaining odd classes, all x/y signed residue obligations mod2.
matrices=[]
for bins in itertools.product(range(5),repeat=4):
 if sum(bins)!=4:continue
 n00,n01,n10,n11=bins
 if all(z%4==2 for z in (n00-n01,n11-n10,n00-n10,n11-n01)):
  matrices.append([list(bins[:2]),list(bins[2:])])
assert matrices==[[[0,2],[2,0]],[[2,0],[0,2]]]
allowed=[]
for a,b in itertools.product(range(-4,5),repeat=2):
 if (a,b)==(0,0)or(a+b)%2:continue
 if abs(a)+abs(b)<4:continue # signed unit-axis/unit-diagonal exclusions
 for ell in (4,6,8):
  if ell>=2*max(abs(a),abs(b)) and ell+2*max(abs(a),abs(b))<=8:
   allowed.append([a,b,ell])
assert allowed==[[-2,-2,4],[-2,2,4],[2,-2,4],[2,2,4]]
out={'status':'PASS conditional extremal-cycle residue charge and growth-eight restriction','author_note':sha(note),'dependencies':{'single_use_report':sha(S.with_name('check_extremal_single_use_independent.json')),'signed_residue_source':sha(res),'minimal_full_drift':sha(drift)},'geometric_controls_not_ant_fronts':controls,'four_class_parity_matrices':matrices,'g8_remaining_cycle_drift_length':allowed,'analytic_review':[
'Every E-cycle vertex has perpendicular incoming/outgoing cycle axes. Thus the actual vertical cycle edges, including quotient seams, match each vertex exactly once; horizontal edges do likewise. Full-drift checker parity is invariant because a+b is even. Every vertical endpoint pair has equal x residue and opposite checker sign, including a=0 where its actual x coordinate is preserved. Horizontal pairs give the y statement. The sums vanish EXACTLY, not merely modulo4.',
'The signed full-front residue law applies via the previously signed finite-future-read overlap reproduction bridge. Subtracting the cycle vertex set preserves each nonzero-coordinate 2 mod4 obligation. Each such residue needs at least two residual odd classes, so |O minus cycle|>=2 max(|a|,|b|). The residual set need not itself be a physical wake; no physical-wake exclusion is applied to it.',
'The signed embedded winding-minus-one E-circle has ell/2 horizontal and ell/2 vertical edges and full displacement -d, hence ell>=2D. Disjoint residual odd classes give g>=ell+2D>=4D, an actual output partition rather than adding overlapping time bounds.',
'At g8, signed minimum full Manhattan drift4 excludes unit diagonal and length2 axes, giving D>=2. The only D<=2 vectors left are the four signed diagonals(2,2). Consequently ell4 and residual size4. Four-bin enumeration verifies only diagonal or off-diagonal population2, checker-pure residual but checker-mixed full wake.',
'At most one cycle is already signed, not newly required. E may be empty or acyclic for any remaining drift. No missing width10 exhaustion, unrestricted g>=12 theorem, autonomous-controller classification, or capture statement is used or obtained.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'controls':controls,'matrices':matrices,'allowed':allowed},indent=2))
