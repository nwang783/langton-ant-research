#!/usr/bin/env python3
"""All-cap chronological lifetime boundary graph; exact controls with complete fields.
No cyclic-order or simple-winding classification is asserted for the root graph.
"""
from pathlib import Path
from collections import Counter
from functools import lru_cache
from itertools import product
import json,hashlib
from lifetime_boundary_graph import analyze
from check_all_cut_wave_interfaces import WORDS,rot
from check_extremal_read_coupling import quotient
R=Path(__file__).resolve().parent;G=R.parent/'nonlinear_global_budget_2026-10-23'

def full_background(name,f):
 E=f['events'];d=f['d'];read={quotient(e['p'],d)[0]for e in E}
 if name=='S104':return {'full_input_black_classes':[],'untouched_black_classes':[],'finite_XOR_cap':[],'scope':'Complete stable WHITE read front. The retained standard finite seed realization is a separate dependency; no infinite initial BLACK profile is supplied.'}
 fn,key=('prepared_wave_five_band_normal_form.json','full_black_orbit_profiles')if name=='P1564'else('three_standard_band_wave_normal_form.json','full_black_profiles')
 N=json.load(open(G/fn));p0=N['pose'][0];h0=N['pose'][1];s=N['drift'][0];B=set()
 for t,b in N[key]:
  for a in range(b,s,2):B.add(quotient(rot((a-p0[0],a-t-p0[1]),(-h0)%4),d)[0])
 assert tuple(rot(tuple(N['drift']),(-h0)%4))==tuple(d)
 U=B-read;I={quotient(E[i]['p'],d)[0]for i in f['input_events']};O={quotient(E[i]['p'],d)[0]for i in f['output_events']};odd={q for q in read if sum(quotient(e['p'],d)[0]==q for e in E)%2};Bout=B^odd
 assert B&read==I and Bout&read==O and Bout-read==U
 expected=(420,524,223,2)if name=='P1564'else(468,652,62,68)
 assert(len(B),len(Bout),len(U),len(N['finite_XOR_cap']))==expected
 return {'normal_form':fn,'normal_form_sha256':hashlib.sha256((G/fn).read_bytes()).hexdigest(),'original_pose':N['pose'],'full_input_black_classes':sorted(B),'full_output_black_classes':sorted(Bout),'untouched_black_classes':sorted(U),'finite_XOR_cap':N['finite_XOR_cap'],'cap_coordinate_scope':'Exact original normal-form coordinates, with original pose retained. The stable read graph uses the stated rigid normalization.','scope':'Infinite prepared input profile, NOT a finite-seed autonomous controller. Every passive unread BLACK strand and finite XOR cap is retained.'}

def fibre_planarity(f,bg):
 E=f['events'];d=f['d'];U=set(map(tuple,bg['untouched_black_classes']));out=[]
 for axis in 'HV':
  fixed=1 if axis=='H'else 0;var=1-fixed
  assert d[fixed]!=0
  for r in range(abs(d[fixed])):
   pairs=[];boundary={}
   for path in f['root_pairing_edges']:
    if path['axis']!=axis:continue
    ee=path['ends'][0];q=E[ee['event']]['p'];v0=q[fixed]+ee['lift']*d[fixed]
    if(r-v0)%d[fixed]:continue
    shift=(r-v0)//d[fixed];keys=[]
    for ee in path['ends']:
     i=ee['event'];q=E[i]['p'];z=ee['lift']+shift;point=(q[0]+z*d[0],q[1]+z*d[1]);assert point[fixed]==r
     key=f"{i}:{ee['type']}";assert key not in boundary;boundary[key]={'type':ee['type'],'spatial_coordinate':point[var]};keys.append(key)
    pairs.append(keys)
   for k,u in enumerate(sorted(U)):
    if(r-u[fixed])%d[fixed]:continue
    z=(r-u[fixed])//d[fixed];pos=u[var]+z*d[var];a=f'passive{k}:I';b=f'passive{k}:O';boundary[a]={'type':'I','spatial_coordinate':pos};boundary[b]={'type':'O','spatial_coordinate':pos};pairs.append([a,b])
   order=sorted(boundary,key=lambda k:(0,boundary[k]['spatial_coordinate'])if boundary[k]['type']=='I'else(1,-boundary[k]['spatial_coordinate']));ind={k:i for i,k in enumerate(order)}
   for n,(aa,bb)in enumerate(pairs):
    a,b=sorted([ind[aa],ind[bb]])
    for cc,dd in pairs[n+1:]:
     c,e=sorted([ind[cc],ind[dd]]);assert not(a<c<b<e or c<a<e<b)
   out.append({'axis':axis,'fixed_coordinate':r,'ordered_boundary':order,'boundary_points':boundary,'noncrossing_pairs':pairs})
 return out

@lru_cache(None)
def matchings(S):
 if not S:return ((),)
 ans=[]
 for j in range(1,len(S),2):
  for a in matchings(S[1:j]):
   for b in matchings(S[j+1:]):ans.append(((S[0],S[j]),)+a+b)
 return tuple(ans)
def middle28():
 # Coordinates T_i = A_i*a+C_i*c+K_i, in increasing T order.
 coeff=[(0,0,0),(0,0,1),(0,0,2),(0,0,6),(0,0,7),(0,6,1),(6,0,2),(6,0,4)]
 horizontal=matchings(tuple(range(8)));vertical=[sum(z,())for z in product(*(matchings(S)for S in[(0,3),(1,4,5,7),(2,6)]))]
 assert len(horizontal)==14 and len(vertical)==2;rows=[]
 for hi,H in enumerate(horizontal):
  for vi,V in enumerate(vertical):
   edges=[{'axis':'H','ends':[a,b],'voltage_coefficients_a_c_constant':[0,0,0]}for a,b in H]
   for a,b in V:
    vv=[y-x for x,y in zip(coeff[a],coeff[b])];assert all(z%3==0 for z in vv);edges.append({'axis':'V','ends':[a,b],'voltage_coefficients_a_c_constant':[z//3 for z in vv]})
   adj={i:[]for i in range(8)}
   for e in edges:
    a,b=e['ends'];v=e['voltage_coefficients_a_c_constant'];adj[a].append((b,v,e['axis']));adj[b].append((a,[-z for z in v],e['axis']))
   left=set(range(8));cycles=[]
   while left:
    start=min(left);at=start;previous=None;vv=[0,0,0];vertices=[]
    while True:
     left.discard(at);vertices.append(at);at,dv,previous=next(e for e in adj[at]if e[2]!=previous);vv=[a+b for a,b in zip(vv,dv)]
     if at==start:break
    cycles.append({'vertices':vertices,'winding_coefficients_a_c_constant':vv})
   parity=[sum(q['winding_coefficients_a_c_constant'][i]for q in cycles)%2 for i in range(3)];assert parity==[0,0,1]
   rows.append({'horizontal_choice':hi,'vertical_choice':vi,'edges':edges,'unoriented_cycles_with_one_declared_orientation':cycles,'total_winding_mod2_coefficients':parity})
 assert len(rows)==28
 return {'full_odd_levels':['0','1','2','6','7','6c+1','6a+2','6a+4'],'scope':'Necessary boundary pairing TYPES only for the signed live family3<=c<=a. All interior lifetime components and clock/spatial feasibility remain unresolved.','horizontal_matchings':horizontal,'vertical_matchings':vertical,'all28_types':rows}

def signature(f):
 return {'input_roots':len(f['input_events']),'output_roots':len(f['output_events']),'boundary_paths':len(f['root_pairing_edges']),'internal_cycle_lengths':dict(Counter(len(c['events'])for c in f['internal_cycles'])),'root_cycle_types':[{'length':c['length'],'absolute_winding':abs(c['winding']),'input_count':c['input_count'],'output_count':c['output_count']}for c in f['root_skeleton_cycles']]}
def main():
 controls={}
 for name,w in WORDS.items():
  f=analyze(w);assert all(not c['voltages']for c in f['internal_cycles']);bg=full_background(name,f);planar=fibre_planarity(f,bg)
  assert len(f['root_pairing_edges'])==len(f['input_events'])+len(f['output_events'])
  assert sum(c['winding']for c in f['root_skeleton_cycles'])%2==1
  controls[name]={'graph':f,'signature':signature(f),'complete_background':bg,'all_fibre_boundary_matchings':planar,'word_sha256':hashlib.sha256(w.encode()).hexdigest()}
  print(name,signature(f),flush=True)
 S=controls['S104']['signature'];assert S['input_roots']==0 and S['output_roots']==12 and S['internal_cycle_lengths']=={14:1,2:4}
 assert S['root_cycle_types']==[{'length':12,'absolute_winding':1,'input_count':0,'output_count':12}]
 rotations=[]
 for phase in[14,37,71]:
  w=WORDS['S104'];f=analyze(w[phase:]+w[:phase]);assert signature(f)==S;rotations.append({'phase':phase,'signature':signature(f)})
 repeats=[]
 for k in[2,3]:
  f=analyze(WORDS['S104']*k);sig=signature(f);assert sig['output_roots']==12*k and len(f['internal_cycles'])==5*k
  assert len(f['root_skeleton_cycles'])==1 and f['root_skeleton_cycles'][0]['length']==12*k and abs(f['root_skeleton_cycles'][0]['winding'])==1
  repeats.append({'multiple':k,'full_drift':f['d'],'signature':sig})
 out={'scope':__doc__,'controls':controls,'genuine_phase_controls':rotations,'full_period_repetition_controls':repeats,'middle_short28_boundary_pairing_types':middle28(),'limits':'No claim that every complete WHITE root cycle is essential, has unit winding, or belongs to one component. These happen in the standard control, not as a proved theorem. Internal cycles are genuine unresolved traffic, not deletable loops. The28 types are necessary and have not been completed or excluded.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['lifetime_boundary_graph.py','check_all_cut_wave_interfaces.py','check_extremal_read_coupling.py','wave_roots_and_stock_scope.json']}}
 (R/'lifetime_boundary_graph_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
