"""Rebuild both physical side currents at all eight complete G3 corners.
One local scalar/port identity, with no front or bounded search.
"""
from itertools import product
from pathlib import Path
import json
H='NESW';vec=dict(N=(0,1),E=(1,0),S=(0,-1),W=(-1,0));quad={(1,1):'NE',(-1,1):'NW',(-1,-1):'SW',(1,-1):'SE'}
portfaces={'W':('SW','NW'),'E':('NE','SE'),'N':('NE','NW'),'S':('SW','SE')}
rows=[]
for hs in product('EW',repeat=4):
 h=''.join(hs);outs=[H[(H.index(x)+(1 if r%2==0 else-1))%4]for r,x in enumerate(h)]
 f={'W':h.count('E'),'E':h.count('W'),'N':outs.count('N'),'S':outs.count('S')}
 ip=[p for p in 'WE'if f[p]==3];op=[p for p in 'NS'if f[p]==3]
 if len(ip)!=1 or len(op)!=1:continue
 inp,outp=ip[0],op[0];hin='E'if inp=='W'else'W';rE=sum(x=='E'for x in h[::2]);rW=2-rE;lE=sum(x=='E'for x in h[1::2]);lW=2-lE;a=-max(rE,rW)
 heights=dict(NE=a+rW,SW=a+rE,NW=a-lE,SE=a-lW)
 turn='RIGHT'if(H.index(outp)-H.index(hin))%4==1 else'LEFT'
 u,v=vec[hin],vec[outp];q=quad[(-u[0]+v[0],-u[1]+v[1])]
 left={q}if turn=='LEFT'else set(heights)-{q};right=set(heights)-left
 hl={q:(z+2 if q in left else 0)for q,z in heights.items()};hr={q:(z+1 if q in right else 0)for q,z in heights.items()}
 fl={p:hl[c]-hl[l]for p,(c,l)in portfaces.items()};fr={p:hr[c]-hr[l]for p,(c,l)in portfaces.items()};fm={p:int(p in(ip+op))for p in portfaces}
 assert all(fl[p]>=0 and fr[p]>=0 and fl[p]+fr[p]+fm[p]==f[p]for p in portfaces)
 assert fl['W']+fl['E']==fl['N']+fl['S']and fr['W']+fr['E']==fr['N']+fr['S']
 assert all(fl[p]==fr[p]==fm[p]==1 for p in ip+op)
 out_ranks=[r for r,x in enumerate(outs)if x==outp];sgn='positive'if out_ranks[1]==2 else'negative'
 rows.append(dict(headings=h,heights=heights,gamma_incoming=hin,gamma_outgoing=outp,turn=turn,sign=sgn,LEFT_faces=sorted(left),RIGHT_faces=sorted(right),h_LEFT=hl,h_RIGHT=hr,full_flows=f,LEFT_flows=fl,RIGHT_flows=fr,middle_flows=fm))
assert len(rows)==8
obj=dict(scope=__doc__,normalization='C right level c=0, L left level c-3=-3; h_LEFT=h-(c-2) on LEFT, zero RIGHT; h_RIGHT=h-(c-1) on RIGHT, zero LEFT.',rows=rows,warning='Balanced side currents, not new ant trajectories; side cycles after partial repair can be nonembedded and are not assumed primitive.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(rows),'local corners')
