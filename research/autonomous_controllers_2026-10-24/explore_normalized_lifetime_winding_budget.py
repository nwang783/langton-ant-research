#!/usr/bin/env python3
"""Controls and exact shared-lifetime data for a CONJECTURAL input budget.
This file does not prove the proposed inequality outside these supplied words.
"""
from pathlib import Path
from collections import defaultdict,Counter
from math import gcd
import json,hashlib
import lifetime_boundary_graph as LB
from check_all_cut_wave_interfaces import WORDS
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent

def stats(w,h=0):
 old=LB.event_word
 try:
  LB.event_word=lambda word:event_word(word,h)
  f=LB.analyze(w)
 finally:LB.event_word=old
 m=gcd(abs(f['d'][0]),abs(f['d'][1]));I=len(f['input_events']);O=len(f['output_events']);winds=[abs(c['winding'])for c in f['root_skeleton_cycles']];S=sum(winds)
 return {'P':len(w),'initial_heading':h,'full_drift':f['d'],'m':m,'I':I,'O':O,'absolute_boundary_windings':sorted(winds),'S':S,'candidate_left':m*(S-1),'candidate_right':2*min(I,O),'candidate_holds_on_this_control':m*(S-1)<=2*min(I,O),'internal_component_lengths':dict(Counter(len(c['events'])for c in f['internal_cycles']))}

def interaction(w):
 E,d,_=event_word(w);P=len(w);H=defaultdict(list);K={};life={};I=[];O=[]
 for e in E:
  q,k=quotient(e['p'],d);K[e['t']]=k;H[q].append((e['t']-k*P,e))
 for es in H.values():
  es.sort(key=lambda z:z[0]);assert all(a[1]['c']!=b[1]['c']for a,b in zip(es,es[1:]))
  if es[0][1]['c']=='L':I.append(es[0][1]['t'])
  if es[-1][1]['c']=='R':O.append(es[-1][1]['t'])
  for (_,a),(_,b)in zip(es,es[1:]):
   if a['c']=='R':
    i,j=a['t'],b['t'];v=K[i]-K[j];age=j+v*P-i;assert age>=4 and age%4==0;life[i]=(i,j,v,age)
 edges=[]
 for r,(i,j,v,age)in life.items():
  edges.append((i,j,v,'alpha',r,age))
  edges.append(((i+1)%P,(j+1)%P,v+int(j==P-1)-int(i==P-1),'beta',r,age))
 for i in I+O:edges.append((i,(i+1)%P,int(i==P-1),'O'if i in O else'I',i,1))
 adj=defaultdict(list)
 for k,(i,j,*_)in enumerate(edges):adj[i].append((k,1));adj[j].append((k,-1))
 assert len(adj)==P and all(len(v)==2 for v in adj.values())
 todo=set(range(P));cs=[];where={}
 while todo:
  st=min(todo);at=st;prev=None;seq=[];wind=0
  while True:
   todo.discard(at);k,s=next(z for z in adj[at]if z[0]!=prev);i,j,v,c,r,age=edges[k];seq.append((k,s));where[k]=(len(cs),s);wind+=s*v;at=j if s==1 else i;prev=k
   if at==st:break
  rr=sum(s for k,s in seq if edges[k][3]in['I','O']);debt=sum(s*edges[k][5]for k,s in seq if edges[k][3]in['alpha','beta']);assert wind*P==rr+debt
  cs.append({'winding':wind,'signed_root_step_count':rr,'unsigned_root_step_count':sum(edges[k][3]in['I','O']for k,s in seq),'signed_lifetime_age_sum':debt,'oriented_edges':seq,'event_count':len(seq)})
 table=[];k=0
 for r,(i,j,v,age)in life.items():
  ca,sa=where[k];cb,sb=where[k+1];table.append({'R_phase':i,'L_phase':j,'alpha_voltage':v,'actual_lifetime_age':age,'alpha_copy':{'component':ca,'traversal_sign':sa},'beta_copy':{'component':cb,'traversal_sign':sb}});k+=2
 sig=Counter((q['alpha_copy']['component']==q['beta_copy']['component'],q['alpha_copy']['traversal_sign']==q['beta_copy']['traversal_sign'])for q in table)
 return {'P':P,'d':d,'I':I,'O':O,'directed_edges_with_positive_age':edges,'expanded_circuits':cs,'every_owned_lifetime_and_both_copies':table,'shared_copy_summary':[{'same_component':a,'same_sign':b,'count':n}for(a,b),n in sorted(sig.items())]}

def main():
 words=dict(WORDS,prepared10='RRRRLLLLRL');all_controls={};all_interactions={}
 for name,w in words.items():
  base=stats(w);assert base['candidate_holds_on_this_control'];rows=[]
  for q in [1,2,3,5]:
   expected=[]
   for z in base['absolute_boundary_windings']:
    k=gcd(q,z);expected.extend([z//k]*k)
   for h in range(4):
    st=stats(w*q,h);assert st['m']==q*base['m']and st['I']==q*base['I']and st['O']==q*base['O'];assert st['S']==base['S']and st['absolute_boundary_windings']==sorted(expected);assert st['candidate_left']==q*base['candidate_left']and st['candidate_right']==q*base['candidate_right'];rows.append(st)
  phases=[]
  for cut in sorted(set([0,1,len(w)//3])):
   st=stats(w[cut:]+w[:cut]);assert all(st[k]==base[k]for k in ['m','I','O','S','candidate_left','candidate_right','absolute_boundary_windings']);phases.append({'cut':cut,'statistics':st})
  all_controls[name]={'word_sha256':hashlib.sha256(w.encode()).hexdigest(),'base':base,'power_rotation_controls':rows,'phase_controls':phases};all_interactions[name]=interaction(w);print(name,base,flush=True)
 out={'status':'EXACT SUPPLIED CONTROLS PASS; CANDIDATE INEQUALITY UNPROVED','candidate':'m*(S-1) <= 2*min(I,O), where m=gcd(|dx|,|dy|) and S=sum absolute full-drift boundary cycle windings','scope':'All-cap non-axis complete alternating fronts. I/O count consumed BLACK-input and permanent-output read roots only. Passive untouched BLACK strands are not consumed inputs.','controls':all_controls,'full_shared_lifetime_interactions':all_interactions,'complete_background_dependency':{'path':'lifetime_boundary_graph_certificate.json','sha256':hashlib.sha256((R/'lifetime_boundary_graph_certificate.json').read_bytes()).hexdigest(),'scope':'All1564/4352 bulk classes, untouched strands and exact finite XOR caps remain those signed supplied normal forms. No autonomous realization is inferred.'},'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['lifetime_boundary_graph.py','check_extremal_read_coupling.py','check_all_cut_wave_interfaces.py']}}
 (R/'normalized_lifetime_winding_budget_controls.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
