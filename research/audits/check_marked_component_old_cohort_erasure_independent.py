from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'kernel_cycle_lift_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note=D/'PRODUCTIVE_RETURN_REMOTE_HELP_TEST_v2.md';assert sha(note)=='b64ec3398bcdfe34ea458d6df099653817b453ce4367fb22d6159fcc74683f9b'
ns={'__file__':str(S.with_name('check_cycle_birth_finite_fuel_independent.py'))};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns);component,step,wvertex,ends=[ns[k]for k in ['component','step','wvertex','ends']];xy=lambda q:[int(q.real),int(q.imag)];norm=lambda q:max(abs(q.real),abs(q.imag))
# Fixed finite control: an actual blank history plus two never-read far archives.
far={10000+10000j,10001+10000j,-10000-10000j};B=set(far);p=0j;h=0;states=[];birth={q:None for q in B};lifes=[]
for t in range(801):
 C=component(B,0,wvertex(p,h))[1];states.append((set(B),p,h,C))
 if t==800:break
 if p in B:
  if birth[p]is not None:lifes.append((p,birth[p],t))
  del birth[p]
 else:birth[p]=t
 p,h,c=step(B,p,h)
controls=[]
for q,b,c in lifes:
 ds=[t for t in range(b+2,c)if q in states[t-1][3]and q not in states[t][3]]
 if not ds:continue
 d=ds[0];M=max(len(states[t][3])for t in range(d-1,c+1));origin=states[d][1];assert M>=1
 assert norm(q-origin)<=M+1
 for t in range(d,c+1):
  K=component(states[t][0],0,ends(q,0)[0])[1];assert q in K and all(norm(e-origin)<=4*M for e in K)
 removed={e for e in states[d][0]if norm(e-origin)>4*M};assert far<=removed
 assert all(states[t][1]not in removed for t in range(d,c+1))
 B2=states[d][0]-removed;p2=states[d][1];h2=states[d][2]
 for t in range(d,c+1):
  old,pp,hh,C=states[t];assert(p2,h2)==(pp,hh)and B2==old-removed
  C2=component(B2,0,wvertex(p2,h2))[1];K1=component(old,0,ends(q,0)[0])[1];K2=component(B2,0,ends(q,0)[0])[1];assert K1==K2 and len(C2)<=len(C)and(q in C)==(q in C2)
  if t<c:p2,h2,_=step(B2,p2,h2)
 assert p2==q and q in B2
 # Prepend the original actual departing L by restoring its local erased cell.
 qp=states[d-1][1];assert qp in states[d-1][0] and norm(qp-origin)<=1
 Bd=states[d][0]-removed;Bp=Bd|{qp};assert Bp==states[d-1][0]-removed
 pp,hh,ch=step(Bp,states[d-1][1],states[d-1][2]);assert ch=='L'and(pp,hh)==states[d][1:3]and Bp==Bd
 controls.append(dict(mark=xy(q),birth=b,departure=d,death=c,M=M,removed=len(removed),active_dormant_switches=sum((q in states[t][3])!=(q in states[t-1][3])for t in range(d+1,c+1))))
assert controls
out={'status':'PASS only marked-component localization and one-time old-cohort erasure lemma, not RH16/4','author_note':sha(note),'named_author_n400_test_NOT_independently_replayed':True,'own_fixed_control_lifetimes':controls,'signed_dependencies':{f:sha(S.with_name(f+'.json'))for f in ['check_active_w_episodes_independent','check_bounded_active_frozen_excursions_independent','check_last_productive_import_independent']},'analytic_review':[
'At the bridge departure all marked-D edges were in the full active component of size<=M. The signed exact metric puts their midpoints within M of the previous head and M+1 of the new departure head. A genuine nonempty marked lifetime implies M>=1.',
'Whenever marked e is active, its cell is within M of the current head and every active edge is within M of that head. As e stays at its original cell, its full component lies within3M+1<=4M of the departure head. Whenever dormant, that complete component is frozen; every activation is an actualR import, and every later departure leaves a subset of the previously local active field. Induction covers arbitrary many unproductive reattachments and all intermediate cuts, not only first return.',
'Erase once the cut-d black cells outside the original4M box. If one were ever first read through marked consumption, that first read would beL on the exact old-cohort lifetime, contradicting the premise. Therefore the entire removed set is never read. First-difference induction preserves every turn, physical head/heading, both geometric cursors and every laterR birth. The new black board is exactly old board minus the fixed removed set at every cut.',
'All complete active-w masses can only decrease under edge deletion. Other active components and z topology may change. But no removed edge belongs to the marked complete component at ANY cut, by localization; its full edge set remains connected and cannot acquire new connections after deletion. Its completeness, active/dormant itinerary, complete archives, actual reimports and final consumption are therefore exact, not just bounded.',
'The predeparture complete active field and departingL cell are also inside the original4M box. Restoring that local cell prepends the same genuine bridgeL with the full local component unchanged. This is a real compact finite initial board for the segment, not a dynamic crop.',
'Important parameter qualification: erasure can reduce the actual maximum to Mprime<=M. The proved support radius is4M with the ORIGINAL M, and no-old-remote-consumption is preserved relative to that same original box. It is NOT automatically preserved relative to the smaller recomputed4Mprime box. No claim that the reduction necessarily yields another RH16/4 counterexample using its own new maximum is signed.',
'RH16/4, any universal remote-fuel charge, finite waiting deadline, or global attraction remains unproved. Named author diagnostics do not establish those statements; this report signs only the analytic localization/erasure reduction and explicit scope.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print('fixed lifetimes',len(controls))
