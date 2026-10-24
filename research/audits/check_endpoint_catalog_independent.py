"""Independent complete half-ray endpoint catalogue and all-future turn certificates."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
P=Path(__file__).resolve();ROOT=P.parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23'
layer=json.loads((R/'compute_exceptional_layer.json').read_text());pts={complex(*q)for q in layer['P']};cap={complex(*q)for q in layer['C']};d=-2-2j;dirs=(1j,1,-1j,-1)
source=P.with_name('check_exceptional_return_map_independent.py');ns={'__file__':str(source)}
exec(compile(source.read_text().split('author=json.loads')[0],str(source),'exec'),ns)
assert pts==ns['odd'] and cap==ns['cap']
base=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());H=base['word'];hh=base['heading'];p=-15+10j;reads=[];heads=[]
for c in H:
 reads.append(p);heads.append(hh);hh=(hh+(1 if c=='R'else-1))%4;p+=dirs[hh]
assert p==-17+8j and hh==base['heading']and len(H)==104
factor10={''.join(H[(i+j)%104]for j in range(10))for i in range(104)};assert len(factor10)==84
rotations={H[i:]+H[:i]for i in range(104)}
def xy(z):return(int(z.real),int(z.imag))
def old(z):
 x,y=xy(z);a=x%2;return(x-y,a),(a-x)//2
def along(q,s,f):
 dx,dy=xy(q-s);fx,fy=xy(f)
 if dx%fx or dy%fy:return None
 a,b=dx//fx,dy//fy
 return a if a==b else None
rclasses={old(z)[0]for z in reads};pclasses={old(z)[0]for z in pts};cclasses={old(z)[0]for z in cap}
lo=min(x-y for x,y in map(xy,cap))-max(x-y for x,y in map(xy,reads));hi=max(x-y for x,y in map(xy,cap))-min(x-y for x,y in map(xy,reads));assert(lo,hi)==(-64,84)
channels=[]
for delta in range(lo,hi+1):
 if delta%2:continue
 for a in(0,1):
  translated={(t+delta,(b+a)%2)for t,b in rclasses}
  if translated&pclasses or not translated&cclasses:continue
  channels.append((delta,a))
assert len(channels)==106
# For every class store the XOR thresholds of inclusive rays k<=b.
def background(channel):
 delta,a=channel;tr=complex(a,a-delta);rs=[q+tr for q in reads]
 hits=[(104*n+i,q,i)for q in cap for i,s in enumerate(rs)if(n:=along(q,s,d))is not None]
 tau,pos,phase=min(hits,key=lambda r:r[0]);assert sum(t==tau for t,_,_ in hits)==1
 rays=defaultdict(set)
 def flip(cl,k):rays[cl].symmetric_difference_update({k})
 for q in pts:cl,k=old(q);flip(cl,k-1)
 for i,q in enumerate(rs):cl,k=old(q);flip(cl,k+(tau-1-i)//104)
 return {cl:sorted(v)for cl,v in rays.items()if v},pos,heads[phase],tau,phase

def color(q,rays,finite):
 cl,k=old(q);return ((sum(k<=b for b in rays.get(cl,()))%2)==1)^(q in finite)

def certify(rays,finite,p,h,word):
 if word not in rotations:return False,0
 raw=[];qq=p;hh=h
 for j,c in enumerate(word):
  raw.append((qq,j,c));hh=(hh+(1 if c=='R'else-1))%4;qq+=dirs[hh]
 f=qq-p
 if hh!=h or f not in(d,-d,2-2j,-2+2j):return False,0
 fx,fy=xy(f);sg=fx//fy;groups=defaultdict(list)
 for q,j,c in raw:
  x,y=xy(q);cl=(x-sg*y,x%2);rep=complex(cl[1],sg*(cl[1]-cl[0]));k=along(q,rep,f);assert k is not None
  groups[cl].append((k,j,c,rep))
 checks=0
 for cl,gs in groups.items():
  # At physical level n, a phase k is present iff n>=k; chronological key is j-104k.
  gs.sort(key=lambda z:z[1]-104*z[0]);rep=gs[0][3];lower=min(k for k,_,_,_ in gs);crit={lower}
  def add(n):
   for z in(n-1,n,n+1):
    if z>=lower:crit.add(z)
  for k,_,_,_ in gs:add(k)
  if fx==fy:
   oc,kc=old(rep);slope=-fx//2
   for th in rays.get(oc,()):add((th-kc)//slope)
  else:
   t0=int(rep.real-rep.imag);stride=fx-fy
   for t,a in rays:
    if a!=int(rep.real)%2 or(t-t0)%stride:continue
    add((t-t0)//stride)
  for q in finite:
   n=along(q,rep,f)
   if n is not None:add(n)
  # Critical levels isolate every change in phase eligibility, background color, or finite XOR.
  for n in sorted(crit):
   active=[c for k,j,c,_ in gs if k<=n];assert active
   checks+=1
   if any(c==cc for c,cc in zip(active,active[1:])):return False,checks
   if color(rep+n*f,rays,finite)!=(active[0]=='L'):return False,checks
 return True,checks

reports=json.loads((R/'endpoint_catalog_results.json').read_text());supplied={tuple(row['channel']):row for row in reports['results']};assert set(supplied)==set(channels)
results=[];dirsout=Counter();checksall=0
for number,ch in enumerate(channels):
 rays,p,h,tau,phi=background(ch);word=H[phi:]+H[:phi]
 ok,nc=certify(rays,set(),p,h,word);assert ok
 bad=p+1000000*d;assert not certify(rays,{bad},p,h,word)[0]
 checksall+=nc
 row=supplied[ch];finite=set(cap);hist=''.join(H[(tau-10+j)%104]for j in range(10));prev=hist not in factor10;badcount=0;trace=''
 for t in range(row['entry']):
  c='L'if color(p,rays,finite)else'R';hist=(hist+c)[-10:];badnow=hist not in factor10;badcount+=prev and badnow;prev=badnow
  finite.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=dirs[h];trace+=c
 assert [list(xy(p)),h]==row['pose']and len(finite)==row['finite_XOR_mass']
 digest=hashlib.sha256(json.dumps(sorted(map(xy,finite)),separators=(',',':')).encode()).hexdigest();assert digest==row['finite_XOR_sha256']
 assert trace[-208:]==row['tail_word']*2
 ok,nc=certify(rays,finite,p,h,row['tail_word']);assert ok,(ch,'future')
 checksall+=nc
 # Retain the exact physical ten-read output seam.
 pp=p;hh=h;ff=set(finite)
 for t in range(10):
  c='L'if color(pp,rays,ff)else'R';assert c==row['tail_word'][t]
  hist=(hist+c)[-10:];badnow=hist not in factor10;badcount+=prev and badnow;prev=badnow
  ff.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=dirs[hh]
 assert badcount==row['K_total'];dirsout[tuple(row['drift'])]+=1
 results.append(dict(channel=ch,first_time=tau,phase=phi,capture_boundary=row['entry'],drift=row['drift'],K=badcount,whole_field_hash=digest,independent_critical_level_checks=nc))
 if(number+1)%20==0:print(number+1,'channels PASS',flush=True)
assert dirsout=={(-2,-2):58,(2,-2):44,(-2,2):1,(2,2):3}
assert [r['channel']for r in results if r['drift']==[2,2]]==[(-12,0),(26,0),(34,1)]
out=dict(status='PASS independent exhaustive channels, complete physical replay and all-future half-ray certificates',note_sha256=hashlib.sha256((R/'universal_endpoint_catalog.md').read_bytes()).hexdigest(),author_code_sha256=hashlib.sha256((R/'endpoint_catalog.py').read_bytes()).hexdigest(),channels=len(results),critical_checks=checksall,maximum_boundary=max(r['capture_boundary']for r in results),maximum_K=max(r['K']for r in results),output_counts={str(k):v for k,v in dirsout.items()},results=results,scope='Only the supplied universal endcap with causal incoming front and both backward persistent-string wakes. All finite XOR bits retained. Physical finite-family transfer also retains all three receding wake arms;103 nonbackward responses stabilize, three may hit the old inherited cap. No classification of that changed cap, finite-seed recurrence, global budget or universal capture.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='results'})
