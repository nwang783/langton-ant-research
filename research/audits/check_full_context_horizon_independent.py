from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23'
# Reuse only our independently signed exact rational segment/site geometry.
ns={'__file__':str(SELF.parent/'check_thin_chord_lifetime_independent.py')};exec((SELF.parent/'check_thin_chord_lifetime_independent.py').read_text().split('cache={};rows=[];raw=0')[0],ns)
candidates=ns['candidates'];G=ns['G'];K=ns['K'];IDS=tuple(G)
contexts={s:walk(raws[s]+mark)[2] for s in IDS}
assert sum(map(len,contexts.values()))==186 and sum(len(o)for i,o in G.values())==68
cache={};rows=[];raw=0
for a,(_,outs)in G.items():
 for o in outs:
  for b,ctx in contexts.items():
   for slot,color in ctx.items():
    for h in range(4):
     raw+=1;p=o-rotation(slot,h)
     if(sum(xy(p))+h)%2:continue
     d=p+(rotation(-1-1j,h)+1+1j)/2
     assert d==complex(*xy(d))and sum(xy(d))%2==0
     if d not in cache:cache[d]=candidates(d)
     M=len(cache[d]);geom=4*M+11 if d else 0;bound=geom-(geom+h)%4 if d else 0
     rows.append(dict(source=a,output=xy(o),candidate=b,slot=xy(slot),black=bool(color),heading=h,head=xy(p),delta=xy(d),M=M,geometric=geom,bound=bound))
assert raw==50592 and len(rows)==25296 and len(cache)==157
assert max(map(len,cache.values()))==80 and max(r['geometric']for r in rows)==331 and max(r['bound']for r in rows)==330
maxima=[r for r in rows if r['bound']==330];assert len(maxima)==8
assert all(r['delta']==(0,14)and r['heading']==2 and r['head']==(-1,13)and not r['black']for r in maxima)
for d,sites in cache.items():assert candidates(d,5)==sites
# Check every role and every exact candidate set against frozen author controls.
ref=json.loads((D/'full_context_horizon_controls.json').read_text())
key=lambda r:(r['source'],tuple(r['output']),r['candidate'],tuple(r['slot']),r['heading'])
rr={(r['source'],tuple(r['output']),r['candidate'],tuple(r['context_slot']),r['current_relative_heading']):(tuple(r['center_delta']),r['candidate_sites'],r['geometric_bound'],r['rounded_bound'],r['before_color'])for r in ref['all_roles']}
assert len(rr)==len(rows)
for r in rows:assert rr[key(r)]==(r['delta'],r['M'],r['geometric'],r['bound'],r['black'])
for r in ref['all_candidate_sites']:
 theirs={tuple(z['entry']):sorted(map(tuple,z['vectors']))for z in r['sites']};assert cache[complex(*r['delta'])]==theirs
c=(-1-1j)/2;offsets=[rotation(c-v,h)-c for ctx in contexts.values()for v in ctx for h in range(4)]
assert max(max(abs(z.real),abs(z.imag))for z in offsets)==8
for j in range(330,1000):assert sum(2*a+10 for a in range(j-330,j+1))==331*(2*j-320)
note=D/'transition_complete_330_frontier.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='222d694e4882435b58f3bde91565277411aff11d85f14534af5e0e194dffc034'
out=dict(status='PASS independent complete-context330 horizon and transition-complete growing frontier',note_sha256=sha,raw_roles=raw,sector_roles=len(rows),context_slots=186,output_slots=68,distinct_deltas=len(cache),max_M=80,max_geometric=331,max_rounded=330,maximizers=maxima,entry_offset=8,entry_horizon='20R+271',all_roles=rows,geometry=[dict(delta=xy(d),sites=[dict(entry=p,vectors=v)for p,v in sorted(ss.items())])for d,ss in sorted(cache.items(),key=lambda z:xy(z[0]))],analytic='Producer-entry to CURRENT-entry is an already actual simple subarc. Candidate context membership fixes its endpoints without assuming candidate validity. Thus omitted old blacks are outside every raw-plus-marker candidate context. Reduced/full boards have identical first failure or successful trace. Induction retains the actual U-entry simplicity premise; remove inputs before fresh outputs and use full source-entry clocks. Stop at retained-language exit.',scope='331 C-age layers, finite but O(r0*j) and spatially growing; no finite-state, recurrence, U/C bound or capture theorem.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha,len(rows),len(cache),maxima)
