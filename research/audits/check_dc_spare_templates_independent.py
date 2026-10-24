"""Independent raw-read masks and exhaustive fixed-cohort helper classification."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
Fs=[ROOT/'core_periodicity_new'/s for s in('dc_spare_templates_frozen_20261023_0937','dc_V_repair_frozen_20261023_0940')]
for F in Fs:
 M=json.loads((F/'manifest.json').read_text())
 for f in M['files']:
  name=f.get('frozen',f.get('file'));assert hashlib.sha256((F/name).read_bytes()).hexdigest()==f['sha256']
K={q for q,b in walk(mark)[2].items()if b};G={}
for a in(0,1,4,5,6,7,8,9):
 e,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];B={q for q,b in req.items()if b};post={e+rotation(q,h)for q in K};G[a]=dict(req=req,I=B-K,O=(B^flip)-post,e=e,h=h,flip=flip,post=post)
A=2+0j;orig=G[1]['O'];assert orig=={2+0j,2+3j,3+1j,3+2j}
def enum(live,anchors):
 cand=set()
 for a,g in G.items():
  for h in range(4):
   for q in anchors:
    for z in g['I']:
     p=q-rotation(z,h)
     if(sum(xy(p))+h)%2==0:cand.add((a,*xy(p),h))
 records={}
 for a,x,y,h in cand:
  p=complex(x,y);g=G[a];I={p+rotation(z,h)for z in g['I']};ctx={p+rotation(z,h)for z in g['req']};outside=I-(live-{A});blocked=(live-I)&ctx
  records[a,x,y,h]=dict(inputs=sorted(map(xy,I)),outside_inputs=sorted(map(xy,outside)),blocking_current_noninputs=sorted(map(xy,blocked)),result='INPUT_OUTSIDE_ALLOWED'if outside else'CURRENT_NONINPUT_IN_CONTEXT'if blocked else'ACCEPT')
 return records
def advance(live,a,p,h):
 g=G[a];I={p+rotation(z,h)for z in g['I']};O={p+rotation(z,h)for z in g['O']};core={p+rotation(z,h)for z in K};post={p+rotation(z,h)for z in g['post']}
 assert I<=live and A not in I and not core&live
 board=live|core
 for z,b in g['req'].items():assert((p+rotation(z,h))in board)==b
 out=(live-I)|O;assert not O&(live-I)and not out&post
 assert(board^{p+rotation(z,h)for z in g['flip']})==out|post
 return out
J=json.loads((Fs[0]/'dc_spare_only_helper_templates.json').read_text());rows=enum(orig,orig-{A});assert len(rows)==111
for q in J['initial_original_spare_only_candidates']:
 key=(q['packet'],*q['pose']);actual=rows.pop(key)
 for k,v in actual.items():assert json.loads(json.dumps(v))==q[k]
assert not rows
R=advance(orig,4,3+5j,2);assert len(R)==8
rows=enum(R,{3+1j});assert len(rows)==46 and all(q['result']!='ACCEPT'for q in rows.values())
for q in J['remaining_original_C_candidates_without_import_or_retirement']:
 actual=rows.pop((q['packet'],*q['pose']))
 for k,v in actual.items():assert json.loads(json.dumps(v))==q[k]
assert not rows
for p,h,anchors,expected in[(2+4j,2,{3+1j,3+2j},(0,3,3,2)),(3+3j,2,{3+1j},(0,4,1,3))]:
 orig=advance(orig,0,p,h);r=enum(orig,anchors);assert[key for key,q in r.items()if q['result']=='ACCEPT']==[expected]
# Preserve every replacement and both core boundaries in the positive repair.
R=G[1]['O'];exits=[]
for a,p,h in[(4,3+5j,2),(0,3+3j,0),(0,4+1j,3)]:
 R=advance(R,a,p,h);g=G[a];exits.append((p+rotation(g['e'],h),(h+g['h'])%4))
assert exits[1]==(4+4j,0);assert(4+1j)-exits[1][0]==-3j
# An intervening exactly-one-C word splits into N zero-C run, one C-bearing
# packet, then W zero-C run. Every component has nonnegative y displacement.
for h in(0,3):assert all(rotation(G[a]['e'],h).imag>=0 for a in(0,4,7))
assert all(G[a]['e'].imag>0 and G[a]['h']==3 for a in(1,5,8))
out=dict(status='PASS complete independent cohort templates and positive FREE-HEAD repair',first_candidates=111,post_V_candidates=46,first_helpers=[[0,2,4,2],[4,3,5,2]],post_V_original_C_consumers=0,repair_final_residuals=sorted(map(xy,R)),repair_D_gap_C_lower_bound=5,manifest_sha256=[hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest()for F in Fs],scope='Necessary fixed-cohort alternatives and a nonphysical local repair. No imported initial roots, actual helper path, unrestricted renewal exclusion or capture follows.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
