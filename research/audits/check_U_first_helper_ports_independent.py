from pathlib import Path
from fractions import Fraction as F
from collections import Counter,deque
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'core_periodicity_new';B=D/'U_first_helper_ports_frozen_20261023_1954';man=json.loads((B/'manifest.json').read_text())
for p,s in man['files'].items():assert hashlib.sha256((B/p).read_bytes()).hexdigest()==s
K={p for p,b in walk(mark)[2].items()if b};G={};IDS=(0,1,4,5,6,7,8,9)
for s in IDS:
 e,h,_,flip=walk(raws[s]);req=walk(raws[s]+mark)[2];black={p for p,b in req.items()if b};G[s]=dict(I=black-K,O=(black^flip)-{e+rotation(p,h)for p in K},ctx=set(req),end=e,h=h)
def cross(a,b):return int(a.real*b.imag-a.imag*b.real)
def pt(z):return(F(int(z.real)),F(int(z.imag)))
def meet(a,b,c,d):
 u=b-a;v=d-c;den=cross(u,v)
 if den:
  t=F(cross(c-a,v),den);q=F(cross(c-a,u),den)
  return{(F(int(a.real))+t*int(u.real),F(int(a.imag))+t*int(u.imag))}if 0<=t<=1 and 0<=q<=1 else set()
 if cross(c-a,u):return set()
 f=(lambda z:int(z.real))if u.real else(lambda z:int(z.imag));lo,hi=sorted((F(f(c-a),f(u)),F(f(d-a),f(u))));lo=max(lo,0);hi=min(hi,1)
 if lo>hi:return set()
 return{(F(int(a.real))+t*int(u.real),F(int(a.imag))+t*int(u.imag))for t in(lo,hi)}
def chords(s,p=0j,h=0):
 base=0 if s<2 else 4 if s<7 else 7;start=2*p+rotation(-1-1j,h);end=start+rotation({0:2+2j,4:2+6j,7:8j}[base],h);ret=[(start,end)]
 e,dh,_,_=walk(raws[base]);p+=rotation(e,h);h=(h+dh)%4
 for _ in range(0 if s in(0,4,7)else 1 if s in(1,5,8)else 2):
  start=2*p+rotation(-1-1j,h);p+=rotation(1j,h);h=(h-1)%4;ret.append((start,2*p+rotation(-1-1j,h)))
 return ret
def edge(q):
 z=1+1j if sum(xy(q))%2==0 else 1-1j
 return(2*q-z,2*q+z)
def bridge(outs,E):
 adj={}
 for q in outs:
  a,b=edge(q);adj.setdefault(a,[]).append((b,q));adj.setdefault(b,[]).append((a,q))
 todo=deque([(E,[E],[])]);seen={E}
 while todo:
  z,path,qs=todo.popleft()
  if z==-1+3j:return path,qs
  for w,q in sorted(adj.get(z,[]),key=lambda x:xy(x[0])):
   if w not in seen:seen.add(w);todo.append((w,path+[w],qs+[q]))
 raise AssertionError('no held-output bridge')
rows=[];gates=[];adjacent_rejects=[]
for s in(7,8,9):
 outs=G[s]['O'];sc=chords(s);c=s-7
 for a in IDS:
  first=min(G[a]['I'],key=xy)
  for h in range(4):
   for q in sorted(outs,key=xy):
    p=q-rotation(first,h);ins={p+rotation(i,h)for i in G[a]['I']};ctx={p+rotation(i,h)for i in G[a]['ctx']};cc=chords(a,p,h)
    if(sum(xy(p))+h)%2:reason='wrong_sector'
    elif not ins<=outs:reason='needs_outside_identity'
    elif(ctx&(outs-ins)):reason='other_current_source_output_in_context'
    elif any(meet(*x,*y)for x in cc for y in sc):
     reason='past_source_chord_contact';assert(p,h)!=(G[s]['end'],G[s]['h']) # no immediate-adjacency exception
    else:
     reason='first_helper_gate';E=cc[0][1];path,qs=bridge(outs,E);assert len(path)==len(set(path))and len(qs)==len(set(qs))
     for i,(u,v)in enumerate(zip(path,path[1:])):
      assert set(edge(qs[i]))=={u,v}
      assert meet(*cc[0],u,v)==({pt(E)}if i==0 else set())
      for j,(x,y)in enumerate(sc):
       if j==0:x=-1+3j
       assert meet(x,y,u,v)==({pt(-1+3j)}if j==0 and i==len(path)-2 else set())
      for k,(x,y)in enumerate(zip(path,path[1:])):
       if k>i+1:assert not meet(u,v,x,y)
     # Exact symbolic angle units pi/4: alpha is 1 for D, strictly (1,2) for V.
     # Represent each angle as coefficient*alpha + integer, no floats.
     dia={(1,1):1,(-1,1):3,(-1,-1):5,(1,-1):7}
     aa=[(1,-2*h)]+[(0,dia[(1 if v.real>u.real else-1,1 if v.imag>u.imag else-1)])for u,v in zip(path,path[1:])]+[(0,2)]
     total=[0,0];turns=[];av=F(1)if a in(0,1)else F(3,2)
     for (ac,ak),(bc,bk)in zip(aa,aa[1:]):
      coef=bc-ac;z=bk-ak
      while coef*av+z<=-4:z+=8
      while coef*av+z>=4:z-=8
      assert -4<coef*av+z<4;turns.append((coef,z));total[0]+=coef;total[1]+=z
     assert total==[-1,-2*c]
     assert [n for n in range(20)if 2*(n-c-1)in(-8,8)]==[c+5]
     gates.append(dict(source=s,consumer=a,head=(*xy(p),h),inputs=sorted(map(xy,ins)),bridge=list(map(xy,path)),bridge_ids=list(map(xy,qs)),symbolic_turns=turns,total_closing=total,age=c+5))
    rows.append(dict(source=s,consumer=a,head=(*xy(p),h),reason=reason))
counts=Counter(r['reason']for r in rows);assert counts==dict(wrong_sector=576,needs_outside_identity=324,other_current_source_output_in_context=231,past_source_chord_contact=15,first_helper_gate=6)
ref=json.loads((B/'first_helper.json').read_text());key=lambda r:(r['source'],r['consumer'],tuple(r['head']))
assert{key(r):r['reason']for r in rows}=={key(r):r['reason']for r in ref['rows']}
assert{(key(g),g['age'])for g in gates}=={(key(g),g['forced_nonnegative_C_age'])for g in ref['cases']}
out=dict(status='PASS six reset-U first-helper ports and exact C clocks',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),counts=dict(counts),gates=gates,all_rows=rows,analytic='At first touch of the reset source component, its current IDs are exactly source outputs. Any outside input is a true merger. All-source survivors hold every bridge output through consumer entry; source partial U/C tails and consumer base interfaces checked literally. Current residual barrier plus automatic U-entry simplicity gives Jordan closure. Exact symbolic closing turn cancels alpha and forces n=c+5. No source/consumer immediate-adjacency exception was discarded.',scope='Only first later source-output touch, reset genealogy. Six necessary gates are not claimed attained; no control after first helper, global births, U count, or capture.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts);print([(g['source'],g['consumer'],g['head'],g['age'])for g in gates])
