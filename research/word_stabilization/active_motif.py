"""Exact finite countermodels for active-motif maximum candidates."""
import json,itertools
from pathlib import Path
DATA=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
def requirements(trace):
 d={}
 for z in trace:d.setdefault(tuple(z['p']),int(z['c']=='L'))
 return d
M=requirements(DATA['C']['trace'][:12])
MS=[]
for name,rec in DATA.items():
 for h in range(4):
  MS.append((name,h,{rot(p,h):v for p,v in requirements(rec['trace']).items()}, {rot(tuple(p),h) for p in rec['odd_visits']}))
def make_patterns(mode):
 raw=[('M',M)] if mode=='marker' else [(k,requirements(r['trace'])) for k,r in DATA.items()]
 return [(k,h,{rot(p,h):v for p,v in req.items()}) for k,req in raw for h in range(4)]
def matches(B,pats):
 out=[]
 for k,h,req in pats:
  anchor=next(p for p,v in req.items() if v)
  for q in B:
   p=q[0]-anchor[0],q[1]-anchor[1]
   if all(((p[0]+d[0],p[1]+d[1]) in B)==bool(v) for d,v in req.items()):out.append((k,h,p))
 return out
def candidates(mode='marker',weights=None):
 pats=make_patterns(mode);weights=weights or {(k,h):0 for k,h,req in pats};fail=[];tested=0
 for name,h,req,toggle in MS:
  for k,g,pat in pats:
   possible={(u[0]-v[0],u[1]-v[1]) for u in toggle for v in pat}
   for p in possible:
    initial=req.copy();ok=True
    for d,v in pat.items():
     q=p[0]+d[0],p[1]+d[1];v=v^(q in toggle)
     if q in initial and initial[q]!=v:ok=False;break
     initial[q]=v
    if not ok:continue
    tested+=1;B={q for q,v in initial.items() if v}
    old=matches(B,pats);new=matches(B^toggle,pats)
    a=max(q[1]+weights[(n,j)] for n,j,q in old)
    b=max(q[1]+weights[(n,j)] for n,j,q in new) if new else -1000
    if b>a:
     fail.append({'macro':[name,h],'field':sorted(B),'before':old,'after':new,'old_score':a,'new_score':b})
 print(mode,'tested',tested,'failures',len(fail),'max increase',max([w['new_score']-w['old_score'] for w in fail]+[0]))
 return fail
if __name__=='__main__':
 for mode in ['marker','macro']:
  fail=candidates(mode);Path(__file__).with_name('active_'+mode+'_counterexamples.json').write_text(json.dumps(fail,indent=2))
  print('examples',fail[:2])
