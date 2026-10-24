#!/usr/bin/env python3
"""Literal201 prepared control: consume X's owned first lifetime, restore guides,
consume the square, then execute the full35 locked named chain. Not a controller.
"""
from pathlib import Path
import json,hashlib
from certify_physical_return_debt import STR
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));T=lambda p:3*p[1]-p[0]+11
X=(2,1);Q=(1,1);A=(1,0);B=(0,0);U=(0,1);V=(-1,1);C=(-1,0)
def main():
 f=json.load(open(R/'open79_X_first_201_chain_discovery.json'));W=f['word'];seed=set(map(tuple,f['initial_black']));black=seed.copy();p=X;h=2;ev=[];last={};owners=[]
 assert len(W)==201 and len(seed)==28
 for time,c in enumerate(W):
  assert c==('L'if p in black else'R');ev.append({'time':time,'position':p,'normal_level':T(p),'incoming_heading':h,'turn':c})
  if c=='L':owners.append({'time':time,'position':p,'owner_R_time':last.get(p,'initial BLACK')})
  last[p]=time;black.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 def reads(q):return [(e['time'],e['incoming_heading'],e['turn'])for e in ev if e['position']==q]
 assert reads(X)==[(0,2,'R'),(20,2,'L'),(192,0,'R'),(200,0,'L')]
 assert reads(U)==[(4,0,'L'),(64,2,'R'),(160,0,'L')]
 assert reads(V)==[(5,3,'L'),(65,3,'R'),(153,1,'L'),(157,1,'R'),(161,3,'L'),(165,1,'R')]
 assert reads(C)==[(6,2,'R'),(158,2,'L'),(162,2,'R'),(166,2,'L')]
 assert reads(B)==[(3,3,'R'),(159,1,'L'),(167,1,'R')]
 assert (p,h)==(Q,3)and len(black)==41
 assert all(T(e['position'])>=13 for e in ev[7:158]if e['time']not in[20,21])
 assert set(seed)<=set(e['position']for e in ev)
 assert sum(o['owner_R_time']=='initial BLACK'for o in owners)==28
 H=[tuple('NESW'.index(c)for c in s)for s in STR];kind,G=graph(H,list(range(13)));assert kind=='open'
 ch=next(ch for ch in G['chains']if ch[0][0]==(12,11));assert len(ch)==35
 anchors={0:(12,0),2:(10,2),3:(11,8),6:(12,8),20:(12,1),21:(11,1),158:(12,9),159:(11,9),162:(12,10)}
 named_chain=[]
 for a,((t,j),k)in enumerate(ch):
  e=ev[166+a];assert e['position']==(11-t+3*k,k)and e['incoming_heading']==H[t][j]and e['turn']==('R'if j%2==0 else'L');anchors[166+a]=(t,j)
  named_chain.append({'time':166+a,'class':t,'rank':j,'full_lift':k,'position':e['position']})
 for time,(t,j)in anchors.items():
  e=ev[time];assert T(e['position'])==t and e['incoming_heading']==H[t][j]and e['turn']==('R'if j%2==0 else'L')
 assert set(anchors)==set(e['time']for e in ev if T(e['position'])<=12)
 # Complete consecutive physical named fragments must use consecutive ranks.
 physical={}
 for time,(t,j)in anchors.items():physical.setdefault(tuple(ev[time]['position']),[]).append((time,j))
 for q,ls in physical.items():
  ls.sort();assert all(b[1]==a[1]+1 for a,b in zip(ls,ls[1:]))
 # All concrete lifetime ownership matters even though net mass grows.
 assert next(o for o in owners if o['time']==20)['owner_R_time']==0
 assert next(o for o in owners if o['time']==159)['owner_R_time']==3
 assert next(o for o in owners if o['time']==160)['owner_R_time']==64
 assert next(o for o in owners if o['time']==161)['owner_R_time']==157
 assert next(o for o in owners if o['time']==200)['owner_R_time']==192
 # In contrast, the exact earlier67 factor leaves X's first lifetime unpaid.
 r67=json.load(open(R/'open79_joint_repair67_certificate.json'));k67={tuple(e['position']):e['turn']=='R'for e in r67['events']};q67=tuple(r67['final_position']);h67=r67['final_heading'];tail67=[]
 for time in range(67,70):
  assert q67 in k67 and not k67[q67];tail67.append((time,q67,h67,'R'));k67[q67]=True;h67=(h67+1)%4;q67=(q67[0]+D[h67][0],q67[1]+D[h67][1])
 assert(q67,h67)==(C,2)
 assert all((11-t+3*k,k)!=X for(t,j),k in ch[:26])
 unpaid67={'forced_known_R_reads':tail67,'forced_C_rank11_time':70,'forced_next_X_time':96,'forced_X_incoming':'N','required_next_X_incoming':'S','reason':'X was read only once in the exact67 factor. The known three-step continuation and complete35 named chain reach X before any intermediate X read. Any earlier disagreement already violates the supplied complete histories. This is independent of colors at cells not read in the67 factor.'}
 out={'scope':__doc__,'word':W,'initial_position':X,'initial_heading':2,'complete_initial_black':sorted(seed),'events':ev,'complete_final_black':sorted(black),'final_position':p,'final_heading':h,'all_L_lifetime_owners':owners,'all_named_read_anchors':anchors,'full35_named_chain':named_chain,'physical_named_rank_fragments':[{ 'position':q,'time_rank_pairs':ls}for q,ls in physical.items()],'earlier67_unread_extension_obstruction':unpaid67,'net_black_mass_change':13,'higher_V_return_lengths':[88,4],'post_C10_return_length':4,'max_read_normal_level':max(T(e['position'])for e in ev),'limits':'Every actual read and named physical rank fragment is checked. Earlier/later named reads, the remaining full79 chronology, full drift ordering of higher classes, period and full odd output inventory are NOT supplied. All28 prepared BLACK inputs are retained and consumed. Positive net13 growth is not a regeneration relation.','dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_MANDATORY_GUIDE_PAIR_AND_UNIT_RETURN.md','partial_drift31_graph.py','open79_X_first_201_chain_discovery.json']}}
 (R/'open79_paid_chain201_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS actual201, full28->41 fields, X R0/L20/R192/L200, guide repair and full35 chain; every named physical fragment has consecutive ranks')
if __name__=='__main__':main()
