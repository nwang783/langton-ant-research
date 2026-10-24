from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';p=SELF.with_name('check_returned_V_source_reduction_independent.py');ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
W,M,walk,xy,raw,I,O,K=[ns[k]for k in('W','M','walk','xy','raw','I','outputs','K')];names=['D','DC','V','VC','VCC','U','UC','UCC'];A=json.loads((D/'C75_immediate_DC_VC_ancestor_bud.json').read_text())
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';COUNT={tuple(map(int,s.split()[:8]))for s in CP.read_text().splitlines()}
raw={**raw,**{n:walk(W[n])for n in['C','F']}}
g=-2-1j;queries=[];surv=[];counts=Counter();births=[]
for sn,slot,start in [('DC',2,-2+1j),('VC',2+2j,-4+1j)]:
 h0=1;assert start+slot*(-1j)==g and slot in O[sn]
 rd=[(i,c)for i,(q,h,c)in enumerate(raw[sn]['reads'])if q==slot];base=[(i,c)for i,(q,h,c)in enumerate(raw[sn[0]]['reads'])if q==slot];assert rd==base and rd[-1]==((8 if sn=='DC'else 16),'R')
 assert start+raw[sn]['p']*(-1j)==0 and(raw[sn]['h']+h0)%4==0
 births.append((sn,xy(start),xy(slot),rd,0,1,4))
 for age in range(5):
  hh=(-age)%4
  for ci,cn in enumerate(names):
   for v in I[cn]:
    ep=slot-v*(-1j)**hh;key=(names.index(sn),ci,*xy(ep),hh,*xy(slot),age)
    why='sector'if(int(ep.real+ep.imag)+hh)%2 else'source_incomplete'if age<1 else'consumer_incomplete'if age+cn.count('C')>4 else'COUNT5'if key in COUNT else'geometry_obligation'
    globalp=start+ep*(-1j);globalh=(hh+1)%4;row=(sn,cn,xy(v),age,xy(ep),hh,xy(globalp),globalh,key,why);queries.append(row);counts[why]+=1
    if why=='geometry_obligation':surv.append(row)
assert len(queries)==230 and len(surv)==4
assert{(z[0],z[1],z[3],z[6],z[7])for z in surv}=={('DC',n,3,p,2)for n in['V','VC']for p in[(-2,2),(-1,1)]}
def ctr(p,h):return 2*p+(-1-1j)*(-1j)**h
def chord(p,h,n):
 a=ctr(p,h);end=p+raw[n]['p']*(-1j)**h;eh=(h+raw[n]['h'])%4;return a,ctr(end,eh)
def det(a,b):return int(a.real*b.imag-a.imag*b.real)
def meet(a,b,c,d):
 u,v,z=b-a,d-c,c-a;den=det(u,v);s=Fraction(det(z,v),den);t=Fraction(det(z,u),den);return s,t,(Fraction(int(a.real))+s*int(u.real),Fraction(int(a.imag))+s*int(u.imag))
oldD=chord(-2+1j,1,'D');oldC=chord(-1,1,'C');assert tuple(map(xy,oldD))==((-5,3),(-3,1))and tuple(map(xy,oldC))==((-3,1),(-1,-1))
cross=[]
for p,old in[(-2+2j,oldD),(-1+1j,oldC)]:
 H=chord(p,2,'V');s,t,q=meet(*old,*H);assert s==t==Fraction(1,2);cross.append((xy(p),list(map(xy,old)),list(map(xy,H)),str(s),str(t),list(map(str,q))))
F=3-4j;local=(g-F)*1j;assert local==-3-5j;fc=walk(W['F']+W['C']+M);fr=walk(W['F']);assert local not in fr['req']and local not in K and not fc['req'][local]
first=next((i,c)for i,(q,h,c)in enumerate(fc['reads'])if q==local);assert first==(78,'R');assert first[0]-len(W['F'])-len(W['C'])==7
controls=[]
for tokens,ref in zip([['DC','DC','DC','D','VC','D','D','U','F','C'],['DC','DC','DC','D','V','DC','V','U','F','C']],A['two_real_finite_board_genuine_bud_clearing_controls']):
 word=''.join(''.join(W[c]for c in n)for n in tokens);tr=walk(word+M);assert tr['feasible'];seed={q for q,c in tr['req'].items()if c};assert sorted(map(xy,seed))==list(map(tuple,ref['complete_finite_seed']))
 B=set(seed);p=0j;h=0;trace=[];birth={q:None for q in B};bud=[]
 for tick,want in enumerate(word+M):
  assert('L'if p in B else'R')==want
  if p==2:bud.append((tick,want,birth.get(p)))
  if want=='L':birth.pop(p)
  else:birth[p]=tick
  trace.append((tick,xy(p),h,want,len(B)));B^={p};h=(h+(1 if want=='R'else-1))%4;p+=1j*(-1j)**h
 assert len(seed)==(29 if tokens[4]=='VC'else 30) and len(trace)==(248 if tokens[4]=='VC'else 256)
 assert bud==[(8,'R',None),(104,'L',8),(len(word)+7,'R',None)]
 # Fresh fullpacket sequence locates actual helper, selected C and foreign, with no pose reset.
 p=0j;h=0;clock=0;tick=0;atomrows=[]
 for packet in tokens:
  for atom in packet:
   atomrows.append((tick,clock,atom,xy(p),h,list(map(xy,chord(p,h,atom)))))
   p+=raw[atom]['p']*(-1j)**h;h=(h+raw[atom]['h'])%4;tick+=len(W[atom]);clock+=atom=='C'
 helper=next(z for z in atomrows if z[0]==85);assert helper[2:5]==('V',(-1,0),1)and helper[1]==3
 old=atomrows[0];s,t,q=meet(*(complex(*v)for v in old[5]),*(complex(*v)for v in helper[5]));assert s==t==Fraction(1,2)
 selected=next(z for z in atomrows if z[0]==35);assert selected[2:5]==('C',(0,3),3)
 f=next(z for z in atomrows if z[2]=='F');ret=atomrows[-1];cp=complex(*selected[3]);ch=selected[4]
 assert (complex(*f[3])-cp)/(-1j)**ch==2-5j and(f[4]-ch)%4==1
 assert (complex(*ret[3])-cp)/(-1j)**ch==-1j and(ret[4]-ch)%4==3
 assert ctr(p,h)==ctr(cp,ch)
 deathown=('ownC_tail',1,2)if tokens[4]=='VC'else('next_actual_word',1,2)
 controls.append({'packets':tokens,'seed':sorted(map(xy,seed)),'complete_trace':trace,'atoms':atomrows,'bud_lifetimes':bud,'clearing_owner':deathown,'final_field':sorted(map(xy,B)),'old_chord_crossing':{'s':str(s),'t':str(t),'point':list(map(str,q))}})
mp=D/'C75_immediate_DC_VC_ancestor_bud_manifest.json';mf=json.loads(mp.read_text());mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='849d340477795d2b4e0283bc905918eed4dfb3cea23f418582a418a32c9a95af'
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS C75 k0 immediateDC/VC older-bud exclusion with genuine finite clearing controls','manifest_sha256':mh,'fresh_source_roles':births,'all230_exact_queries':queries,'query_counts':dict(counts),'four_survivors':surv,'strict_midpoint_contacts':cross,'foreign_suffix_first_read':[xy(local),first,'following_actual_word',7,8],'full_positive_controls':controls,'analytic_review':[
'The real previous parent DC/VC finishes at selectedD0N. The original residual g(-2,-1) is fresh D8R or V16R, in fullO and untouched by its ownC. Parent fullentry clock0, selectedD1, foreign4. The source has actually completed, and every possible retiring full consumer must finish by foreign4, including mandatory tails.',
'Fresh all230 full-input alignments, including marker-only absorption, leave precisely DC-source V/VC upper or selected inputs at age3 in two actual poses. All VC-source cases and every age4 alignment are excluded. The signed COUNT5 data are used at their true FULL source and FULL consumer entries, not shifted atomic birth clocks.',
'The two surviving helper V-base chords strictly cross genuine older parent D or its actual C at exact midpoint of both. They are nonadjacent actual atoms in the same preforeign U-entry-simple path. Their exclusion uses that hypothesis; it is not an unconditional color/permanence theorem. A first residual retirement must occur through a true full input, including exit-core absorption, so no later core rewrite can bypass this first-consumer argument.',
'Without that first retirement the SAME original g is black at F entry. F RAW and returnedC do not read it; the first actual suffix read is R at combined78, belonging to the next actual word tick7/read8. The before-WHITE contradiction uses no postforeign age law.',
'Two independent full-board executions of248/256 reads from exactly29/30 black cells attain actual oldbud R8 then L104, with respective ownC or followingword read2 ownership, and reach the same final C75 geometry. Both have the explicit earlier parent-D/helper-V midpoint crossing. They are genuine countercontrols to any source-free bud permanence claim, but not U-entry attainments.',
'Only C75 k0 DC/VC parents are removed. Its four k1/k2 DC/VC interfaces remain necessary and open; D15/D30 are untouched. No returned-path simplicity or recursive older-parent bound is claimed.'
],'dependencies':mf['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dict(counts))
