from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
s=(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text();exec(s.split('geometries=[]')[0]);SELF=Path(__file__).resolve()
a=json.loads((D/'first_foreign_all_source_join.json').read_text());prefix=json.loads((D/'foreign_first_contact_interface.json').read_text());tail=json.loads((D/'foreign_tail_first_contact.json').read_text())
records=[]
for i,g in enumerate(prefix['rows']):
 for f in 'FQB':
  for age,bit in zip(g['permitted_C_ages'],g['preceding_C_bits']):records.append(('F_prefix',f,g['source_atom'],i,tuple(g['foreign_pose']),age,bit))
for f,gs in tail['rows'].items():
 for i,g in enumerate(gs):
  for age,bit in zip(g['permitted_C_ages'],g['preceding_C_bits']):records.append((f+'_tail',f,g['source_atom'],i,tuple(g['foreign_pose']),age,bit))
assert len(records)==len(set(records))==375
ref={(r['piece'],r['foreign'],r['source'],r['geometry_id'],tuple(r['foreign_pose']),r['C_age'],r['previous_C']):r['exclusion_dependency']for r in a['cases']};assert set(records)==set(ref)
count=Counter()
for row in records:
 piece,f,source,i,pose,n,bit=row
 reason='complete8_foreign_adjacency'if bit else 'first_foreign_U_source_exclusion'if source=='U'else 'first_foreign_C_source_exclusion'if source=='C'else 'DV_foreign_prefix_guard'if piece=='F_prefix'else 'DV_foreign_tail_guard'
 assert ref[row]==reason;count[reason]+=1
assert dict(count)==a['disjoint_exclusion_counts'];assert sorted(count.values())==[25,29,60,72,189]
assert Counter(r[2]for r in records)=={'D':56,'C':53,'V':122,'U':144}
# Reconstruct all actual vertices at raw endpoints and the real F56 cut.
pts={};internal={};joins={}
for f in 'FQB':
 t=walk(W[f]);cut=walk(W[f][:56]);assert t['feasible']and cut['feasible'];assert W[f][:56]==W['F']
 ps=[(-1,-1),xy(center(cut['p'],cut['h']))]
 if f!='F':ps.append(xy(center(t['p'],t['h'])))
 assert ps==[tuple(x)for x in [a['foreign_pieces'][f][0][0]]+[p[1]for p in a['foreign_pieces'][f]]]
 for u,v in zip(ps,ps[1:]):assert u!=v
 if len(ps)==3:
  internal[f]=cross(minus(ps[1],ps[0]),minus(ps[2],ps[1]));assert meet(ps[0],ps[1],ps[1],ps[2])[:2]==(F(1),F(0))
 pts[f]=ps
for old in 'VU':
 t=walk(W[old]);assert t['h']==0
 v=minus(xy(center(t['p'],t['h'])),(-1,-1));joins[old]=cross(v,minus(pts['F'][1],pts['F'][0]));assert joins[old]!=0
assert internal=={'Q':24,'B':40}and joins=={'V':32,'U':48}
for path,h in a['dependency_manifests'].items():
 p=R/path;assert hashlib.sha256(p.read_bytes()).hexdigest()==h;m=json.loads(p.read_text());fs=m['files'];items=fs.items()if isinstance(fs,dict)else((r.get('frozen',r.get('path')),r['sha256'])for r in fs)
 for f,v in items:assert hashlib.sha256((p.parent/f).read_bytes()).hexdigest()==v
for path,h in a['independent_dependency_reports'].items():
 p=R/path;assert hashlib.sha256(p.read_bytes()).hexdigest()==h;assert json.loads(p.read_text())['status'].startswith('PASS')
man=D/'first_foreign_all_source_join_manifest.json';sha=hashlib.sha256(man.read_bytes()).hexdigest();assert sha=='89e23b42f325e0af556a0488ec6699d99311487424930730cd228408ba515662'
for f,h in json.loads(man.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS one-first-foreign U-entry proxy simplicity','manifest_sha256':sha,'clock_labels':375,'source_counts':dict(Counter(r[2]for r in records)),'exclusion_counts':dict(count),'literal_foreign_vertices':pts,'internal_determinants':internal,'old_terminal_join_determinants':joins,'analytic':['The old finite U-entry atomic path is injective. The appended foreign is itself injective by its noncollinear literal pieces. Its initial point is the old terminal point and cannot be revisited by the new proxy.','Plain V/U are the only actual preceding full packets, with no C tail. The old/new adjacent pieces are noncollinear, hence share only their true endpoint. All other old segments have positive distance from this endpoint because the old path is finite and simple. Thus any nonadjacent contact has an earliest strictly positive new parameter.','Every old internal vertex has a unique outgoing old segment, including the factor entry. Using source parameter [0,1) neither drops that vertex nor falsely includes the old terminal point. A new F-prefix endpoint belongs to the prefix catalogue. A first contact in the open tail has no prior prefix contact except actual initial adjacency; the signed tail catalogue retains collinear onset and legal initial-adjacency endpoint conventions.','At this chronological first contact the intervening old simple arc plus new contact-free arc has precisely the signed catalogue Jordan premise. It does not require that the whole extended proxy was already simple, and no eight-language lifetime is imported across the foreign.','All 375 necessary labels are removed by five separately signed source/adjacency classes. Therefore the one extended finite proxy is injective apart from consecutive endpoints.'],'scope':'One actual first complete F/Q/B after a finite actual U-entry complete-eight factor only. No returned-eight or second-foreign simplicity, generic mixed-graph coverage, eventual entry, termination or universal capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(count)
