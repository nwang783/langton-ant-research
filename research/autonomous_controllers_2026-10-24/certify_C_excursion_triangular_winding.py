#!/usr/bin/env python3
"""Finite lifted discovery-excursion winding, without any visit/period cap."""
from pathlib import Path
from fractions import Fraction
import json, hashlib, math
from certify_active_C_entry_exit_forests import analyze, active_C
from check_extremal_read_coupling import event_word, quotient
R=Path(__file__).resolve().parent

def occ(E,d,t):
 P=len(E);e=dict(E[t%P]);q=t//P;e['t']=t;e['p']=(e['p'][0]+q*d[0],e['p'][1]+q*d[1]);return e

def winding(poly,u):
 cx,cy=2*u[0]+1,2*u[1]+1
 return sum((1 if b[1]<a[1] else -1) for a,b in zip(poly,poly[1:])
  if a[0]==b[0] and 2*a[0]>cx and min(2*a[1],2*b[1])<cy<max(2*a[1],2*b[1]))

def face_lifts_in_box(u,d,box):
 lo=hi=None
 for axis in range(2):
  a=2*box[axis][0]-(2*u[axis]+1);b=2*box[axis][1]-(2*u[axis]+1);v=2*d[axis]
  if not v:
   if not a<=0<=b:return []
   continue
  q1,q2=sorted([Fraction(a,v),Fraction(b,v)])
  l=math.ceil(q1);h=math.floor(q2);lo=l if lo is None else max(lo,l);hi=h if hi is None else min(hi,h)
 assert lo is not None
 return range(lo,hi+1)

def control(z,details=False):
 w=z['word'];P=len(w);E,d,h=event_word(w,h=z['initial_heading']);d=tuple(d)
 first={tuple(x['class']):x['first_time'] for x in z['C_face_histories']}
 F={tuple(x['source']):x for x in z['WHITE_first_entry_edges']}
 out=[]
 for cy in z['WHITE_first_entry_cycles']:
  vs={tuple(v) for v in cy['vertices']};inv={tuple(F[v]['target']):(v,F[v]) for v in vs};assert len(inv)==len(vs)
  u=min(vs);start=u;faces=[];ex=[];first_times=[]
  for j in range(len(vs)):
   faces.append(u);q,k=quotient(u,d);first_times.append(first[q]+k*P)
   childq,e=inv[q];nu=e['voltage'];child=(childq[0]+(k-nu)*d[0],childq[1]+(k-nu)*d[1])
   l0=E[e['L_phase']];lC=active_C(l0['p'],l0['hi']);lq,lk=quotient(lC,d);assert lq==q
   lt=e['L_phase']+(k-lk)*P;rt=lt-e['R_to_L_age'];ee=[occ(E,d,t) for t in range(rt,lt)]
   root=ee[0];end=occ(E,d,lt);after=occ(E,d,lt+1)
   assert root['p']==end['p'] and root['hi']==end['hi'] and root['c']=='R' and end['c']=='L'
   assert all(x['p']!=root['p'] for x in ee[1:])
   assert active_C(root['p'],root['hi'])==u and active_C(after['p'],after['hi'])==child
   assert first[childq]+(k-nu)*P==lt+1
   assert first_times[-1]<=rt<lt+1
   poly=[x['p'] for x in ee]+[root['p']];box=[(min(p[a] for p in poly),max(p[a] for p in poly)) for a in range(2)]
   ex.append({'parent_index':j,'parent':u,'child':child,'R_time':rt,'L_time':lt,'length':lt-rt,'word':''.join(e['c'] for e in ee),'box':box,'events':ee,'poly':poly})
   u=child
  m=len(vs);assert u==(start[0]+d[0],start[1]+d[1]);assert all(a<b for a,b in zip(first_times,first_times[1:]));assert first_times[-1]<first_times[0]+P
  M=[[0]*m for _ in range(m)]
  for x in ex:
   j=x['parent_index'];actual_C={active_C(e['p'],e['hi']) for e in x['events']};entries=[]
   for a,v in enumerate(faces):
    for k in face_lifts_in_box(v,d,x['box']):
     idx=a+k*m;vf=(v[0]+k*d[0],v[1]+k*d[1]);ww=winding(x['poly'],vf)
     if idx>j:
      assert vf not in actual_C and first_times[a]+k*P>x['L_time']
      assert ww==0
     if idx==j:assert ww==1
     entries.append({'spine_index':idx,'relative_index':idx-j,'face':vf,'winding':ww,'first_activation':first_times[a]+k*P})
     M[a][j]+=ww
   assert winding(x['poly'],x['parent'])==1 and winding(x['poly'],x['child'])==0
   x['all_spine_faces_in_geometric_box']=sorted(entries,key=lambda a:a['spine_index'])
   x['nonzero_relative_coefficients']=[[a['relative_index'],a['winding']] for a in x['all_spine_faces_in_geometric_box'] if a['winding']]
   if not details:x.pop('events');x.pop('poly');x.pop('word')
  out.append({'cycle_parent_vertices':faces,'first_activation_times':first_times,'full_drift':d,'period':P,'excursions':ex,'period_aliased_winding_matrix':M,'matrix_rows_are_face_types_columns_are_excursion_types':True})
 return out

def main():
 base=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']
 bb={n:control(z,True) for n,z in base.items()}
 assert len(bb['S104'])==2 and len(bb['M10'])==1 and all(not bb[n] for n in ['P1564','Q4352','F80'])
 controls=[]
 for n in ['S104','M10']:
  w=base[n]['word']
  for h in range(4):
   for q in [1,2,3,5]:
    cc=control(analyze(w*q,h));controls.append({'name':n,'heading':h,'power':q,'cycles':cc})
  for phase in sorted({1,len(w)//3,len(w)//2,len(w)-1}):
   cc=control(analyze(w[phase:]+w[:phase]));controls.append({'name':n,'phase':phase,'cycles':cc})
 neg=[]
 for cy in bb['S104']:
  for e in cy['excursions']:
   if e['length']==92:
    neg=[a for a in e['all_spine_faces_in_geometric_box'] if a['winding']<0]
    assert [(a['relative_index'],a['winding']) for a in neg]==[(-3,-1),(-2,-1)]
    assert sorted(cy['period_aliased_winding_matrix'])==[[0,0],[1,-1]] or sorted(cy['period_aliased_winding_matrix'])==[[-1,1],[0,0]]
 assert len(neg)==2
 deps=['ACTIVE_C_FIRST_ENTRY_LAST_EXIT_OWNERSHIP.md','C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md','active_C_entry_exit_forests_certificate.json','C_cycle_excursion_normal_form_certificate.json','check_extremal_read_coupling.py']
 out={'status':'AUTHOR checked, independent audit pending','scope':'Selected actual WHITE-owned C-discovery cycles only. Whole background and lifetime ownership hypotheses are inherited unchanged. No positivity, finite alphabet, WHITE-only S1 or controller classification.',
 'base_controls':bb,'representation_controls':controls,'standard_negative_older_faces':neg,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
 p=R/'C_excursion_triangular_winding_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n')
 for n,cs in bb.items():
  print(n,[(c['period_aliased_winding_matrix'],[(e['R_time'],e['length'],e['nonzero_relative_coefficients']) for e in c['excursions']]) for c in cs])
 print('PASS',len(controls),'representation controls',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
