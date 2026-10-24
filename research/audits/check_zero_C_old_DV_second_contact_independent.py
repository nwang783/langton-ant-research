from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
import hashlib,json,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'zero_preforeign_C_old_DV_slice_manifest.json';assert sha(man)=='5d1d4d312c60a1fbd9fb6b30a804ad66b47cff062f59d0e013d9d480d0ebdad7';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(ns['__file__']).read_text().split('triples=[]')[0],ns);W,M,walk,chord,pose,pieces,minus,cross,meet,xy=[ns[k]for k in['W','M','walk','chord','pose','pieces','minus','cross','meet','xy']];ref=json.loads((D/'zero_preforeign_C_old_DV_slice.json').read_text());ranks={'D':2,'C':2,'V':1,'U':0};boxes=[];geoms=[];rows=[]
for old in'DV':
 oc=chord(old);ov=minus(oc[1],oc[0]);ep,eh=pose(old);assert eh==0;ox,oy=xy(ep)
 for A in'FQB':
  pcs,ap,pts=pieces(A)
  for b1 in'DCVU':
   first=chord(b1,*ap);p2=pose(b1,*ap)
   for b2 in'DCVU':
    if b1=='C'and b2=='U':continue
    if b1!='C'and ranks[old]<=ranks[b2]:continue
    new=chord(b2,*p2);nv=minus(new[1],new[0]);assert cross(ov,nv)
    corners=[tuple(F(oc[0][k]+ss*ov[k]-new[0][k]-tt*nv[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bounds=[(math.floor(min(q[k]for q in corners)),math.ceil(max(q[k]for q in corners)))for k in(0,1)];boxes.append((old,A,b1,b2,bounds))
    for x in range(bounds[0][0],bounds[0][1]+1):
     for y in range(bounds[1][0],bounds[1][1]+1):
      if x<ox or y<oy or(x+y)%2:continue
      shift=lambda q:tuple(q[k]+2*(x,y)[k]for k in(0,1));hit=meet(*oc,*map(shift,new))
      if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
      bad=False
      for ii,pc in enumerate(pcs):
       z=meet(*oc,*map(shift,pc))
       if z is not None:
        trueadj=old=='V'and ii==0 and(x,y)==(ox,oy)and len(z)==3 and z[:2]==(F(1),F(0))
        if not trueadj:bad=True
      if meet(*oc,*map(shift,first))is not None:bad=True
      if bad:continue
      geoms.append((old,A,b1,b2,x,y,str(hit[0]),str(hit[1])))
      X,Y=x-ox,y-oy
      for v in range(X+1):
       d=X-v;rest=Y-d-3*v
       if rest<0 or rest%4:continue
       u=rest//4
       for run in sorted(set(permutations('D'*d+'V'*v+'U'*u))):
        last=run[-1]if run else old
        if last not in('VU'if A in'FQ'else'U'):continue
        tok=(old,)+run+(A,b1,b2);w=''.join(W[a]for a in tok)+M;zz=walk(w);assert not zz['feasible'];p=0j;h=0;prev={}
        for t,c in enumerate(w):
         if t==zz['i']:break
         prev[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
        assert p==zz['q']and prev[p][1]==w[t]
        rr=next(z for z in ref['all106_actual_N_run_whole_word_candidates']if tuple(z['tokens'])==tok);assert rr['foreign_pose']==[x,y,0]and rr['exact_N_run_counts']==dict(D=d,V=v,U=u)
        assert rr['result']['conflict_read']==t and rr['result']['previous_read']==prev[p][0]and rr['result']['cell']==list(xy(p))
        for ti,ownerfield in[(t,'later_conflicting_actual_physical_owner'),(prev[p][0],'previous_actual_physical_owner')]:
         off=0;actual=None
         for ii,a in enumerate(tok):
          if ti<off+len(W[a]):actual=(a,ti-off);break
          off+=len(W[a])
         owner=rr[ownerfield]
         if actual:assert owner['actual_raw_name']==actual[0]and owner['RAW_tick0']==actual[1]and owner['physical_read_number1']==actual[1]+1
         else:assert owner['role']=='next_actual_word_RAW'and owner['RAW_tick0']==ti-off and owner['physical_read_number1']==ti-off+1
        rows.append((tok,x,y,t,prev[p][0],xy(p)))
assert len(boxes)==45 and len(geoms)==67 and len(rows)==106 and len({z[0]for z in rows})==106
assert Counter(z[0][0]for z in rows)=={'D':79,'V':27};assert Counter(z[0][-3]for z in rows)=={'F':20,'Q':53,'B':33}
rf={(q['old_source'],q['foreign'],q['first_ordinary'],q['second_ordinary'],*q['foreign_head'][:2],str(F(*q['source_contact']['s'])),str(F(*q['source_contact']['t'])))for q in ref['all67_source_geometry_heads_clear_through_firstordinary']};assert rf==set(geoms)
out={'status':'PASS complete zero-preforeign-C old-D/V SECOND-contact slice only','author_manifest':sha(man),'exact_boxes':45,'source_geometries_after_prior_clearance':67,'all_complete_N_run_words':106,'by_source':{'D':79,'V':27},'by_foreign':{'F':20,'Q':53,'B':33},'fresh_wholeword_conflicts':rows,'analytic_review':[
'At actualn0, sourcefull mustplainD/V; any ownCtail would already make agepositive. With b1notC, alphaold>alphab2 yields DtargetsV/U andVtargetU. Withb1C alltargets allowed by angle, but CU literal conflict removesU. Exactly45 choices, each with nonzero chord determinant.',
'Every head bound comes from the four rational contact-parallelogram corners. Exact outgoingownership0<=s<1 and newtime0<t<=1 is retained. Foreign andfirstreturned must already avoid oldsource. The ONLY permitted source-toforeign adjacency is sourceV END to foreignSTART at its actual same pose/heading with empty interveningrun. Collinear earlier overlaps are rejected, not silently omitted.',
'From Dexit1,1 or Vexit1,3, alloldN packets yield x=x0+d+v,y=y0+d+3v+4u. Exactx fixes finitev range andydeterminesu; ALL permutations and actual complete lastV/U foreign rules are checked. This exhausts arbitrary runlength without a chosen depth bound.',
'All106 unique wholeword+actualM11 candidates have immutable equal consecutive cell reads. Fresh physical trajectories confirm both timestamps and both actualRAW owners, including terminalnextwordprefix owners. No external or earlier initialboard can repair an internal equal-read conflict.',
'Only these oldD/Vn0 contacts are excluded. Together with independently signed oldUn0 and actual oldC requiringn>=1, every possible genuine oldsource secondcontact would need at leastoneC BEFOREforeign. The effective tangentN may additionally include b1C, but is not a producer funding clock. No n>=1, general secondatomsimplicity or capture theorem follows.' ]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
