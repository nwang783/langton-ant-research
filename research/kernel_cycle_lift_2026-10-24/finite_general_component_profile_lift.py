"""Exact finite GENERAL complete-active-component path lifting, with unchanged archives.
A pure helper: no files are modified on import and no profile enumeration occurs.
"""
from pathlib import Path
import sys
ROOT=Path('/workspace/shared/langton')
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,sector,vertices,comp,step

def add(p,q):return p[0]+q[0],p[1]+q[1]
def transform(S,p,h):return {add(p,rot(tuple(q),h))for q in S}
def ports(C,p,h,k):
 V=vertices(C,k)|{cursor(p,h)};P=set()
 for x,y in V:
  for sx in(-1,1):
   for sy in(-1,1):
    q=((x+sx)//2,(y+sy)//2);assert(x,y)in ends(q,k);P.add(q)
 return P

def plan(macros):
 p=(0,0);h=0;k=sector(p,h);R=[];seams=[0]
 for m,macro in enumerate(macros):
  if m:
   assert N==transform(macro['transitions'][0]['input_component'],p,h),'Incompatible prescribed active-component seam'
  for j,a in enumerate(macro['transitions']):
   C=transform(a['input_component'],p,h);assert comp(C,k,cursor(p,h))==C
   R.append(dict(p=p,h=h,C=C,turn=a['turn'],macro=m,local=j))
   pn=add(p,rot(tuple(a['output_pose'][0]),h));hn=(h+a['output_pose'][1])%4
   N=transform(a['output_active'],p,h)
   if j+1<len(macro['transitions']):
    assert N==transform(macro['transitions'][j+1]['input_component'],pn,hn)
   p,h=pn,hn
  seams.append(len(R))
 R.append(dict(p=p,h=h,C=N,turn=None,macro=len(macros),local=0))
 return R,k,seams

def lift(macros,retain_trace=False):
 R,k,seams=plan(macros);constraints={};parity={}
 for t,a in enumerate(R):
  for q in sorted(ports(a['C'],a['p'],a['h'],k)):
   bit=int(q in a['C'])^parity.get(q,0)
   cur=dict(cut=t,black=bit,current_black=q in a['C'],read_parity=parity.get(q,0),macro=a['macro'],local=a['local'])
   if q in constraints and constraints[q]['black']!=bit:
    return dict(status='NO_COMPLETE_BOARD_LIFT',macros=[a.get('index')for a in macros],conflict_cell=q,first=constraints[q],second=cur)
   constraints.setdefault(q,cur)
  if a['turn']is not None:parity[a['p']]=parity.get(a['p'],0)^1
 B={q for q,a in constraints.items()if a['black']};seed=set(B);birth={q:None for q in B};p=(0,0);h=0;events=[];trace=[];maxC=0
 for t,a in enumerate(R):
  assert(p,h)==(a['p'],a['h']);C=comp(B,k,cursor(p,h));assert C==a['C'];maxC=max(maxC,len(C))
  if retain_trace:trace.append(dict(cut=t,pose=[p,h],C=sorted(C),full_black=sorted(B)))
  if a['turn']is None:break
  q=p;c=a['turn'];assert c==('L'if q in B else'R')
  if c=='R':
   w=cursor(p,h);u,v=ends(q,k);other=v if u==w else u
   D=comp(B,k,other)if other not in vertices(C,k)|{w}else set()
   if D:
    events.append(dict(kind='whole_component_import',update=t,macro=a['macro'],local=a['local'],cell=q,component=sorted(D),lifetimes=[dict(cell=e,birth=birth[e],birth_macro=None if birth[e]is None else next(z for z in range(len(seams)-1)if seams[z]<=birth[e]<seams[z+1]))for e in sorted(D)]))
   birth[q]=t
  else:
   events.append(dict(kind='actual_consumption',update=t,macro=a['macro'],local=a['local'],cell=q,birth=birth[q]));birth.pop(q)
  p,h=step(B,p,h)
 return dict(status='ACTUAL_FINITE_BOARD_LIFT',macros=[a.get('index')for a in macros],word=''.join(a['word']for a in macros),initial_black=sorted(seed),initial_mass=len(seed),final_black=sorted(B),final_pose=[p,h],maximum_complete_active_mass=maxC,seams=seams,events=events,trace=trace if retain_trace else None)
