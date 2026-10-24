from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,importlib.util
R=Path('/workspace/shared/langton');H=Path('/workspace/shared/langton/old_D_third_age3_beta_loss_2026-10-24')
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS
J=json.load(open(R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json'))
C=json.load(open(R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json'))

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for t in w:h=(h+(1 if t=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h

def raw(t):return ''.join(W[a]for a in t)
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if u[0] else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return('parallel',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

angles=[r for r in J['all831_conditional_preFOREIGN_old_source_angle_interfaces']if r['old_source']=='D' and r['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']==3];rows=[];geos=[]
a,b=chord('D',(0,0,0));u=sub(b,a)
for ai,angle in enumerate(angles):
 n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=angle['total_ordinary_C_before_third'];b1,b2,b3=(angle[k]for k in['first','second','third']);hh=angle['third_heading_relative_old'];c,d=chord(b3,(0,0,hh));v=sub(d,c);den=det(u,v)
 corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)]
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:
    ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
    if not(0<=ss<1 and 0<tt<=1):continue
   else:
    if det(zz,u):continue
    k=0 if u[0] else 1;q,mul=Q(zz[k],u[k]),Q(v[k],u[k]);assert mul>0
    if q>=0:continue
    ss,tt=Q(0),-q/mul
    if not(0<tt<=1):continue
   p3=(x,y,hh);geos.append((ai,p3,ss,tt))
   for A in'FQB':
    ha=angle['true_FOREIGN_heading_relative_old'];delta=after(raw(A+b1+b2),(0,0,ha));pa=(x-delta[0],y-delta[1],ha);fcut=after(W['F'],pa);ep=after(W[A],pa);verts=[z(pa),z(fcut)]
    if A!='F':verts.append(z(ep))
    for bb in[b1,b2]:ep=after(W[bb],ep);verts.append(z(ep))
    assert ep==p3
    T=A+b1+b2+b3;tr=l.trace(raw(T)+l.M);early=any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:]));base='earlier_contact'if early else('local_immutable'if not tr['feasible']else'live')
    cases=[('DC',None)]+[('D',nextfull)for nextfull in('D','DC','V','VC','VCC','U','UC','UCC')]
    for full,nextfull in cases:
     facts={(2,0)};why=base;cuts=[]
     if n<=2:facts.add((1,-1))
     if full=='DC':
      if n<1:why='full_source_uncompleted'
      facts.update([(2,3),(3,1),(3,2)])
     else:
      if nextfull.count('C')>n:why='actual_next_full_uncompleted'
      if nextfull[0]=='D':facts.add((3,1))
      elif nextfull[0]=='V':facts.update([(1,1),(2,1),(3,2)])
      else:facts.update([(1,1),(1,2),(2,1),(2,2)])
     if why=='live':
      if full=='D'and nextfull[0]=='U':
       Actx=l.trace(W[A]+l.M)['first']
       if any(l.rot(sub(g,pa[:2]),-pa[2]) in Actx for g in[(1,1),(1,2),(2,1),(2,2)]):why='young_nextU_FOREIGN_star_effect'
      if why=='live':
       for g in facts:
        local=l.rot(sub(g,pa[:2]),-pa[2]);fr=tr['first'].get(local)
        if local in l.K or(fr and fr[0]=='R'):cuts.append(g)
       why='CURRENT_cut'if cuts else'NECESSARY'
     rows.append(dict(source=full,nextfull=nextfull,n=n,b1=b1,b2=b2,b3=b3,A=A,pa=pa,p3=p3,why=why,cuts=cuts))

# The previous atomic EXIT at selected-D clock zero supplies beta.
# Source D/DC never reads it. Every possible first loss is at clock three,
# in a completed plain E-oriented D/V/U, by signed atomic-exit maturity.
beta=(1,-1); common=(2,0); loss_ports=[]
for atom in 'DVU':
 geom=l.literal_geometry(W[atom]);trace=l.trace(W[atom]+l.M)
 for inp in map(tuple,geom['inputs']):
  pp=sub(beta,l.rot(inp,1));end=after(W[atom],(*pp,1));local_common=l.rot(sub(common,pp),-1)
  if(sum(pp)+1)%2:why='sector'
  elif list(local_common)in geom['inputs']:why='takes_held_source_common'
  elif atom=='D':
   assert z((*pp,1))==z((0,0,0));why='repeats_source_D_ENTRY'
  elif end==(1,-2,1):why='repeats_second_D_EXIT_before_third_ENTRY'
  else:
   assert(atom,inp,pp,end)==('U',(-1,2),(-1,-2),(3,-2,1))
   g=add(pp,l.rot((-1,1),1));assert g==(0,-1)
   why='deleted_source_core_cannot_fund_lower_a'
  loss_ports.append(dict(atom=atom,input=inp,head=(*pp,1),raw_exit=end,common_local=local_common,reason=why))
assert len(loss_ports)==8
assert Counter(p['reason']for p in loss_ports)==dict(sector=2,takes_held_source_common=2,repeats_source_D_ENTRY=1,repeats_second_D_EXIT_before_third_ENTRY=2,deleted_source_core_cannot_fund_lower_a=1)
# Source deletion is a real final L, not absence of an endpoint identity.
source_deletions=[]
for full in ('D','DC'):
 tr=l.trace(raw(full)+l.M);geom=l.literal_geometry(raw(full));g=(0,-1)
 assert tr['last'][g]==('L',3) and list(g)not in geom['outputs']
 assert g not in {add(tuple(geom['endpoint'][:2]),l.rot(k,geom['endpoint'][2]))for k in l.K}
 source_deletions.append(dict(source=full,cell=g,last_turn_tick0=tr['last'][g],in_full_O=False,in_exit_K=False))
# Every clock-zero full producer after the selected D starts N with head y>=1;
# all complete output local y are nonnegative, including every own C tail.
zero_clock_exports=[]
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 geom=l.literal_geometry(raw(full));assert min(p[1]for p in geom['outputs'])>=0
 zero_clock_exports.append(dict(full=full,outputs=geom['outputs'],minimum_output_y=min(p[1]for p in geom['outputs'])))
slot=json.load(open(R/'audits/dcuv_count5_replay/queries.json'))['slots']['7:(-1, 1)']
assert slot['certified_minimum_C_age']==3
remaining=[r for r in rows if r['why']=='NECESSARY'];assert len(remaining)==162
physical={}
for r in remaining:
 assert r['b2']=='D' and r['b3']in('D','C') and tuple(r['p3'])==(0,-1,3)
 k=(r['A'],tuple(r['pa']),r['b1'],r['b2'],r['b3']);physical[k]=r
 assert z(tuple(r['p3']))==z((1,-2,1))
 tr=l.trace(raw(r['A']+r['b1']+r['b2']+r['b3'])+l.M);q=l.rot(sub(beta,tuple(r['pa'][:2])),-r['pa'][2])
 assert tr['first'][q][0]=='R' and q not in l.K
 r['final_cut']='incoming_beta_first_loss_exhaustion'
 r['beta_first_required_turn_tick0']=tr['first'][q]
assert len(physical)==18 and len(rows)==1458
result=dict(scope='Only outgoing old D, true pre-FIRST-foreign age3, global first contact in THIRD ordinary RAW, genuine U-entry full G8 prefix, actual terminal M11. No foreign maturation or whole-tail simplicity.',angles=len(angles),outgoing_heads=len(geos),typed_rows=rows,initial_partition=dict(Counter(r['why']for r in rows)),first_beta_loss_ports=loss_ports,source_core_deletions=source_deletions,zero_clock_full_exports=zero_clock_exports,late_producer_lower_a_minimum=3,remaining_physical_targets=list(physical.values()),final='all 1458 genuine source/nextfull masks excluded')
(H/'D_third_age3_beta_loss.json').write_text(json.dumps(result,indent=2)+'\n')
print(dict(angles=len(angles),heads=len(geos),typed=len(rows),partition=result['initial_partition'],beta_ports=len(loss_ports),residual_types=len(remaining),residual_physical=len(physical),final=result['final']))
