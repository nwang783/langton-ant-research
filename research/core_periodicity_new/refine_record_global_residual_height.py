"""Add a global upper bound on residual-token height to a frozen band model.
CLI FIRST_FAR_TRANSVERSE_MODEL.json PREFIX. Every old spatial/color constraint
is retained. New low-order bits encode Q-F; colors are shifted uniformly.
The initial global whitening bound is F=floor((S-I-1)/2). This is a semantic
refinement, not a completed record theorem without a no-hit invariant.
"""
from pathlib import Path
import json,sys,hashlib,math
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='guarded_reset_global_record_far_transverse_bands_v1'
H=json.loads(Path(J['height_model_file']).read_text());assert H['format']=='guarded_reset_global_record_far_height_first_funding_v1'
B=json.loads(Path(J['base_model_file']).read_text());from resource_profile import load_profile
P,D,M=load_profile(Path(B['resource_profile_file']));G=D['geometry']['geometry'];phase=B['target_global_phase'];S=B['record_threshold'];I=B['initial_token_weight'];A=B['core_offsets'];T={(a,h):t for a,h,t in B['created_peaks']};F=(S-I-1)//2;near=len(B['poses']);cut=H['lower_cutoff'];keep=B['keep']
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(q):return sum(rot(q,phase))
mi={(a,h):max(ht(rot(q,h))for q in G[a]['inputs'])for a in keep for h in range(4)}
mo={(a,h):max(ht(rot(q,h))for q in G[a]['outputs'])for a in keep for h in range(4)}
limit={(a,h):(S-1-max(A[(h+phase)%4],T[a,(h+phase)%4]))//2 for a in keep for h in range(4)}
Qcap=max([F]+[lim-(lim-h)%2+mo[a,h]for(a,h),lim in limit.items()]);qb=max(1,(Qcap-F).bit_length());qmask=(1<<qb)-1

def coord(p):
 if p<near:
  x,y,h=B['poses'][p];q=ht((x,y));return h,q,q
 k,h,q,bi=J['far_controls'][p-near];return h,q,cut if q is None else q

def anyq(lo,hi,h):return lo is None or lo+(h-lo)%2<=hi
relations=[];rdetails=[]
for ei,e in enumerate(J['geometric_edges']):
 fr,to=e[:2];a=e[8];assert a in keep;goal=bool(e[7]);first=fr==J['geometric_initial_control']
 if first:
  oldi=J['geometric_edge_provenance'][ei][1];why=H['geometric_edge_provenance'][oldi]
  if why[0]=='first_far':
   h,q=why[1:3];lo=q;hi=cut if q is None else q
  else:
   assert why[0]=='first_entry';_,aa,x,y,h,_,_=why;assert aa==a;lo=hi=ht((x,y))
 else:h,lo,hi=coord(fr)
 delta=ht(rot(G[a]['endpoint'][:2],h))
 if not goal:
  hh,dl,du=coord(to);assert hh==(h+G[a]['endpoint'][2])%4
  if dl is not None:lo=dl-delta if lo is None else max(lo,dl-delta)
  hi=min(hi,du-delta,limit[a,h])
 if first:hi=min(hi,F-mi[a,h])
 rr=[]
 for Q in ([F]if first else range(F,Qcap+1)):
  upper=min(hi,Q-mi[a,h]);upper-=(upper-h)%2
  if not anyq(lo,upper,h):continue
  if goal:rr.append([Q,Q]);continue
  for Q2 in range(Q,Qcap+1):
   if Q2==Q:ok=anyq(lo,min(upper,Q-mo[a,h]),h)
   else:
    q=Q2-mo[a,h];ok=(q-h)%2==0 and q<=upper and(lo is None or q>=lo)
   if ok:rr.append([Q,Q2])
 relations.append(rr);rdetails.append({'heading':h,'source_height_lower':lo,'source_height_upper':hi,'input_offset':mi[a,h],'output_offset':mo[a,h],'first':first,'goal':goal})
TT=[];emap=[]
for ti,t in enumerate(J['transitions']):
 ei=J['edge_map'][ti][0]
 for Q,Q2 in relations[ei]:
  fr,to,k,v,f,c,r,g,a=t;TT.append([fr,to,(k<<qb)|qmask,(v<<qb)|(Q-F),f<<qb,(c<<qb)|qmask,(r<<qb)|(Q2-F),g,a]);emap.append([ti,Q,Q2])
n=J['n']+qb;start=[J['start'][0],(J['start'][1]<<qb)|qmask,J['start'][2]<<qb]
N={'format':'guarded_reset_global_record_residual_height_bound_v1','n':n,'out':J['out'],'start':start,'reentry':[],'transitions':TT,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'initial_height_bound':F,'height_upper_bound':Qcap,'height_bits':qb,'color_bit_shift':qb,'geometric_height_relations':relations,'geometric_relation_details':rdetails,'edge_map':emap,'scope':'After global existential high-initial-residual whitening, Q is a monotone upper bound on every residual identity height, including cells outside the retained patch. Each packet requires all residual inputs at height<=Q and raises Q to max(Q,max output height). Core cells are separate. Existing first-far funding, spatial bands, literal DFA and exact retained residual colors remain in force.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {N['out']+1} {len(TT)} 0\n");f.write(' '.join(map(str,start))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':n,'Q_bits':qb,'Q_range':[F,Qcap],'positions':N['out']+1,'edges':len(TT)}))
