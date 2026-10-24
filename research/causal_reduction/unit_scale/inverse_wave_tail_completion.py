"""Exact finite completion of a prescribed inverse-standard tail.
New initial edits may be assigned only outside the entire future wave READ set
and outside the already executed inverse prefix. No prefix search is performed.
"""
from pathlib import Path
from collections import defaultdict
import json
P=Path(__file__).resolve().parent;G=P.parents[1]/'nonlinear_global_budget_2026-10-23'
H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
N=json.loads((G/'prepared_wave_five_band_normal_form.json').read_text())
J=json.loads((G/'prepared_travelling_wave_certificate.json').read_text())
V=((0,1),(1,0),(0,-1),(-1,0));B={tuple(j)for j in N['full_black_orbit_profiles']};BASE={tuple(q)for q in N['finite_XOR_cap']}
def trace(word,p,h):
 rows=[]
 for i,c in enumerate(word):
  rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return rows,p,h
wave,_,_=trace(J['word'],tuple(N['pose'][0]),N['pose'][1]);FUTURE={}
for _,(x,y),_,_ in wave:
 key=x-y,x%14;k=x//14;FUTURE[key]=min(k,FUTURE.get(key,k))
def future_read(p):
 x,y=p;return (x-y,x%14)in FUTURE and x//14>=FUTURE[x-y,x%14]
def bulk(p):return (p[0]-p[1],p[0]%2)in B
# Canonical SW writer phase0 (-15,-16), W: its inverse phase0 is (-14,-16), E.
forward,_,_=trace(H,(-15,-16),3);TARGETS=defaultdict(list)
for phase,q,h,c in forward:
 p=q[0]-V[h][0],q[1]-V[h][1];head=(h+2)%4
 word=''.join('L'if H[(phase-1-i)%104]=='R'else'R'for i in range(104))
 rows,ep,eh=trace(word,p,head);assert eh==head and(ep[0]-p[0],ep[1]-p[1])==(2,2)
 groups=defaultdict(list)
 for i,z,hh,ch in rows:
  dx,dy=z[0]-p[0],z[1]-p[1];groups[dx-dy,dx%2].append((i-104*(dx//2),dx//2,ch))
 groups={j:tuple(sorted(g))for j,g in groups.items()}
 fringe=set()
 for(t,a),group in groups.items():
  lo=min(g[1]for g in group);hi=max(g[1]for g in group)
  for k in range(lo,hi+1):fringe.add((a+2*k,a+2*k-t))
 TARGETS[p[0]-p[1],p[0]%2,head].append((phase,word,groups,tuple(fringe)))

def completion(p,h,edits,flips,seen,details=False):
 """Return all finite admissible tail completions at this exact physical pose."""
 current=BASE^set(edits)^set(flips);answers=[]
 for phase,word,groups,fringe in TARGETS.get((p[0]-p[1],p[0]%2,h),()):
  # Every far ray has its stable first color; compare the full profile, not a horizon.
  if any((g[0][2]=='L')!=bulk((p[0]+a,p[1]+a-t))for(t,a),g in groups.items()):continue
  def required(z):
   x,y=z[0]-p[0],z[1]-p[1];group=groups.get((x-y,x%2),())
   for time,k,ch in group:
    if k<=x//2:return ch=='L'
   return None
  critical=current|{(p[0]+x,p[1]+y)for x,y in fringe};extra=set();bad=[]
  for z in critical:
   want=required(z)
   if want is None or (bulk(z)^(z in current))==want:continue
   if z in seen or future_read(z):bad.append(z)
   else:extra.add(z)
  if not bad:answers.append({'phase':phase,'word':word,'extra_initial_XOR':sorted(extra),'tail_pose':[p,h]})
  elif details:answers.append({'phase':phase,'rejected_fixed_or_past':sorted(bad),'free_fringe_edits':sorted(extra)})
 return answers

if __name__=='__main__':
 rows,p,h=trace('LLR',(-6,-7),2);flips={q for _,q,_,_ in rows}
 print(json.dumps({'LLR_pose':[p,h],'completion':completion(p,h,{(-6,-7)},flips,flips,True)},indent=2))
