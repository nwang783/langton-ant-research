#!/usr/bin/env python3
"""Exhaustive all-cap actual read-minimum interface for full drift(3,1)."""
from itertools import product
from collections import Counter
import json
from partial_drift31_graph import graph,quotient31,D

def depart(hs,ho):return[j for j,h in enumerate(hs)if(h+(1 if j%2==0 else-1))%4==ho]
def words(axis,nmax,in_h,in_count,out_h,out_count,relations=[]):
 ww=[]
 for n in range(nmax+1):
  for hs in product((axis,axis+2),repeat=n):
   ii=[j for j,h in enumerate(hs)if h==in_h];oo=depart(hs,out_h)
   if len(ii)!=in_count or len(oo)!=out_count:continue
   if all(ii[b]==oo[a]+1 for a,b,L in relations):ww.append(hs)
 return ww

def returns_to(H,G,level):
 result=[];paths=[];pts=G['points']
 for chain in G['chains']:
  (i,j),k=chain[0];assert k==0;hi=H[i][j];p=pts[i];source=(p[0]-D[hi][0],p[1]-D[hi][1])
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;p=pts[ii];target=(p[0]+3*kk+D[ho][0],p[1]+kk+D[ho][1])
  if source!=target or 3*source[1]-source[0]!=level:continue
  a=[z for z,h in enumerate(H[i])if h==hi].index(j);b=depart(H[ii],ho).index(jj)
  result.append((a,b,len(chain)+1));paths.append({'outgoing_heading':hi,'incoming_heading':ho,'outgoing_ordinal':a,'incoming_ordinal':b,'duration':len(chain)+1,'physical_base':source,'lower_chain':chain})
 return result,paths

def main():
 branches=[];ss=Counter();qs=Counter()
 for h1,n2s in [((3,),(0,1)),((3,1),(2,3))]:
  for n2 in n2s:
   v2=(2,)*n2;a=(n2+1)//2
   for h3 in words(1,2*(a+1),3,a,2,1):
    H=[(),(),(),(2,),h1,v2,h3];k,G=graph(H);ss[k]+=1;entry={'histories':H,'lower_outcome':k}
    if k!='open':entry['witness']=G;branches.append(entry);continue
    rr,paths=returns_to(H,G,4);assert all(p['outgoing_heading']==1 and p['incoming_heading']==0 for p in paths)
    I=len(h1);J=h3.count(1);bound=2*(I+J)+1;ds=words(0,bound,0,I,1,J,rr);entry.update({'V4_I_N_J_E':[I,J],'derived_bound':bound,'first_return_paths':paths,'complete_V4_domain':ds});out=[]
    for v4 in ds:
     HH=H+[v4];kind,w=graph(HH);qs[kind]+=1;out.append({'word':v4,'outcome':kind,'witness':w})
    entry['V4_outcomes']=out;branches.append(entry)
 survivors=[]
 for bi,b in enumerate(branches):
  for qi,q in enumerate(b.get('V4_outcomes',[])):
   if q['outcome']=='open':
    v=q['word'];n0=v.index(0);assert n0 in(2,4) and all(x==2 for x in v[:n0]);assert n0%2==0
    survivors.append({'lower_index':bi,'V4_index':qi,'complete_histories':b['histories']+[v],'first_N_rank':n0})
 assert len(branches)==17 and ss=={'open':14,'positive_rank_clock_cycle':3} and qs=={'open':25,'positive_rank_clock_cycle':5}
 # Explicit seven-event OPEN clock model. These are not all202 phases.
 clocks={0:[208],1:[209],2:[],3:[5,9],4:[0,4,8]};H0=[(),(),(),(2,),(3,),(),(1,1),(2,2,0)];P=202
 k,G=graph(H0);assert k=='open';events=[]
 for i,hs in enumerate(H0):
  t=i-3
  if not hs:continue
  ts=clocks[t];assert len(ts)==len(hs)and all(b-a>=4 and(b-a)%4==0 for a,b in zip(ts,ts[1:]))
  for rank,(h,clock)in enumerate(zip(hs,ts)):
   phase=clock%P;lift=(phase-clock)//P;p=(-t+3*lift,lift);assert phase%4==((p[0]%2)+2*(p[1]%2))%4 if p[1]%2==0 else phase%4==(3-p[0]%2)
   events.append({'level':t,'rank':rank,'heading':h,'clock':clock,'phase':phase,'physical_position':p})
 assert len({e['phase']for e in events})==7
 for chain in G['chains']:
  values=[clocks[i-3][j]+v*P for(i,j),v in chain];assert all(b==a+1 for a,b in zip(values,values[1:]))
 # Literal blank ten-read factor, not complete-future histories.
 black=set();p=(-4,0);h=2;factor=[]
 for time in range(10):
  turn='L'if p in black else'R';factor.append({'time':time,'point':p,'incoming_heading':h,'turn':turn});black.symmetric_difference_update({p});h=(h+(1 if turn=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert ''.join(e['turn']for e in factor)=='RRRRLRRRRL' and (p,h)==((-3,1),0)
 # All compass transition formulas are verified directly, including voltages.
 for t in range(-20,21):
  for heading,(dx,dy)in enumerate(D):
   rep,k=quotient31((-t+dx,dy));assert rep==(-(t+3*dy-dx),0) and k==dy
 result={'scope':__doc__,'full_drift':[3,1],'normal':'T=3y-x','representative':'(-T,0)','initial_empty_read_levels':[-3,-2,-1],'lower_counts':dict(ss),'V4_counts':dict(qs),'branches':branches,'all25_open_interfaces':survivors,'open_seven_event_clock_model':{'period_parameter':P,'complete_named_histories':H0,'events':events,'chains':G['chains'],'missing_phases':195,'warning':'Only an OPEN necessary clock interface; no full202-event orbit or board is supplied.'},'blank_factor':{'start_position':[-4,0],'start_heading':2,'initial_black':[],'events':factor,'final_position':p,'final_heading':h,'complete_final_black':sorted(black),'warning':'Ten actual reads only. Named histories are not certified terminal in its future; this is not a translating controller.'},'limitations':'All25 are necessary OPEN local interfaces, not completions. No growth, period, width, or global visit cap was assumed. Chirality(3,-1) is not identified by reflection.'}
 json.dump(result,open('drift31_read_minimum_certificate.json','w'),indent=2)
 print('LOWER',dict(ss),'V4',dict(qs))
 for b in branches:
  if any(x['outcome']=='open'for x in b.get('V4_outcomes',[])):
   print('OPEN lower', [''.join('NESW'[h]for h in w)for w in b['histories'][3:]],'V4',[''.join('NESW'[h]for h in x['word'])for x in b['V4_outcomes']if x['outcome']=='open'])
if __name__=='__main__':main()
