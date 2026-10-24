from pathlib import Path
from itertools import permutations
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';ns={'__file__':str(SELF)};exec((SELF.parent/'check_shifted_UC_current_fence_independent.py').read_text().split('cat=')[0],ns)
W,M,walk,xy,at,center,edge,meet=[ns[k]for k in('W','M','walk','xy','at','center','edge','meet')];rows=[]
for f,fp,L in[('F',3-4j,-7),('Q',5-4j,-7),('B',6-3j,-5)]:
 for k in([1,2]if f in'FQ'else[1]):
  p=-5-k-k*1j;star={at(q,p,1)for q in[0j,1j,1+0j,1+1j]};Z={at(q,p,1)for q in[1+0j,1+1j,2+0j,2+1j]};start=center(p,1)
  ff=walk(W[f]);prefix=walk(W['F']);full=walk(W[f]+W['C']+M);assert full['feasible'];foot={at(q,fp,1)for q in full['req']}
  fs=center(fp,1);fe=center(at(ff['p'],fp,1),(ff['h']+1)%4);mid=center(at(prefix['p'],fp,1),(prefix['h']+1)%4)
  pieces=[(fs,fe)]if f=='F'else[(fs,mid),(mid,fe)];pieces.append((fe,1+1j));assert min(z.real for e in pieces for z in e)>=1
  assert not(star|Z)&foot
  def support(cells):
   adj={}
   for q in cells:
    a,b=edge(q);adj.setdefault(a,set()).add(b);adj.setdefault(b,set()).add(a)
    assert all(not meet(a,b,c,d)for c,d in pieces)
   seen={start};todo=[start]
   for a in todo:
    for b in adj[a]:
     if b not in seen:seen.add(b);todo.append(b)
   assert len(seen)==len(adj)
   return min(z.imag for z in seen)
  low=support(star);assert low==-2*k-3
  if low<=L:kind='permanent_star_support'
  else:
   assert support(star|Z)==L;gate=at(3-1j,p,1);assert gate==-7-4j and gate.imag==fp.imag
   kind='cycle_break_gap10_impossible'if f=='F'else'Q_three_U_suffix_required_open'
   assert fp.real-gate.real==(10 if f=='F'else 12)
  rows.append({'foreign':f,'k':k,'UCentry':xy(p),'support':L,'star_min':low,'disposition':kind})
assert sum(r['disposition']!='Q_three_U_suffix_required_open'for r in rows)==4
suffix=W['U']*3+W['Q']+W['C']+M;tr=walk(suffix);assert tr['feasible'];seed={q for q,b in tr['req'].items()if b};B=set(seed);p=0j;h=0
for c in suffix:assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
suffix_end=[xy(p),h]
# Exhaust actual endpoint equations, not a guessed connector depth.
solutions=[];tests=[]
for ds in range(8):
 for vs in range(8):
  for us in range(8):
   budget=7-ds-3*vs-4*us
   if budget<0 or ds+vs+us==0:continue
   for ve in range(budget+1):
    de=budget-ve;rem=5+ds+vs-de-3*ve
    if rem<0 or rem%4:continue
    ue=rem//4
    if de+ve+ue==0:continue
    solutions.append((ds,vs,us,de,ve,ue))
    for S in sorted(set(permutations('D'*ds+'V'*vs+'U'*us))):
     if S[0]!='D':continue
     for E in sorted(set(permutations('D'*de+'V'*ve+'U'*ue))):
      # The finalC in each stage is an OWN tail of its last actual base.
      label='UCDDC'+''.join(S)+'C'+''.join(E)+'C'+'UUUQC';r=walk(''.join(W[c]for c in label)+M);assert not r['feasible'];tests.append({'S':S,'E':E,'word':label,'failure_tick':r['i'],'cell':xy(r['q']),'first_tick':r['first']})
A=json.loads((D/'Q_UC_D_empty_N_connector_family.json').read_text());assert len(solutions)==22 and len(tests)==83
assert set(solutions)==set(map(tuple,A['count_solutions']))
assert {(tuple(r['S']),tuple(r['E']))for r in A['rows']}=={(r['S'],r['E'])for r in tests}
mp=D/'DC_C1_UC_support_separator_manifest.json';mf=json.loads(mp.read_text())
for f,h in mf['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in mf['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h
out={'status':'PASS four UC-parent current-support cuts; Q U3 renewal branch retained, empty-N subfamily excluded','manifest_sha256':hashlib.sha256(mp.read_bytes()).hexdigest(),'five_UC_rows':rows,'prepared_suffix':{'read_count':len(suffix),'seed':sorted(map(xy,seed)),'mass':len(seed),'end':suffix_end},'all22_endpoint_count_solutions':solutions,'all83_failed_whole_words':tests,'analytic':['The previously signed whole-loop height horizon places the earlier genuine U-entry center strictly inside the chronological-first-contact Jordan loop. Each connected original current Ustar contains that center and is disjoint from every later old boundary by the current-residual barrier. Exact full foreign/returned contexts miss all star/cycle cells, and all their real doubled edges lie strictly left of every repaired foreign and returned segment. No postforeign age rule or assumed exterior path is used.','Star minima -2k-3 reach the global support for F/Q k2 and B k1, contradicting strict interior. At F/Q k1 the intact original cycle would reach support too. Its genuine first breaker must be the exact source-age4 right U gate(-7,-4,E), plain because the foreign has that same Cclock. Equal y permits only U strides4. Gap10 excludesF; gap12 explicitly retains exactlythreeU beforeQ. A newly reborn q is not a barrier against its own producing chord.','For Q only, impose EMPTY prebreaker N as an explicit additional restriction. Starting UC,D,DC exits(-3,7,S); S and E stages each carry their final actual C tail. Exact endpoint equations bound dS+3vS+4uS<=7 and give22 nonnegative count solutions. Signed first-W-D is the first S base in this rotated creator frame. All S/E orderings satisfying it give83 distinct whole words, each independently fails an immutable read constraint. No artificial internal marker or truncated-depth search is used.','The prepared UUUQC+M suffix is independently executed on one complete finite board. It is NOT certified to have the old UC/DC ancestry or target contact; it prevents an overstrong suffix-only exclusion. Nonempty prebreaker N and all other remaining parent histories stay open.'],'scope':mf['scope'],'dependencies':mf['dependencies']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
