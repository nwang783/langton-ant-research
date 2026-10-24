from pathlib import Path
from collections import Counter
P=Path(__file__).resolve();SS=P.with_name('check_six_C_contact_independent.py');exec(compile(SS.read_text().split("B=ROOT/'core_periodicity_new/six_C_contact")[0],str(SS),'exec'))
import math
B=ROOT/'core_periodicity_new/four_C_contact_gate_frozen_20261023_1455';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_four_C_center_contact_gate.json').read_text())
geoms=[]
for a,(_,_,O,da)in atoms.items():
 for b,(need,I,_,db)in atoms.items():
  corners=[s*da-t*db for s in(0,1)for t in(0,1)];den=det(da,db)
  for x in range(math.ceil(min(z.real for z in corners)/2),math.floor(max(z.real for z in corners)/2)+1):
   for y in range(math.ceil(min(z.imag for z in corners)/2),math.floor(max(z.imag for z in corners)/2)+1):
    if(x+y)%2:continue
    pos=complex(x,y)
    if den:
     s=Fraction(det(2*pos,db),den);t=Fraction(det(2*pos,da),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if det(pos,da):continue
     s=Fraction(0);t=Fraction(-2*x,int(db.real))if db.real else Fraction(-2*y,int(db.imag))
     if not(0<t<=1)or 2*pos+t*db!=0:continue
    geoms.append((a,b,pos,s,t))
assert len(geoms)==23
roles=[]
for src in ids:
 roles.append(('D'if base[src]==0 else'V'if base[src]==4 else'U',src,0j,0,0,counts[src]));p=G[base[src]][0];h=0
 for shift in range(counts[src]):roles.append(('C',src,p,h,shift,counts[src]-shift));p+=rotation(1j,h);h=(h-1)%4
# Independently reconstruct all upper-slot age0..4 exclusions; no new threshold inferred.
upper=[]
for src in ids:
 for o in G[src][4]:
  for dst in(7,8,9):
   for n in range(5):
    h=(-n)%4;p=o-rotation(2j,h);hb=(src,dst,*xy(p),h,*xy(o));cq=(mp[src],mp[dst],*xy(p),h,*xy(o),n)
    if n<counts[src]:why='BEFORE_FULL_SOURCE_EXIT'
    elif(int(p.real+p.imag)+h)%2:why='WRONG_SECTOR'
    elif hb in HB:why='SIGNED_HB_EXCLUDED'
    else:assert cq in C5;why='SIGNED_COUNT5_EXCLUDED'
    upper.append((cq,hb,why))
AK={(r['earlier_atom'],r['later_atom'],tuple(r['later_pose'][:2])):i for i,r in enumerate(J['all_23_canonical_geometries'])};red=[];core=[];queries=[]
for a,b,p,s,t in geoms:
 gi=AK[a,b,xy(p)];ar=J['all_23_canonical_geometries'][gi];assert Fraction(ar['earlier_parameter'])==s and Fraction(ar['later_parameter'])==t
 need=atoms[b][0];local=2-p;assert p.real<=0
 if need.get(local)is False or local in K:why='SIGNED_ATOMIC_FOUR_C_COMMON_OUTPUT_STILL_CURRENT_BUT_TARGET_WHITE_OR_CORE'
 elif b=='U'and p==-2j:
  for ri,(an,src,sp,sh,shift,remaining)in enumerate(roles):
   if an!=a:continue
   cell=sp;same=cell in G[src][4];maximum=4+shift if same else 4-remaining;assert maximum<5
   for dst in(7,8,9):core.append((gi,ri,src,dst,xy(cell),same,maximum))
  why='OLD_CORE_TO_U_UPPER_INPUT_TOO_YOUNG'
 elif a in('V','U'):
  q=1j if a=='U'and p==-1+1j else 0j;assert need.get(q-p)is False or q-p in K
  for src in((4,5,6)if a=='V'else(7,8,9)):
   assert q in G[src][4]
   for n in range(5):
    h=(-n)%4
    for dst in ids:
     for slot in G[dst][3]:
      pp=q-rotation(slot,h);hb=(src,dst,*xy(pp),h,*xy(q));cq=(mp[src],mp[dst],*xy(pp),h,*xy(q),n)
      if n<counts[src]:reason='BEFORE_FULL_SOURCE_EXIT'
      elif(int(pp.real+pp.imag)+h)%2:reason='WRONG_SECTOR'
      elif hb in HB:reason='SIGNED_HB_EXCLUDED'
      elif cq in C5:reason='SIGNED_COUNT5_EXCLUDED'
      else:
       ep=pp+rotation(G[base[dst]][0],h);c0=2*pp+rotation(-1-1j,h);c1=2*ep+rotation(-1-1j,h)
       if meet(-1-1j,-1-1j+atoms[a][3],c0,c1):assert n>=2;reason='EARLIER_NONADJACENT_CLOSED_CENTER_CONTACT'
       elif b!='C'and n+counts[dst]>4:reason='CONSUMING_FULL_PACKET_CANNOT_FINISH_BEFORE_TARGET_BASE'
       else:
        end=pp+rotation(G[dst][0],h);eh=(h+G[dst][1])%4;assert n+counts[dst]==4 and eh==0 and not zero_reach(end,p,0);reason='EXACT_FINAL_ZERO_C_SEMIGROUP_CANNOT_REACH_TARGET'
      queries.append((gi,src,dst,n,xy(slot),xy(pp),reason))
  why='MANDATORY_HARD_COHORT_RETIREMENT_IMPLIES_EARLIER_CONTACT_OR_IMPOSSIBLE_ZERO_CONE'
 else:assert a in('D','C')and b=='C'and p==-1-1j;why='OPEN_D_OR_C_TO_C_GATE'
 red.append((gi,why))
assert len(core)==45 and len(queries)==1725
# Actual complete board and ordered current-residual ledger, not just turn constraints.
word=(1,0,5,5,6);seed={complex(x,y)for x,y in[(-5,2),(-4,1),(-3,-1),(-3,3),(-2,0),(-2,4),(-1,-1),(-1,0),(0,-1),(0,0),(0,1),(0,2),(1,0)]};board=set(seed);ledger=board-K;pose=0j;h=0;raw='';edges=[];clock=0
for src in word:
 assert all((pose+rotation(z,h)in board)==bit for z,bit in G[src][2].items())
 II={pose+rotation(z,h)for z in G[src][3]};OO={pose+rotation(z,h)for z in G[src][4]};assert II<=ledger;ledger-=II;assert not(ledger&OO);ledger|=OO
 for an,wrd in[('D'if base[src]==0 else'V'if base[src]==4 else'U',raws[base[src]])]+[('C',C)]*counts[src]:
  start=2*pose+rotation(-1-1j,h);oldclock=clock
  for c in wrd:
   assert(pose in board)==(c=='L');board.symmetric_difference_update({pose});h=(h+(1 if c=='R'else-1))%4;pose+=(1j,1,-1j,-1)[h]
  clock+=an=='C';edges.append((an,oldclock,start,2*pose+rotation(-1-1j,h)));raw+=wrd
 assert board-{pose+rotation(z,h)for z in K}==ledger
assert len(raw)==149 and(pose,h)==(-1,3)and len(edges)==10 and clock==5
for c in mark:
 assert(pose in board)==(c=='L');board.symmetric_difference_update({pose});h=(h+(1 if c=='R'else-1))%4;pose+=(1j,1,-1j,-1)[h]
contacts=[(i,j)for i in range(10)for j in range(i+2,10)if meet(edges[i][2],edges[i][3],edges[j][2],edges[j][3])];assert contacts==[(0,9)]and edges[9][1]==4
history={};p=0j;h=0;bad=None
for t,c in enumerate(raw*2):
 if p in history and history[p][1]==c:bad=(t,xy(p),history[p][0]);break
 history[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
assert bad==(160,(-2,0),120)
# Author finite outputs checked below by exact keys.
auth={(r['geometry_index'],r['full_source'],r['consumer'],r['entry_C_age'],tuple(r['consumer_input'])):r for r in J['all_1725_hard_retirement_options']};assert len(auth)==1725
for gi,src,dst,n,slot,pp,why in queries:assert auth[gi,src,dst,n,slot]['reason']==why and tuple(auth[gi,src,dst,n,slot]['consumer_pose'])==(*pp,(-n)%4)
assert dict(red)=={r['geometry_index']:r['reason']for r in J['all_geometry_reductions']}
out=dict(status='PASS independent four-C canonical contact gate and actual13-cell sharpness',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometries=[(a,b,xy(p),str(s),str(t))for a,b,p,s,t in geoms],reductions=red,upper_age_queries=len(upper),core_age_cases=core,retirement_queries=queries,positive_word=word,seed=sorted(map(xy,seed)),unique_nonadjacent_contact=contacts,double_word_first_conflict=bad,scope='At first center contact with entry gap4 only D/C-to-C(-1,-1,N) remains. D-to-C is physically attained by13-cell DC,D,VC,VC,VCC with actual marker and current ledger; endpointclock5, not samefullpose or renewal. No no-contact/global-budget claim.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('core_age_cases','retirement_queries')})
