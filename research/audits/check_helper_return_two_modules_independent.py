from pathlib import Path
from collections import defaultdict
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'kernel_cycle_lift_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ns={'__file__':str(S.with_name('check_cycle_birth_finite_fuel_independent.py'))};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns);ends,wvertex=ns['ends'],ns['wvertex'];V=(1j,1,-1j,-1);cx=lambda q:complex(*q);xy=lambda q:[int(q.real),int(q.imag)]
refs=json.loads((D/'helper_return_connector_or_growth_certificate.json').read_text())['controls'];mr=json.loads((D/'two_module_connector_or_growth_certificate.json').read_text())['controls']
ans=[]
for ref,mod in zip(refs,mr):
 B={cx(q)for q in ref['initial_black']};p=cx(ref['initial_pose'][0]);h=ref['initial_pose'][1];birth={q:None for q in B};G=defaultdict(dict);lat=int(wvertex(p,h).real+wvertex(p,h).imag)%4;d,j=ref['departure'],ref['helper_consumption'];f,e=cx(ref['helper']),cx(ref['parent']);M=0;deaths=[];first=None
 def edit(q,on):
  a,z=ends(q,lat)
  if on:G[a][z]=q;G[z][a]=q
  else:del G[a][z];del G[z][a]
 def comp(v):
  seen={v};todo=[v];edges=set()
  for a in todo:
   for z,q in G[a].items():
    edges.add(q)
    if z not in seen:seen.add(z);todo.append(z)
  return edges
 for q in B:edit(q,True)
 for t in range(j+1):
  C=comp(wvertex(p,h))
  if d-1<=t:M=max(M,len(C))
  if t==d:
   base=set(B);old=set(B);born0=dict(birth);p0=p;c0=set(C);E=comp(ends(e,lat)[0]);F=comp(ends(f,lat)[0]);U=E|F
   assert E.isdisjoint(F)and E.isdisjoint(C)and F.isdisjoint(C)
   assert B=={cx(q)for q in ref['departure_full_black']}and birth=={cx(q):v for q,v in ref['departure_births']}and C=={cx(q)for q in ref['departure_active']}
  if t>=d and first is None:
   assert F==comp(ends(f,lat)[0]) if f not in C else F<=C
   if f in C:
    assert lastR and lastq in C-F and F<=B
    first={'cut':t,'previous_R_cell':xy(lastq),'active_mass':len(C),'complete_active':sorted(map(xy,C))}
  if t==j:
   assert p==f and birth[f]==ref['helper_birth']and birth[e]==ref['parent_birth']and first is not None
   assert B=={cx(q)for q in ref['helper_pre_read_full_black']}and birth=={cx(q):v for q,v in ref['helper_pre_read_births']}and C=={cx(q)for q in ref['helper_pre_read_active']}
   L=int(max(abs(p.real-p0.real),abs(p.imag-p0.imag)));axis=0 if abs(p.real-p0.real)>=abs(p.imag-p0.imag)else 1;coord=lambda q:int(q.real if axis==0 else q.imag);lines=range(min(coord(p),coord(p0))+1,max(coord(p),coord(p0)))
   fresh={q for q in B if birth[q]is not None and birth[q]>=d};K=len(deaths);H=sum(q not in U for _,q,_ in deaths);delta=len(B)-len(base);pd=delta-len(C)+len(c0)
   for r in lines:
    diff={q for q in B^base if coord(q)==r};kr=[q for _,q,_ in deaths if coord(q)==r];fr={q for q in fresh if coord(q)==r};delta_r=sum(coord(q)==r for q in B)-sum(coord(q)==r for q in base)
    charge=sum((1 if q in B else -1)*(-1)**int(q.imag if axis==0 else q.real)for q in diff)
    assert charge%4==2 and len(diff)>=2 and delta_r+2*len(kr)>=2 and len(fr)+len(kr)>=2
   left=set(B);dd=[]
   while left:
    q=next(iter(left));A=comp(ends(q,lat)[0]);left-=A
    if A!=C and A&fresh:dd.append(A)
   bound=(max(0,2*(L-1)-K-M)+M-2)//(M-1)
   assert all(len(A)<=M-1 for A in dd)and len(dd)>=bound
   assert len(E)<=M-1 and len(F)<=M-1 and K-H<=len(U)-2
   assert delta+2*K>=2*(L-1)and pd>=2*(L-1)-2*K-M and delta+2*H>=2*L+2-2*len(U)>=2*L-4*M+6 and pd+2*H>=2*L+2-2*len(U)-M
   checks={'distance':L,'M':M,'old_consumption_count':K,'global_mass_change':delta,'passive_mass_change':pd,'new_fresh_mass':len(fresh),'new_dormant_component_count':len(dd),'new_dormant_component_lower_bound':bound}
   for k,v in checks.items():assert ref[k]==v,(k,v,ref[k])
   assert E=={cx(q)for q in mod['parent_module']}and F=={cx(q)for q in mod['helper_module']};assert first==mod['helper_first_R_import'];assert H==mod['H']and K==mod['K']
   assert {(frozenset(a),frozenset(a&fresh))for a in dd}=={(frozenset(cx(q)for q in a['edges']),frozenset(cx(q)for q in a['fresh']))for a in ref['new_complete_dormant_components']}
   ans.append(dict(checks,departure=d,helper_read=j,parent_module_size=len(E),helper_module_size=len(F),external_old_consumptions=H,first_import=first['cut'],remote=L>4*M));break
  q=p;on=q not in B
  if on:B.add(q);birth[q]=t
  else:
   if d<=t<j and q in old:deaths.append((t,q,born0[q]));old.remove(q)
   B.remove(q);birth.pop(q)
  edit(q,on);h=(h+(1 if on else-1))%4;p+=V[h];lastR=on;lastq=q
out={'status':'PASS return-leg axial charge and two-fixed-module corollary, with fresh named full-board controls','sources':{n:sha(D/n)for n in ['HELPER_RETURN_CONNECTOR_OR_ARCHIVE_GROWTH.md','TWO_FROZEN_MODULES_NEED_EXTERNAL_INPUT_OR_GROWTH.md','helper_return_connector_or_growth_certificate.json','two_module_connector_or_growth_certificate.json']},'controls':ans,'analytic_review':[
'Strict separating lines have signed discrepancy2mod4 by retained axial charge. New-only minus old-only equals total mass change; every old-only cell requires one DISTINCT retired cut-d lifetime. Thus delta+2K>=2(L-1), with K all old retirements allowing losses off the separating lines. Old consumed-and-reborn cells strengthen the inequality, not a loophole.',
'Current fresh born[d,j) cells plus old retired lifetimes cover each discrepancy. After removing active<=M fresh cells, each complete dormant component containing fresh lifetime has a last actual bridge-L departure within[d,j] and at mostM-1 edges, then is literally frozen. This proves the fresh-component ceiling, not a global monotone resource.',
'Two marked modules are the FIXED full cut-d components and FIXED original lifetime sets. Parent component<=M-1 from the covered d-1 bridge departure. Remote helper is outside both active and parent module by metric; before first subsequent activation its complete component is frozen. First R import adds a NEW edge, so even an initial root helper component<=M-1. Distinct surviving marks reduce possible internal retirements by2.',
'K=H+inside, inside<=|E union D|-2 gives delta+2H>=2L+2-2|E union D|>=2L-4M+6. Passive inequality safely subtractsM. Helper cutj is PRE-L, and both marks remain current original lifetimes; including death would need a correction.',
'Blank short range L2 is not a remote theorem example; distinct modules and their bounds are checked separately. Named n400 original20-cell seed is replayed throughhelper20628, full boards/births/fields and all strict lines/components match. Later parent248084 is retained source dependency, not freshly replayed here.',
'No birth-to-d activecap is needed; d-1 needed only for parent module bound. Old means black atd, not older thanhelperbirth. Arbitrary reattachments, new supports and legal rebirths retained. No across-overlapping-leg additivity, finite original fuel, attraction or capture consequence.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(ans)
