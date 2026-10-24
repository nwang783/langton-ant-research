"""One exact shared-band overlap control for the permanent-output packing lemma."""
from pathlib import Path
import json
from check_return_permanent_output_debt import twenty,DXY,future
P=Path(__file__).parent
n=400;N=624*n-1516+983;J=set(range(-1000,0));w=len(J)
B={q:-i-1 for i,q in enumerate(sorted(twenty(n)))};p=(0,0);h=1
poses=[];born={};dead={};events=[]
for t in range(N):
    poses.append(p);old=B.pop(p,None);events.append((p,old))
    if old is None:B[p]=t;born[t]=p;h=(h+1)%4
    else:dead[old]=t;h=(h-1)%4
    p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
poses.append(p)
word,drift,tail,tests=future(B,p,h);dead.update({i:N+d for i,d in tail.items()})
L=[sum(i in dead for i in range(-20,0))];LJ=[sum(i in dead and q[0] in J for q,i in {q:-i-1 for i,q in enumerate(sorted(twenty(n)))}.items())];PJ=[0]
permanent=[]
for t,(q,old) in enumerate(events):
    change=(int(t in dead) if old is None else -1)
    L.append(L[-1]+change);LJ.append(LJ[-1]+change*int(q[0] in J))
    perm=old is None and t not in dead
    PJ.append(PJ[-1]+int(perm and q[0] in J))
    if perm and q[0] in J:permanent.append((t,q))
M=max(L);assert M==77<w

# Exact minimum-x range query, choosing the earliest minimizing cut.
size=1
while size<len(poses):size*=2
tree=[(10**100,N+1)]*(2*size)
for i,q in enumerate(poses):tree[size+i]=(q[0],i)
for i in range(size-1,0,-1):tree[i]=min(tree[2*i],tree[2*i+1])
def peak(a,d):
    a+=size;d+=size+1;ans=(10**100,N+1)
    while a<d:
        if a%2:ans=min(ans,tree[a]);a+=1
        if d%2:d-=1;ans=min(ans,tree[d])
        a//=2;d//=2
    return ans

selected=[];diff=[0]*(N+1)
for b,q in born.items():
    d=dead.get(b)
    if d is None or d>N or q[0]<0 or poses[b+1][0]<0:continue
    x,tau=peak(b+1,d)
    if x>=-1000:continue
    a=b+1;stock=LJ[a]+2*LJ[tau]+LJ[d];paid=PJ[d]-PJ[a]
    assert paid+stock>=4*w and paid>=4*(w-M)
    selected.append(dict(birth=b,death=d,cell=q,peak_cut=tau,peak_x=x,
                         band_relevant_at_three_cuts=[LJ[a],LJ[tau],LJ[d]],
                         permanent_band_births=paid,exact_stock_debt=stock))
    diff[a]+=1;diff[d]-=1
mult=[];a=0
for t in range(N):a+=diff[t];mult.append(a)
used=[(t,q) for t,q in permanent if mult[t]]
Q=max(mult[t] for t,q in permanent)
weighted=sum(mult[t] for t,q in permanent)
assert weighted==sum(r['permanent_band_births'] for r in selected)
assert Q<=M and 4*len(selected)*(w-M)<=weighted<=Q*len(used)<=M*len(used)
# A literal disjoint selection, with closed black-cut endpoints and half-open
# permanent-birth intervals [b+1,d). Equal endpoints do not double-charge.
disjoint=[];last=-1
for r in sorted(selected,key=lambda r:r['death']):
    if r['birth']+1>=last:disjoint.append(r);last=r['death']
assert sum(r['permanent_band_births'] for r in disjoint)<=len(used)
ys=[q[1] for t,q in used]
out=dict(status='AUTHOR bounded full-future control; independent audit pending',
         parameter=n,updates=N,band_columns=[-1000,-1],band_width=w,relevant_mass_cap=M,
         full_future_ray_tests=tests,selected_returns=selected,selected_count=len(selected),
         distinct_permanent_band_cells=len(used),permanent_output_y_range=[min(ys),max(ys)],
         summed_permanent_band_debt=weighted,exact_maximum_overlap=Q,
         lower_bound=4*len(selected)*(w-M),upper_bound=M*len(used),
         disjoint_selected_births=[r['birth'] for r in disjoint],
         scope='One literal shared-band control, not an all-parameter or recurrent-orbit claim.')
(P/'RETURN_BAND_PACKING_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='selected_returns'},indent=2))
