from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();F=D/'SHIFTED_WAKE_CONTACT_INVENTORY_MANIFEST.json';assert sha(F)=='31eedb7f709071137b9fcb621e6407a08983ba1c05891f587aee3705be5f3bfd';M=json.loads(F.read_text())
for f,h in M['files'].items():assert sha(D/f)==h
J=json.loads((D/'SHIFTED_WAKE_CONTACT_INVENTORY_CHECKED.json').read_text());G={-1j,1+1j,1+3j,2+2j};B=set(G);p=0j;h=1;V=[1j,1,-1j,-1];trace=[];word=''
for t in range(286):
 trace.append(p);c='L'if p in B else'R';word+=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
Q=trace[182:];U=word[182:];delta=2+2j;xy=lambda q:[int(q.real),int(q.imag)];ray=lambda z:int(z.real)//2 if z.real==z.imag and z.real%2==0 else None
perms=[]
for phase,q in enumerate(Q):
 if U[phase]!='R':continue
 hits=[104*m+i for i,z in enumerate(Q)if(m:=ray(q-z))is not None and m>=0]
 if max(hits)==phase:perms.append((phase,q))
assert len(perms)==12
rows=[]
for phase,q in perms:
 aligns=[]
 for i,z in enumerate(Q):
  m=ray(q-z+8)
  if m is not None:assert m>=3;aligns.append(dict(copy_offset=m,phase=i,time_constant=104*m+i-14,turn=U[i]))
 first=min(aligns,key=lambda z:z['time_constant'])if aligns else None
 rows.append(dict(outgoing_phase=phase,outgoing_cell=xy(q),return_alignments=aligns,first=first))
assert rows==J['rows'];Fnd={tuple(z['outgoing_cell']):z['first']['time_constant']for z in rows if z['first']};assert Fnd=={(5,8):311,(6,8):312,(6,7):313,(6,9):325}
assert all(z['first']['turn']=='R'and sum(z['outgoing_cell'])>=13 for z in rows if z['first'])
for c in Fnd.values():assert 2<=c//104<=3
for z in J['parameter_tests']:
 K=z['K'];counts={str(q):max(0,(104*K-c+103)//104)for q,c in Fnd.items()};assert sum(counts.values())==4*K-11==z['periodic_output_contacts_before_nominal_marker']
out=dict(status='PASS exact prescribed nominal-strand clearing inventory ONLY',manifest=sha(F),proof=M['files']['SHIFTED_RETURN_WAKE_CLEARING_OBLIGATION.md'],fresh_actual_permanent_output_classes=len(perms),ray_alignment_pairs=12*104,first_contact_offsets={str(k):v for k,v in Fnd.items()},formula='4K-11 forK>=3 before destination',analytic_review=[
'Fresh literal G286 computes the actual104 Q and all12 permanent R anchors by complete nonnegative ray equalities. All12x104 return alignments rebuilt. Every match has copy difference>=3, so phase14 truncation creates no omitted early branch.',
'Before offset104K, anchor311 contributesK-2 copies, each312/313/325 contributesK-3. Destination is phase90 copyK-3 at exactly104K, excluded. All copied output indices<=K-3 are actually written by stage0, whose full-period count k+K-4 exceeds them for k>=10.',
'Own-reference last reads and signed shifted-stage complete read-set separation keep these SAME identities black at actual returne. Their sums>=13 exclude entire protected actual recovery. Thus they are ACTUAL permanent outputs, not consumed inputs in the actual continuation.',
'The nominal strand first demands R at R271(5,8),offset311. Any unchanged producing prefix preserves that R-born BLACK bit until an added physical read; clearing only the launch marker cannot legalize this exact word. This does NOT bound contact count for an alternative route, actual consumption, or relevant population.'
],dependencies={'audits/check_shifted_port_module_independent.json':sha(S.parent/'check_shifted_port_module_independent.json'),'audits/check_moving_capacity_independent.json':sha(S.parent/'check_moving_capacity_independent.json')});S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
