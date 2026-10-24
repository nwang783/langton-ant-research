#!/usr/bin/env python3
"""Full-field nonstandard translating-word certificate on an exact inherited endpoint."""
from pathlib import Path
from collections import defaultdict,Counter
import runpy,json,hashlib,time
ROOT=Path(__file__).parent;E=runpy.run_path(str(ROOT/'changed_endpoint_catalog.py'))
color=E['initial_color'];V=E['V'];along=E['along'];old_orbit=E['old_orbit'];toggle=E['toggle']

def cert_parallel(rows,F,p,h,word):
 slots=[];pp=p;hh=h
 for i,ch in enumerate(word):
  slots.append((pp,i,ch));hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 f=(pp[0]-p[0],pp[1]-p[1]);assert hh==h and f[0]==f[1] and f[0]!=0
 stride=abs(f[0]);assert stride%2==0
 groups=defaultdict(list)
 for q,i,ch in slots:
  x,y=q;t=x-y;a=x%stride;c=(a,a-t);k=(x-a)//f[0];assert q==(c[0]+k*f[0],c[1]+k*f[1]);groups[(t,a)].append((k,i,ch,c))
 checks=0;finite_boundary_checks=0;ray_critical_checks=0;index=defaultdict(list)
 for q in F:
  x,y=q;t=x-y;a=x%stride;c=(a,a-t);n=along(q,c,f);assert n is not None;index[(t,a)].append(n)
 for j,group in groups.items():
  group.sort(key=lambda z:(-z[0],z[1]));mn=min(z[0]for z in group);mx=max(z[0]for z in group);c=group[0][3]
  for a,b in zip(group,group[1:]):
   if a[2]==b[2]:return None
  for n in range(mn,mx):
   first=next(z for z in group if z[0]<=n);q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1;finite_boundary_checks+=1
   if color(q,rows,F)!=(first[2]=='L'):return None
  want=group[0][2]=='L';tests={mx};oj,kc=old_orbit(c);slope=-f[0]//2
  for th in rows.get(oj,()):
   # old orbit coordinate kc+slope*n crosses the threshold at this rational point.
   n=(th-kc)//slope
   for z in [n-1,n,n+1]:
    if z>=mx:tests.add(z)
  for n in index.get(j,()):
   for z in [n-1,n,n+1]:
    if z>=mx:tests.add(z)
  for n in tests:
   q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1;ray_critical_checks+=1
   if color(q,rows,F)!=want:return None
 return {'period':len(word),'drift':list(f),'read_orbits':len(groups),'finite_boundary_checks':finite_boundary_checks,'complete_ray_critical_checks':ray_critical_checks,'total_checks':checks,'read_t_hull':[min(q[0]-q[1]for q,i,ch in slots),max(q[0]-q[1]for q,i,ch in slots)]}

def main():
 node=json.loads((ROOT/'prepared_travelling_wave_input.json').read_text());rows={tuple(j):[0]for j in node['profiles']};cap={tuple(q)for q in node['cap']};rows,F,p,h,tau,phi=E['incoming'](rows,cap,(12,1));first_pose=[list(p),h];hist=''.join(E['H'][(tau-10+j)%104]for j in range(10));prefix=[];P=[];start=time.time()
 # Candidate begins83 steps after the exact first finite-cap read.
 for i in range(83):
  ch='L'if color(p,rows,F)else'R';prefix.append(ch);hist=(hist+ch)[-10:];toggle(F,p);h=(h+(-1 if ch=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 ff=set(F);pp=p;hh=h;word=''
 for i in range(1564):
  ch='L'if color(pp,rows,ff)else'R';word+=ch;toggle(ff,pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 cert=cert_parallel(rows,F,p,h,word);assert cert
 # Countercontrols on every read orbit: perturb a far, actually fresh ray cell.
 slots=[];pp=p;hh=h
 for i,ch in enumerate(word):
  slots.append((pp,i,ch));hh=(hh+(-1 if ch=='L'else 1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
 representatives={}
 for q,i,ch in slots:representatives.setdefault((q[0]-q[1],q[0]%14),q)
 rejected=0
 for q in representatives.values():
  far=(q[0]+14000000,q[1]+14000000);bad=set(F);toggle(bad,far);assert cert_parallel(rows,bad,p,h,word)is None;rejected+=1
 factors=E['FACTORS'];bad=[]
 for i in range(len(word)):
  ten=''.join(word[(i-9+j)%len(word)]for j in range(10));bad.append(ten not in factors)
 kperiod=sum(bad[i]and bad[(i-1)%len(word)]for i in range(len(word)))
 report={'scope':'Exact infinite prepared72-profile endpoint. Nonstandard travelling-wave certificate only; no finite original itinerary or noncapture claim.','node':node['state_sha256'],'channel':[12,1],'initial_cap_mass':len(cap),'entry_from_first_cap_read':83,'first_cap_read_pose':first_pose,'first_cap_read_global_index':tau,'wave_pose':[list(p),h],'finite_XOR_mass_at_wave':len(F),'finite_XOR_sha256':hashlib.sha256(json.dumps(sorted(F),separators=(',',':')).encode()).hexdigest(),'prefix_word':''.join(prefix),'word':word,'word_sha256':hashlib.sha256(word.encode()).hexdigest(),'certificate':cert,'bad_ten_per_period':sum(bad),'adjacent_K_per_period':kperiod,'primitive_word':all(word!=word[:m]*(len(word)//m)for m in range(1,len(word))if len(word)%m==0),'far_flip_rejections':rejected,'elapsed_seconds':time.time()-start}
 (ROOT/'prepared_travelling_wave_certificate.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k not in ['word','prefix_word']},indent=2),flush=True)
if __name__=='__main__':main()
