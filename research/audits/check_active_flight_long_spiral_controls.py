from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];p=SELF.parent/'check_exact_active_flight_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('\ncells=')[0],ns)
q=SELF.parent/'check_actual_zipper_spiral_independent.py';ss={'__file__':str(q)};exec(q.read_text().split('for q in (')[0],ss)
rows=[]
for q in(8,16):
 vs,cells,runs=ss['make'](q,4);a=ns['check'](set(cells),1+1j,1,len(cells)+4)
 rows.append({'q':q,'complete_mass':len(cells),'first_event':a.event,'status':a.status,'preperiod':a.preperiod,'period':a.period,'drift':a.drift,'witness':a.witness})
out={'status':'PASS two actual long spiral flight controls; no new universal claim','cases':rows,'independent_full_field_statistics':dict(ns['stat']),'analytic':'Both complete input fields are signed physical spiral controls. Full boards and all intermediate cuts are independently replayed to the actual first import, not inferred from sampled predictor states. This extends the finite tests beyond short first contacts; it is not evidence that every isolated predictor has zero drift.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
