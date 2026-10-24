"""Exact port geometry for twelve supplied cap6 return words; no profile scan.
Grammar coverage is separate. Final black cells follow from their last R read.
"""
from pathlib import Path
import sys,json
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import DIR,cursor,ends,vertices,comp
WORDS=['RRRRL','RRRRLL','RRRRLRRL','RRRRLLRL','RRRRLLRRL','RRRRLLLLRL','RRRRLRLRRL','RRRRLRL','RRRRLRLL','RRRRLRRLL','RRRRLRLRL','RRRRLRRLRL']
EXPECTED={'RRRRL':('MASS',3),'RRRRLL':('MASS',3),'RRRRLRRL':('MASS',5),'RRRRLLRL':('MASS',4),'RRRRLLRRL':('MASS',5),'RRRRLLLLRL':('SATURATED_NONFIRST',2),'RRRRLRLRRL':('SATURATED_NONFIRST',2)}
rows=[]
for W in WORDS:
 p=(0,0);h=0;last={};reads=[]
 for t,c in enumerate(W):
  reads.append(dict(slot=t,cell=p,turn=c));last[p]=(c,t)
  h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 F={q for q,(c,t)in last.items()if c=='R'};r=cursor(p,h)
 assert r not in vertices(F,1),'This would rule out an empty final component directly'
 N={(r[0]+a,r[1]+b)for a in(-2,2)for b in(-2,2)};U=set();touches=[]
 for v in sorted(N):
  C=comp(F,1,v);U|=C;touches.append(dict(neighbor=v,mandatory_component_edges=sorted(C)))
 a,b=ends(p,1);assert r in(a,b);u=b if a==r else a
 typ='MASS'if len(U)>=3 else'SATURATED_NONFIRST'if len(U)==2 and u not in vertices(U,1)else'OPEN'
 if W in EXPECTED:assert(typ,len(U))==EXPECTED[W]
 else:assert typ=='OPEN'
 rows.append(dict(word=W,length=len(W),exit_pose=[p,h],empty_w_cursor=r,first_R_other_endpoint=u,mandatory_final_black=sorted(F),last_read_owners=[dict(cell=q,turn=c,slot=t)for q,(c,t)in sorted(last.items())],neighbor_forced_components=touches,mandatory_import_union=sorted(U),mandatory_import_mass=len(U),first_tip_in_mandatory_import=u in vertices(U,1),classification=typ,read_trace=reads))
assert sum(a['classification']!='OPEN'for a in rows)==7
out=dict(status='PASS exact forced-black neighbor-port geometry for twelve supplied words',fixed_w_sector=1,cap=6,old_edge_budget=2,trapped_word_count=7,open_word_count=5,rows=rows,scope='For ANY actual empty-to-empty execution of a listed trapped word, its current mandatory black edges force cap6 failure within9 more updates. This finite coordinate table does not itself prove the12 words exhaust the cap6 kernel; that is a separate grammar dependency.')
(OUT/'empty_cursor_import_budget_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'rows':[{k:a[k]for k in['word','mandatory_import_mass','first_tip_in_mandatory_import','classification']}for a in rows]},indent=2))
