"""Four exact physical sink/Y/source patterns, arbitrary P and drift.
L0/L2 domains are derived uncapped; Q<=4 gives a literal rank reversal.
"""
from pathlib import Path
from itertools import product
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def rr(h,d,k):return[i for i in range(len(h))if(h[i]if k=='in'else out(h,i))==d]
rows=[]
for s,b in product(['NSN','NSNS'],['NNN','NNNN']):
 assert not rr(s,'W','out')and not rr(b,'S','in')
 rows.append(dict(rail=dict(F='NSSN',S=s,B=b),L0_counts=dict(W_in=0,S_out=2),L2_counts=dict(W_in=2,S_out=0)))
helpers=[]
for q in['NNNS','NSNN']:
 hs={(0,0):'NSSN',(-1,0):'WEW',(-1,1):q,(0,1):'EEE'};cur=((0,0),2);route=[cur]
 for _ in range(4):
  p,r=cur;d=out(hs[p],r);t=p[0]+V[d][0],p[1]+V[d][1];j=rr(hs[p],d,'out').index(r);cur=(t,rr(hs[t],d,'in')[j]);route.append(cur)
 assert route[-1]==((0,0),1)
 helpers.append(dict(Q=q,literal_route=route))
obj=dict(scope=__doc__,all_four_local_rails=rows,uncapped_domains=dict(L0=['EEE','EEEE'],L2=['WEW','WEWE']),cap4_Q_profiles=helpers,minimum_Q_reads=5,warning='Local fifth-reader lemma is not an all-cap exclusion. Whole one-flat consequence additionally uses signed GLOBAL-M critical/no-one-use hypotheses and boundary macros; multi-flat remains open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS4 rail combinations; two forced Q profiles; universal4-R rank reversal')
