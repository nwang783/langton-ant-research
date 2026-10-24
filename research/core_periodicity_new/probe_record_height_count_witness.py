"""Exact height-count necessary-condition replay for an existing geometric witness.
No claim about absence of other words. Initial high residual counts are zero.
"""
from pathlib import Path
import json,sys,collections
src,txt,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];F=J['initial_bound'];phase=J['phase'];lines=txt.read_text().splitlines();w=list(map(int,next(s for s in lines if s.startswith('word ')).split()[1:]));states=[list(map(int,s.split())) for s in lines if s and s[0] in '-0123456789'];assert len(states)==len(w)
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
C=collections.Counter();first=None;rows=[]
for i,(a,st) in enumerate(zip(w,states)):
 h,q=st[:2];assert q>J['lower_cutoff'],'This replay needs an exact height rather than a low bin.'
 inp=collections.Counter(q+ht(rot(p,h)) for p in G[a]['inputs'] if q+ht(rot(p,h))>F)
 output=collections.Counter(q+ht(rot(p,h)) for p in G[a]['outputs'] if q+ht(rot(p,h))>F)
 deficit={k:v-C[k]for k,v in inp.items()if v>C[k]}
 if deficit and first is None:first=i
 rows.append(dict(index=i,packet=a,heading=h,height=q,counts_before=dict(C),inputs=dict(inp),outputs=dict(output),deficit=deficit))
 C.subtract(inp);C.update(output)
R={'format':'record_height_count_witness_diagnostic_v1','source':str(src.resolve()),'witness':str(txt.resolve()),'initial_height_bound':F,'first_deficit_packet':first,'rows':rows,'scope':'Exact necessary height-resource replay for this one path; negative counts refute only that abstract path.'};out.write_text(json.dumps(R,indent=2)+'\n');print(json.dumps({'first_deficit_packet':first,'first_deficit':rows[first]if first is not None else None,'final_counts':dict(C)},indent=2))
