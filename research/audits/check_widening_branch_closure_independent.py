from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
S=SELF.with_name('check_changed_endpoint_catalog_independent.py');n={'__file__':str(S)}
exec(compile(S.read_text().split('results=[];nchecks=')[0],str(S),'exec'),n)
rows,C=n['make_changed']((34,1));P=set(rows);assert len(P)==48
r=next(v for v in n['capsup'][(34,1)]['results'] if v['channel']==[50,0]);assert r['drift']==[2,2]
rr,p,h,_,_=n['incoming'](rows,C,(50,0));F=set(C)
p,h,_,trace=n['replay'](rr,F,p,h,r['entry']);assert [list(n['xy'](p)),h]==r['pose']
ok,tests=n['certify'](rr,F,p,h,r['tail_word']);assert ok
rs={cl:set(v)for cl,v in rr.items()};pp=p;hh=h
for c in r['tail_word']:
 cl,k=n['old'](pp);rs.setdefault(cl,set()).symmetric_difference_update({k})
 hh=(hh+(1 if c=='R'else-1))%4;pp+=n['dirs'][hh]
assert pp-p==2+2j and hh==h
settled={cl for cl,v in rs.items()if len(v)%2};assert len(settled)==72
required={(t+66,(a+1)%2)for t,a in n['rclasses']};assert len(required)==22
hits=required&settled;oldhits=required&n['pclasses'];expected={(42,0),(42,1),(43,1),(44,1),(46,0),(47,0),(48,1)}
assert hits==oldhits==expected
note=ROOT/'new_constructive_2026-10-23/widening_branch_translation_closure.md'
assert hashlib.sha256(note.read_bytes()).hexdigest()=='5e22021a5b21d424afe6ff79578b5af83ba2ed7e850811429c15d0820a75ecd8'
out=dict(status='PASS independent exact translated-channel obstruction',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),second_reaction_steps=len(trace),tail_critical_checks=tests,settled_classes=len(settled),required_classes=len(required),original_black_hits=sorted(hits),scope='Only dictated clean incoming channel66,1 after34,1 then50,0; longitudinal shifts and finite caps cannot change these infinite orbit conflicts. No arbitrary widening, unclean-entry, finite itinerary or capture exclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
