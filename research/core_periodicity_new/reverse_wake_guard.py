"""Exact mature standard-wake guards for time-reversed104 fronts."""
import json
from collections import Counter
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'recovered_bundle/ant_global/root/standard.json').read_text())
W=data['word'];h0=data['heading'];P=len(W)
def path(w,h):
 p=(0,0);qs=[]
 for a in w:
  qs.append(p);h=(h+(1 if a=='R' else -1))%4;d=D[h];p=(p[0]+d[0],p[1]+d[1])
 return qs,p,h
ps,d,h=path(W,h0);assert d==(-2,-2) and h==h0
# Quotient by the full period d: transverse coordinate x-y and x parity.
def key(p):return p[0]-p[1],p[0]%2
count=Counter(key(p) for p in ps);wake={k for k,n in count.items() if n%2}
V=''.join('L' if a=='R' else 'R' for a in W[::-1]);hr=(h0+2)%4
rs,dr,hh=path(V,hr);assert dr==(2,2) and hh==hr
# Reverse front's start at the exact incoming-edge reversal of the original endpoint.
q0=(d[0]-D[h0][0],d[1]-D[h0][1]);assert q0==ps[-1]
groups={}
for i,p in enumerate(rs):groups.setdefault(key(p),[]).append((i,p))
guard={}; spans={}
for k,lst in groups.items():
 # Point p=(parity,parity-transverse)+a*dr. At a remote point, first visit
 # maximizes a*P-i over the phases in this drift orbit.
 order=sorted(lst,key=lambda z:((z[1][0]-z[1][0]%2)//2)*P-z[0],reverse=True)
 assert all(V[order[j][0]]!=V[order[j+1][0]] for j in range(len(order)-1))
 guard[k]=(V[order[0][0]]=='L')
 spans[k]=max(p[0]//2 for _,p in lst)-min(p[0]//2 for _,p in lst)
required={k for k,b in guard.items() if b}
def shift_keys(ks,q):return {(t+q[0]-q[1],(a+q[0])%2) for t,a in ks}
assert shift_keys(required,q0)==wake
sigma_writer=(h0%2) # start cell parity0
# All relative translations are classified by transverse shift delta and x parity.
# q=q0+s: reversal sector is opposite writer; same-sector iff sx+sy odd,
# equivalently delta odd. Longitudinal changes by d preserve all guards.
trans=[t for t,a in wake]; lo=min(trans)-max(trans)-1;hi=max(trans)-min(trans)+1
rows=[]
for delta in range(lo,hi+1):
 for a in (0,1):
  shifted={(t+delta,(x+a)%2) for t,x in wake}
  missing=shifted-wake
  rows.append({'delta':delta,'x_parity':a,'same_sector':bool(delta%2),
               'missing_L_orbits':len(missing),'missing':sorted(missing)})
same=[r for r in rows if r['same_sector']]
best=min(r['missing_L_orbits'] for r in same)
allmatches=[r for r in rows if not r['missing_L_orbits']]
F={(W+W)[i:i+10] for i in range(P)}
vv=V*2;bad=[vv[i:i+10] not in F for i in range(P)]
K=sum(bad[i-1] and bad[i] for i in range(P))
out={'status':'exact orbit-class guard calculation; no general no-renewal theorem',
     'W':W,'V':V,'writer_heading':h0,'reverse_heading':hr,'drift':d,
     'q0':q0,'wake_black_orbits':sorted(wake),'reverse_required_L_orbits':sorted(required),
     'read_orbits':len(groups),'max_orbit_phase_span':max(spans.values()),
     'same_sector_min_missing_L_orbits':best,'same_sector_best_offsets':[r for r in same if r['missing_L_orbits']==best],
     'all_zero_missing_offsets':allmatches,'reverse_bad_windows_per104':sum(bad),'reverse_K_per104':K,
     'all_offset_rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('W','V','all_offset_rows','reverse_required_L_orbits')},indent=2))
