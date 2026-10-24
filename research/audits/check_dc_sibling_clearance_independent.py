"""Literal core/residual partition, simultaneous sibling and spine controls.
Does not import any author's geometric or control implementation.
"""
from pathlib import Path
import sys,json,hashlib
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
K={p for p,b in walk(mark)[2].items()if b}
end,h,_,fl=walk(raws[1]);req=walk(raws[1]+mark)[2];entry={p for p,b in req.items()if b};I=entry-K;O=(entry^fl)-{end+rotation(p,h)for p in K}
assert I=={1j} and O=={2+0j,2+3j,3+1j,3+2j}
G={a:(walk(raws[a]+mark)[2],walk(raws[a]))for a in(0,1,4,5,6,7,8,9)}
assert max(len({p for p,b in r.items()if b}-K)for r,w in G.values())==5
J=json.loads((ROOT/'cut_order_obstruction_2026-10-23/mass_sensitive/dc_sibling_clearance.json').read_text());records=[]
for q in sorted(O,key=xy):
 for h in range(4):
  p=q-rotation(1j,h)
  if(sum(xy(p))+h)%2:continue
  core={p+rotation(z,h)for z in K};requirements={p+rotation(z,h):b for z,b in req.items()};inputs={p+rotation(z,h)for z in I};others=O-{q}
  core_retire=others&core;white={z for z in others if z in requirements and not requirements[z]};coin=others&inputs;outside=others-set(requirements)
  assert core_retire|white|coin|outside==others
  row=dict(source_cell=list(xy(q)),target_heading=h,target_head=list(xy(p)),core_retire=sorted(map(list,map(xy,core_retire))),white_retire=sorted(map(list,map(xy,white))),coinputs=sorted(map(list,map(xy,coin))),outside_context=sorted(map(list,map(xy,outside))),must_retire=sorted(map(list,map(xy,core_retire|white))))
  old=next(r for r in J['records']if r['source_cell']==list(xy(q))and r['target_heading']==h)
  assert all(row[k]==old[k]for k in row),(row,old);records.append(row)
assert len(records)==8
# Exact period-four zero-local-clearance spine, with every ordered spare kept.
poses=[(0j,0)]
for k in range(4):
 p,h=poses[-1];hh=(h+1)%4;pp=p+rotation(2,h)-rotation(1j,hh);poses.append((pp,hh))
assert poses==[(0j,0),(1+0j,1),(1-1j,2),(-1j,3),(0j,0)]
spares=O-{2+0j};slots=set()
for p,h in poses[:4]:slots|={p+rotation(z,h)for z in spares}
assert len(slots)==12
for pp,hh in poses[1:4]:assert spares.isdisjoint({pp+rotation(z,hh)for z in req})
assert all(z in req and not req[z]for z in spares)
cp=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';op=ROOT/'core_periodicity_new/chronology_dcuv/recurrent8_counted/closure.tsv'
assert hashlib.sha256(cp.read_bytes()).hexdigest()=='f68f23f8189dc750489ed3aabd48741fde629d1263503ac9cff94fb703163f58'
assert hashlib.sha256(op.read_bytes()).hexdigest()=='e8ad57fc2f640f31e4ab0493440089418248dc03f8575dbb71b2d85bf4dcc4e4'
query=(1,1,1,0,1,2,0,3)
for p in(cp,op):assert query in{tuple(map(int,l.split()[:8]))for l in p.read_text().splitlines()}
# Eight-comb relaxation: independently iterate fresh IDs, not physical colors.
F=ROOT/'core_periodicity_new/dc_eight_comb_frozen_20261023_0919';M=json.loads((F/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((F/f['file']).read_bytes()).hexdigest()==f['sha256']
roots=[rotation(complex(100,100+(1-(-r)%4)%2+10*(r//4)),(-r)%4)for r in range(8)]
active={p:(None,r)for r,p in enumerate(roots)};lastposes=[]
for t in range(5000):
 r=t%8;j=t//8;h=(-r)%4;parent=roots[r]+rotation(j*(3+1j),h);born,owner=active.pop(parent);assert owner==r and(born is None or t-born==8)
 p=parent-rotation(1j,h);assert(sum(xy(p))+h)%2==0 and h==(-t)%4
 for z in O:
  cell=p+rotation(z,h);assert cell not in active;active[cell]=(t,r)
 assert len(active)==8+3*(t+1)
 lastposes.append((p,h))
assert lastposes[1][0]!=lastposes[0][0]+rotation(end,lastposes[0][1])
# The fixed same-heading repeat embeds exactly two spares in the next old core.
shift=3+1j;blocked={z for z in O-{3+2j}if z-shift in K};assert blocked=={2+0j,3+1j}
# The marginal role has not been excluded; no feasibility is inferred.
import check_genealogy_saturation_roles_independent as RG
for h in range(4):
 u=RG.index[1,3+2j,h];assert(u,u,8,int(rotation(3+1j,h).imag))in RG.fundamental
RF=ROOT/'core_periodicity_new/dc_rotating_spine_clearance_frozen_20261023_0924';RM=json.loads((RF/'manifest.json').read_text())
for f in RM['files']:assert hashlib.sha256((RF/f['frozen']).read_bytes()).hexdigest()==f['sha256']
out=dict(status='PASS literal sibling partition, period-four clearance and explicitly nonphysical comb control',self_transfer_rows=records,rotating_spine_poses=[[*xy(p),h]for p,h in poses],age3_query=list(query),minimum_rotating_gap=7,spare_slots=len(slots),comb_events=5000,comb_old_core_blockers=sorted(map(xy,blocked)),frozen_rotating_bundle_sha256=hashlib.sha256((RF/'manifest.json').read_bytes()).hexdigest(),frozen_comb_bundle_sha256=hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),scope='Ordered residual retirement is not physical black deletion. All-N support counts follow from distinct birth IDs; no fresh fuel, physical realization, no-support theorem or capture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
