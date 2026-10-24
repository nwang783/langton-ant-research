"""All1024 local windows, using the separately written complex-heading walker."""
from check_uv_crossing_independent import *
rows=[];unexcluded=[];ruled_out=0
for a in map(''.join,itertools.product('UV',repeat=5)):
 ta,sa,ea=window(a,False);last={p:(i,l)for i,(p,l)in enumerate(ta)}
 for b in map(''.join,itertools.product('UV',repeat=5)):
  tb,sb,eb=window(b,True);first={}
  for i,(p,l)in enumerate(tb):first.setdefault(p,(i,l))
  witnesses=[p for p in last.keys()&first.keys() if last[p][1]==first[p][1] and sa<p.imag<ea-1 and eb+1<p.imag<sb and p.imag<ea-5]
  rule=(a[2]=='V' and b[1]==b[2]=='V')
  assert rule or witnesses,(a,b)
  if not rule:ruled_out+=1
  if not witnesses:unexcluded.append([a,b])
  else:
   q=min(witnesses,key=lambda p:(p.imag,p.real));rows.append({'north':a,'south':b,'witness':[int(q.real),int(q.imag)],'north_last':last[q],'south_first':first[q]})
assert ruled_out==896 and len(unexcluded)==56 and len(rows)==968
out={'status':'PASS','universal_necessary_rule':'earlier outgoing V, later incoming and outgoing V','ruled_out_violations':ruled_out,'total_shielded_conflicts':len(rows),'not_excluded_by_this_test':unexcluded,'cases':rows}
(R/'audits/uv_shared_center_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 896 rule violations excluded, 968 total witnesses,56 not excluded')
