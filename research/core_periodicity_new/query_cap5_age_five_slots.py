"""Exhaustive author membership queries; independent enumeration is separate."""
from pathlib import Path
import json,hashlib,collections
R=Path(__file__).resolve().parent;D=R/'chronology_dcuv';G=json.loads((D/'literal_residual_geometry.json').read_text())['geometry'];ids=[0,1,4,5,6,7,8,9];mp={a:i for i,a in enumerate(ids)}
P={tuple(map(int,s.split()[:7]))for s in(D/'protected_patch2.tsv').read_text().splitlines()};C={tuple(map(int,s.split()[:8]))for s in(D/'critical_ucc_count5/closure.tsv').read_text().splitlines()}
slots=[(6,(0,3)),(6,(1,2))]+[(b,q)for b in[7,8,9]for q in[(-1,4),(0,2),(0,3)]]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
rows=[];stats=collections.Counter();families=[]
for b,q in slots:
 st=collections.Counter()
 for a in ids:
  for r0 in G[a]['outputs']:
   r=tuple(r0)
   for h in range(4):
    z=rot(q,h);p=(r[0]-z[0],r[1]-z[1]);t=(a,b,*p,h,*r);ct=(mp[a],mp[b],*p,h,*r,4)
    status='heading'if h else'sector'if(sum(p)-h)%2 else'signed_HB'if t in P else'signed_count5'if ct in C else'OPEN'
    assert status!='OPEN',(a,b,p,h,r,q);rows.append({'original_tuple':t,'counted_tuple':ct,'target_input':q,'status':status});stats[status]+=1;st[status]+=1
 families.append({'target_original':b,'target_name':G[b]['name'],'target_input':q,'new_minimum_produced_C_age':5,'prior_signed_minimum':4,'query_status_counts':dict(st)})
Q=D/'critical_ucc_count5/age_five_queries';Q.mkdir(exist_ok=True)
inputs=[D/'literal_residual_geometry.json',D/'counted_input_age_rules_complete.json',D/'protected_patch2.tsv',D/'critical_ucc_count5/closure.tsv',D/'critical_ucc_count5/frozen_20261023_0813/manifest.json',Path(__file__).resolve()]
J={'status':'ALL_EXACT_AGE4_ALIGNMENTS_EXCLUDED_AUTHOR_QUERY','scope':'Combined with signed JO age>=4, produced identities at these11 inputs have age>=5. Initial identities are exempt. No all-count freshness or record closure.','mapping_new_to_original':ids,'rows':rows,'families':families,'status_counts':dict(stats),'input_hashes':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in inputs}}
(Q/'queries.json').write_text(json.dumps(J,indent=2)+'\n');(Q/'queries.tsv').write_text(''.join(' '.join(map(str,r['counted_tuple']))+'\n'for r in rows if r['status']=='signed_count5'))
M={p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in Q.iterdir()if p.is_file()};(Q/'manifest.json').write_text(json.dumps(M,indent=2)+'\n');print({'slots':len(slots),'queries':len(rows),'status_counts':dict(stats)})
