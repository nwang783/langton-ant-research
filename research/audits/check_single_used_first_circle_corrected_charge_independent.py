from pathlib import Path
import json,hashlib,itertools
P=Path(__file__);R=P.parent.parent;D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind=D/'SINGLE_USED_FIRST_CIRCLE_CHARGE_SHA256SUMS';deps={}
for line in bind.read_text().splitlines():
 h,f=line.split(None,1);assert sha(D/f)==h;deps[f]=h
assert deps['SINGLE_USED_FIRST_CIRCLE_CORRECTED_CHARGE.md']=='7774dde0ca943ac9ff63b1125f4c8efaa5afc337ef71ea840281db3621e910e9'
f=lambda n:min(n%4,(-n)%4)
assert [f(i)for i in range(4)]==[0,1,2,1]and all(abs(f(i+1)-f(i))<=1 for i in range(4))
checks=0
for a in range(1,5):
 for k in range(6):
  for choices in itertools.product([(i,s)for i in range(a)for s in(-1,1)],repeat=k):
   q=[0]*a
   for i,s in choices:q[i]+=s
   phi=sum(f(2+x)for x in q);assert phi>=2*a-k;checks+=1
lengths=[ell for ell in range(2,17,2)if ell>=6 and ell//2%2==1];assert lengths==[6,10,14]
out={'status':'PASS conditional all-cap full-fibre corrected charge for genuinely single-used first-R circle','bindings_sha256':sha(bind),'dependencies':deps,'algebra_controls':checks,'drift31_growth8_possible_lengths':lengths,'analytic_review':['Hypothesis is a genuinely physical single-used first-R circle in a complete WHITE front. Signed29cce supplies embedded essential winding-1 and the exact singleton RIGHT / triple-or-quadruple LEFT inventory. The existence of such a circle is NOT proved for arbitrary drift/front or arbitrary first-R cycle.','Each vertex has one vertical and one horizontal cycle edge, giving separate perfect matchings of all circle classes. Checker sign is well-defined because full drift preserves parity. Vertical pairs cancel signed x-fibre totals; horizontal pairs cancel y-fibres. This remains true across a quotient seam because the full coordinate residue is unchanged and checker signs flip across the actual unit edge. Zero drift coordinates have no modular obligation and are assigned Phi0.','Removing k even quadruple classes leaves circle odd sum minus q in every fibre. Full-front odd signed sum2mod4 therefore demands residual sum2+q, with min absolute representative f. The outside odd subset need not be physically realizable or independently balanced. Each residual class contributes one unit in its one fibre, so its cardinality is separately at leastPhi_x andPhi_y, hence maximum rather than sum.','The f distance-to4Z is1-Lipschitz; k signed quadruple contributions lower baseline2|a| by at mostk. Thus g>=ell-k+maxPhi>=ell+2D-2k for both drift signs and zero-coordinate cases. No overlap with event-time or other output reservations is added.','For a simple embedded essential rectilinear loop in the flat translation cylinder, disjoint parallel straight core and an annulus cut give total turning0. Equivalently its tangent rotation number is the essential straight class. Since all corners are90degrees, RIGHT=LEFT=ell/2. Hence k=ell/2-tau and g>=2D+2tau. Distinct singleton RIGHT classes implyell<=2g.','At full drift3,1, ell/2 horizontal and ell/2 vertical unit steps have odd counts, ell>=2D=6 and ell<=16 atg8, giving6,10,14; tau<=1. These are necessary conditional restrictions only. Full-diagonalg8 circle forcing is a separately signed premise, not extended to3,1.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
