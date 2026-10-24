from pathlib import Path
from collections import Counter
P=Path(__file__).resolve();SS=P.with_name('check_D_first_W5_gate_independent.py');exec(compile(SS.read_text().split('rows=[];late=[]')[0],str(SS),'exec'))
TT=P.with_name('check_atomic_crossing_contexts_independent.py');env={};exec(compile(TT.read_text().split('rows=[];start=')[0],str(TT),'exec'),dict(__file__=str(TT)),env) if False else None
# Fresh atomic masks from literal words plus actual marker.
atoms={}
for name,wrd in [('D',raws[0]),('V',raws[4]),('U',raws[7]),('C',C)]:
 e,dh,_,flips=walk(wrd);need=walk(wrd+mark)[2];bl={z for z,c in need.items()if c};O=(bl^flips)-{e+rotation(z,dh)for z in K};atoms[name]=(need,bl-K,O,2*e+rotation(-1-1j,dh)+1+1j)
B=ROOT/'core_periodicity_new/six_C_contact_frozen_20261023_1454';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
for rel,sha in M['external_immutable_inputs'].items():assert hashlib.sha256((D/rel).read_bytes()).hexdigest()==sha
J=json.loads((B/'02_six_C_first_contact_reduction.json').read_text());ranks={'D':2,'C':2,'V':1,'U':0};geoms=[];start=-1-1j
import math
for a,(_,_,O,da)in atoms.items():
 for b,(need,I,_,db)in atoms.items():
  if ranks[a]>=ranks[b]:continue
  db=-db;den=det(da,db);corners=[2*start+s*da-t*db for s in(0,1)for t in(0,1)]
  for x in range(math.ceil(min(z.real for z in corners)/2),math.floor(max(z.real for z in corners)/2)+1):
   for y in range(math.ceil(min(z.imag for z in corners)/2),math.floor(max(z.imag for z in corners)/2)+1):
    if(x+y)%2:continue
    pos=complex(x,y);off=2*pos-2*start;s=Fraction(det(off,db),den);t=Fraction(det(off,da),den)
    if not(0<=s<1 and 0<t<=1):continue
    forced=[];contacts=[]
    for q in O:
     local=pos-q
     if local in need:
      typ='INPUT'if local in I else'CORE'if need[local]else'WHITE';contacts.append((xy(q),typ))
      if typ!='INPUT':forced.append(q)
    geoms.append((a,b,pos,s,t,forced,contacts))
assert len(geoms)==8
AK={(r['first_atom'],r['later_atom'],tuple(r['later_pose'][:2])):i for i,r in enumerate(J['geometries'])}
def one_w_s(p,target):
 z=target-p;B=-int(z.real)-1
 if B<0:return False
 # W-zero displacement(-a,y) has 0<=y<=a<=B; independent semigroup membership.
 for a in range(B+1):
  for y in range(a+1):
   w=complex(-a,y)
   if zero_reach(0,w,3)and zero_reach(p+w-1,target,2):return True
 return False
queries=[];hardrows=[]
for a,b,pos,s,t,forced,contacts in geoms:
 gi=AK[a,b,xy(pos)];auth=J['geometries'][gi];assert Fraction(auth['earlier_parameter'])==s and Fraction(auth['later_parameter'])==t
 assert set(map(xy,forced))==set(map(tuple,auth['forced_prior_retirement_outputs']))
 hard=[]
 for q in forced:
  unresolved=[]
  for src in((4,5,6)if a=='V'else(7,8,9)):
   assert q in G[src][4]
   for n in range(7):
    h=(-n)%4
    for dst in ids:
     for slot in G[dst][3]:
      pp=q-rotation(slot,h);hb=(src,dst,*xy(pp),h,*xy(q));query=(mp[src],mp[dst],*xy(pp),h,*xy(q),min(5,n))
      if n<counts[src]:why='BEFORE_SOURCE_FULL_EXIT'
      elif(int(pp.real+pp.imag)+h)%2:why='SECTOR'
      elif hb in HB:why='SIGNED_HB'
      elif query in C5:why='SIGNED_COUNT5'
      else:
       ep=pp+rotation(G[base[dst]][0],h);c0=2*pp+rotation(start,h);c1=2*ep+rotation(start,h)
       if meet(start,start+atoms[a][3],c0,c1):assert n in(3,5,6);why='EARLIER_CLOSED_CONTACT'
       elif b!='C'and n+counts[dst]>6:why='FULL_TAIL_ENDS_AFTER_LATER_BASE'
       elif n==6 and not zero_reach(ep,pos,2):why='ZERO_C_BASE_EXIT_TO_TARGET_IMPOSSIBLE'
       elif n==5 and not one_w_s(ep,pos):why='ONE_C_BASE_EXIT_TO_TARGET_IMPOSSIBLE'
       else:why='UNRESOLVED_NONCONTACT_CLEARER';unresolved.append((src,n,dst,xy(slot)))
      queries.append((gi,src,xy(q),dst,xy(pp),h,xy(slot),n,why))
  if not unresolved:hard.append(xy(q))
 if forced:assert hard
 else:assert(a,b,xy(pos),s,t)==('U','V',(0,4),Fraction(1,2),1)and set(contacts)=={((-1,2),'INPUT'),((0,1),'INPUT')}
 hardrows.append((gi,sorted(hard)))
actual={(r['geometry_index'],r['source_full'],tuple(r['source_output']),r['consumer_full'],tuple(r['input']),r['source_age']):r for r in J['clearance_queries']};assert len(queries)==len(actual)==13524
for gi,src,q,dst,pp,h,slot,n,why in queries:
 rr=actual[gi,src,q,dst,slot,n];assert rr['reason']==why and tuple(rr['consumer_pose'])==(*pp,h)
for gi,hard in hardrows:assert hard==sorted(map(tuple,J['cases'][gi]['hard_outputs']))
old=[]
for src in(7,8,9):
 for dst in(4,5,6):
  for q in(-1+2j,1j):
   hb=(src,dst,0,4,2,*xy(q));cq=(mp[src],mp[dst],0,4,2,*xy(q),5);old.append((src,dst,xy(q),hb in HB,cq in C5))
assert sum(r[-2]for r in old)==3 and not any(r[-1]for r in old)
# UCC's entire complete producer finishes at C2. Any new output at either already-filled target cell has birth>=2, too young for VCC at C6.
assert counts[9]==2 and(9,6,0,4,2,-1,2)in HB
out=dict(status='PASS independent canonical six-C geometry and all timely-clearer cones',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),geometries=[(a,b,xy(p),str(s),str(t))for a,b,p,s,t,f,c in geoms],queries=queries,reason_counts=dict(Counter(r[-1]for r in queries)),hard_outputs=hardrows,old_cohort=old,scope='Seven of eight canonical gap6 first center contacts force an earlier nonadjacent CLOSED contact. Exact one-C W/S semigroup and internal-target unfinished full tails retained. U-to-V(0,4,S) input-only gate remains; only UCC-to-VCC tail combination additionally excluded. No attainability, renewal, fuel or global capture.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='queries'})
