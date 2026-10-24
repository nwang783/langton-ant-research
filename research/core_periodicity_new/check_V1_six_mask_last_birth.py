"""Same fixed six-mask, concrete UCC-q-origin original V1 branch, cap26. No path search."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';G=json.loads(GP.read_text())['geometry'];PP=W/'atomic_core_record_interface_frozen_20261023_1359/04_root_out.json';POT=json.loads(PP.read_text());AA=POT['core_offsets'];TT={tuple(x[:2]):x[2]for x in POT['created_peaks']};CP=W/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';IDS=[0,1,4,5,6,7,8,9];mp={x:i for i,x in enumerate(IDS)}
F=[(-1,1),(-1,2),(-1,4),(0,2),(0,3),(-2,3)];FS=set(F);HELP=(-1,5);S=26;creator_global_H=6;creator_global_phase=3;I=28
CWORD=G[1]['word'][len(G[0]['word']):]
def rot(p,h):x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def H(p):return p[1]-p[0]
def globalH(p):return creator_global_H-H(p)
def score(a,p,h):return 2*globalH(p)+AA[(h+creator_global_phase)%4],2*globalH(p)+TT[a,(h+creator_global_phase)%4]
def ctx(a,p,h):return {add(p,rot(z[:2],h))for z in G[a]['requirements']}
def center(p,h):return add((2*p[0],2*p[1]),rot((-1,-1),h))
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and sum((p[k]-a[k])*(p[k]-b[k])for k in[0,1])<=0
def touch(a,b,c,d):
 u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
 if z:
  s=Fraction(cross(r,v),z);t=Fraction(cross(r,u),z);return 0<=s<=1 and 0<=t<=1
 return any(on(p,a,b)and on(p,c,d)for p in[a,b,c,d])
def run(word,p,h):
 for ch in word:h=(h+(-1 if ch=='L'else 1))%4;p=add(p,rot((0,1),h))
 return p,h
def zeroN(dx,dy):
 if dx<0 or dy<dx:return None
 for v in range(dx+1):
  r=dy-dx-2*v
  if r>=0 and r%4==0:return dict(D=dx-v,V=v,U=r//4)
 return None
def oneC_E_to_N(dx,dy):
 # Three turning full types. Pre E and post N zero-C cones are exact.
 for a in[1,5,8]:
  tx,ty=rot(tuple(G[a]['endpoint'][:2]),1);R=dx-tx
  if R<0:continue
  for eu in range(R//4+1):
   for ev in range((R-4*eu)//3+1):
    for ed in range(R-4*eu-3*ev+1):
     px=ed+3*ev+4*eu;py=-ed-ev
     q=zeroN(R-px,dy-ty-py)
     if q is not None:return dict(pre_E=dict(D=ed,V=ev,U=eu),turn=a,post_N=q)
 return None
# Future source types and their mandatory q-consumer types remain separate.
placements={}
for a in IDS:
 for h in range(4):
  for o in G[a]['outputs']:
   for z in F:
    p=sub(z,rot(o,h));placements[a,*p,h]=(a,p,h)
rows=[];wanted=set()
for creator in[9]:
 for helper in[4]:
  future_ctx=ctx(creator,(0,0),0)|ctx(helper,HELP,2)
  for a,p,h in placements.values():
   O={add(p,rot(o,h)):tuple(o)for o in G[a]['outputs']};cohort=sorted(FS&O.keys());old=sorted(FS-O.keys());r=dict(creator=creator,helper=helper,producer=a,pose=[*p,h],new_final_cells=cohort,older_final_cells=old)
   if(sum(p)+h)%2:r['reason']='wrong_sector'
   else:
    en,cr=score(a,p,h);r.update(original_entry=en,original_created=cr)
    if max(en,cr)>=S:r['reason']='original_record_funding'
    elif ctx(a,p,h)&set(old):r.update(reason='complete_context_hits_older_final_identity',hits=sorted(ctx(a,p,h)&set(old)))
    elif len(set(cohort)&set(F[:5]))>=4:r['reason']='signed_max_three_same_producer_U_inputs'
    elif a in[7,8,9] and ({add(p,rot(z,h))for z in[(0,0),(0,1),(1,0),(1,1)]}&future_ctx):r['reason']='permanent_U_left_star_hits_actual_future_context'
    else:
     # Only a U-family earlier producer grants simplicity for its whole suffix.
     if a in[7,8,9]:
      pos=p;hh=h;arcs=[]
      for at in[7]+['C']*G[a]['name'].count('C'):
       X=center(pos,hh);pos,hh=run(CWORD if at=='C'else G[at]['word'],pos,hh);Y=center(pos,hh);arcs.append((X,Y))
      future_arcs=[]
      for name,fa,fp,fh in[('creator',creator,(0,0),0),('mandatory_helper',helper,HELP,2)]:
       fx=fp;ff=fh;fb=0 if fa in[0,1]else 4 if fa in[4,5,6]else 7
       for fj,at in enumerate([fb]+['C']*G[fa]['name'].count('C')):
        XX=center(fx,ff);fx,ff=run(CWORD if at=='C'else G[at]['word'],fx,ff);YY=center(fx,ff);future_arcs.append((name,fj,XX,YY))
      bad=[]
      for j,(X,Y)in enumerate(arcs):
       for name,fj,XX,YY in future_arcs:
        if touch(X,Y,XX,YY):
         if name=='creator'and fj==0 and j==len(arcs)-1 and pos==(0,0)and hh==0 and Y==(-1,-1):continue
         bad.append([j,name,fj])
      if bad:r.update(reason='U_producer_suffix_nonadjacent_center_contact',contact_atoms=bad)
     if 'reason'not in r:
      r['reason']='common_age_query_pending';r['age_cases']=[]
      # h = C gap modulo4. First5 are exact0..4; large case is >=5.
      kk=[k for k in range(5)if k%4==h]+[next(k for k in range(5,9)if k%4==h)]
      for k in kk:
       if G[a]['name'].count('C')>k:continue
       cc=dict(representative_age=k,age_class=min(k,5),queries=[])
       for z in cohort:
        if z==F[5]:target=helper;tp=HELP;th=2;age=k+2
        else:target=creator;tp=(0,0);th=0;age=k
        rel=rot(sub(tp,p),-h);key=(mp[a],mp[target],*rel,(th-h)%4,*O[z],min(age,5));wanted.add(key);cc['queries'].append(list(key))
       r['age_cases'].append(cc)
      r['forced_prior_produced_inputs']=[dict(slot=si,cell=add(p,rot(z,h)),activation=I+2*globalH(add(p,rot(z,h))))for si,z in enumerate(G[a]['inputs'])if I+2*globalH(add(p,rot(z,h)))>=S]
   rows.append(r)
excluded=set()
for line in CP.open():
 key=tuple(map(int,line.split()[:8]))
 if key in wanted:excluded.add(key)
for r in rows:
 if r['reason']!='common_age_query_pending':continue
 alive=[]
 for c in r['age_cases']:
  bad=[x for x in c['queries']if tuple(x)in excluded]
  if bad:c.update(reason='signed_count5_query_excluded',excluded_queries=bad);continue
  k=c['representative_age'];a=r['producer'];p=tuple(r['pose'][:2]);h=r['pose'][2];dx,dy,dh=G[a]['endpoint'];ep=add(p,rot((dx,dy),h));eh=(h+dh)%4;left=k-G[a]['name'].count('C')
  if k<5 and left in[0,1]:
   goal=sub((0,0),ep)
   if left==0:assert eh==0;q=zeroN(*goal)
   else:assert eh==1;q=oneC_E_to_N(*goal)
   if q is None:c['reason']='exact_zero_or_one_C_endpoint_cone';continue
   c['necessary_endpoint_counts']=q
  c['reason']='necessary_last_birth_obligation_not_attainment';alive.append(c)
 r['reason']='surviving_last_birth_obligation'if alive else'no_common_legal_age_and_timely_endpoint';r['surviving_age_cases']=alive
counts=dict(Counter(r['reason']for r in rows));surv=[r for r in rows if r['reason']=='surviving_last_birth_obligation'];D=[GP,PP,CP,Path(__file__).resolve()]+[W/s/'manifest.json'for s in['U_recycled_q_consumer_frozen_20261023_1954','U_max_three_cohort_frozen_20261023_1805','U_left_star_permanence_frozen_20261023_1918','U_entry_simplicity_frozen_20261023_1616','U_q_source_history_frozen_20261023_2027']]
R=dict(status='AUTHOR_FIXED_SIX_MASK_V1_LAST_BIRTH_NECESSITY_NOT_CLOSURE',scope='Concrete ORIGINAL unfunded V1 whose lower input is genuine UCC recycled-q. Creating UCC0,N has original globalH6 phase3, IMMEDIATELY followed by goal V(-1,5,S) at clock2. Fixed six mask I_U plus selected helper(-2,3), all genuinely produced/current before creator. Original record cap26, not enlarged history. Last-full-producer and same-clock final-identity survival only; surviving obligations are NOT actual prefixes or whole V1 closure. Plain-U q branch separate. No trajectory/depth/C cap.',fixed_six_mask=F,creator_original_global_H=6,creator_original_global_phase=3,threshold=S,raw_placements=len(placements),counts=counts,all_cases=rows,surviving_obligations=surv,needed_count_queries=len(wanted),matched_excluded_count_queries=len(excluded),dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/V1_six_mask_last_birth.json').write_text(json.dumps(R,indent=2)+'\n')
print(json.dumps(dict(placements=len(placements),counts=counts,survivors=len(surv),producer_counts=dict(Counter(x['producer']for x in surv))),indent=2))
for r in surv[:30]:print('SURV',r['creator'],r['helper'],r['producer'],r['pose'],r['new_final_cells'],[(c['representative_age'],c.get('necessary_endpoint_counts'))for c in r['surviving_age_cases']],r['forced_prior_produced_inputs'])
