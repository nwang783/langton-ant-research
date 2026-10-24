#!/usr/bin/env python3
"""Exact universal far-endpoint channels; retain full half-ray background and XOR field."""
from pathlib import Path
from collections import defaultdict,Counter
from bisect import bisect_left
import json,time,hashlib
ROOT=Path(__file__).parent
DATA=json.loads((ROOT/'compute_exceptional_layer.json').read_text())
PSET={tuple(q)for q in DATA['P']};CAP={tuple(q)for q in DATA['C']};d=(-2,-2)
base=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text())
H=base['word'];HH=base['heading'];PER=len(H);V=((0,1),(1,0),(0,-1),(-1,0))
# standard.json is based at0; translate to retained source entry for the fixed gauge.
entry=(-15,10);pos=entry;head=HH;PH=[];HD=[]
for ch in H:
 PH.append(pos);HD.append(head);head=(head+(-1 if ch=='L'else 1))%4;v=V[head];pos=(pos[0]+v[0],pos[1]+v[1])
assert (pos[0]-entry[0],pos[1]-entry[1])==d
FACTORS={''.join(H[(i+j)%PER]for j in range(10))for i in range(PER)};assert len(FACTORS)==84
ROTATIONS={H[i:]+H[:i]for i in range(PER)}
def old_orbit(q):
 x,y=q;a=x%2;return(x-y,a),(a-x)//2

def along(q,c,f):
 ns=[]
 for v,w in zip((q[0]-c[0],q[1]-c[1]),f):
  if w==0:
   if v:return None
  else:
   if v%w:return None
   ns.append(v//w)
 return ns[0]if ns and len(set(ns))==1 else None

RORB={old_orbit(q)[0]for q in PH};PORB={old_orbit(q)[0]for q in PSET};CORB={old_orbit(q)[0]for q in CAP}
CHANNELS=[]
for delta in range(-64,85,2):
 for a in[0,1]:
  rr={(t+delta,(b+a)%2)for t,b in RORB}
  if rr.isdisjoint(PORB)and rr&CORB:CHANNELS.append((delta,a))
assert len(CHANNELS)==106

def make_initial(channel,with_cap=True):
 delta,a=channel;trans=(a,a-delta);rel=[(x+trans[0],y+trans[1])for x,y in PH]
 hits=[]
 for q in CAP:
  for i,s in enumerate(rel):
   n=along(q,s,d)
   if n is not None:hits.append((n*PER+i,q,i))
 tau,p,phi=min(hits)
 rows=defaultdict(set)
 def toggle(j,k):
  if k in rows[j]:rows[j].remove(k)
  else:rows[j].add(k)
 for q in PSET:
  j,k=old_orbit(q);toggle(j,k-1) # old pair of wakes has copies i<0
 for i,s in enumerate(rel):
  j,k=old_orbit(s);toggle(j,k+(tau-i-1)//PER)
 rows={j:sorted(vals)for j,vals in rows.items()if vals}
 return rows,set(CAP)if with_cap else set(),p,HD[phi],tau,phi

def row_color(q,rows):
 j,k=old_orbit(q);r=rows.get(j,());return (len(r)-bisect_left(r,k))%2==1

def initial_color(q,rows,F):return row_color(q,rows)^(q in F)

def certify(rows,F,p,h,word):
 slots=[];hh=h;qq=p
 for i,ch in enumerate(word):
  slots.append((qq,i,ch));hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];qq=(qq[0]+v[0],qq[1]+v[1])
 f=(qq[0]-p[0],qq[1]-p[1])
 if hh!=h or f not in[(-2,-2),(2,2),(2,-2),(-2,2)]:return None
 sign=1 if f[0]*f[1]>0 else -1
 groups=defaultdict(list)
 for q,i,ch in slots:
  x,y=q;t=x-sign*y;a=x%2;c=(a,sign*(a-t));k=(x-a)//f[0]
  assert q==(c[0]+k*f[0],c[1]+k*f[1])
  groups[(t,a)].append((k,i,ch,c))
 checks=0
 for group in groups.values():
  group.sort(key=lambda a:(-a[0],a[1]));mn=min(g[0]for g in group);mx=max(g[0]for g in group);c=group[0][3]
  for x,y in zip(group,group[1:]):
   if x[2]==y[2]:return None
  for n in range(mn,mx):
   first=next(g for g in group if g[0]<=n);q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1
   if initial_color(q,rows,F)!=(first[2]=='L'):return None
  want=group[0][2]=='L';tests={mx}
  if f[0]==f[1]:
   j,kc=old_orbit(c);slope=1 if f==d else -1
   for th in rows.get(j,()):
    n=(th-kc)//slope
    for z in[n-1,n,n+1]:
     if z>=mx:tests.add(z)
  else:
   # Every background support orbit meets this ray in at most one point.
   if want:return None # outside finitely many crossings the background is white
   tc=c[0]-c[1];stride=f[0]-f[1]
   for (t,a)in rows:
    if a!=c[0]%2 or(t-tc)%stride:continue
    n=(t-tc)//stride
    if n>=mx:tests.add(n)
  for q in F:
   n=along(q,c,f)
   if n is not None and n>=mx:
    tests.add(n);tests.add(n+1)
    if n-1>=mx:tests.add(n-1)
  for n in tests:
   q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1
   if initial_color(q,rows,F)!=want:return None
 return {'drift':list(f),'checked_initial_ray_positions':checks,'read_orbits':len(groups)}

# Countercontrols: on the unchanged incoming causal front every entire H tail
# is exact, but a black flip one million periods ahead on a fresh ray rejects.
def controls():
 total=0
 for channel in CHANNELS:
  rows,F,p,h,tau,phi=make_initial(channel,with_cap=False);word=H[phi:]+H[:phi]
  assert certify(rows,F,p,h,word)
  # a first fresh read in a far copy of the predicted path
  q=(p[0]+1000000*d[0],p[1]+1000000*d[1]);bad={q}
  # p may not be first-read in its orbit; choose any far predicted read with white initial color.
  if initial_color(q,rows,F):
   ss=p;hh=h
   for ch in word:
    qq=(ss[0]+1000000*d[0],ss[1]+1000000*d[1])
    if not initial_color(qq,rows,F):q=qq;break
    hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];ss=(ss[0]+v[0],ss[1]+v[1])
  assert not initial_color(q,rows,F)
  assert certify(rows,{q},p,h,word)is None
  total+=2
 return total

def solve(channel,limit=300000):
 rows,F,p,h,tau,phi=make_initial(channel)
 hist=''.join(H[(tau-10+j)%PER]for j in range(10));prev_bad=hist not in FACTORS;K=0;recent='';attempts=0
 for t in range(limit+1):
  if t>=208 and t%104==0 and recent[:104]==recent[104:]and recent[104:]in ROTATIONS:
   word=recent[104:];attempts+=1;cert=certify(rows,F,p,h,word)
   if cert:
    # Count the only still-possible future boundary K, on a copy of the full field.
    ff=set(F);pp=p;hh=h;history=hist;bad0=prev_bad;extra=0
    for _ in range(10):
     ch='L'if initial_color(pp,rows,ff)else'R';history=(history+ch)[-10:];bad=history not in FACTORS;extra+=bad and bad0;bad0=bad
     if pp in ff:ff.remove(pp)
     else:ff.add(pp)
     hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
    return {'channel':channel,'status':'CERTIFIED','entry':t,'pose':[list(p),h],**cert,'tail_word':word,'K_total':K+extra,'finite_XOR_mass':len(F),'finite_XOR_sha256':hashlib.sha256(json.dumps(sorted(F),separators=(',',':')).encode()).hexdigest(),'attempts':attempts}
  if t==limit:break
  ch='L'if initial_color(p,rows,F)else'R';hist=(hist+ch)[-10:];bad=hist not in FACTORS;K+=bad and prev_bad;prev_bad=bad
  recent=(recent+ch)[-208:]
  if p in F:F.remove(p)
  else:F.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 return {'channel':channel,'status':'UNKNOWN','limit':limit,'K_observed':K,'finite_XOR_mass':len(F),'attempts':attempts}

if __name__=='__main__':
 started=time.time();ctrl=controls();results=[]
 for i,ch in enumerate(CHANNELS):
  r=solve(ch);results.append(r)
  if i%10==0:print(i+1,'/',len(CHANNELS),r,flush=True)
  out={'status':'EXACT_CERTIFICATES_WITH_RESOURCE_LIMITS','controls':ctrl,'channel_count':len(CHANNELS),'results':results,'elapsed_seconds':time.time()-started,'scope':'Only one explicitly supplied universal endcap/profile. UNKNOWN is not impossibility; no global capture inference.'}
  (ROOT/'endpoint_catalog_results.json').write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',Counter(tuple(r.get('drift',[]))for r in results),flush=True)
