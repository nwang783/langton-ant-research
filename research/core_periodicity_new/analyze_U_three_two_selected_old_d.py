"""One fixed surviving static 3+2 support pattern; no path search.
U(-1,1,N) old d=(0,3) must retire while a,q,c survive, before
DC(-1,6,E) freshly installs its goal replacement. Exact finite clearers.
"""
from pathlib import Path
import json,collections
import analyze_U_three_plus_two_DC_fork_all_sources as X
W=Path(__file__).resolve().parent;G=X.G;IDS=X.IDS
P={(-1,1),(-1,2),(0,2)};cell=(0,3);source=(7,(-1,1),0);Q=(1,(-1,6),1);goal=(7,(0,0),0)
def end(a,p,h):
 e=G[a]['endpoint'];return(*X.add(p,X.rot(e[:2],h)),(h+e[2])%4)
def allowed_adj(A,B,left,right):
 # Every closed intersection must be just the common endpoint of adjacent
 # full packets. Noncollinear segments are tested conservatively here.
 u=X.sub(A[1],A[0]);v=X.sub(B[1],B[0])
 return A[1]==B[0] and A[1]==left and A[1]==right and X.cross(u,v)!=0
rows=[]
for a in IDS:
 for h in range(4):
  for si,i in enumerate(G[a]['inputs']):
   p=X.sub(cell,X.rot(i,h));r=dict(packet=a,pose=[*p,h],input_slot=si)
   if(sum(p)+h)%2:r['reason']='sector'
   elif X.ctx(a,p,h)&P:r.update(reason='protected_context',hits=sorted(X.ctx(a,p,h)&P))
   else:
    C=X.chords(a,p,h);r['source_contacts']=[(i,j)for i,A in enumerate(X.chords(*source))for j,B in enumerate(C)if X.contact(A,B)];r['goal_contacts']=[(i,j)for i,A in enumerate(C)for j,B in enumerate(X.chords(*goal))if X.contact(A,B)];r['Q_contacts']=[(i,j)for i,A in enumerate(C)for j,B in enumerate(X.chords(*Q))if X.contact(A,B)]
    r['source_adjacent_possible']=(*p,h)==end(*source);r['Q_adjacent_possible']=end(a,p,h)==(*Q[1],Q[2])
    if r['goal_contacts']:r['reason']='goal_contact'
    elif r['source_contacts']and not r['source_adjacent_possible']:r['reason']='source_nonadjacent_contact'
    elif r['Q_contacts']and not r['Q_adjacent_possible']:r['reason']='Q_nonadjacent_contact'
    else:r['reason']='static_clearer_not_actual_history'
   rows.append(r)
counts=dict(collections.Counter(r['reason']for r in rows));R=dict(status='ONE_STATIC_COHORT_FIRST_CLEARER_QUERY_NOT_EXCLUSION',scope=__doc__,counts=counts,rows=rows);(W/'chronology_dcuv/U_three_two_selected_old_d.json').write_text(json.dumps(R,indent=2)+'\n');print(json.dumps(counts,indent=2));print(json.dumps([r for r in rows if r['reason']=='static_clearer_not_actual_history'],indent=2))
