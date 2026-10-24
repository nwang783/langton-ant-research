"""Literal complete-context placements plus already signed exact counted clauses."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/u_age_four_pair_frozen_20261023_1056';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_u_age_four_pair_cohort.json').read_text())
for path,digest in J['dependencies'].items():assert hashlib.sha256((ROOT/'core_periodicity_new'/path).read_bytes()).hexdigest()==digest
ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)};K={z for z,b in walk(mark)[2].items()if b};G={}
for b in ids:
    e,h,_,flip=walk(raws[b]);req=walk(raws[b]+mark)[2];black={z for z,c in req.items()if c}
    G[b]=(sorted((black^flip)-{e+rotation(z,h)for z in K},key=xy),set(req),e,h)
closure=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
forbidden={tuple(map(int,line.split()[:8]))for line in closure.read_text().splitlines()}
a=-1+1j;q=-1+2j;upper={-1+4j,2j,3j}
def candidates(cell,h,protected,target,age):
    out=[]
    for b in ids:
        O,context,e,dh=G[b]
        for oi,o in enumerate(O):
            head=cell-rotation(o,h)
            if (sum(xy(head))+h)%2:continue
            if any(head+rotation(z,h)in protected for z in context):continue
            physical=[head+rotation(z,h)for z in O];rel=o-rotation(cell,-h)
            query=(mp[b],mp[target],*xy(rel),(-h)%4,*xy(o),age)
            out.append({'packet':b,'head':[*xy(head),h],'output_slot':oi,'output_cell':list(xy(cell)),
                        'other_lower_is_output':a in physical,'a_output_slot':physical.index(a)if a in physical else None,
                        'counted':{'tuple':list(query),'excluded':query in forbidden}})
    return out
survivors={};checked=0
for case in J['cases']:
    target=case['consumer']
    for e in case['distinct_birth_options']:
        got=candidates(a,e['a_heading'],upper|{q},target,e['a_age'])
        assert got==e['producer_placements']and all(z['counted']['excluded']for z in got);checked+=len(got)
    got=candidates(q,0,upper,target,4);expected=case['q_geometry_placements']
    # Author adds a separate lower-a query only to survivors.
    assert got==[{k:v for k,v in z.items()if k!='a_counted'}for z in expected]
    keep=[]
    for z in got:
        if z['counted']['excluded']:continue
        assert z['other_lower_is_output'];b=z['packet'];o=G[b][0][z['a_output_slot']];rel=o-a
        query=(mp[b],mp[target],*xy(rel),0,*xy(o),4);assert query not in forbidden
        keep.append(z)
    assert len(keep)=={7:8,8:6,9:0}[target];survivors[target]=keep
model=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json').read_text())
potential=Path(model['potential_file']);assert hashlib.sha256(potential.read_bytes()).hexdigest()==model['potential_sha256']
weights=json.loads(potential.read_text())['values']
A=(0,22,20,10);height=lambda z:int(z.imag-z.real);record=[]
for z in survivors[7]:
    b=z['packet'];p=complex(*z['head'][:2]);O,_,e,h=G[b]
    value=max(2*height(p+e)+A[(h+1)%4],*(2*height(p+o)+weights[f'w_{b}_{i}_1']for i,o in enumerate(O)))
    record.append({'packet':b,'head':z['head'],'created_peak':value,'excluded_by_strict_record':value>=30})
assert record==J['U1_strict_record_filter']
out={'status':'PASS independent literal placements, signed count queries and strict-record arithmetic',
     'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),
     'distinct_birth_excluded_queries':checked,'same_birth_survivors':{k:len(v)for k,v in survivors.items()},
     'U1_record_sources':record,'scope':'Produced lower-q age4 forces same lower-a producer/age; surviving templates are necessary only, not attained. U1 remains open.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
