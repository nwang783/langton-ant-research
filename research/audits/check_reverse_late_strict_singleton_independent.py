from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib,ast
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';vec={'N':1j,'E':1,'S':-1j,'W':-1};name={v:k for k,v in vec.items()};cp={'A':1,'Z':0,'Y':1j,'B':1+1j};op={'A':1-1j,'Z':-1-1j,'Y':-1+1j,'B':1+1j};f=-2+2j
# Exhaust every allowable original-WHITE reversed first-color/history class at f.
local=[]
for black,ns in[(False,[2,4]),(True,[1,3])]:
 for n in ns:
  for hh in product('EW',repeat=n):
   Rheads=hh[1::2]if black else hh[::2];Lheads=hh[::2]if black else hh[1::2]
   if Counter(Rheads)['E']!=Counter(Rheads)['W']or hh.count('W')!=1:continue
   a=-2-Counter(Rheads)['E'];Ls={'NW':a-Counter(Lheads)['E'],'SE':a-Counter(Lheads)['W']}
   local.append({'black':black,'word':''.join(hh),'L':Ls,'passes_floor':min(Ls.values())>=-3})
assert{(z['black'],z['word'])for z in local}=={(False,'EEWE'),(False,'WEEE'),(True,'W')};assert[z['word']for z in local if z['passes_floor']]==['W']
base=json.loads((D/'canonical_max_face_child_ports.json').read_text())['rows']
def exact(h):return next(r for r in base if r['headings']==h)
F=exact(dict(A='NNSN',Z='WWEW',Y='NSSS',B='EEWE'));I=exact(dict(A='NNSN',Z='WWWE',Y='NSNN',B='WEEE'))
parents=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['B']=='EEWE'and all(len(x)==4 for x in r['headings'].values())];Gs=[r for r in base if r['headings']['A']=='NNSN'and r['headings']['Z']=='WWWE'and all(len(x)==4 for x in r['headings'].values())]
def solve(packages):
 hs={};hc={};births=[]
 for row,ll,q in packages:
  rot=1j**q
  def cell(z):return ll+(1+1j)/2+rot*(z-(1+1j)/2)
  for k,h in row['headings'].items():
   z=cell(cp[k]);hh=''.join(name[vec[c]*rot]for c in h)
   if z in hs and hs[z]!=hh:return
   hs[z]=hh
  for z,h in [(ll,0)]+[(ll+op[k]*rot,0 if row['other'].get(k,'M')=='M'else-int(row['other'][k][2:]))for k in op]:
   if z in hc and hc[z]!=h:return
   hc[z]=h
  births.append((cell(cp['A']),[(cell(cp[k]),vec[c]*rot)for k,c in [('A','W'),('Z','N'),('Y','E'),('B','S')]]))
 if f in hs and hs[f]!='W':return
 hs[f]='W';outs={z:[vec[c]*(1j if z==f or k%2 else-1j)for k,c in enumerate(h)]for z,h in hs.items()};nodes=[(z,k)for z,h in hs.items()for k in range(len(h))];edges=[]
 for z,h in hs.items():
  for k in range(len(h)-1):edges.append(((z,k),(z,k+1),4))
  for direction in set(outs[z]):
   w=z+direction
   if w not in hs:continue
   aa=[(z,k)for k,c in enumerate(outs[z])if c==direction];bb=[(w,k)for k,c in enumerate(hs[w])if vec[c]==direction]
   if len(aa)!=len(bb):return
   for a,b in zip(aa,bb):edges.extend([(a,b,1),(b,a,-1)])
 # Also check absent output directions toward a known neighbor with required inputs.
 for z,h in hs.items():
  for direction in [1,-1,1j,-1j]:
   w=z+direction
   if w not in hs:continue
   if sum(c==direction for c in outs[z])!=sum(vec[c]==direction for c in hs[w]):return
 for ent,bound in births:
  first=[]
  for z,v in bound:
   ranks=[k for k,c in enumerate(outs[z])if c==v]
   if not ranks:return
   first.append((z,ranks[0]))
  if(ent,1)not in first:return
  edges.extend(((ent,1),z,1)for z in first if z!=(ent,1))
 t={z:0 for z in nodes}
 for _ in nodes:
  change=False
  for a,b,k in edges:
   if t[b]<t[a]+k:t[b]=t[a]+k;change=True
  if not change:break
 else:return
 levels=[]
 for z,h in hs.items():
  black=z==f;rr=Counter(h[1::2]if black else h[::2]);ll=Counter(h[::2]if black else h[1::2])
  if h[0]in'EW':Csp={'NE':(z,rr['W']),'SW':(z-1-1j,rr['E'])};Lsp={'NW':ll['E'],'SE':ll['W']}
  else:Csp={'NW':(z-1,rr['S']),'SE':(z-1j,rr['N'])};Lsp={'NE':ll['S'],'SW':ll['N']}
  aa={hc[p]-n for p,n in Csp.values()if p in hc};assert len(aa)==1;a=next(iter(aa));Cs={k:a+n for k,(p,n)in Csp.items()};Ls={k:a-n for k,n in Lsp.items()};assert max(Cs.values())<=0
  if min(Ls.values()) < -3:return
  levels.append((int(z.real),int(z.imag),h,Cs,Ls))
 route=[(-1+1j,2),(-1+2j,1),(f,0),(-2+1j,3),(-1+1j,3)];tt=[t[z]for z in route];assert tt==list(range(tt[0],tt[0]+5))and hs[-2+1j]=='NNNS'
 return {'J':packages[1][0]['headings'],'P0':packages[2][0]['headings'],'G':packages[4][0]['headings'],'levels':levels,'route_offsets':[q-tt[0]for q in tt]}
rows=[];attempts=0
for j,p,g in product(parents,parents,Gs):
 if p['other']['Y']!='M-2':continue
 attempts+=1;z=solve([(F,0j,0),(j,-1-1j,1),(p,-2+0j,0),(I,-1+1j,3),(g,1+1j,3)])
 if z is not None:rows.append(z)
A=json.loads((D/'reverse_late_D4_black_singleton_helper.json').read_text());assert len(rows)==len(A['rows'])==12 and attempts==A['attempts'];assert Counter(json.dumps([r[k]for k in['J','P0','G']],sort_keys=True)for r in rows)==Counter(json.dumps([r[k]for k in['J','P0','G']],sort_keys=True)for r in A['rows'])
files=['reverse_late_D4_strict_helper_singleton_escape.md','reverse_late_D4_black_singleton_helper.py','reverse_late_D4_black_singleton_helper.json'];hh={p:hashlib.sha256((D/p).read_bytes()).hexdigest()for p in files};assert hh[files[0]]=='a649812e2325b0fec11c3587024911387e33af9efe9364254da8ac526344a0c0'
out={'status':'PASS conditional reverse late strict helper singleton escape and source occurrence injection','source_hashes':hh,'all_flat_oneW_allowable_reversed_histories':local,'independent_composite_attempts':attempts,'twelve_full_port_necessary_rows':rows,'analytic_review':[
'The original WHITE cap4 reversal allows only reverseWHITE evenRL/RLRL and reverseBLACK oddL/LRL. Flat reverseC heights require equal R-heading counts, excluding both oneR cases. One W input leaves exactly WHITE EEWE/WEEE or BLACK singletonW. WHITE alternatives force reverseL=lambda-5 below trueglobalfloorlambda-3; singleton respects the floor and does not touch reverseheightlambda plateau.',
'For g=NSNN, its second E output L1 supplies uL1. The exact uR2 secondN ->tL1 ->fL ->gL1 route forces uL1=uR2+4, contradicting actual rank order. For gNNNS the thirdE instead supplies uL3, giving the real five-event RLLLL route with every edge exactlyone tick.',
'The independent full package join rebuilds physical coordinate/heading overlaps, all shared ordinal ports, canonical first-boundary minima and same-cell gaps, allowing the sole BLACK f. The global reverseL floor leaves exactly12 necessary composites, not a realized exterior. Extra zero-output or K1 order at off-Q helpers is not imposed.',
'Reversing actual read events gives original RRRRL around the maximum-C unit face. Singletonf is originalR incomingN, C heightsM/M-1, bothL=M-1. Thus it is a genuine TOP odd output away from the root-free M-3 collar, not a contradiction to that collar.',
'A singleton originalR has one actual incoming heading, fixing the quarter-rotation of this precise source template. Its cell then fixes D by the rotatedoffset(-2,2). Equal full-drift f classes therefore recover equal actual source-face classes. No reflection or extra phase frame is available. This yields one-per-distinct-source injection only; it can overlap all existing singleton reservations.'
],'scope':'Conditional displayed actual reverse late D4 route with known maximum-plateau corners WHITE four-read and strict off-plateau f. No general reverse-late classification, complete front realization, original fuel or added disjoint budget.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(rows))
