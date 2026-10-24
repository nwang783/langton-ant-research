#!/usr/bin/env python3
"""Author controls for a conditional all-cap boundary lemma, not classification."""
import json,hashlib
from pathlib import Path
from itertools import product
from check_extremal_read_coupling import ROOT,D,quotient,event_word,cycles
import enumerate_g8_cycle_two_outer_rows as core
from itertools import combinations
DRIFT=(2,-2)
def cwords(I,J):
 out=[]
 for n in range(max(I,J),2*(I+J)+2):
  z=I+J-n//2
  if z%2:continue
  a=z//2;b=I-a
  if not 0<=a<=(n+1)//2 or not 0<=b<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),a),combinations(range(1,n,2),b)):
   E=set(rr)|set(ll);hs=tuple(1 if k in E else 3 for k in range(n));ee=sorted(E);ss=[k for k,h in enumerate(hs)if(h+(1 if k%2==0 else-1))%4==2]
   if ee[1]==ss[0]+1:out.append(hs)
 return out

def qwords(I,J,rels):
 out=[];total=0
 for odd in(0,1):
  for X in range(I+1):
   n=2*(J-I+2*X)-odd
   if n<max(I,J)or n<1:continue
   if not 0<=X<=(n+1)//2 or not 0<=I-X<=n//2:continue
   for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),I-X)):
    N=set(rr)|set(ll);hs=tuple(0 if k in N else 2 for k in range(n));nn=sorted(N);ww=[k for k,h in enumerate(hs)if(h+(1 if k%2==0 else-1))%4==3];assert len(ww)==J;total+=1
    if all(nn[b]==ww[a]+1 for a,b,L in rels):out.append(hs)
 return out,total

def lower(a,b):
 core.PTS=[(r,t-r)for t in range(-1,2)for r in(0,1)];core.IX={p:i for i,p in enumerate(core.PTS)}
 H=[(3,),(3,),(2,2,0,2),(2,2,0),a,b];kind,wit=core.assess(H);assert kind=='open_survivor';rels=[[],[]]
 for chain in wit['chains']:
  (i,j),k0=chain[0];assert k0==0;h=H[i][j];p=core.PTS[i];sp=(p[0]-D[h][0],p[1]-D[h][1]);sr,sk=quotient(sp,DRIFT)
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;q=core.PTS[ii];tp=(q[0]+kk*2+D[ho][0],q[1]-kk*2+D[ho][1]);tr,tk=quotient(tp,DRIFT)
  assert sum(sp)==sum(tp)==2 and h==3 and ho==0
  if sp==tp:
   aord=[z for z,hh in enumerate(H[i])if hh==h].index(j)
   bord=[z for z,hh in enumerate(H[ii])if(hh+(1 if z%2==0 else-1))%4==ho].index(jj)
   rels[sr[0]].append((aord,bord,len(chain)+1))
 return H,rels



def main():
 std=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());ev,d,_=event_word(std['word']);assert d==(-2,2)
 H={};P=len(ev)
 for e in ev:
  p=(-e['p'][0],2-e['p'][1]);r,k=quotient(p,(2,-2));H.setdefault(r,[]).append({'rank_time':e['t']-k*P,'phase':e['t'],'hi':(e['hi']+2)%4,'ho':(e['ho']+2)%4,'turn':e['c']})
 for h in H.values():h.sort(key=lambda x:x['rank_time'])
 F={};E={};single=[]
 for p,h in H.items():
  q,k=quotient(tuple(p[i]+D[h[0]['ho']][i]for i in(0,1)),(2,-2));F[p]=(q,k)
  if h[0]['rank_time']+1==H[q][-1]['rank_time']+k*P:E[p]=(q,k)
 for c in cycles(F):
  uses=[sum(e['ho']==H[p][0]['ho']for e in H[p])for p in c['cells']]
  if all(n==1 for n in uses):single.append(dict(c,headings=[''.join('NESW'[e['hi']]for e in H[p])for p in c['cells']]))
 assert len(single)==1 and sorted(single[0]['headings'])==sorted(['W','W','SSN','SSNS'])
 A=cwords(2,3);B=cwords(3,2)
 assert [''.join('NESW'[h]for h in x)for x in A]==['EEWWWW','WEWWEW','EEWWWWW','WEWWEWW']
 assert [''.join('NESW'[h]for h in x)for x in B]==['EEE','EEWEWW','EEWWWE','WEWWEE','EEWEWWW','EEWWWEW','WEWWEEW']
 HH,rel=lower(A[0],B[0]);q,nq=qwords(3,0,rel[0]);r,nr=qwords(1,4,rel[1])
 assert nq==2 and nr==15 and len(q)==len(r)==2
 quads=[]
 for qq,rr in product(q,r):
  v=[0]*4
  for i,hs in enumerate(HH+[qq,rr]):
   t=i//2-1;x=i%2;y=t-x
   if len(hs)%2:v[2*x+y%2]+=1
  targets=[z for z in product(range(9),repeat=4)if sum(z)==8 and all(w%4==2 for w in[z[0]-z[1],z[3]-z[2],z[0]-z[2],z[3]-z[1]])and all(a<=b for a,b in zip(v,z))]
  quads.append({'Q_headings':[''.join('NESW'[h]for h in qq),''.join('NESW'[h]for h in rr)],'parity_bin_inventory_00_01_10_11':v,'possible_full_g8_bin_inventories':targets})
 assert sum(not x['possible_full_g8_bin_inventories']for x in quads)==1
 sample=[]
 for p,h in sorted(H.items(),key=lambda z:(sum(z[0]),z[0][0])):sample.append({'point':p,'headings':''.join('NESW'[e['hi']]for e in h),'events':h})
 result={'scope':__doc__,'standard_source_sha256':hashlib.sha256((ROOT/'recovered_bundle/ant_global/root/standard.json').read_bytes()).hexdigest(),'standard_full_drift':[2,-2],'standard_period':P,'standard_growth':12,'all_standard_stable_histories':sample,'standard_first_cycles':cycles(F),'standard_E_cycles':cycles(E),'single_used_first_cycles':single,'A0_words':A,'A1_words':B,'standard_adjacent_next_row_relations':rel,'four_next_row_modes':quads,'warning':'All g8 modes here are open necessary interfaces; none is an alternative controller. Full standard positive control has growth12.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:v for k,v in result.items()if k not in('all_standard_stable_histories','A0_words','A1_words')},indent=2))
if __name__=='__main__':main()
