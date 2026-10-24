"""Exact eventual-word certificates on a bilateral standard wake plus finite XOR defects.
Search is only a source of candidates; certify_period is an all-time check.
"""
import json
from pathlib import Path
from collections import defaultdict, Counter
D=((0,1),(1,0),(0,-1),(-1,0))
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())
W=DATA['word']; T={(-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),(2,0),(3,0),(5,1),(6,1),(7,0),(7,1)}
def background(p):return (p[0]-p[1],p[0]%2) in T
def add(p,q):return p[0]+q[0],p[1]+q[1]
def times(p,k):return p[0]*k,p[1]*k

def orbit_key(p,d):
 # Canonical quotient by full vector d; also return p=c+k*d.
 a,b=d;x,y=p
 if a:
  k=x//a;c=(x-k*a,y-k*b)
 else:
  k=y//b;c=(x,y-k*b)
 return c,k

def certify_period(word, p, h, errors):
 """All future turns equal word^omega on initial T XOR finite errors, or False.
 No finite-prefix match substitutes for this exact orbit arithmetic.
 """
 pos=p;hh=h;groups=defaultdict(list)
 reads=[]
 for i,c in enumerate(word):
  reads.append(pos);hh=(hh+(1 if c=='R' else -1))%4;pos=add(pos,D[hh])
 d=pos[0]-p[0],pos[1]-p[1]
 if hh!=h or d==(0,0):return False
 for i,q in enumerate(reads):
  c,k=orbit_key(q,d);groups[c].append((k,i,word[i]))
 error_ns=defaultdict(set)
 for q in errors:
  c,k=orbit_key(q,d)
  if c in groups:error_ns[c].add(k)
 for c,phase in groups.items():
  phase.sort(key=lambda row:(-row[0],row[1]))
  mn=min(k for k,i,s in phase);mx=max(k for k,i,s in phase)
  # Boundary cells and every finite perturbation on a touched ray.
  ns=set(range(mn,mx+1)) | {n for n in error_ns[c] if n>=mn}
  delta=d[0]-d[1];tc=c[0]-c[1]
  if delta:
   # Background can be black at only these finitely many transverse crossings.
   for t,a in T:
    if (t-tc)%delta==0:
     n=(t-tc)//delta
     if n>=mn:ns.add(n)
   # Beyond all finite crossings and perturbations, the first letter must be R.
   stable_required=False
   if phase[0][2]!='R':return False
  else:
   # Background is periodic with period at most2 along this orbit.
   for n in (mx,mx+1):
    q=add(c,times(d,n))
    if background(q)!=(phase[0][2]=='L'):return False
  # Check stabilized per-cell chronology. Boundary order is a subsequence.
  if any(a[2]==b[2] for a,b in zip(phase,phase[1:])):return False
  for n in ns:
   letters=[s for k,i,s in phase if k<=n]
   if not letters:continue
   q=add(c,times(d,n));black=background(q) ^ (q in errors)
   if black != (letters[0]=='L'):return False
   if any(a==b for a,b in zip(letters,letters[1:])):return False
 return {'period':len(word),'drift':d,'growth':word.count('R')-word.count('L'),
         'word':word,'read_orbits':len(groups),'stable_first_L_orbits':sum(seq[0][2]=='L' for seq in groups.values())}

def run_pose(p,h,limit=50000):
 errors=set();hist=[];poses=[(p,h)];cert=None
 # Candidate periods from104, plus short periods, then occasional wider search.
 for step in range(1,limit+1):
  black=background(p) ^ (p in errors);hist.append('L' if black else 'R')
  if p in errors:errors.remove(p)
  else:errors.add(p)
  h=(h+(-1 if black else 1))%4;p=add(p,D[h]);poses.append((p,h))
  if step>=312 and step%104==0:
   s=''.join(hist[-312:])
   if s[:104]==s[104:208]==s[208:]:
    cert=certify_period(s[:104],p,h,errors)
    if cert:return {'capture':step,'position':p,'heading':h,'certificate':cert,'errors':len(errors)}
  if step>=192 and step%64==0:
   s=''.join(hist[-192:])
   for n in range(2,65,2):
    if len(s)>=3*n and s[-n:]==s[-2*n:-n]==s[-3*n:-2*n]:
     cert=certify_period(s[-n:],p,h,errors)
     if cert:return {'capture':step,'position':p,'heading':h,'certificate':cert,'errors':len(errors)}
  if step>=1536 and step%2048==0:
   s=''.join(hist[-1536:])
   for n in range(2,513,2):
    if s[-n:]==s[-2*n:-n]==s[-3*n:-2*n]:
     cert=certify_period(s[-n:],p,h,errors)
     if cert:return {'capture':step,'position':p,'heading':h,'certificate':cert,'errors':len(errors)}
 return {'unresolved_at':limit,'position':p,'heading':h,'errors':len(errors),'recent_word':''.join(hist[-256:])}

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=50000);ap.add_argument('--lo',type=int,default=-10);ap.add_argument('--hi',type=int,default=14);args=ap.parse_args()
 rows=[]
 for t in range(args.lo,args.hi+1):
  for a in (0,1):
   p=(a,a-t)
   for h in range(4):
    if (h-p[0]-p[1])%2 != DATA['heading']%2:continue
    row={'start_position':p,'start_heading':h,'transverse':t,'x_parity':a,**run_pose(p,h,args.limit)};rows.append(row)
    print(json.dumps({k:v for k,v in row.items() if k not in ('certificate','recent_word')} | ({'period':row['certificate']['period'],'drift':row['certificate']['drift'],'growth':row['certificate']['growth']} if 'certificate' in row else {})),flush=True)
 out={'scope':'ONLY listed undecorated same-sector bilateral-wake poses; no arbitrary-cap or finite-seed classification','rows':rows}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
