"""Complete predecessor reduction for the signed four U1 age-four cohorts.
No depth cap: the one-C-source forced turn uses an unbounded monotonicity lemma.
"""
from pathlib import Path
import json,hashlib,collections
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];RP=W/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';M=json.loads(RP.read_text());A=M['core_offsets'];T={(a,h):v for a,h,v in M['created_peaks']};keep=[0,1,4,5,6,7,8,9]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def peak(a,p,h):return 2*(p[1]-p[0])+max(A[(h+1)%4],T[a,(h+1)%4])
def check_literal(chain):
 need={};par=set()
 for i,(a,p,h)in enumerate(chain):
  for x,y,bit,*_ in G[a]['requirements']:
   z=add(p,rot((x,y),h));r=bool(bit)^(z in par)
   if z in need and need[z]!=r:return dict(packet_index=i,packet=a,cell=z,earlier_initial_bit=need[z],later_initial_bit=r)
   need[z]=r
  for q in G[a]['raw_odd']:
   z=add(p,rot(q,h))
   if z in par:par.remove(z)
   else:par.add(z)
 return None
# W-heading zero-C packets raise H; after ANY such step no positive-C packet fits.
zero_H=[rot(G[a]['endpoint'][:2],3)[1]-rot(G[a]['endpoint'][:2],3)[0]for a in[0,4,7]];assert zero_H==[2,4,4]
positive_caps={a:(29-max(A[0],T[a,0]))//2 for a in keep if G[a]['name'].count('C')};assert positive_caps=={1:6,5:4,6:0,8:4,9:0}
assert[ a for a in positive_caps if 5<=positive_caps[a]]==[1]
rows=[]
for s,ps in[(5,(-4,-2)),(6,(-4,-2)),(8,(-3,-3)),(9,(-3,-3))]:
 cs=G[s]['name'].count('C');se=add(ps,G[s]['endpoint'][:2]);sh=G[s]['endpoint'][2];assert (se,sh)==(((-3,2),3)if cs==1 else((-4,2),2))
 assert min(28+2*((ps[1]+y)-(ps[0]+x))for x,y in G[s]['inputs'])>30
 for a in keep:
  ca=G[a]['name'].count('C');ha=ca;pa=sub(ps,rot(G[a]['endpoint'][:2],ha));r=dict(source=s,source_pose=[*ps,0],predecessor=a,predecessor_pose=[*pa,ha],predecessor_peak=peak(a,pa,ha))
  if r['predecessor_peak']>=30:r['reason']='STRICT_RECORD_REJECTED'
  else:
   pair=[(a,pa,ha),(s,ps,0)];conflict=check_literal(pair)
   if conflict is not None:r.update(reason='PAIR_LITERAL_REJECTED',conflict=conflict)
   elif ca==2:
    assert s==5 and cs==1
    conflict=check_literal(pair+[(1,se,3)]);assert conflict is not None and conflict['packet_index']==2
    r.update(reason='FORCED_DC_THREE_PACKET_LITERAL_REJECTED',conflict=conflict)
   else:
    assert ca==0 and a in[0,4,7];r['reason']='ZERO_C_PREDECESSOR_NECESSARY_SUPERSET'
  rows.append(r)
counts=collections.Counter(r['reason']for r in rows);assert counts=={'STRICT_RECORD_REJECTED':10,'PAIR_LITERAL_REJECTED':8,'FORCED_DC_THREE_PACKET_LITERAL_REJECTED':2,'ZERO_C_PREDECESSOR_NECESSARY_SUPERSET':12}
O=dict(status='AUTHOR_U1_AGE4_PREDECESSOR_REDUCTION_PASS',scope='Strict unfunded outer U1, produced q age4 only. Uses signed four full-record source templates. Producer cannot be factor-first by initial activations, and its immediate predecessor must be zero-C D/V/U. One-C sources additionally have forced following DC. Does not exclude q4 or prove older support descent.',rows=rows,counts=counts,W_zero_C_height_increments=zero_H,W_positive_C_head_height_caps=positive_caps,common_two_C_return_starts=[[[-4,2,2],2],[[-5,3,2],2]],dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,W/'u1_minclock_cohort_frozen_20261023_1118/manifest.json',W/'u_lower_pair_equivalence_frozen_20261023_1146/manifest.json',Path(__file__).resolve()]})
(W/'chronology_dcuv/U1_age4_predecessor_reduction.json').write_text(json.dumps(O,indent=2)+'\n');print(dict(counts));print(json.dumps([r for r in rows if r['reason'].startswith('FORCED')],indent=2))
