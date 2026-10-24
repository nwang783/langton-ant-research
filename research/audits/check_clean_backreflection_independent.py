from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];S=SELF.with_name('check_changed_endpoint_catalog_independent.py');ns={'__file__':str(S)};exec(compile(S.read_text().split('results=[];nchecks=')[0],str(S),'exec'),ns)
H=ns['H'];dirs=(1j,1,-1j,-1);xy=ns['xy'];old=ns['old'];U=ROOT/'new_constructive_2026-10-23'
def tr(word,p,h):
 rows=[];start=p;hi=h
 for i,c in enumerate(word):rows.append((p,i,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return rows,p-start,h
base=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());rs,f,h=tr(H,0j,base['heading']);heads=[];hh=base['heading']
for c in H:heads.append(hh);hh=(hh+(1 if c=='R'else-1))%4
controls=[]
def sig(word,p,h):
 rows,f,eh=tr(word,p,h);assert eh==h and f in(2+2j,-2-2j);gs=defaultdict(list)
 for q,i,c in rows:
  x,y=xy(q);a=x%2;gs[(x-y,a)].append(((x-a)//int(f.real),i,c))
 for v in gs.values():
  v.sort(key=lambda z:z[1]-104*z[0]);assert v[0][2]=='R'and all(a[2]!=b[2]for a,b in zip(v,v[1:]))
 odd={cl for cl,v in gs.items()if len(v)%2};assert len(gs)==22 and len(odd)==12
 return set(gs),odd
for flip in(0,2):
 for j,(p,_,_)in enumerate(rs):
  if flip:p=-p
  A,B=sig(H[j:]+H[:j],p,(heads[j]+flip)%4);controls.append((flip,j,len(A),len(B)))
reports=[];final=[]
for first,second in[((-12,0),(26,0)),((26,0),(-12,0))]:
 rows,C=ns['make_changed'](first);oldP=set(rows);assert len(oldP)==48
 rr,p,h,tau,phi=ns['incoming'](rows,C,second);pin={cl for cl,v in rr.items()if len(v)%2};I=pin^oldP;assert len(I)==12 and not I&oldP
 rec=next(r for r in ns['capsup'][first]['results']if tuple(r['channel'])==second);F=set(C);p,h,_,word=ns['replay'](rr,F,p,h,rec['entry']);assert [list(xy(p)),h]==rec['pose'];ok,tests=ns['certify'](rr,F,p,h,rec['tail_word']);assert ok
 Rout,O=sig(rec['tail_word'],p,h);assert not Rout&pin
 rr={cl:set(v)for cl,v in rr.items()};trr,f,eh=tr(rec['tail_word'],p,h);assert f==2+2j
 for q,i,c in trr:
  cl,k=old(q);rr.setdefault(cl,set()).symmetric_difference_update({k})
 profile={cl for cl,v in rr.items()if len(v)%2};assert profile==oldP|I|O and len(profile)==72
 # Canonical threshold0 half-rays; evaluate finite XOR on every interval
 # between the complete old thresholds, rather than comparing capped crops.
 cap=set(F)
 for(t,a),v in rr.items():
  if not v:continue
  for k in range(min(min(v),0),max(max(v),0)+1):
   if(sum(k<=b for b in v)%2)^((t,a)in profile and k<=0):cap.symmetric_difference_update({complex(a-2*k,a-2*k-t)})
 blocked=[]
 for delta,a in[(-12,0),(26,0)]:
  hits={(t+delta,(b+a)%2)for t,b in ns['rclasses']}&profile;assert len(hits)>=12;blocked.append(len(hits))
 final.append((profile,cap));reports.append(dict(first=first,second=second,profile_counts=[48,60,72],cap_mass=len(cap),cap_sha256=hashlib.sha256(json.dumps(sorted(map(xy,cap)),separators=(',',':')).encode()).hexdigest(),blocked_counts=blocked,second_reaction_steps=rec['entry'],whole_future_checks=tests))
assert final[0]==final[1]
out=dict(status='PASS independent all-phase standard profile ingredients and exact two-order complete-field commutation',note_sha256=hashlib.sha256((U/'clean_backreflection_profile_growth.md').read_bytes()).hexdigest(),phase_controls=len(controls),reports=reports,full_cap_xor=0,scope='Analytic +24 applies only clean standard backreflections of finite NE-profile substrates with finite transients; no finite-original itinerary, widening upper bound or capture claim. The two supplied endpoint operations commute, not invert.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(reports)
