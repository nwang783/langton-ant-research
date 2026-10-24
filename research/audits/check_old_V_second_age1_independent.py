from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_V_second_contact_age1_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='4c9dd20beb68a05afd5261efe03afd721a442a95dad2287f650b11b084659f37'
for f,h in json.loads(man.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'old_V_age1.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_U_second_creator_bud_guards_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nsource=[]')[0],ns);W,M,K=[ns[k]for k in('W','M','K')];V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];rot=lambda h:(-1j)**h;center=lambda p,h:2*p+(-1-1j)*rot(h);cross=lambda p,q:int(p.real)*int(q.imag)-int(p.imag)*int(q.real)
def tr(word,p=0j,h=0):
 rr=[];last={};req={};bad=None
 for i,c in enumerate(word):
  rr.append((p,h,c))
  if p not in last:req[p]=c=='L'
  elif last[p][0]==c and bad is None:bad=(i,last[p][1],p,c)
  last[p]=(c,i);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return dict(p=p,h=h,reads=rr,last=last,req=req,bad=bad)
G={a:tr(W[a])for a in'DCVUFQB'}
def meet(a,b,c,d):
 u=b-a;v=d-c;den=cross(u,v);z=c-a
 if den:
  s=F(cross(z,v),den);t=F(cross(z,u),den);return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if cross(z,u):return None
 ax=0 if u.real else 1;co=lambda p:int(p.real)if ax==0 else int(p.imag);s0=F(co(c-a),co(u));s1=F(co(d-a),co(u));lo=max(F(0),min(s0,s1));hi=min(F(1),max(s0,s1))
 if lo>hi:return None
 if lo<hi:return('OVERLAP',lo,hi)
 t=F(co(a-c),co(v))+lo*F(co(u),co(v));return(lo,t)
def pieces(seq):
 p=0j;h=0;out=[]
 for a in seq:
  z=G[a];c=center(p,h);en=p+rot(h)*z['p'];eh=(h+z['h'])%4;d=center(en,eh)
  if a in'QB':bend=2*p+(-7-3j)*rot(h);out.extend([(c,bend),(bend,d)])
  else:out.append((c,d))
  p,h=en,eh
 return out
# Universal produced minimum is used only at preforeign age0/1, including external-to-core absorption.
qmin=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert len(qmin['slots'])==23
for z in qmin['slots'].values():assert z['certified_minimum_C_age']>=2 and z['unexcluded_counts_0_to_4'][:2]==[0,0]and all('OPEN'not in r['reasons_0_through_4'][:2]for r in z['rows'])
sources={}
for src in('V','VC'):
 s=tr(''.join(W[a]for a in src));ek={s['p']+k*rot(s['h'])for k in K};O={p for p,(c,t)in s['last'].items()if c=='R'and p not in ek};assert len(O)==(6 if src=='V'else 9);sources[src]=(s,O)
# Reconstruct all16 pair boxes, exact rational contact and active sector.
geos=[];parallel_starts=[];a=-1-1j;v=2+6j
for b1 in'DCVU':
 for b2 in'DCVU':
  h=0 if b1=='C'else 1;c=center(0j,h);z=G[b2];vv=center(z['p']*rot(h),(h+z['h'])%4)-c;den=cross(v,vv)
  corners=[(a+s*v-c-t*vv)/2 for s in(0,1)for t in(0,1)];xs=range(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))+1);ys=range(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners))+1)
  for x in xs:
   for y in ys:
    if(x+y+h)%2:continue
    p=complex(x,y);zz=c+2*p-a
    if den:
     s=F(cross(zz,vv),den);t=F(cross(zz,v),den)
     if not(0<=s<1 and 0<t<=1):continue
     kind='nonparallel'
    else:
     if cross(zz,v):continue
     assert b2=='V'and h==0 and vv==v;start=F(int(zz.real),int(v.real))
     if 0<=start<1:parallel_starts.append((b1,b2,x,y,h,str(start)));continue
     s=F(0);t=-start
     if not(0<t<=1):continue
     kind='parallel_first_positive_onset'
    geos.append(dict(first=b1,second=b2,second_pose=[x,y,h],source_s=str(s),second_t=str(t),kind=kind))
canon=lambda x:json.dumps(x,sort_keys=True);assert len(geos)==50 and set(map(canon,geos))==set(map(canon,ref['all50_b1_typed_SECOND_geometries']))
# Actual pair endpoints and full before-colors, with full V/VC source identities.
rows=[];remain=[];cnt=Counter()
for geo in geos:
 b1,b2=geo['first'],geo['second'];p2=complex(*geo['second_pose'][:2]);ha=3
 for A in'FQB':
  disp=tr(W[A]+W[b1]);ap=p2-rot(ha)*disp['p'];assert(ha+disp['h'])%4==geo['second_pose'][2];f=tr(W[A]+W[b1]+W[b2]+M)
  for src,(sd,O)in sources.items():
   row={**geo,'FOREIGN':A,'FOREIGN_pose':[*xy(ap),ha],'source_full':src,'true_source_to_FOREIGN_C_age':1}
   if f['bad']:why='literal_A_FIRST_SECOND_conflict'
   elif any((o-ap)/rot(ha)in K for o in O):why='genuine_SOURCE_CURRENT_in_FOREIGN_entryK'
   elif any(f['req'].get((o-ap)/rot(ha))is False for o in O):why='genuine_SOURCE_BLACK_vs_combined_before_WHITE'
   else:
    why='necessary_one_C_endpoint_obligation';remain.append(row)
    for c,d in pieces(A+b1):
     c=2*ap+c*rot(ha);d=2*ap+d*rot(ha)
     assert all(meet(c,d,e,f)is None for e,f in pieces(src))
   row['classification']=why;cnt[why]+=1;rows.append(row)
assert len(rows)==300 and len(remain)==54 and cnt==ref['classification_counts']
def key(z):return(z['source_full'],z['FOREIGN'],tuple(z['FOREIGN_pose']),z['first'],z['second'],tuple(z['second_pose']))
assert {key(z):z['classification']for z in rows}=={key(z):z['classification']for z in ref['all300_fullsource_foreign_typed_states']}
def perms(d,v,u):
 counts={'D':d,'V':v,'U':u};out=[]
 def go(prefix):
  if not sum(counts.values()):out.append(prefix);return
  for a in'DVU':
   if counts[a]:counts[a]-=1;go(prefix+a);counts[a]+=1
 go('');return out
obligations=[];allwords=[];positive={}
for z in remain:
 x,y,_=z['FOREIGN_pose'];src=z['source_full'];allowed='VU'if z['FOREIGN']in'FQ'else'U';RHS=y-4;connectors=[];tuples=[]
 # Exact domain from nonnegative y equation, NOT a depth cutoff.
 for dn in range(max(RHS+1,0)):
  for vn in range(max(RHS//3+1,0)):
   for un in range(max(RHS//4+1,0)):
    if src=='VC'and(dn or vn or un):continue
    if src=='V'and dn+vn+un==0:continue
    rest=RHS-dn-3*vn-4*un
    if rest<0:continue
    for dw in range(rest+1):
     vw=rest-dw;num=1+dn+vn-dw-3*vw-x
     if num<0 or num%4:continue
     uw=num//4
     ww=[w for w in perms(dw,vw,uw)if w and w[-1]in allowed]
     if not ww:continue
     nn=['']if src=='VC'else[r+'C'for r in perms(dn,vn,un)];connectors.extend(n+w for n in nn for w in ww);tuples.append(((dn,vn,un),(dw,vw,uw)))
 r=next(a for a in ref['all54_unbounded_one_C_endpoint_obligations']if key(a['source_case'])==key(z));assert sorted(connectors)==sorted(r['all_actual_full_connectors']);obligations.append(dict(source_case=key(z),count_solutions=tuples,connectors=sorted(connectors)))
 for run in connectors:
  seq=src+run+z['FOREIGN']+z['first']+z['second'];raw=''.join(W[a]for a in seq);t=tr(raw+M);allwords.append((key(z),run,seq,t['bad']is None))
  if t['bad']is None:positive[seq]=(z,run,t)
assert len(allwords)==26 and sum(bool(z['connectors'])for z in obligations)==18 and set(positive)=={'VCDUFDD','VCDUUQVD','VCVUFVD','VCVUQDD'}
assert {(a,b,c,d)for a,b,c,d in allwords}=={(key(z['source_case']),z['connector'],z['word'],z['feasible'])for z in ref['all26_endpoint_exhaustive_whole_words']}
# Naturally complete reverse closure, all8 predecessor tests for every reached word.
G8=('D','DC','V','VC','VCC','U','UC','UCC');closure=[];queries=0
for seq in sorted(positive):
 todo=[seq];seen=set();edges=[]
 while todo:
  s=todo.pop();assert s not in seen;seen.add(s);allow=[]
  for before in G8:
   queries+=1;t=tr(''.join(W[a]for a in before+s)+M)
   if t['bad']is None:allow.append(before);todo.append(before+s)
   else:assert t['bad'][0]>=0
  edges.append((s,allow))
 assert edges==[(seq,['D']),('D'+seq,[])];closure.append(edges)
assert queries==64
controls=[]
for seq,(z,run,t)in sorted(positive.items()):
 control=next(v for v in ref['four_genuine_VC_entry_physical_controls']if v['word']==seq);B={p for p,c in t['req'].items()if c};assert B=={complex(*p)for p in control['complete_initial_BLACK_board']};labels={p:('initial',p)for p in B};src,outs=sources['VC'];born={p:src['last'][p][1]for p in outs};srcL=len(W['V'])+len(W['C']);preL=srcL+sum(len(W[a])for a in run);alive=None
 for i,(p,h,c)in enumerate(t['reads']):
  if i==preL:alive=all(labels.get(o)==('birth',born[o])and(o-p)/rot(h)not in K for o in outs)
  author=control['all_actual_fine_reads'][i];assert author['tick0']==i and author['cell']==xy(p)and author['turn']==c;assert(p in B)==(c=='L')
  if c=='L':B.remove(p);labels.pop(p)
  else:B.add(p);labels[p]=('birth',i)
 assert alive;pc=pieces(seq);hits=[]
 for j,(a,b)in enumerate(pc):
  for k in range(j+1,len(pc)):
   hit=meet(a,b,*pc[k])
   if k==j+1:assert hit==(F(1),F(0))
   elif hit is not None:hits.append((j,k,hit))
 assert hits==[(0,len(pc)-1,(F(0),F(1)))];controls.append(dict(word=seq,mass=control['mass'],physical_reads=len(t['reads']),all9_original_VC_outputs_CURRENT_before_A=True,unique_new_contact='second terminal to outgoing oldV start',complete_final_mass=len(B)))
out=dict(status='PASS complete true-age1 old-V SECOND-contact slice excluded for U-entry history; four prepared VC controls retained',manifest=sha(man),geometry_count=50,typed_count=300,classification_counts=dict(cnt),all54_endpoint_obligations=obligations,wholeword_count=26,all64_query_reverse_closure=closure,four_actual_prepared_controls=controls,analytic_review=[
'Actual full source is V or VC, not VCC: at true source-entry to foreignC-age1 an actual second tail cannot have completed. VC owns its real C1; plainV needs a nonempty later N-base run ending in an actual FIRST C-tail. All23 signed produced input slots exclude age0/1 retirement or core absorption, so six/nine genuine sourceO identities are CURRENT only at the preforeign cut. No age assertion is transported through A.',
'All16 exact angle pairs are reconstructed by second headingE unless b1=C thenN. Rational head parallelograms, active parity, old0<=s<1 and new0<t<=1 give50 geometries. Collinear same-direction positive onset is included; CUT2 starts already on old source are separately excluded by signed one-return simplicity. Old terminal belongs to its actual next atom, including sourceVC C1, not the V source.',
'Three foreign endpoints and two fullsource roles yield300 states. Full literal A+b1+b2+actualM requirements independently give234 source-beforeWHITE and12 intrinsic conflicts, leaving54. Every surviving prior foreign/first piece misses the genuine full source V/C chord path; no legal immediate adjacency is silently discarded.',
'Nonnegative y equation bounds all N counts and W D/V counts; x then fixes W U. Exact actual lastW rules V/U beforeF/Q orU beforeB ensure complete parser boundaries. Independent all-count/all-order enumeration yields18 nonempty obligations and26 whole words,22 impossible and4 actual prepared VC entries. This is endpoint exhaustion, not bounded search.',
'Each of the four complete minimal boards is replayed at every fine read; all nine sourceVC last-R identities remain SAME CURRENT at foreign entry. Adjacent joins are exactly their endpoints; the only nonadjacent proxy contact is second terminal returning to oldV START. Positive controls are genuine and must not be erased by an overstrong source-free claim.',
'All eight possible full predecessors of each control are tested, exactlyD survives; all eight before that D extension fail. The64-query reverse graph closes naturally, without a depth cap, and contains noU-family entry. Any longer uninterrupted complete-eight prefix has an actual last full packet, so must follow that closed graph. Thus only the intended U-entry age1 slice is excluded.',
'Other oldV ages, oldD/C sources, later contacts, arbitrary returned tails and global capture remain open.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(cnt,controls)
