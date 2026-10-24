from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];s=(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text();exec(s.split('geometries=[]')[0]);SELF=Path(__file__).resolve();D=R/'one_foreign_return_U_star_2026-10-23';a=json.loads((D/'one_foreign_return_U_star.json').read_text());K={-1-1j,-1,-1j,0,1};L={0,1j,1,1+1j};E={2,2+1j};names=['D','DC','V','VC','VCC','U','UC','UCC'];inv={n:walk(''.join(W[c]for c in n)+M)for n in names};raw={n:walk(''.join(W[c]for c in n))for n in names}
ports={}
for n in names:
 inputs={q for q,c in inv[n]['req'].items()if c}-K
 for q in L:
  for slot in inputs:
   for h in range(4):
    p=q-slot*(-1j)**h
    if(int(p.real+p.imag)+h)%2:continue
    ctx={p+z*(-1j)**h:c for z,c in inv[n]['req'].items()};core={p+z*(-1j)**h for z in K}
    if L&core or any(z in ctx and not ctx[z]for z in L):continue
    ports[n,*xy(p),h]=(p,h)
assert len(ports)==24
provided={(r['returned_packet'],*r['returned_entry_pose'],r['foreign']):r for r in a['rows']};counts=Counter();depths=Counter();proofs=[];zero=[]
for(n,x,y,h),(p,h)in ports.items():
 for f in'FQB':
  af=walk(W[f]);hf=(h-2)%4;fp=p-af['p']*(-1j)**hf;ac=walk(W[f]+M);comb=walk(W[f]+''.join(W[c]for c in n)+M);assert comb['feasible'];assert not L&{fp+z*(-1j)**hf for z in ac['req']}
  ctx={fp+z*(-1j)**hf:c for z,c in comb['req'].items()};core={fp+z*(-1j)**hf for z in K};ref=provided[n,x,y,h,f];assert(*xy(fp),hf)==tuple(ref['foreign_pose']);read=[]
  for tag in L:
   hits=[(i,ch)for i,(z,hh,ch)in enumerate(comb['reads'])if fp+z*(-1j)**hf==tag]
   if hits:read.append((tag,hits[0]))
  assert len(read)==1 and read[0][1][1]=='L';phase=read[0][1][0]-len(W[f]);assert phase=={'D':11,'DC':11,'V':19,'VC':19,'U':29,'UC':29}[n]
  assert tuple(ref['original_star_first_read']['cell'])==xy(read[0][0])and ref['original_star_first_read']['phase_in_returned_packet']==phase
  ownraw=phase<len(''.join(W[c]for c in n));assert('returned packet RAW'==ref['original_star_first_read']['physical_owner'])==ownraw
  depth=0;trace=[]
  while True:
   hp=3*depth-depth*1j;star={hp+q for q in L};east={hp+q for q in E}
   bad={q for q in star if q in core or ctx.get(q)is False};absent={q for q in east if q in core or ctx.get(q)is False};trace.append((bad,absent))
   if bad or not absent:break
   depth+=1;assert depth<=3
  assert len(trace)==len(ref['genuine_renewal_guard_trace'])
  for(j,(bad,absent)),rr in zip(enumerate(trace),ref['genuine_renewal_guard_trace']):
   assert rr['source_C_entry_clock']==4*j and tuple(rr['pose'])==(3*j,-j,0)
   assert set(map(tuple,[xy(q)for q in bad]))=={tuple(r['cell'])for r in rr['star_conflicts']};assert{xy(q)for q in absent}=={tuple(r['cell'])for r in rr['east_absence_forcing_witnesses']}
  if bad:kind='universal_genuine_ancestry_guard_obstruction';bound=None;depths[depth]+=1
  elif depth==0 and h==1:assert fp.imag<=4 and hf==3;kind='necessary_foreign_clock_at_least5';bound=5
  elif depth==0 and h==2:
   assert hf==0;kind='necessary_foreign_clock_at_least4';bound=4
   xx,yy=xy(fp);sol=[]
   for d in range(max(0,xx+1)):
    v=xx-d;rem=yy-4-d-3*v
    if rem<0 or rem%4:continue
    u=rem//4;last=[b for b,c in[('V',v),('U',u)]if c and(f!='B'or b=='U')]
    if last:sol.append((d,v,u,last))
   if sol:
    assert n in('U','UC')
    if f=='Q':assert sol==[(2,1,0,['V'])];lab='UDDVQ'
    else:assert f=='B'and sol==[(2,0,1,['U'])];lab='UDDUB'
    word=''.join(W[c]for c in lab+n)+M;lit=walk(word);assert not lit['feasible'];off=sum(len(W[c])for c in lab);assert(lit['i']-off,lit['q'],lit['first'])==(1,5j,39)
   zero.append((n,f,xy(fp),sol))
  elif depth==1 and n in('V','VC'):
   assert(f,fp-(3-1j),hf)==('F',3-2j,1);z=(4-fp)*(1j)**hf;assert z==-3-2j;hits=[(i,ch)for i,(q,hh,ch)in enumerate(ac['reads'])if q==z];assert hits[0]==(57,'L');kind='necessary_foreign_clock_at_least11_with_actual_first_renewal';bound=11
  else:assert depth==1 and n in('U','UC')and hf==1;kind='necessary_foreign_clock_at_least7_with_actual_first_renewal';bound=7
  assert(kind,bound)==(ref['classification'],ref['necessary_foreign_C_age_at_least']);counts[kind]+=1
assert len(provided)==72 and counts=={'universal_genuine_ancestry_guard_obstruction':37,'necessary_foreign_clock_at_least5':9,'necessary_foreign_clock_at_least4':18,'necessary_foreign_clock_at_least11_with_actual_first_renewal':2,'necessary_foreign_clock_at_least7_with_actual_first_renewal':6};assert depths=={1:33,2:2,3:2};assert len(zero)==18 and sum(bool(r[-1])for r in zero)==4
man=D/'manifest.json';sha=hashlib.sha256(man.read_bytes()).hexdigest();assert sha=='bd9bb22d83028aad7aa2b137ee801db8b203f389458a0d45d3083ec6b4cf2662'
for f,h in json.loads(man.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in a['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
errata={}
for name,pref in [('erratum_manifest.json','61a7309a'),('ownership_erratum_manifest.json','7012d5f0')]:
 ep=D/name; eh=hashlib.sha256(ep.read_bytes()).hexdigest();assert eh.startswith(pref);errata[name]=eh
 for f,h in json.loads(ep.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS one-foreign then one-returned-packet original U-star ancestry table WITH both mandatory prose errata','bound_errata':errata,'manifest_sha256':sha,'independently_generated_return_ports':24,'suffixes':72,'classifications':dict(counts),'universal_guard_depths':dict(depths),'zero_clock_rows':18,'zero_clock_forced_word_rows':4,'erratum':'In prose section Thirty-five necessary residues, item2, sixteen no-solution rows must read fourteen; checker uses18total/4forced. Also U/UC old-star read is phase29, not25: plain U is following-word phase1/exit-core absorption, UC is its own RAW. The JSON ownership is already correct.','analytic':['The24 return-port universe is independently generated from all full input alignments while retaining every original L identity outside entry core and requiring complete-context compatibility. Each of its three uniquely inverted foreign entries misses the entire original star in its COMPLETE context, not merely RAW.','The combined actual foreign+packet+marker before-mask accounts for all intervening flips. A required-WHITE or entry-core east identity must have retired BEFORE the foreign, forcing a genuine earlier right U-family renewal at clock4. Every such producer freshly installs its own permanent star within the still-uninterrupted eight factor. Repeat only while a concrete next-east absence witness exists; the finite exact rows stop at depth<=3.','Guardian contradictions use current identities only at foreign ENTRY. They do not assert postforeign permanence: foreign toggles and changed core have already been incorporated in the combined before-mask. This proves37 all-age exclusions, not prepared ancestry.','Residual W-heading foreign clocks1 are impossible by the exact one-C y>=5 cone while all target y<=4, giving>=5. Residual N-heading foreign clock0 has14 impossible head equations and4 uniquely forced words UDDVQ(U/UC),UDDUB(U/UC), all failing returned Uphase1 at(0,5), initially required by actual second-D tick39L. Hence>=4.','Six E-heading foreign residues force actual H1at4 and therefore next congruent clock>=7. Two F residues are exactly H1-relative marker-only F(3,-2,E), whose signed relative lower clock7 yields absolute>=11. The required guardian tag is unread through F RAW and read at its successor phase1.','D/V returned gates absorb the tag in exit core and the next word owns phase1; DC/VC own that read in their RAW. Plain U likewise absorbs the tag into exit core for following-word phase1 (returned phase29), whereas UC owns phase29 in its RAW. Foreign marker-only prior absorption of an original tag is a separate case, explicitly excluded here.'],'scope':'One first foreign missing the entire original star in COMPLETE context, followed by exactly one complete-eight packet. Necessary residues are not attained. No returned-path simplicity, postforeign permanence, later packet/foreign extension or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
