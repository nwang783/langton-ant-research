from pathlib import Path
from collections import Counter
from itertools import permutations
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_returned_V_source_reduction_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
walk,W,M,xy,raw,ctx,I,outputs,K=[ns[x]for x in('walk','W','M','xy','raw','ctx','I','outputs','K')]
AR={n:walk(W[n])for n in'DCVU'};AC={n:walk(W[n]+M)for n in'DCVU'}
AO={n:({q for q,b in AC[n]['req'].items()if b}^AR[n]['odd'])-{AR[n]['p']+q*(-1j)**AR[n]['h']for q in K}for n in'DCVU'}
assert all(q.imag>=0 and q.real+q.imag>=0 for s in AO.values()for q in s)
b,bp,g,g1,gm,z,beta=2,3+1j,0,1j,-1-1j,-1j,1-1j
for n in('D','DC'):
 assert[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==gm]==[(2,'L')]
 assert[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==z]==[(3,'L')]
 assert gm not in outputs[n]and z not in outputs[n]
first=[];prev=[]
for n in'DCVU':
 a=AR[n];rr=a['reads']
 assert[(i,c)for i,(q,h,c)in enumerate(rr)if q==-1-1j]==[(2,'L')]
 assert[(i,c)for i,(q,h,c)in enumerate(rr)if q==-1]==[(1,'L')]
 assert[(i,c)for i,(q,h,c)in enumerate(rr)if q==2][-1]==(8,'R')
 first.append((n,xy(1+1j),xy(bp)))
 h=-a['h']%4;e=-a['p']*(-1j)**h;o={'D':2,'C':1+2j,'V':2+2j,'U':1+3j}[n]
 assert e+o*(-1j)**h==beta;prev.append((n,xy(e),h,xy(beta)))
mins=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())['slots'];assert mins['4:(1, 2)']['certified_minimum_C_age']==3 and mins['4:(0, 3)']['certified_minimum_C_age']==2 and mins['7:(0, 3)']['certified_minimum_C_age']==5
roles=[];E=[]
def ctr(p,h):return 2*p+(-1-1j)*(-1j)**h
for h in(2,1):
 for n in'DCVU':
  for o in sorted(AO[n],key=xy):
   e=gm-o*(-1j)**h;end=e+AR[n]['p']*(-1j)**h
   if(int(e.real+e.imag)+h)%2:why='sector'
   elif b in{e+q*(-1j)**h for q in AC[n]['req']}:why='held_bud_context'
   elif n=='C'and h==1:why='late_C4'
   elif h==2:
    if ctr(e,h)in(-1-1j,1+1j):why='old_D_vertex_repeat'
    elif n=='V':assert e==1+1j and e+(1+2j)*(-1j)**h==z;why='deleted_selected_min3'
    else:assert n=='U'and e==2j and e+3j*(-1j)**h==z;why='deleted_upper_min5'
   elif ctr(end,h)==1+1j:why='old_D_exit_repeat'
   elif n=='U'and o==-1+2j:
    assert e==-3-2j and e+(-1+2j)*(-1j)**h==gm
    assert[(i,c)for i,(q,hh,c)in enumerate(AR[n]['reads'])if q==o]==[(13,'L'),(21,'R')];why='earliest_rebirth_circular_true_input'
   else:assert(n,e,end)==('V',-2-1j,1-2j);why='sole_E3_origin';E.append(end)
   roles.append((h,n,xy(o),xy(e),xy(end),why))
assert len(roles)==38 and E==[1-2j]
def counts(delta,heading='E'):
 x,y=xy(delta);out=[]
 if heading=='N':
  for v in range(max(0,x+1)):
   d=x-v;rem=y-d-3*v
   if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 else:
  down=-y
  for v in range(max(0,down+1)):
   d=down-v;rem=x-d-3*v
   if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
def ends(identity,target,f,ix):
 rr=[]
 for n in'DVU':
  for q in sorted(I[n],key=xy):
   e=identity-q*(-1j);end=e+AR[n]['p']*(-1j);sol=counts(target-end)
   assert end!=target and all(u==0 and(v==0 or f=='B')for d,v,u in sol)
   rr.append((ix,xy(identity),n,xy(q),xy(e),xy(end),sol))
 return rr
# Exhaust clock1 N/C/W stages from endpoint equations, not a search depth.
portal={};rejected=[]
for f,target in [('F',-3+4j),('Q',-5+4j),('B',-6+3j)]:
 found=set()
 for nd in range(int(target.imag)-1):
  total=int(target.imag)-2-nd
  for v in range(total+1):
   d=total-v;rem=1+nd-d-3*v-int(target.real)
   if rem<0 or rem%4:continue
   u=rem//4
   for tup in set(permutations('D'*d+'V'*v+'U'*u)):
    s=''.join(tup)
    if not s or s[-1]not in('VU'if f!='B'else'U'):continue
    if s[0]=='U':rejected.append((f,nd,s));continue
    found.add('D'*(nd+1)+'C'+s+f+'V')
 portal[f]=sorted(found)
assert set(sum(portal.values(),[]))=={'DCDVFV','DDCDUFV','DCDDUQV','DCVVQV','DDCVUQV','DCVUBV'}
cat=json.loads((ROOT/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases'];D=ROOT/'returned_D_source_join_2026-10-24';ref=json.loads((D/'D_source_join.json').read_text());by={r['case']:r for r in ref['all60_D_source_rows']};summary=Counter();rows=[];ee=[];head=[]
for ix,r in enumerate(cat):
 if r['source_atom']!='D':continue
 f,t=r['foreign'],r['returned_atom'];e=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2];age=r['source_to_foreign_C_age'];c=walk(W[f]+W[t]+M);assert c['feasible'];mask={e+q*(-1j)**h:v for q,v in c['req'].items()};core={e+q*(-1j)**h for q in K};guard=None
 if age==2:
  assert mask[beta]is False;guard=beta;kind='actual_previous_atomic_exit_bud_age2_before_WHITE'
 elif age<=1:
  if mask.get(g)is True:guard=g;kind='first_post_D_deleted_00_has_no_N0_or_W1_rebirth'
  elif mask.get(b)is False:assert age==1;guard=b;kind='genuine_D_R8_common_bud_current_age1_before_WHITE'
  elif age==0 and mask.get(g1)is True:guard=g1;kind='first_post_D_deleted_01_has_no_clock0_N_rebirth'
  elif age==0:
   assert t=='V';sol=counts(e-(1+1j),'N');head.append((ix,sol))
   if f=='F':assert all(v==u==0 for d,v,u in sol);kind='clock0_head_count_has_no_actual_allowed_last_foreign_packet'
   else:
    word='DDDVQV'if f=='Q'else'DDDUBV';bad=walk(''.join(W[n]for n in word)+M);assert not bad['feasible']and bad['q']==1+2j and bad['i']==(113 if f=='Q'else 133)
    assert sol==([(2,1,0)]if f=='Q'else[(2,0,1),(0,2,0)]);kind='clock0_forced_word_actual_deleted_core_conflict'
  else:assert(f,e)in[('F',-3+4j),('Q',-5+4j),('B',-6+3j)]and t=='V';kind='six_attained_D_entry_connectors_have_complete_finite_no_U_entry_predecessor_closure'
 else:
  assert age==3 and h==1
  if mask.get(bp)is False:guard=bp;ee+=ends(bp,e,f,ix);kind='first_actual_post_D_common_R8_bud_E3_endpoint_guard'
  elif mask.get(b)is False:guard=b;ee+=ends(b,e,f,ix);kind='original_D_R8_common_bud_E3_endpoint_guard'
  elif ix in(6,54):
   assert mask[gm]is True and f=='F';guard=gm;ee+=ends(b,e,f,ix);sol=counts(e-E[0]);assert all(v==u==0 for d,v,u in sol);head.append((ix,sol));kind='spatially_unretirable_D_bud_plus_deleted_minus11_rebirth_guard'
  else:assert ix in(15,30);kind='OPEN_necessary_clock3_geometry_not_attained'
 if guard is not None:assert guard not in core;loc=(guard-e)*1j**h;firstread=next((i,ch)for i,(q,hh,ch)in enumerate(c['reads'])if q==loc);assert list(firstread)==by[ix]['actual_combined_first_read']
 assert kind==by[ix]['exclusion'];summary[kind]+=1;rows.append((ix,kind))
assert len(rows)==60 and len(ee)==128 and dict(summary)==ref['classification_counts']
mp=D/'manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='bdb22f14c223c6b1b9a157fa18191e17d38a9a009193c8600c444571399d6e28'
for a in json.loads(mp.read_text())['files']:assert hashlib.sha256((D/a['file']).read_bytes()).hexdigest()==a['sha256']
for f,h in ref['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
out={'status':'PASS 58 of60 old-D first-returned-contact labels excluded under actual U-entry ancestry; rows15/30 retained','manifest_sha256':mh,'classifications':dict(summary),'all38_deleted_minus11_origin_roles':roles,'all128_clearer_endpoint_obligations':ee,'four_real_prior_atomic_exit_interfaces':prev,'four_real_post_D_interfaces':first,'three_clock1_complete_endpoint_exhaustions':portal,'C_U_rejected_endpoint_words':rejected,'clock0_and_gm_endpoint_counts':head,'analytic':['Old D cannot be first atom of a U-entry factor. Its real immediately prior atomic exit supplies beta=(1,-1), with signed exit-bud clock zero at that actual exit. No fictitious fullproducer birth clock is assigned; both possible D/DC containing sources and prior internal C interfaces are retained.','Every source D base has a real following old atom because complete D-to-foreign adjacency is forbidden. Internal C1 of DC is allowed and starts clock0. Its common R8 birth and its original-source clock, not a shifted full completion clock, give bp maturity. Source D/DC deletions remain absent from own outputs and exit core.','Clock0 N and clock1 W cones exclude the required post-deletion g/g1 residual births. Exact clock1 equations force only six listed raw connectors, and independently signed all96 minimal V+M11 predecessor queries close their reverse trees without U-entry ancestry. These positive D-entry controls remain legal; no preforeign age law is used through the foreign.','At clock3 all prior full clearers must be plain E D/V/U, with all eight inputs retained. Full positive tails would complete too late. All128 endpoint tests include both target-local held-b proof and direct WHITE guards, arbitrary zero-C E lengths, and true final V/U adjacency.','For gm earliest-rebirth analysis, held b is established spatially for the particular target, not assumed permanent. Actual simple old path forbids source start/exit repeats; z was genuinely deleted, so V selected min3 and U upper min5 apply to any rebirth. V upper min2 is never replaced by min3. Recycled q requires the same gm residual before its new R, so cannot be its earliest rebirth. No missing S stage follows the final surviving E3 origin.'],'scope':'Only first new returned-atom contact catalogue, under genuine U-entry old-eight ancestry and one first foreign. Two D-source geometries remain; no returned simplicity or global capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
