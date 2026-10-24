import json,hashlib,itertools
from pathlib import Path
R=Path('/workspace/shared/langton');P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(P/'DRIFT31_EXTREME_READ_SHA256SUMS').read_text().splitlines():h,f=line.split(None,1);assert sha(P/f)==h
J=json.loads((P/'drift31_extreme_read_controls.json').read_text());v=[1j,1,-1j,-1];T=lambda p:int(3*p.imag-p.real);o=lambda h,r:(h+(1 if r%2==0 else-1))%4
# At a true read extremum both the incoming predecessor and next read must stay on its side.
mn=[h for h in range(4)if T(v[h])<=0 and T(v[o(h,0)])>=0];mx=[h for h in range(4)if T(v[h])>=0 and T(v[o(h,0)])<=0];assert mn==[2]and mx==[0]and T(v[o(2,1)])<0 and T(v[o(0,1)])>0
# Exact unlimited-word derivations: all-S output determines EW alternating; one E gives n1/2.
h13=[[(1 if i%2==0 else 3)for i in range(n)]for n in(1,2)]
# All N arrivals and no W output allow only empty or the first R.
h12=[[],[0]]
# All-E output determines NS alternating; two N gives n3/4.
h8=[[(0 if i%2==0 else 2)for i in range(n)]for n in(3,4)]
assert h13==J['top13_complete_choices']and h12==J['top12_complete_choices']and h8==J['all_E_T8_choices']
known={4:[2,2,0,2],5:[1,1,3],6:[0,0,0],7:[1,1,1,3]};points=[-8+0j,-7+0j,-7-1j,-8-1j,-8+0j];roles=[(7,0,0),(4,0,-1),(5,2,-1)]
for i,(t,r,k)in enumerate(roles,1):
 assert points[i]==-t+k*(3+1j);ih=known[t][r];assert points[i]-points[i-1]==v[ih]and points[i+1]-points[i]==v[o(ih,r)]
assert [list(map(int,(p.real,p.imag)))for p in points]==J['physical_four_return']
for hs in h8:assert hs[0]==hs[2]==0 and o(hs[0],0)==1
# Complete residual inventories: extrema depend on ALL reads, not emitted support assumptions.
for c in(2,3):
 ts=[0,1,2,5,6,8,13,6*c+2];assert all(sum((-1)**t for t in ts if(-t)%3==r)%4==2 for r in range(3));assert sum((-1)**t for t in ts)%4==2
 canonical=[((-t)%3,(t+(-t)%3)//3)for t in ts];assert sum(y for r,y in canonical)%2==1
report={'status':'PASS complete-read maximum lemma and conditional two-quadruple s5/all-parameter plus s2,c2 exclusions','proof_sha256':sha(P/'DRIFT31_TWO_QUAD_EXTREME_READ_EXCLUSIONS.md'),'script_sha256':sha(Path(__file__)),'dependencies':{'middle_reads':sha(R/'audits/drift31_middle_reads_independent.json'),'wake_interleaving':sha(R/'audits/drift31_wake_interleaving_independent.json')},'top_histories':{'T14':[0],'T13':h13,'T12':h12,'T9':[],'T8':h8},'physical_rank_skip_points':[[int(p.real),int(p.imag)]for p in points],'analytic_scope':['Full finite READ quotient has a maximum since T is invariant under actual nonzero d(3,1). At that maximum only N/W arrival is possible; horizontal W first R exits above, so maximum is vertical-even and N singleton. A second N/L would again exit above. Therefore max FULL odd inventory equals the complete read maximum, even. Unread external field is irrelevant, not assumed absent.','T0 minimum S singleton fixes vertical-even checker sector. With signed b<a<=c, s5 full odd maximum6c+5 is odd, impossible for every parameter; s2 remains.','For c2 the entire odd set fixes max14. Zero ports and exact alternation force T13 E, T12 empty, T9 empty, T8 NSN orNSNS. The explicit same-physical four-return skips T8 rank1. No unknown sibling or high class is treated empty except via proved max or zero-port/odd-status deductions.','Remaining s2,c>=3,1<=b<a<=c and all-quadruple branch remain OPEN; passing parity sets are not controllers.'],'not_claimed':['unconditional existence of single-used circle','all drift3,1 fronts excluded','growth8 excluded','physical realization of candidate odd sets']}
p=R/'audits/drift31_extreme_read_independent.json';p.write_text(json.dumps(report,indent=2)+'\n');print(sha(p));print(report['status'])
