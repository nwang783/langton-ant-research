#!/usr/bin/env python3
"""Discovery exact derived minimum interface for full drift(3,1), no visit cap."""
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
 result={'scope':__doc__,'lower_counts':dict(ss),'V4_counts':dict(qs),'branches':branches};json.dump(result,open('drift31_read_minimum_discovery.json','w'),indent=2)
 print('LOWER',dict(ss),'V4',dict(qs))
 for b in branches:
  if any(x['outcome']=='open'for x in b.get('V4_outcomes',[])):
   print('OPEN lower', [''.join('NESW'[h]for h in w)for w in b['histories'][3:]],'V4',[''.join('NESW'[h]for h in x['word'])for x in b['V4_outcomes']if x['outcome']=='open'])
if __name__=='__main__':main()
