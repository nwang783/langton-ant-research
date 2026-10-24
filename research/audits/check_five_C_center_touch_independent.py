from pathlib import Path
from collections import Counter
import math
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/five_C_center_touch_frozen_20261023_1550';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_five_C_center_touch.json').read_text());steps={'D':1+1j,'C':1+1j,'V':1+3j,'U':4j};center=-1-1j;geoms=[]
for a,u0 in steps.items():
 for b,v0 in steps.items():
  u=2*u0;v=rotation(2*v0,3);corners=[center-rotation(center,3)+s*u-t*v for s in(0,1)for t in(0,1)]
  for x in range(math.ceil(min(z.real for z in corners)/2),math.floor(max(z.real for z in corners)/2)+1):
   for y in range(math.ceil(min(z.imag for z in corners)/2),math.floor(max(z.imag for z in corners)/2)+1):
    if(x+y+3)%2:continue
    p=complex(x,y);z=2*p+rotation(center,3)-center;den=det(u,v);s=Fraction(det(z,v),den);t=Fraction(det(z,u),den)
    if 0<=s<1 and 0<t<=1 and not(0<s<1 and 0<t<1):geoms.append((a,b,xy(p),s,t))
assert len(geoms)==24 and set(geoms)=={(r['a'],r['b'],tuple(r['p']),Fraction(r['s']),Fraction(r['t']))for r in J['all_24_geometries']}
geo={i:(r['a'],r['b'],complex(*r['p']))for i,r in enumerate(J['all_24_geometries'])};roles=[]
for src in ids:
 atom='D'if base[src]==0 else'V'if base[src]==4 else'U';roles.append((atom,src,0j,0,0,counts[src]))
 for j in range(counts[src]):
  p,h,_,_=walk(raws[base[src]]+C*j);roles.append(('C',src,p,h,j,counts[src]-j))
assert len(roles)==15
for r,(a,src,p,h,j,rem)in zip(J['all_15_source_roles'],roles):assert(r['atom'],r['source'],tuple(r['p']),r['h'],r['shift'],r['remaining'])==(a,src,xy(p),h,j,rem)
need={a:G[b][2]for a,b in [('D',0),('V',4),('U',7)]};need['C']=walk(C+mark)[2]
outputs={a:G[b][4]for a,b in [('D',0),('V',4),('U',7)]};ce,ch,_,odd=walk(C);outputs['C']=(K^odd)-{ce+rotation(q,ch)for q in K}
def closed(a,dst,p,h):
 ep=p+rotation(G[base[dst]][0],h)
 return meet(center,center+2*steps[a],2*p+rotation(center,h),2*ep+rotation(center,h))
def one(p,t,h):
 z=rotation(t-p,-h);X,Y=int(z.real),int(z.imag)
 if Y<1:return False
 return any(zero_reach(0,complex(x,y),0)and zero_reach(complex(x,y+1),complex(X,Y),3)for y in range(Y)for x in range(y+1))
def retirement(a,q,b,target):
 rows=[]
 for ri,(atom,src,sp,sh,j,rem)in enumerate(roles):
  if atom!=a:continue
  fo=sp+rotation(q,sh);assert fo in G[src][4]
  for n in range(6):
   h=(-n)%4
   for dst in ids:
    for slot in G[dst][3]:
     pp=q-rotation(slot,h);fp=sp+rotation(pp,sh);fh=(h+sh)%4;age=n+j
     hb=(src,dst,*xy(fp),fh,*xy(fo));cq=(mp[src],mp[dst],*xy(fp),fh,*xy(fo),min(age,5));ep=pp+rotation(G[base[dst]][0],h)
     if n<rem:why='BEFORE_FULL_SOURCE_EXIT'
     elif(int(fp.real+fp.imag)+fh)%2:why='WRONG_SECTOR'
     elif hb in HB:why='SIGNED_HB_EXCLUDED'
     elif cq in C5:why='SIGNED_COUNT5_EXCLUDED'
     elif closed(a,dst,pp,h):assert n>=2;why='EARLIER_NONADJACENT_CLOSED_CONTACT'
     elif b!='C'and n+counts[dst]>5:why='FULL_CONSUMER_CANNOT_FINISH_BEFORE_TARGET_BASE'
     elif n==5 and not zero_reach(ep,target,3):why='EXACT_ZERO_C_CONE_CANNOT_REACH_TARGET'
     elif n==4 and not one(ep,target,h):why='EXACT_ONE_C_CONE_CANNOT_REACH_TARGET'
     else:why='RESIDUAL_OPTION'
     rows.append(dict(role=ri,src=src,n=n,dst=dst,slot=xy(slot),pose=(*xy(pp),h),ep=ep,hb=hb,cq=cq,why=why))
 return rows

def compare(rows,auth,change=None):
 ref={(r['source_role_index'],r['atomic_entry_C_gap'],r['consumer'],tuple(r['consumer_input'])):r for r in auth};assert len(rows)==len(ref)
 for r in rows:
  ar=ref[r['role'],r['n'],r['dst'],r['slot']];why=change(r)if change and r['why']=='RESIDUAL_OPTION'else r['why']
  assert ar['reason']==why and tuple(ar['consumer_pose'])==r['pose']and tuple(ar['counted_query'])==r['cq']and tuple(ar['HB_query'])==r['hb']

def secondary(r,b,p):
 if r['n']==3:
  assert r['dst']in(4,5)and r['pose']==(0,1,1);local=rotation(2-1j-p,1)
  assert local in K or(b=='U'and local==-1+1j)
  return'FRESH_V_EXIT_BUD_STILL_CURRENT_IN_TARGET_CORE_OR_TOO_YOUNG_U_LOWER'
 assert b=='U'and p==1 and r['n']==5 and(r['dst'],r['pose'])in((4,(4,-1,3)),(7,(5,0,3)))and r['ep']==p
 return'OPEN_IMMEDIATE_V_OR_U_PREDECESSOR_OF_TARGET_U'
primary=0;hardcases=0;gate=[]
assert len(J['hard_retirement_tables'])==20
for table in J['hard_retirement_tables']:
 gi=table['geometry_index'];a,b,p=geo[gi];q=complex(*table['hard_source_output']);assert q in outputs[a]
 local=rotation(q-p,1);assert local in K or need[b].get(local)is False
 rs=retirement(a,q,b,p);opened=[r for r in rs if r['why']=='RESIDUAL_OPTION'];primary+=len(rs)
 if opened:
  assert a=='D'and(b,p)in[('V',2-1j),('U',1+0j),('U',3+0j)]
  compare(rs,table['rows'],lambda r:secondary(r,b,p));gate.extend((gi,r['n'],r['dst'],r['pose'])for r in opened if r['n']==5)
 else:hardcases+=1;compare(rs,table['rows'])
assert primary==9522 and hardcases==17 and len(gate)==4
# Remaining four old-core/bud/positive-gate geometries are exactly accounted for.
left=set(geo)-{t['geometry_index']for t in J['hard_retirement_tables']}
assert {geo[i]for i in left}=={('D','D',-1j),('C','D',-1j),('C','C',-1j),('D','C',-1j)}
assert all(q.imag>=0 for a in ids for q in G[a][4])
oldroles=[]
for ri,(a,src,sp,sh,j,rem)in enumerate(roles):
 if a not in('D','C'):continue
 fq=sp+rotation(-1-1j,sh);assert fq not in G[src][4]
 if not rem:assert a=='D'and src==0 and G[0][0].imag>-1
 oldroles.append((ri,xy(fq)))
assert len(oldroles)==9 and set(oldroles)=={(r['role_index'],tuple(r['full_frame_cell']))for r in J['old_core_role_cases']}
age4=[];origins=[]
for src in ids:
 for o in G[src][4]:
  for dst in(0,1):
   pp=o-1j;hb=(src,dst,*xy(pp),0,*xy(o));cq=(mp[src],mp[dst],*xy(pp),0,*xy(o),4)
   why='WRONG_SECTOR'if int(pp.real+pp.imag)%2 else'SIGNED_HB_EXCLUDED'if hb in HB else'SIGNED_COUNT5_EXCLUDED'
   if why=='SIGNED_COUNT5_EXCLUDED':assert cq in C5
   age4.append((cq,hb,why))
   for atom in('D','C'):
    p=-1-1j+o;rp=rotation(-1j-p,-2);hb=(src,dst,*xy(rp),1,*xy(o));cq=(mp[src],mp[dst],*xy(rp),1,*xy(o),3)
    if(int(p.real+p.imag)+2)%2:why='WRONG_SECTOR'
    elif hb in HB:why='SIGNED_HB_EXCLUDED'
    elif cq in C5:why='SIGNED_COUNT5_EXCLUDED'
    elif closed(atom,src,p,2):why='EARLIER_CLOSED_CONTACT'
    else:
     assert src==0 and o==2 and p==1-1j
     ep=p+rotation(G[0][0],2);assert 2*ep+rotation(center,2)==-2j+rotation(center,3)
     why='PRODUCER_EXIT_CENTER_REPEATS_AT_TARGET_ENTRY_BEFORE_ENDPOINT_CONTACT'
    origins.append((atom,src,xy(o),dst,(*xy(p),2),cq,hb,why))
assert len(age4)==136 and set(age4)=={(tuple(r['query']),tuple(r['HB_query']),r['reason'])for r in J['all_136_D_input_exact_age_four_queries']}
assert len(origins)==272 and set(origins)=={(r['earlier_atom'],r['producer'],tuple(r['output']),r['target'],tuple(r['producer_pose']),tuple(r['query']),tuple(r['HB_query']),r['reason'])for r in J['all_272_old_core_clock_two_producer_cases']}
# Incoming actual-C predecessor bud and both complete prior helper-entry tables.
rs=retirement('C',1-1j,'C',-1j);assert len(rs)==966
def incoming_reason(r):
 if r['n']==3:
  assert r['src']==1 and r['dst']in(4,5)and r['pose']==(-2,-1,1)
  assert 2*r['ep']+rotation(center,1)==-2j+rotation(center,3)
  return'CLEARING_BASE_EXIT_CENTER_REPEATS_AT_TARGET_ENTRY'
 assert r['n']==5 and((r['dst']in(4,5,6)and r['pose']==(3,-2,3))or(r['dst']in(7,8,9)and r['pose']==(4,-1,3)))
 return'CLEARING_HELPER_NEEDS_UNRETIRABLE_OLD_C_COMMON_OUTPUT_WHITE'
compare(rs,J['all_966_C_incoming_bud_retirement_cases'],incoming_reason)
late=0
for tab in J['late_helper_common_output_tables']:
 atom=tab['helper_atom'];p=complex(*tab['helper_pose'][:2]);assert(atom,p)in[('V',3-2j),('U',4-1j)];assert need[atom][rotation(2-p,1)]is False
 rs=retirement('C',2+0j,atom,p);assert not any(r['why']=='RESIDUAL_OPTION'for r in rs);compare(rs,tab['rows']);late+=len(rs)
assert late==1932
# Direct literal control and full ordered core/residual replay.
sup=J['actual_sixteen_cell_control'];word=sup['word'];raw=''.join(raws[a]for a in word);req=walk(raw+mark)[2];seed={q for q,c in req.items()if c};assert len(seed)==16 and set(map(xy,seed))==set(map(tuple,sup['seed']))and len(raw)==190
field=set(seed);ledger={q:('entry',None)for q in seed-K};p=0j;h=0;clock=0;edges=[]
for pi,src in enumerate(word):
 assert field==set(ledger)|{p+rotation(q,h)for q in K} and not(set(ledger)&{p+rotation(q,h)for q in K})
 for q in G[src][3]:ledger.pop(p+rotation(q,h))
 for q in G[src][4]:z=p+rotation(q,h);assert z not in ledger;ledger[z]=(pi,clock)
 for atom,wr in [('D'if base[src]==0 else'V'if base[src]==4 else'U',raws[base[src]])]+[('C',C)]*counts[src]:
  begin=2*p+rotation(center,h);entry=(*xy(p),h);oldclock=clock
  for c in wr:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
  clock+=atom=='C';edges.append((atom,begin,2*p+rotation(center,h),oldclock,entry))
 assert field==set(ledger)|{p+rotation(q,h)for q in K}
for c in mark:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
# Every exact nonadjacent pair is reconstructed; earliest canonical point is D start/C end.
hits=[]
for bi,(_,b0,b1,bc,_)in enumerate(edges):
 for ai,(_,a0,a1,ac,_)in enumerate(edges[:max(0,bi-1)]):
  u=a1-a0;v=b1-b0;z=b0-a0;den=det(u,v)
  if den:
   s=Fraction(det(z,v),den);t=Fraction(det(z,u),den)
   if not(0<=s<=1 and 0<=t<=1):continue
  else:
   if det(z,u):continue
   axis=(lambda q:q.real)if v.real else(lambda q:q.imag);t0=Fraction(int(axis(-z)),int(axis(v)));t1=Fraction(int(axis(u-z)),int(axis(v)));t=max(Fraction(0),min(t0,t1));hi=min(Fraction(1),max(t0,t1))
   if t>hi:continue
   axis2=(lambda q:q.real)if u.real else(lambda q:q.imag);s=Fraction(int(axis2(z)),int(axis2(u)))+t*Fraction(int(axis2(v)),int(axis2(u)))
  hits.append((bi+t,ai,bi,s,t))
assert min(r[0]for r in hits)==12 and len(edges)==12
canon=set()
for time,ai,bi,s,t in hits:
 if time!=12:continue
 if s==1:ai+=1;s=0
 if t==0:bi-=1;t=1
 canon.add((ai,bi,s,t))
assert canon=={(0,11,0,1)}and edges[0][0]=='D'and edges[11][0]=='C'and edges[11][3]==5 and edges[11][4]==(0,-1,3)
prepend=[]
for src in ids:
 pp=0j;hh=0;last={};bad=None
 for tick,c in enumerate(raws[src]+raw+mark):
  if pp in last and last[pp]==c:bad=(tick,xy(pp),c);break
  last[pp]=c;hh=(hh+(1 if c=='R'else-1))%4;pp+=(1j,1,-1j,-1)[hh]
 assert bad is not None;prepend.append((src,bad))
assert {(a,t,p,c)for a,(t,p,c)in prepend}=={(r['prepend'],r['conflict']['tick'],tuple(r['conflict']['cell']),r['conflict']['prescribed'])for r in J['fixed_control_eight_prepended_packet_conflicts']}
out=dict(status='PASS independent five-C nonproper first-contact reduction and actual16-cell endpoint gate',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometries=24,primary_rows=primary,primary_hard_cases=hardcases,old_core_roles=9,age4_queries=136,birth2_origins=272,incoming_bud_queries=966,late_helper_rows=late,conditional_D_U_gate=gate,control=dict(mass=16,word=word,raw_length=190,first_path_contact=12,entry_C_gap=5,target_exit_C=6),prepends=prepend,scope='Nonproper five-C first contacts reduce to realD->C(0,-1,W) or D->U(1,0,W) with the independently specified late V/U helper. Signed1548 eliminates the latter conditional helper history, so only D->C remains after combination. Internal C targets retain unfinished consumer tails. No generic factor-entry-only law or global noncontact/capture claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
