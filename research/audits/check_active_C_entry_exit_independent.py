from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md';Jf=D/'active_C_entry_exit_forests_certificate.json';assert sha(P).startswith('1ae8a8e5')and sha(Jf).startswith('e192b487')and sha(D/'certify_active_C_entry_exit_forests.py').startswith('a82f1fb5');J=json.loads(Jf.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];key=lambda p:(p.real,p.imag);off=[-1j,-1-1j,-1,0j]
def analyze(w,h0=0,author=None):
 n=len(w);p=0j;h=h0;E=[]
 for i,c in enumerate(w):
  hi=h;h=(h+(1 if c=='R'else -1))%4;E.append(dict(t=i,p=p,hi=hi,ho=h,c=c));p+=V[h]
 d=p;assert h==h0 and d and int(d.real+d.imag)%2==0
 axis=0 if d.real else 1;dd=int(d.real if axis==0 else d.imag)
 def rep(p):
  coord=int(p.real if axis==0 else p.imag);k=coord//abs(dd)*(1 if dd>0 else-1);return p-k*d,k
 def ev(t):
  k,i=divmod(t,n);e=E[i];return e['p']+k*d,e['hi'],e['c'],i
 def face(t):
  p,h,c,i=ev(t);return p+off[h]
 H=defaultdict(list);F=defaultdict(list)
 for e in E:
  q,k=rep(e['p']);H[q].append((e['t']-k*n,e));q,k=rep(e['p']+off[e['hi']]);F[q].append((e['t']-k*n,e['t']))
 for a in(H,F):
  for q,ls in a.items():ls.sort()
 for q,ls in H.items():assert all(a[1]['c']!=b[1]['c']for a,b in zip(ls,ls[1:]))
 assert len({int(q.real+q.imag)%2 for q in F})==1
 starts={q:ls[0][0]for q,ls in F.items()};ends={q:ls[-1][0]for q,ls in F.items()};graphs=[{},{}]
 for q in F:
  for which in range(2):
   t=starts[q]-1 if which==0 else ends[q];p,hh,c,i=ev(t);assert c=='L';assert face(t+1 if which==0 else t)==q;u=face(t if which==0 else t+1);target,nu=rep(u);assert target in F;rc,k=rep(p);ls=H[rc];r=next(j for j,(tt,e)in enumerate(ls)if tt==t-k*n);assert abs((u-q).real)==abs((u-q).imag)==1
   assert p==(q+u+1+1j)/2
   edge=dict(source=xy(q),target=xy(target),voltage=nu,L_phase=i,L_rank=r,read_class=xy(rc))
   if which==0:
    gap=starts[q]-starts[target]-nu*n;assert gap>=1;white=ls[0][1]['c']=='R';assert r==(1 if white else 0);edge.update(WHITE_first=white,clock_gap=gap)
    if white:
     age=ls[1][0]-ls[0][0];assert ls[0][1]['hi']==hh and age>=4 and age%4==0 and gap>=age+1;edge.update(R_owner_phase=ls[0][1]['t'],R_to_L_age=age,idle_before_owner=gap-age-1)
   else:
    gap=ends[target]+nu*n-ends[q];assert gap>=1;ll=max(j for j,(_,e)in enumerate(ls)if e['c']=='L');assert r==ll;endsR=ls[-1][1]['c']=='R';edge.update(ends_R=endsR,clock_gap=gap)
    if endsR:
     age=ls[-1][0]-ls[r][0];assert r==len(ls)-2 and(ls[-1][1]['hi']-hh)%4==2 and age>=4 and age%4==0 and gap>=age;edge.update(final_R_phase=ls[-1][1]['t'],L_to_R_gap=age,idle_after_final_R=gap-age)
   graphs[which][q]=edge
 for G in graphs:assert len({tuple(e['read_class'])for e in G.values()})==len(G)
 def cycles(G):
  remain=set(G);out=[]
  while remain:
   path=[];at={};u=next(iter(remain))
   while u in remain and u not in at:at[u]=len(path);path.append(u);u=complex(*G[u]['target'])
   if u in at:
    cyc=path[at[u]:];out.append((frozenset(cyc),sum(G[v]['voltage']for v in cyc),sum(G[v]['clock_gap']for v in cyc)))
   remain.difference_update(path)
  return out
 fw={q:e for q,e in graphs[0].items()if e['WHITE_first']};cycs=[cycles(graphs[0]),cycles(fw),cycles(graphs[1])];assert cycs[0]and cycs[2]
 for j,ls in enumerate(cycs):
  for cc,v,gap in ls:
   assert v==(-1 if j<2 else 1)and gap==n
   if j==1:assert n>=5*len(cc)
   if j==2:assert n>=len(cc)+3*sum(graphs[1][q]['ends_R']for q in cc)
 inputs=[q for q,ls in H.items()if ls[0][1]['c']=='L'];outputs=[q for q,ls in H.items()if ls[-1][1]['c']=='R'];blackentry=[e['L_phase']for e in graphs[0].values()if not e['WHITE_first']];hidden=sorted(H[q][0][1]['t']for q in inputs if H[q][0][1]['t']not in blackentry)
 sig=(len(F),len(inputs),len(outputs),len(blackentry),*[len(a)for a in cycs]);assert inputs or(len(fw)==len(F)and cycs[1])
 if author:
  assert author['drift']==xy(d)and author['initial_heading']==h0 and author['period']==n
  readrows=[]
  for q,ls in sorted(H.items(),key=lambda z:key(z[0])):readrows.append(dict(**{'class':xy(q)},reads=[dict(canonical_time=t,**{**e,'p':xy(e['p'])})for t,e in ls]))
  assert readrows==author['read_histories']
  facrows=[dict(**{'class':xy(q)},first_time=starts[q],last_time=ends[q],visits=[dict(canonical_time=t,phase=i)for t,i in ls])for q,ls in sorted(F.items(),key=lambda z:key(z[0]))];assert facrows==author['C_face_histories']
  for G,title in[(graphs[0],'first_entry_edges'),(fw,'WHITE_first_entry_edges'),(graphs[1],'last_exit_edges')]:assert [v for q,v in sorted(G.items(),key=lambda z:key(z[0]))]==author[title]
  for cs,title in zip(cycs,['first_entry_cycles','WHITE_first_entry_cycles','last_exit_cycles']):
   other={(frozenset(complex(*q)for q in r['vertices']),r['winding'],r['sum_clock_gaps'])for r in author[title]};assert set(cs)==other
  assert hidden==author['other_BLACK_input_phases']and sorted(blackentry)==author['first_input_entry_phases']
 return sig
base={};summary={}
for name,z in J['base_controls'].items():
 w=z['word'];s=analyze(w,author=z);base[name]=w;summary[name]=s
for r in J['representation_controls']:
 w=base[r['name']]
 if 'phase_rotation'in r:k=r['phase_rotation'];s=analyze(w[k:]+w[:k])
 else:s=analyze(w*r['power'],r['heading'])
 assert list(s)==r['summary']
assert len(J['representation_controls'])==105 and summary['S104']==(10,0,12,0,2,2,2)and summary['M10']==(2,1,1,0,1,1,1)
O={'status':'PASS all-cap physical active-C first-entry/last-exit ownership scaffold ONLY','proof':sha(P),'certificate':sha(Jf),'script':sha(S),'summaries':summary,'representation_controls':105,'analytic_review':['Every physicalCface has finitelymany activecuts under nonzerodrift, and there are finitelymany FULLd classes. Its earliestcut has a precedingL; everyL atthat readcell activatesboth incidentCfaces, so thismustbethe firstL. WHITE firstL isrank1 with R0 atsameheading, otherwiseR0alreadyactivatedthe newface. BLACK firstL isrank0 andremainsan explicitinputedge. The clockgap is1+ownedage+idle>=5 or>=1.','At the lastactivecut the stepmustL, anditis the lastL ofits physicalreadcell. An endingR isthen the immediatelynextcellread and mustbeoppositeheading, oritwouldreactivatethe oldface. Thus its actualRownerliesinthe targetCface and suppliesgap>=age>=4; endingL suppliesgap>=1. No cap or initialWHITE restriction isneeded here.','Both physical selected-edge graphs lie on ONE checkerparity rotatedsquarelattice. Diagonal edges canonlycross an edgeof the oppositeparity lattice, absenthere. A readcell has onlyonefirstL/lastL, so its physicaledgeorbit cannotbe selectedtwice within eithergraph. This rulesout doubled/reversed edgealiasing even for loop/parallel-edge quotients. A functionalcycle usesdistinctfaceclasses and isthereforean embedded cylinder curve, not merelya projected lifetimepath.','Positive canonical gaps telescope to -Psumvoltage forfirstentry and +Psumvoltage forlastexit. Contractiblecyclesare impossible. Embeddedessentialcircles onthe FULLd cylinder have primitivewinding, hence exactly-1/+1, retaining nonprimitive physicaldrifts and shortquotients. This topological argument isseparatefrom finitecontrols.','Removing onlyBLACK-first discoveryedges leavesa partialfunctionalgraph with rootedtrees andpossibly intactWHITE-ownedcycles. CompleteWHITE removesnone, so finitefunctionalgraph forcesatleastone sameheadingR0/L1 essentialcycle, but imposesno readcap or singleusededge. Allcycleclockboundsfollowfromthe exact gaps.','Independently rebuilt allcomplete readandCface histories, everyphysicalowner, seams, arrowsandcycles forfive suppliedwords, thenall105 rotation/power/phasecontrols. Prepared10 hasgenuineBLACK inputL5 but noBLACK discoveryedge, so WHITE-owneddiscoverycycle isnot equivalentto aWHITE front orunit lifetimewinding. Standardhas two cyclesandactualhighreadhistories. No rootbudget, WHITE S1, controllerclassification, noveltyclaim oruniversalcapture follows.']}
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
