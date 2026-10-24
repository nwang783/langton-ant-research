from pathlib import Path
from collections import Counter,defaultdict
from itertools import permutations
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for line in(D/'SURGERY_SHA256SUMS').read_text().splitlines():h,p=line.split(None,1);assert sha(R/p)==h
corr=D/'REORDER_RIGIDITY_SCOPE_CORRECTION.md';assert sha(corr)=='b932313bd60ac8b32cbe780dbe37e36e0df52a64307902fa70e8af5b046a164d'
ns={'__file__':str(S.with_name('check_all_cap_extremal_read_coupling_independent.py'))};exec(Path(ns['__file__']).read_text().split('std=json.loads')[0],ns);trace,key=[ns[k]for k in['trace','key']]
W=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=len(W);ref=json.loads((D/'standard_pose_excursion_surgery.json').read_text());hist=Counter();rows=[];bad=[];seen=set();maxall=0;maxmovable=0
for phase in range(P):
 base=W[phase:]+W[:phase];ev,dr,hh=trace(base);assert hh==0;cuts=[t for t,p,hi,ho,c in ev if p==0j and hi==0];assert cuts[0]==0
 slots=[base[a:b]for a,b in zip(cuts,cuts[1:])];tail=base[cuts[-1]:];hist[len(slots)]+=1;maxall=max([maxall]+list(map(len,slots)))
 if len(slots)>=2:maxmovable=max([maxmovable]+list(map(len,slots)))
 assert cuts==ref['source_pose_slots'][phase]['cuts']and list(map(len,slots))==ref['source_pose_slots'][phase]['loop_lengths']
 for slot in slots:assert trace(slot)[1:]==(0j,0)
 inventory=Counter(z[1:]for z in ev)
 for perm in permutations(range(len(slots))):
  cand=''.join(slots[i]for i in perm)+tail;events,d,h=trace(cand);assert(d,h)==(dr,hh)and Counter(z[1:]for z in events)==inventory
  H=defaultdict(list)
  for t,p,hi,ho,c in events:
   q,k=key(p,d);H[q].append((t-P*k,t,k,c))
  for q in H:H[q].sort()
  failures=[(q,a,b)for q,ls in H.items()for a,b in zip(ls,ls[1:])if a[-1]==b[-1]]
  standard=cand in {W[i:]+W[:i]for i in range(P)}
  if standard:assert not failures and all(ls[0][-1]=='R'for ls in H.values())
  else:assert failures;bad.append((phase,perm,[[int(failures[0][0].real),int(failures[0][0].imag)],failures[0][1],failures[0][2]]))
  rr=next(z for z in ref['all_candidates']if z['base_phase']==phase and tuple(z['permutation'])==perm);assert rr['word']==cand
  if failures:
   assert rr['result']['status']=='nonalternating';a,b=rr['result']['first'],rr['result']['second'];q=complex(*rr['result']['class']);assert a['turn']==b['turn'];events_q=[]
   for t,p,hi,ho,c in events:
    qq,k=key(p,d)
    if qq==q:events_q.append((t-P*k,t,k,c))
   events_q.sort();pair=((a['clock'],a['phase'],a['copy'],a['turn']),(b['clock'],b['phase'],b['copy'],b['turn']));assert pair in list(zip(events_q,events_q[1:]))
  else:assert rr['result']['status']=='complete_WHITE'
  assert cand not in seen;seen.add(cand);rows.append((phase,perm,standard))
assert dict(hist)=={0:47,1:31,2:18,3:7,4:1}and len(rows)==180 and len(bad)==76 and maxall==100 and maxmovable==92
out={'status':'PASS complete180 one-pose standard excursion-reordering family WITH mandatory100/92 prose correction','author_note':sha(D/'STANDARD_ONE_POSE_REORDER_RIGIDITY.md'),'mandatory_correction':sha(corr),'loop_count_distribution':dict(hist),'parameter_choices':180,'distinct_words':180,'standard_WHITE_controls':104,'nonstandard_immutable_stable_class_failures':76,'max_slot_any_phase':100,'max_slot_with_nontrivial_permutation':92,'fresh_failures':bad,'analytic_review':[
'At each of104 actual cyclic phase seams, every cut returning to the exact starting position AND incoming heading is retained. Adjacent cuts define ALL original complete excursions, with an unchanged terminal tail. Enumerating permutations includes empty/singleton cases and arbitrary fixed-slot subsets. No new excursion or radius bound is introduced.',
'Each moved excursion starts and ends at the same physical pose; therefore its actual spatial event multiset, not merely displacement/turn count, is invariant. Fresh full (cell,incoming,outgoing,turn) counters match for every candidate.',
'For a fixed nonzero full drift d, the complete visit list at class representative is ordered by exact t-kP. Each stored rejection is two adjacent equal turns in that COMPLETE list, not a finite-prefix boundary mismatch. At a sufficiently forward copy every listed visit occurs at nonnegative execution time, so no finite or infinite prepared initial board can repair the immutable consecutive-color conflict.',
'Exactly104 candidates are the genuine standard phase words, each with alternating complete WHITE histories; all other76 fail. All180 words are distinct, and all76 AUTHOR witnesses were separately checked against fresh complete lists.',
'Original prose longest available92 was incorrect. Mandatoryb932313b corrects global maximum100 at singleton-loop phase3; largest slot in a phase permitting nontrivial permutation is92 atphase56. Frozen enumeration unchanged.',
'One-pose, one-period surgery only. No simultaneous multi-pose compensation, longer-window rearrangement, changed event inventory, general autonomous classification or finite-seed capture is excluded.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
