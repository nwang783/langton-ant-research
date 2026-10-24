from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_detoured_collector_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Normalized exact dual corner patches')[0],ns)
P,C,conn,old,fixed=ns['build'](8);B=old|fixed;component,ends,wvertex,step,phys=[ns[x]for x in('component','ends','wvertex','step','phys')];p=1+1j;h=1;k=2
p,h,ch=step(B,p,h);assert ch=='L';marker=next(iter(fixed));mv=ends(marker,k)[0];archive=component(B,k,mv)[1];d=len(archive);assert archive==fixed and d==191
W=0;returns=0;maxpre=0;checks=[]
for i in range(1,len(P)-1):
 r=1+int((P[i+1]-P[i])/(P[i]-P[i-1])==1j);active0=component(B,k,wvertex(p,h))[1];assert marker not in active0
 arms=set();imported=False;oldarchive=set(archive)
 for _ in range(r):
  q=p;assert q not in B;arms.add(q);p,h,ch=step(B,p,h);assert ch=='R'
  if marker in component(B,k,wvertex(p,h))[1]:imported=True
 pre=component(B,k,wvertex(p,h))[1];maxpre=max(maxpre,len(pre));assert p in pre
 if imported:
  returns+=1;W+=r;assert oldarchive|arms<=pre and p not in oldarchive|arms and len(pre)>=d+W+1
 p,h,ch=step(B,p,h);assert ch=='L';archive=component(B,k,mv)[1];assert oldarchive<=archive and marker not in component(B,k,wvertex(p,h))[1]
 if imported:assert arms<=archive
 checks.append((r,imported,len(pre),len(archive)))
assert(returns,W,d,maxpre,len(archive),len(B))==(159,166,191,358,357,357)
D=ROOT/'active_w_archive_itinerary_2026-10-23';note=D/'ORDINARY_ARCHIVE_GROWTH.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='9a9dfcd0ce10d1adb91e7bdc5b133699aff6a01c7cf541ee01b279d5b5d957a8'
out={'status':'PASS protected full-archive growth within one proper ordinary epoch','note_sha256':sha,'independent_collector_control':{'q':8,'entry_mass':351,'first_post_L_archive':d,'temporary_returns':returns,'all_charged_R_arms':W,'last_pre_L_active_mass':maxpre,'final_archive_mass':len(archive),'equality':'358=191+166+1'},'all159_block_checks':checks,'analytic':['At any proper post-L restart, subsequent ordinary active fields are nested exact old far-side components. A different complete archive is disjoint from those fields. Future ordinary L edges all lie in the retained old active field, so none deletes any archive edge or any of its internal connecting paths. Complete post-L archive components containing a fixed marker are therefore monotone by actual edge-lifetime inclusion.','R can temporarily import the marker component at most once in a block because w is stationary and R never deactivates it. All R arms in that block share the departure cursor; after the bridge L, all remain with the imported archive on the departure side. If any reached the retained far side it would bypass the bridge, outside ordinary scope. This includes arms written BEFORE the particular importing R.','Ordinary newborn lifetimes are never consumed within the epoch, so every charged arm is a distinct lifetime and coordinate. k returning blocks contribute W=sum r>=k and protect at least d+W archive edges.','Immediately before the last returning block L, all those edges are ACTIVE together with its distinct old departing bridge. Thus any cap M at EVERY fine cut implies W<=max(0,M-d-1), and likewise k. If k=0 the inequality is trivial even when dormant d>M. A post-L-only cap would be insufficient.'],'scope':'One ordinary old-bridge epoch, or a proper post-L restart within it. No monotonicity across exceptional renewals, global return bound, original-root budget or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
