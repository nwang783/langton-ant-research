#!/usr/bin/env python3
"""Exact C-stream quadratic energy and source-owned excursion transfer."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
from certify_active_C_entry_exit_forests import analyze,active_C
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent

def compute(z,blocks=None):
 w=z['word'];P=len(w);d=tuple(z['drift']);E,dd,hh=event_word(w,h=z['initial_heading']);assert dd==d
 if blocks is None:blocks=[('period',P)]
 labels=[];ranges=[]
 for name,n in blocks:ranges.append((name,len(labels),len(labels)+n));labels +=[name]*n
 assert len(labels)==P and len(set(name for name,n in blocks))==len(blocks)
 def q(p):return quotient(p,d)[0]
 G=defaultdict(list);classes=[];weights={};lifetimes=[];inputs=[];outputs=[];birth=Counter();consume=Counter();opp=Counter();inputcharge=Counter();outputcharge=Counter();M=Counter()
 for H in z['read_histories']:
  p=tuple(H['class']);es=H['reads'];axis=es[0]['hi']%2
  sign=lambda e:1 if e['hi']==axis else-1
  a=sum(sign(e)for e in es if e['c']=='R');u=q(active_C(p,axis));v=q(active_C(p,axis+2));G[u].append((v,-a));G[v].append((u,a))
  classes.append({'read_class':p,'axis_heading':axis,'R_imbalance':a,'C_plus':u,'C_minus':v,'complete_reads':es})
  for j,e in enumerate(es):
   t=e['t'];b=labels[t];weights[t]=a*sign(e)
   if e['c']=='R':
    birth[b]+=weights[t]
    if j==len(es)-1:outputs.append({'phase':t,'class':p,'charge':weights[t],'block':b});outputcharge[b]+=weights[t]
   else:
    consume[b]+=weights[t]
    if j==0:inputs.append({'phase':t,'class':p,'charge':weights[t],'block':b});inputcharge[b]+=weights[t]
    else:
     r=es[j-1];assert r['c']=='R';rt=r['t'];age=e['canonical_time']-r['canonical_time'];owner_time=t-age;k=(owner_time-rt)//P
     assert rt+k*P==owner_time and tuple(E[rt]['p'][i]+k*d[i]for i in[0,1])==tuple(E[t]['p'])
     charge=a*sign(r);opposite=e['hi']!=r['hi'];source=labels[rt];M[source,b,k]+=charge
     if opposite:opp[b]+=2*charge
     lifetimes.append({'R_phase':rt,'L_phase':t,'owner_period':k,'owner_time':owner_time,'age':age,'class':p,'owner_heading':r['hi'],'consumer_heading':e['hi'],'source_block':source,'target_block':b,'birth_charge':charge,'opposite':opposite})
 # Actual balanced current supplies a periodic stream; reconstruct it directly.
 h={next(iter(G)):0};todo=list(h)
 while todo:
  u=todo.pop()
  for v,gap in G[u]:
   if v in h:assert h[v]==h[u]+gap
   else:h[v]=h[u]+gap;todo.append(v)
 assert len(h)==len(G);mn=min(h.values());h={q0:v-mn for q0,v in h.items()}
 getC=lambda t:q(active_C(E[t%P]['p'],E[t%P]['hi']))
 rows=[]
 for name,start,end in ranges:
  ci,cf=getC(start),getC(end);Q=h[ci]-h[cf];assert consume[name]==Q
  inc=sum(v for(s,t,k),v in M.items()if t==name);out=sum(v for(s,t,k),v in M.items()if s==name)
  assert consume[name]==inc-opp[name]+inputcharge[name]
  assert birth[name]==out+outputcharge[name]
  ew=w[start:end];_,ed,eh=event_word(ew,h=E[start]['hi']);closed=ed==(0,0)and eh==E[start]['hi']
  if closed:assert Q==0
  rows.append({'block':name,'interval':[start,end],'word':ew,'closed_head_pose':closed,'C_start':ci,'C_end':cf,'C_height_drop':Q,
   'birth_charge':birth[name],'owned_incoming_charge':inc,'opposite_owner_charge':opp[name],'input_charge':inputcharge[name],'permanent_output_charge':outputcharge[name],'owned_outgoing_charge':out,
   'signed_decorated_stock_flux':birth[name]-inc-inputcharge[name]})
 energy=sum(x['R_imbalance']**2 for x in classes);DI=sum(opp.values());O=sum(outputcharge.values());I=sum(inputcharge.values())
 assert sum(consume.values())==0 and energy==sum(birth.values())==DI+O-I
 return {'period':P,'drift':d,'heading':z['initial_heading'],'word':w,'energy':energy,'opposite_owner_charge':DI,'output_charge':O,'input_charge':I,'input_count':len(inputs),'output_count':len(outputs),
  'all_read_classes':classes,'all_C_heights':[{'class':q0,'height':v}for q0,v in sorted(h.items())],'all_owned_lifetimes':lifetimes,'input_roots':inputs,'permanent_output_roots':outputs,
  'block_rows':rows,'full_owner_matrix':[{'source':s,'target':t,'owner_period':k,'charge':v}for(s,t,k),v in sorted(M.items())]}

def main():
 src=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text());base={n:compute(z)for n,z in src['base_controls'].items()};S=src['base_controls']['S104']['word'];M=src['base_controls']['M10']['word'];F=src['base_controls']['F80']['word']
 cases={'standard_8_92':compute(analyze(S[46:]+S[:46],0),[('E8',8),('K1',2),('E92',92),('K2',2)]),
  'standard_12_88':compute(analyze(S[14:]+S[:14],0),[('E12',12),('K1',2),('E88',88),('K2',2)]),
  'prepared10':compute(analyze(M[1:]+M[:1],1),[('E8',8),('K',2)]),
  'prepared80_five_excursions':compute(analyze(F[1:]+F[:1],1),[('E1',8),('K1',2),('E2',8),('K2',9),('E3',8),('K3',7),('E4',8),('K4',16),('E5',8),('K5',6)])}
 assert [(base[n]['energy'],base[n]['opposite_owner_charge'],base[n]['output_charge'],base[n]['input_charge'])for n in base]==[(60,52,8,0),(782,462,320,0),(2402,1706,689,-7),(5,4,1,0),(44,26,16,-2)]
 assert any(x['R_phase']==43 and x['L_phase']==51 and x['birth_charge']==-1 and x['opposite']for x in base['S104']['all_owned_lifetimes'])
 assert any(x['R_phase']==62 and x['L_phase']==50 and x['owner_period']==-1 and x['birth_charge']==3 and x['age']==92 for x in base['S104']['all_owned_lifetimes'])
 assert base['M10']['input_count']==1 and base['M10']['input_charge']==0
 assert base['P1564']['input_count']==197 and base['P1564']['input_charge']==0
 assert sorted((z['phase'],z['charge'])for z in base['F80']['input_roots'])==[(15,0),(21,-2)]
 # High active C height is not attained on any standard discovery cycle.
 st=src['base_controls']['S104'];hh={tuple(x['class']):x['height']for x in base['S104']['all_C_heights']};cycle_heights=[[hh[tuple(q)]for q in c['vertices']]for c in st['WHITE_first_entry_cycles']]
 active={tuple(q['class'])for q in st['C_face_histories']};assert cycle_heights==[[3,3],[2,2]]and max(hh[q]for q in active)==4 and hh[(1,-2)]==4
 checks=[]
 for name,z in src['base_controls'].items():
  for rot in range(4):
   for k in[1,2,3,5]:
    a=compute(analyze(z['word']*k,rot));b=base[name]
    for key in['energy','opposite_owner_charge','output_charge','input_charge','input_count','output_count']:assert a[key]==k*b[key]
    checks.append({'name':name,'rotation':rot,'power':k,'energy':a['energy'],'input_charge':a['input_charge']})
 out={'status':'AUTHOR exact signed C-stream/owned-fuel identity; independent audit pending','scope':'Conserved signed transfer, not a monotonicity, input detector, finite alphabet or winding budget.',
  'base_controls':base,'excursion_partitions':cases,'all80_rotation_power_controls':checks,
  'standard_extremal_cycle_countercheck':{'all_active_C_classes':[{'class':q,'height':hh[q]}for q in sorted(active)],'discovery_cycle_heights':cycle_heights,'higher_active_face':[1,-2],
   'scope':'No discovery cycle attains even the active-C maximum in standard. Highest-cycle selection does not make all other active C heights lower. No claim about which geometric side is exterior.'},
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'active_C_entry_exit_forests_certificate.json',R/'C_cycle_excursion_normal_form_certificate.json',R.parent/'periodic_classification_new/white_front_stream_defect_criterion.md',R.parent/'periodic_classification_new/cap_three_shifted_stream_height.md']}}
 dest=R/'C_stream_owned_fuel_energy_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 for n,a in base.items():print(n,a['energy'],a['opposite_owner_charge'],a['output_charge'],a['input_charge'])
 print('PASS source-owned signed energy and all closed-excursion C-height drops');print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
