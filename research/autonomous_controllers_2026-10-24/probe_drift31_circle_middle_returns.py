import json,time
from collections import Counter
from partial_drift31_graph import graph
from certify_drift31_read_minimum import words,returns_to,depart
from certify_first_N_return_rules import reject_rule

def budget(H):
 n=sum(len(h)%2 for h in H);s=[0]*3
 for t,h in enumerate(H):
  if len(h)%2:s[-t%3]+=(-1)**t
 f=lambda x:min(x%4,(-x)%4)
 return n+sum(f(2-x)for x in s)<=8

def main():
 z=json.load(open('drift31_single_used_g8_shapes_certificate.json'));out=[];S=Counter();start=time.time()
 for q in z['all_quadruple_placements']:
  if q['outcome']!='OPEN_circle_interface':continue
  H=[q['complete_circle_histories'][str(t)]for t in range(6)]
  for v6 in q['first_exterior_cell_T6']['all_complete_domains']:
   A=H+[v6];k,G=graph(A,list(range(7)));assert k=='open';rel,paths=returns_to(A,G,7);assert all(p['outgoing_heading']==2 and p['incoming_heading']==3 for p in paths)
   I=len(depart(v6,3));J=3;bound=2*(I+J);ds=words(1,bound,3,I,2,J,rel);cc=Counter();surv=[]
   for h7 in ds:
    B=A+[h7]
    if not budget(B):cc['g8_residue_budget']+=1;continue
    kind,w=graph(B,list(range(8)))
    if kind=='open':
     rs,pp=returns_to(B,w,8);assert all(p['outgoing_heading']==1 and p['incoming_heading']==0 for p in pp)
     JJ=h7.count(1);r=reject_rule(JJ,[{'W_ordinal':a,'N_ordinal':b,'duration':L}for a,b,L in rs])
     if r is not None:kind=r['rule']
     else:surv.append({'T7_history':h7,'T8_first_returns':pp,'T8_E_count':JJ})
    cc[kind]+=1
   S.update(cc);out.append({'circle_T5':H[5],'T6':v6,'T7_counts':[I,J],'T7_derived_bound':bound,'T7_returns':paths,'T7_domain_size':len(ds),'outcomes':dict(cc),'survivors':surv})
   print('mode',len(H[5]),''.join('NESW'[h]for h in v6),'domain',len(ds),'counts',dict(cc),flush=True)
 json.dump({'scope':'Discovery of exact middle-read obligations only','aggregate':dict(S),'cases':out},open('drift31_circle_middle_returns_discovery.json','w'),indent=2);print('TOTAL',dict(S),'seconds',time.time()-start)
if __name__=='__main__':main()
