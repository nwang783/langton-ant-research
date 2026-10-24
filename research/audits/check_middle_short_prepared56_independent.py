from pathlib import Path
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'MIDDLE_SHORT_PREPARED56_NONDICIONARY_RETURN_AND_SUFFIX_TRAP.md':'d93e57dc37db9d9258bf73e9d26d1d15ab1420b425a6b22d2856352ab0b0c1cd','certify_middle_short_prepared56.py':'14787eec269a05702f832f25135b91eac57413f7adce79c0ea496e828214a6e4','middle_short_prepared56_certificate.json':'fe35b8091f5bd1dd2e4bfcdd4ab712b0474cb400ae06bd017a65887cb1d060a6'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'middle_short_prepared56_certificate.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
V=(1j,1,-1j,-1);off=(-1j,-1-1j,-1,0j);xy=lambda p:[int(p.real),int(p.imag)];face=lambda p,h:p+off[h];lev=lambda p,h:int(3*face(p,h).imag-face(p,h).real)
pre='RRRRLRRRRLLLLRLLRRRRLLRLLRRRRLLR';E='RRRLLRLRRLRRLRRLRLLR';G='LLLL';word=pre+E+G;assert word==J['word'];seed={complex(*q)for q in J['whole_initial_black']};assert seed=={-10+1j,-9-1j,-9+4j,-8+2j,-8+4j,-7+1j}
B={q:None for q in seed};p=-8+0j;h=0;visited=set();read=[];states={}
for t,c in enumerate(word):
 if t in(0,32,52):states[t]=(dict(B),p,h)
 rr=J['all56_events_with_exact_input_or_R_owners'][t];assert rr['t']==t and rr['p']==xy(p)and rr['hi']==h and rr['c']==c
 assert (p in B)==(c=='L');owner=B.get(p)
 if c=='L':assert rr['actual_R_owner_within_factor']==owner and rr['input_lifetime']==(owner is None);del B[p]
 else:B[p]=t
 visited.add(p);read.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
states[56]=(dict(B),p,h);assert(p,h)==(-8+0j,2)and len(B)==12 and set(B)=={complex(*q)for q in J['whole_final_black']}
for r in J['whole_checkpoint_fields']:
 bb,pp,hh=states[r['time']];assert set(bb)=={complex(*q)for q in r['whole_black_field']}and r['head']==xy(pp)and r['heading']==hh
assert[len(states[t][0])for t in(0,32,52,56)]==[6,12,16,12]and read[54]==(-7+1j,0,'L')and J['all56_events_with_exact_input_or_R_owners'][54]['input_lifetime']
assert states[32][1:]==states[52][1:]==(-8+0j,2)and all(q!=-8 for q,h,c in read[33:52])
assert[lev(q,h)for q,h,c in read[32:52]]==J['nonstandard_E1']['active_C_levels']and min(lev(q,h)for q,h,c in read[32:52])>=7
# Every previously read site's actual color is fixed, every unread color is free.
branches=[]
for choice in('R','L'):
 known={q:q in B for q in visited};p=-8+0j;h=2;trace=[];new=[]
 while lev(p,h)not in(1,3,5):
  t=len(trace)
  if p not in known:
   assert(p,h,t)==(-10-1j,3,3);c=choice;new.append((xy(p),t,c))
  else:c='L'if known[p]else'R'
  trace.append((t,xy(p),h,c,xy(face(p,h)),lev(p,h)));known[p]=c=='R';h=(h+(1 if c=='R'else-1))%4;p+=V[h];assert p!=-8
  assert len(trace)<=7
 r=next(r for r in J['all_two_unread_continuation_branches']if r['chosen_turn_at_only_unknown_cell']==choice)
 assert r['forced_next_read']==dict(position=xy(p),heading=h,C_face=xy(face(p,h)),C_level=lev(p,h),relative_time=len(trace))
 assert trace==[(z['relative_time'],z['position'],z['heading'],z['turn'],z['C_face'],z['C_level'])for z in r['actual_prefix']]
 branches.append(dict(choice=choice,unknown=new,forced_core=xy(face(p,h)),level=lev(p,h),offset=len(trace)))
assert[(r['level'],r['offset'])for r in branches]==[(3,7),(5,4)]
out=dict(status='PASS literal prepared56 non-dictionary return and exact arbitrary-unread suffix trap',bindings=files,dependencies=J['dependencies'],whole_masses=[6,12,16,12],literal_reads=56,branches=branches,analytic=[
'The complete six-cell initial board, all56 reads, every actual initial/R-born owner and all four full fields independently replay. E20 is a genuine root-first-return with identical S head pose, no intermediate root read and active C level at least7. Its mass gain is4. G third read54 is genuinely initial BLACK at-7,1, not an internally paid R lifetime.',
'The next required E2 must avoid all complete core-face classes C1/3/5. Starting from the actual56 field, the only free color before failure is the previously unread cell-10,-1 at relative3. Its two choices force core level5 atoffset4 or level3 atoffset7, before any root return. Arbitrary edits to every other unread initial cell cannot change this finite exhaustive branch.',
'This is a positive finite prepared factor plus rejection of its ONE exact suffix. It disproves an overextension of the standard dictionary restriction but does not exclude arbitrary E1/G words, either whole core order, a WHITE front or a controller. The unpaid finite input may have an earlier full-drift owner in a hypothetical completion.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
