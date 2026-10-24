from pathlib import Path
from fractions import Fraction
import math,json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'C_DISCOVERY_EXCURSION_TRIANGULAR_WINDING.md';F=D/'C_excursion_triangular_winding_certificate.json'
assert sha(P)=='d6407a02283e4f22232977f2a278c81ebb15429237fbee4c748a6ea6b1ea3961'and sha(F)=='591a616b670d0410cd4baf821e8734a4f4ffd3e9b6c1e6a59657c3c3a95ad2df';assert sha(D/'certify_C_excursion_triangular_winding.py').startswith('1add89c5')
J=json.loads(F.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
q=S.with_name('check_active_C_entry_exit_independent.py');src=q.read_text().split('base={};summary={}')[0].replace(' return sig',' return dict(E=E,d=d,n=n,ev=ev,rep=rep,face=face,H=H,F=F,starts=starts,fw=fw,cycles=cycs[1])');ns={'__file__':str(q)};exec(src,ns);analyze=ns['analyze'];xy=ns['xy'];off=ns['off']
base=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']
def winding(poly,u):
 cx=2*u.real+1;cy=2*u.imag+1;v=0
 for a,b in zip(poly,poly[1:]):
  if a.real!=b.real or 2*a.real>=cx:continue
  if 2*a.imag<cy<2*b.imag:v+=1
  if 2*b.imag<cy<2*a.imag:v-=1
 return v
def reconstruct(w,h0,author):
 a=analyze(w,h0);P=a['n'];d=a['d'];rep=a['rep'];ev=a['ev'];starts=a['starts'];fw=a['fw'];results=[]
 assert len(author)==len(a['cycles'])
 for classes,vol,gap in a['cycles']:
  inv={complex(*fw[c]['target']):c for c in classes};u=min(classes,key=lambda q:(q.real,q.imag));initial=u;faces=[];first=[];exc=[]
  for j in range(len(classes)):
   faces.append(u);q,k=rep(u);first.append(starts[q]+k*P);v=inv[q];edge=fw[v];child=v+(k-edge['voltage'])*d
   lt=starts[v]+(k-edge['voltage'])*P-1;root,hh,turn,phase=ev(lt);rc,rk=rep(root);hist=a['H'][rc];rt=hist[0][0]+rk*P
   assert hist[0][1]['c']=='R'and hist[1][0]+rk*P==lt and ev(rt)[:2]==(root,hh)and turn=='L'
   assert rt>=first[-1]and rt<lt and a['face'](rt)==u and a['face'](lt+1)==child
   event=[ev(t)for t in range(rt,lt)];poly=[z[0]for z in event]+[root];assert poly[0]==poly[-1]and all(z!=root for z in poly[1:-1])
   box=[(min(z.real for z in poly),max(z.real for z in poly)),(min(z.imag for z in poly),max(z.imag for z in poly))]
   exc.append(dict(parent=u,child=child,rt=rt,lt=lt,word=''.join(z[2]for z in event),poly=poly,box=box,active={z[0]+off[z[1]]for z in event}));u=child
  m=len(classes);assert u==initial+d and first==sorted(first)and first[-1]<first[0]+P
  au=next(z for z in author if z['cycle_parent_vertices']==[xy(v)for v in faces]);matrix=[[0]*m for _ in range(m)]
  assert au['first_activation_times']==first and au['full_drift']==xy(d)
  for i,e in enumerate(exc):
   entries=[]
   for j,v in enumerate(faces):
    lo=None;hi=None;empty=False
    for axis in range(2):
     vv=int(v.real if axis==0 else v.imag);dd=int(d.real if axis==0 else d.imag);lower,upper=e['box'][axis]
     if dd==0:
      if not 2*lower<=2*vv+1<=2*upper:empty=True
     else:
      bounds=sorted([Fraction(int(2*lower)-(2*vv+1),2*dd),Fraction(int(2*upper)-(2*vv+1),2*dd)]);ll=math.ceil(bounds[0]);hh=math.floor(bounds[1]);lo=ll if lo is None else max(lo,ll);hi=hh if hi is None else min(hi,hh)
    if empty:continue
    assert lo is not None and hi is not None
    for k in range(lo,hi+1):
     point=v+k*d;idx=j+k*m;wind=winding(e['poly'],point);t=first[j]+k*P
     if idx>i:assert point not in e['active']and t>e['lt']and wind==0
     if idx==i:assert wind==1
     entries.append(dict(spine_index=idx,relative_index=idx-i,face=xy(point),winding=wind,first_activation=t));matrix[j][i]+=wind
   entries.sort(key=lambda z:z['spine_index']);ae=au['excursions'][i]
   assert ae['R_time']==e['rt']and ae['L_time']==e['lt']and ae['length']==e['lt']-e['rt']and ae['parent']==xy(e['parent'])and ae['child']==xy(e['child'])
   if 'poly'in ae:assert ae['poly']==[xy(z)for z in e['poly']]and ae['word']==e['word']
   assert entries==ae['all_spine_faces_in_geometric_box']
   assert [[z['relative_index'],z['winding']]for z in entries if z['winding']]==ae['nonzero_relative_coefficients']
   assert winding(e['poly'],e['parent'])==1 and winding(e['poly'],e['child'])==0
  assert matrix==au['period_aliased_winding_matrix'];results.append(dict(parent_faces=[xy(v)for v in faces],lengths=[e['lt']-e['rt']for e in exc],matrix=matrix))
 return results
controls={}
for name,z in base.items():controls[name]=reconstruct(z['word'],z['initial_heading'],J['base_controls'][name])
for z in J['representation_controls']:
 w=base[z['name']]['word']
 if 'phase'in z:w=w[z['phase']:]+w[:z['phase']];h=0
 else:w*=z['power'];h=z['heading']
 reconstruct(w,h,z['cycles'])
assert len(J['representation_controls'])==40
O=dict(status='PASS all-cap lifted C-discovery excursion triangular winding ONLY',proof=sha(P),certificate=sha(F),script=sha(S),controls=controls,representation_controls=40,analytic_review=['Use the signed embedded FULL-d WHITE-owned discovery cycle and its actual chronological lifts, not projected lifetime planarity. Every later selected face is unactivated during E_i. At a shared C-edge read vertex any actual allowed-axis visit activates one of the two endpoints; hence every future spine-edge vertex is unread during E_i. The proper future diagonal half-ray meets unit grid paths only at those vertices, so lies in the complement and connects every later face to infinity. Its winding is zero.','The root between parent and child is visited only at firstR and the endpoint firstL, with identical incoming heading. The closed polygon uses exactly the clockwise R corner there. The two adjacent C-face winding values differ by+1 on the active parent side; future child has zero, hence parent+1. Repeated edges or self-intersections elsewhere do not affect this local current identity.','For finite linear combinations, the greatest nonzero excursion index sees only its own diagonal+1, proving independence. This does not apply to infinite periodic sums or period-aliased matrices. No physical deletion/surgery or fuel payment follows.','Independent full-class active-C reconstruction supplies every lift and first activation; a left-ray winding sum independently checks every geometric-box face and all40 representations. Standard E92 has older indices-3,-2 each-1 and singular aliased matrix. Prepared10 satisfies the same triangular law while retaining its real input.'],scope='Only a selected actual WHITE-owned C-entry cycle; arbitrary read cap/period. Future ray unread only during the excursion, not a permanently unread outer row. No positivity of old coefficients, bounded backward support, finite alphabet, input detector, WHITE S1 or controller/global attraction theorem.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
