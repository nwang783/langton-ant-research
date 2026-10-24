from pathlib import Path
from collections import Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'core_periodicity_new';B=D/'U_cohort_first_touch_frozen_20261023_2005';m=json.loads((B/'manifest.json').read_text())
for p,s in m['files'].items():assert hashlib.sha256((B/p).read_bytes()).hexdigest()==s
ns={'__file__':str(SELF.parent/'check_plain_U_first_touch_merger_independent.py')};exec((SELF.parent/'check_plain_U_first_touch_merger_independent.py').read_text().split('for first in G:')[0],ns)
G=ns['G'];chords=ns['chords'];meet=ns['meet'];pt=ns['pt'];rotation=ns['rotation'];xy=ns['xy'];raws=ns['raws'];end=ns['end'];bad_past=ns['bad_past'];L={0j,1j,1+0j,1+1j}
ports=json.loads((SELF.parent/'check_U_first_helper_ports_independent.json').read_text())['gates'];rows=[];startup=[];extra=[]
for s in(7,8,9):
 R=G[s]['O'];fp,fh=end(s,0j,0);z=fp+rotation(2+0j,fh);c=s-7
 for first in G:
  for case in [g for g in ports if g['source']==s]:
   goal=case['consumer'];gp=complex(*case['head'][:2]);gh=case['head'][2];gctx={gp+rotation(q,gh)for q in G[goal]['ctx']};gins={gp+rotation(q,gh)for q in G[goal]['I']}
   assert case['age']-c==5 and (rotation(gp-fp,-fh),(gh-fh)%4)in((2-1j,3),(3-2j,3))
   if first in(7,8,9):
    assert{fp+rotation(q,fh)for q in L}&gctx;startup.append((s,first,goal,'permanent_U_star'));continue
   assert z in{fp+rotation(q,fh)for q in G[first]['O']}and z in gctx-gins
   p=fp;h=fh;base=0 if first<2 else 4
   for tick,ch in enumerate(raws[first]):
    if tick>=len(raws[base]):assert p!=z
    h=(h+(1 if ch=='R'else-1))%4;p+=(1j,1+0j,-1j,-1+0j)[h]
   for a in G:
    for h in range(4):
     for k,i in enumerate(sorted(G[a]['I'],key=xy)):
      p=z-rotation(i,h);ep,eh=end(a,p,h);ctx={p+rotation(q,h)for q in G[a]['ctx']}
      if(sum(xy(p))+h)%2:reason='wrong_sector'
      elif ctx&R:reason='unchanged_source_cohort_in_context'
      elif bad_past(a,p,h,s,0j,0)or bad_past(a,p,h,first,fp,fh):reason='past_source_or_immediate_successor_chord'
      elif bad_past(goal,gp,gh,a,p,h):reason='future_first_helper_chord'
      elif a in(7,8,9)and{p+rotation(q,h)for q in L}&gctx:
       reason='clearer_U_star_blocks_helper';assert rotation(p-fp,-fh)==3-1j and(h-fh)%4==0 and goal==4 and s in(8,9);assert p in{gp+rotation(q,gh)for q in ns['ns']['K']};extra.append((s,first,goal,a,xy(p),h))
      else:
       loc=rotation(p-fp,-fh);locend=rotation(ep-fp,-fh);assert(h-fh)%4==3 and loc.imag in(0,1)and locend.imag>=1;reason='relative_clock1_head_too_low_or_clock5_exit_too_high'
      rows.append(dict(source=s,first=first,goal=goal,consumer=a,head=(*xy(p),h),slot=k,reason=reason))
   startup.append((s,first,goal,'guard_unretirable'))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=1380,unchanged_source_cohort_in_context=1090,past_source_or_immediate_successor_chord=36,future_first_helper_chord=58,clearer_U_star_blocks_helper=25,relative_clock1_head_too_low_or_clock5_exit_too_high=171)
ref=json.loads((B/'U_cohort_first_touch.json').read_text());key=lambda r:(r['source'],r['first'],r['goal'],r['consumer'],tuple(r['head']),r['slot']);assert{key(r):r['reason']for r in rows}=={key(r):r['reason']for r in ref['guard_clearer_rows']}
assert len(startup)==48
for a in(0,4,7):assert G[a]['h']==0 and G[a]['end'].imag>0 and rotation(G[a]['end'],3).imag>=0
for a in(1,5,8):assert G[a]['h']==3 and G[a]['end'].imag>=2
out=dict(status='PASS every genuine U-family fresh cohort first touch imports an outside identity',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),startup=startup,extra_U_star_cases=extra,all_rows=rows,analytic='Own six first-helper gates normalize at source full exit to W-headed D/DC(2,-1) or V(3,-2), all5Cs later. Immediate U successors permanently block goals; D/V successors freshly install common z(2,0). Exact guard-clearer contexts and source/successor/future-goal chords retain legitimate adjacent endpoint exceptions. Extra25 U clearers at relative(3,-1,N) permanently install a goal-core cell. Remaining171 W clearers are too low at C1 or too high to reach goal after C5. Therefore no first consumer can have all inputs in the unchanged cohort.',scope='Literal outside-cohort identity theorem requires no reset. Reset-at-source genealogy then gives a genuine first-touch component merger. In original genealogy the imported ID may already share the component; no oldness, later-touch or global U/birth bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
