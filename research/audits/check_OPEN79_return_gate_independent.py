from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'OPEN79_PREPARATION_RETURN_DEBT_GATE.md')=='fa387e763a9b2c27fe7648d5fa1b9b4a7ad3d79d1fd1a98acf2747e572a79633'
assert sha(D/'certify_open79_preparation_return_gate.py')=='5ce330c3627f4bcd621034d2822368f4bb7cd3b4ec44cdda38cae17daa61e108'
assert sha(D/'open79_preparation_return_gate_certificate.json')=='0d604fb6fb2b53c19d3f031993d9515fe6c28763d91da0ff15868461b94f026b'
J=json.loads((D/'open79_preparation_return_gate_certificate.json').read_text())
for f,h in J['dependency_hashes'].items():assert sha(D/f)==h
old=S.with_name('check_OPEN79_preparation_age_independent.json');assert sha(old)=='a9d91a1957bdba708ff3a112907ac17084da8402d8ff7cb31fd13914c56a6129'
vec=(1j,1,-1j,-1);xy=lambda q:[int(q.real),int(q.imag)]
def events(w,p=0j):
 h=2;ev=[]
 for t,ch in enumerate(w):
  ev.append(dict(time=t,position=xy(p),incoming_heading=h,turn=ch));h=(h+(1 if ch=='R' else -1))%4;p+=vec[h]
 return ev,p,h
pal={}
for n in(4,8,12):
 for ch in 'RL':
  result=[]
  for bits in range(1<<(n-1)):
   w=ch+''.join('L' if bits>>i&1 else 'R' for i in range(n-1));ev,p,h=events(w)
   if p==0 and h==2 and all(e['position']!=[0,0] for e in ev[1:]):result.append(w)
  pal[n,ch]=set(result);assert len(result)=={4:1,8:5,12:44}[n]
for r in J['palettes']:assert pal[r['length'],r['first_turn']]==set(r['all_geometric_first_return_words'])
layouts={(a,b)for a in range(4,17,4)for b in range(4,17-a,4)};assert layouts==set(map(tuple,J['complete_two_return_layouts']))
rows={r['word']:r for r in J['cases']};rebuilt=set();count=Counter();positive=None
for n,m in sorted(layouts):
 for u in pal[n,'R']:
  for v in pal[m,'L']:
   w='RLRRLL'+u+v+'R';assert w not in rebuilt;rebuilt.add(w);r=rows[w];ev,p,h=events(w,2+1j);assert ev==r['events'] and r['return_lengths']==[n,m]
   assert all(ev[t]['position']==[-1,0] and ev[t]['incoming_heading']==2 for t in(6,6+n,6+n+m))
   prior={};bad=None;seed=set()
   for e in ev:
    q=tuple(e['position']);prev=prior.get(q)
    if prev is None and e['turn']=='L':seed.add(q)
    if prev and prev['turn']==e['turn'] and bad is None:bad=dict(earlier_read=prev,later_read=e)
    prior[q]=e
   if bad:
    assert r['outcome']=='physical_color_contradiction' and r['witness']==bad;count['color']+=1
   else:
    atX=[e for e in ev if e['position']==[2,1]];assert [(e['time'],e['incoming_heading'],e['turn'])for e in atX]==[(0,2,'R'),(16,0,'L')]
    assert r['outcome']=='supplied_first_R_rank1_heading_contradiction';assert r['witness']['required_incoming_heading_at_rank1']==2
    B=set(seed)
    for e in ev:
     q=tuple(e['position']);assert(q in B)==(e['turn']=='L');B.symmetric_difference_update({q})
    z=r['prepared_positive_factor'];assert sorted(map(list,seed))==z['initial_black'] and sorted(map(list,B))==z['complete_final_black'] and xy(p)==z['final_position'] and h==z['final_heading']
    assert seed=={(-1,1),(0,1),(1,1),(2,0)} and B=={(-2,0),(-2,1),(-1,0),(0,0),(1,0)};positive=z;count['complete_history_mismatch']+=1
assert rebuilt==set(rows) and len(rows)==124 and dict(count)==dict(color=123,complete_history_mismatch=1)
out=dict(status='PASS conditional OPEN79 two-return >=20 and earlier preparation span >=64',proof_sha256=sha(D/'OPEN79_PREPARATION_RETURN_DEBT_GATE.md'),certificate_sha256=sha(D/'open79_preparation_return_gate_certificate.json'),script_sha256=sha(S),palettes={str(k):len(v)for k,v in pal.items()},cases=124,outcomes=dict(count),full_prepared_positive=positive,analytic_review=['The two target returns are consecutive reads at the same physical C with incoming S. Alternating move axes imply any return has even numbers of horizontal and vertical steps, hence positive length divisible by4. Total below20 has exactly the six enumerated layouts; no unknown trajectory cutoff is imposed.','The inherited six-step RLRRLL preparation is actual and retains prepared BLACK helper lifetimes. 123 words fail literal alternation against arbitrary input. The unique genuine23-read factor is not discarded: its next X read is N/L at16, contradicting the supplied COMPLETE X=T12 rank1 S after actual FIRST R rank0.','Same-cell rank10->11 costs >=4. Exact previously signed ages P+6 and P-34 subtract to t12,3-t12,0=40+(t12,11-t12,8)>=64. This uses no exterior cap, period upper bound, WHITE helper shortcut, or assertion that total20 is attained. Other outer gaps and longer continuations remain open.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
