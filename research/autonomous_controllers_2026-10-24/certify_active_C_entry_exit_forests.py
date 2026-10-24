#!/usr/bin/env python3
"""Full-drift, all-cap active-C first-entry and last-exit ownership graphs.
All graphs concern actual C-face visits, not BLACK-field components.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from check_extremal_read_coupling import event_word,quotient
from check_all_cut_wave_interfaces import WORDS
R=Path(__file__).resolve().parent

def active_C(p,h):
 x,y=p
 return [(x,y-1),(x-1,y-1),(x-1,y),(x,y)][h]

def circuits(G):
 seen=set();out=[]
 for r in G:
  path=[];loc={};u=r
  while u in G and u not in seen and u not in loc:
   loc[u]=len(path);path.append(u);u=G[u]['target']
  if u in loc:
   c=path[loc[u]:]
   out.append({'vertices':c,'winding':sum(G[v]['voltage']for v in c),
    'physical_read_classes':[G[v]['read_class']for v in c],
    'read_phases':[G[v]['L_phase']for v in c],
    'sum_clock_gaps':sum(G[v]['clock_gap']for v in c)})
  seen.update(path)
 return out

def analyze(w,h0=0):
 E,d,h=event_word(w,h=h0);P=len(w);assert h==h0 and d!=(0,0)
 H=defaultdict(list);C=defaultdict(list);CL={};CQ={};RQ={}
 for e in E:
  i=e['t'];q,k=quotient(e['p'],d);H[q].append((i-P*k,e));RQ[i]=q
  q,k=quotient(active_C(e['p'],e['hi']),d);C[q].append((i-P*k,e));CQ[i]=q;CL[i]=k
 for es in H.values():
  es.sort(key=lambda x:x[0]);assert all(es[i][1]['c']!=es[i+1][1]['c']for i in range(len(es)-1))
 for es in C.values():es.sort(key=lambda x:x[0])
 rank={e['t']:i for es in H.values()for i,(_,e)in enumerate(es)}
 first={q:es[0][0]for q,es in C.items()};last={q:es[-1][0]for q,es in C.items()}
 F={};FW={};B={}
 for q,es in C.items():
  a,e=es[0];i=e['t'];j=(i-1)%P;le=E[j];assert le['c']=='L'
  hh=H[RQ[j]];white=hh[0][1]['c']=='R';k=rank[j]
  assert k==(1 if white else 0)
  nu=CL[j]-CL[i]-int(i==0);parent=CQ[j]
  delta=a-first[parent]-nu*P;assert delta>=1
  edge={'target':parent,'voltage':nu,'L_phase':j,'L_rank':k,'read_class':RQ[j],
    'WHITE_first':white,'clock_gap':delta}
  if white:
   rtime,re=hh[0];ltime,_=hh[1];age=ltime-rtime
   assert re['hi']==le['hi']and age>=4 and age%4==0 and delta>=age+1
   edge.update({'R_owner_phase':re['t'],'R_to_L_age':age,'idle_before_owner':delta-age-1})
   FW[q]=edge
  F[q]=edge
  b,e=es[-1];i=e['t'];assert e['c']=='L';j=(i+1)%P
  hh=H[RQ[i]];k=rank[i];ll=max(k0 for k0,(_,z)in enumerate(hh)if z['c']=='L');assert k==ll
  nu=CL[j]-CL[i]+int(i==P-1);target=CQ[j];delta=last[target]+nu*P-b;assert delta>=1
  edge={'target':target,'voltage':nu,'L_phase':i,'L_rank':k,'read_class':RQ[i],
    'ends_R':hh[-1][1]['c']=='R','clock_gap':delta}
  if edge['ends_R']:
   rtime,re=hh[-1];ltime,_=hh[k];gap=rtime-ltime
   assert k==len(hh)-2 and (re['hi']-e['hi'])%4==2 and gap>=4 and gap%4==0 and delta>=gap
   edge.update({'final_R_phase':re['t'],'L_to_R_gap':gap,'idle_after_final_R':delta-gap})
  B[q]=edge
 # Distinct selected face arrows use distinct physical read-edge orbits.
 assert len({z['read_class']for z in F.values()})==len(F)
 assert len({z['read_class']for z in B.values()})==len(B)
 FC,FWC,BC=circuits(F),circuits(FW),circuits(B)
 assert FC and BC
 assert all(z['winding']==-1 and z['sum_clock_gaps']==P for z in FC+FWC)
 assert all(z['winding']==1 and z['sum_clock_gaps']==P for z in BC)
 assert all(P>=5*len(z['vertices'])for z in FWC)
 for z in BC:assert P>=len(z['vertices'])+3*sum(B[v]['ends_R']for v in z['vertices'])
 I=[q for q,es in H.items()if es[0][1]['c']=='L'];O=[q for q,es in H.items()if es[-1][1]['c']=='R']
 if not I:assert len(FW)==len(F)and FWC
 def rows(G):return [{'source':q,**v}for q,v in sorted(G.items())]
 return {'word':w,'period':P,'drift':d,'initial_heading':h0,'C_face_count':len(C),'input_count':len(I),
  'output_count':len(O),'first_input_entry_count':len(F)-len(FW),
  'first_input_entry_phases':sorted(v['L_phase']for v in F.values()if not v['WHITE_first']),
  'other_BLACK_input_phases':sorted(es[0][1]['t']for q,es in H.items()if es[0][1]['c']=='L'and es[0][1]['t']not in {v['L_phase']for v in F.values()}),
  'read_histories':[{'class':q,'reads':[{'canonical_time':t,**e}for t,e in es]}for q,es in sorted(H.items())],
  'C_face_histories':[{'class':q,'first_time':first[q],'last_time':last[q],'visits':[{'canonical_time':t,'phase':e['t']}for t,e in es]}for q,es in sorted(C.items())],
  'first_entry_edges':rows(F),'WHITE_first_entry_edges':rows(FW),'last_exit_edges':rows(B),
  'first_entry_cycles':FC,'WHITE_first_entry_cycles':FWC,'last_exit_cycles':BC}

def sig(z):return(z['C_face_count'],z['input_count'],z['output_count'],z['first_input_entry_count'],len(z['first_entry_cycles']),len(z['WHITE_first_entry_cycles']),len(z['last_exit_cycles']))

def main():
 w80=json.loads((R/'prepared80_budget_falsifier_independent_confirmation.json').read_text())['word']
 words={**WORDS,'M10':'RRRRLLLLRL','F80':w80};base={n:analyze(w)for n,w in words.items()};controls=[]
 for name,w in words.items():
  z=base[name];s=sig(z)
  for h in range(4):
   for power in[1,2,3,5]:
    zz=analyze(w*power,h);ss=sig(zz);assert ss==tuple(v*power if j<4 else v for j,v in enumerate(s))
    controls.append({'name':name,'heading':h,'power':power,'summary':ss})
  for k in sorted({0,1,len(w)//3,len(w)//2,len(w)-1}):
   zz=analyze(w[k:]+w[:k]);assert sig(zz)==s
   controls.append({'name':name,'phase_rotation':k,'summary':sig(zz)})
 assert sig(base['S104'])==(10,0,12,0,2,2,2)
 assert sig(base['P1564'])==(292,197,301,168,1,0,1)
 assert sig(base['Q4352'])==(592,406,590,319,1,0,1)
 assert sig(base['M10'])==(2,1,1,0,1,1,1)
 assert sig(base['F80'])==(14,2,14,1,1,0,1)
 # The BLACK input of M10 is genuine but NOT a discovery entry.
 assert base['M10']['other_BLACK_input_phases']==[5]
 out={'status':'AUTHOR CHECKED all-cap active-C entry/exit lemma and exact controls; independent audit pending',
  'scope':'Necessary physical ownership graphs, not lifetime boundary circuits or controller classification. Prepared controls retain their existing full background hypotheses.',
  'base_controls':base,'representation_controls':controls,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in['check_extremal_read_coupling.py','check_all_cut_wave_interfaces.py','prepared80_budget_falsifier_independent_confirmation.json']}}
 p=R/'active_C_entry_exit_forests_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n')
 for n,z in base.items():print(n,sig(z))
 print('PASS',len(controls),'rotation/power/phase controls; JSON',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
