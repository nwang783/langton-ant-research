"""Independent literal full-output and CRT common-period matrix for the two signed waves."""
from pathlib import Path
from collections import defaultdict
from math import lcm
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23';V=(1j,1,-1j,-1);data={};sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for period,nfile,cfile,key in [(1564,'prepared_wave_five_band_normal_form.json','prepared_travelling_wave_certificate.json','full_black_orbit_profiles'),(4352,'three_standard_band_wave_normal_form.json','second_prepared_wave_certificate.json','full_black_profiles')]:
 N=json.loads((R/nfile).read_text());C=json.loads((R/cfile).read_text());word=C['word'];assert len(word)==period;p=complex(*N['pose'][0]);h=N['pose'][1];start=p;heading=h;s=N['drift'][0];groups=defaultdict(list)
 for i,c in enumerate(word):
  x,y=int(p.real),int(p.imag);a=x%s;k=(x-a)//s;groups[x-y,a].append((i-period*k,k,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 assert p-start==s*(1+1j)and h==heading
 source={(t,a)for t,b in N[key]for a in range(s)if a%2==b};out=set(source);need={};maxspan=0
 for orbit,slots in groups.items():
  slots.sort();assert all(a[2]!=b[2]for a,b in zip(slots,slots[1:]));need[orbit]=slots[0][2]=='L';assert (orbit in source)==need[orbit]
  maxspan=max(maxspan,max(k for _,k,_ in slots)-min(k for _,k,_ in slots))
  if len(slots)%2:out.symmetric_difference_update({orbit})
  assert (orbit in out)==(slots[-1][2]=='R')
 assert maxspan==1
 data[period]=dict(stride=s,need=need,source=source,output=out,read=set(groups),span=maxspan,black_normals={t for(t,a),b in need.items()if b})
expected={1564:(420,223,301,524),4352:(468,62,590,652)}
for period,d in data.items():assert (len(d['source']),len(d['source']-d['read']),len(d['output']&d['read']),len(d['output']))==expected[period]
rows=[]
for source,S in data.items():
 for target,C in data.items():
  common=lcm(S['stride'],C['stride']);L=common//C['stride'];g=S['stride']//L
  loout=min(t for t,a in S['output']);hiout=max(t for t,a in S['output'])
  for sign in (1,-1):
   lo=loout-min(sign*t for t in C['black_normals']);hi=hiout-max(sign*t for t in C['black_normals']);alignments=[]
   for normalshift in range(lo,hi+1):
    if normalshift%2:continue
    for xshift in range(g):
     mismatches=[]
     for (t,a),want in sorted(C['need'].items()):
      tt=sign*t+normalshift;bad=[]
      for copy in range(L):
       xx=sign*(a+C['stride']*copy)+xshift
       if ((tt,xx%S['stride'])in S['output'])!=want:bad.append(copy)
      if bad:mismatches.append(((t,a),want,bad))
     assert mismatches
     alignments.append(dict(normalshift=normalshift,xshift=xshift,wrong_classes=len(mismatches),wrong_physical_colors=sum(len(z[2])for z in mismatches),witness=mismatches[0]))
   rows.append(dict(source=source,target=target,halfturn=sign==-1,normal_interval=[lo,hi],alignments=len(alignments),background_copies=L,min_wrong_classes=min((x['wrong_classes']for x in alignments),default=None),min_wrong_colors=min((x['wrong_physical_colors']for x in alignments),default=None),details=alignments))
assert [(x['alignments'],x['min_wrong_classes'],x['min_wrong_colors'])for x in rows]==[(154,159,159),(154,180,180),(46,946,3065),(46,963,3280),(0,None,None),(0,None,None),(234,479,479),(234,478,478)]
# Match COMPLETE output profiles, not merely the consumer read-support output.
author=json.loads((R/'prepared_wave_bulk_transition_matrix.json').read_text())
for period,d in data.items():assert set(map(tuple,author['waves'][str(period)]['complete_output_profiles']))==d['output']
out=dict(status='PASS independent two-wave complete mature bulk and all-translation common-period obstruction',note_sha256=sha(R/'prepared_wave_complete_output_nonrenewal.md'),waves={p:dict(stride=d['stride'],read_classes=len(d['read']),input_black=len(d['source']),untouched_black=len(d['source']-d['read']),complete_output_black=len(d['output']),complete_output_profiles=sorted(d['output']))for p,d in data.items()},matrix=rows,phase_argument='At physical cyclic phase s each shifted slot key i-P*k changes by the common -s, including wrapped slots; full ordered colors therefore do not change.',repair_bound='A*floor(max(0,n-Delta)/L) initial XOR edits, from n-Delta complete-list physical cells per orbit.',scope='Only the two supplied words on unchanged mature outputs up to finite XOR cap. No arbitrary consumer, endpoint routing, or original-mass resource claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print([(x['source'],x['target'],x['halfturn'],x['alignments'],x['min_wrong_classes'],x['min_wrong_colors'])for x in rows])
