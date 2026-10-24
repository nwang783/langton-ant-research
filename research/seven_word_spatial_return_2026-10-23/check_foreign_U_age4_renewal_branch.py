"""One prescribed signed-renewal extension and its exact immutable conflict.
No creator-prefix enumeration or new word-tree search.
"""
from pathlib import Path
import hashlib,json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
G=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text())['macro_words']
G8=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
M='LLLLRLRRRRL';V=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)}
W={a:G[i]['word']for i,a in enumerate('DCVUFQB')};W.update(UCC=W['U']+2*W['C'],VC=W['V']+W['C'],DC=W['D']+W['C'])
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def derive(word):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(word):
  need=(ch=='L')^(p in par);assert p not in req or req[p]==need
  req[p]=need;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
preds=[]
for a,p in(('D',(2,2)),('V',(2,0)),('U',(3,-1))):
 core={add(p,q)for q in K};preds.append(dict(atom=a,pose=(*p,0),old_star_core_hits=sorted(core&L)))
assert preds[0]['old_star_core_hits']==[(1,1)] and preds[1]['old_star_core_hits']==[(1,0)] and not preds[2]['old_star_core_hits']
freq,_,fep,fh,fr=derive(W['F']+M);fpose=(3,3)
raw_tags=L&{add(fpose,q)for q,ts in fr.items()if any(t<56 for t,ch in ts)}
marker_tags=L&{add(fpose,q)for q,ts in fr.items()if ts[0][0]>=56}
assert not raw_tags and marker_tags=={(0,1)}
assert fr[(-3,-2)][0]==(57,'L')
recipe=['UCC','V','DC','D','VC','D','U','F'];p=(0,0);h=0;par=set();req={};first={};reads={};poses=[];tick=0;conflict=None
for label in recipe:
 poses.append(dict(label=label,tick=tick,pose=(*p,h)))
 for local_phase,ch in enumerate(W[label]):
  need=(ch=='L')^(p in par)
  if p in req and req[p]!=need:
   conflict=dict(label=label,global_tick=tick,local_phase=local_phase,cell=p,proposed_turn=ch,forced_actual_turn='L'if p in par else'R',first_read=first[p],previous_reads=reads[p],first_initial_color=req[p],new_initial_color=need);break
  req[p]=need;first.setdefault(p,(tick,ch));reads.setdefault(p,[]).append((tick,ch,label));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h]);tick+=1
 if conflict:break
assert conflict['global_tick']==196 and conflict['local_phase']==14 and conflict['cell']==(2,4)
assert conflict['previous_reads']==[(36,'R','UCC')]
assert reads[(0,1)]==[(11,'R','UCC'),(15,'L','UCC'),(19,'R','UCC')]
seed={q for q,b in req.items()if b};assert len(seed)==20
# Replay the actual complete finite board through the consistent prefix and
# verify the uniquely forced deviation, without continuing the false word.
board=set(seed);p=(0,0);h=0;word=''.join(W[a]for a in recipe)
for t,ch in enumerate(word[:196]):
 assert(ch=='L')==(p in board)
 board.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
assert p==(2,4) and p in board and word[196]=='R' and (0,1) in board
D=[R/'core_periodicity_new/causal_cycle_renewal_20261023_1841/manifest.json',R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',Path(__file__).resolve()]
o=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_AUDIT',scope='Necessary immediate-renewal reduction for foreign F(3,3,N) with preceding-C bit zero, and one prescribed impossible extension of the signed actual renewal control. No all-renewal extension exclusion, attained foreign reset or prefix search.',immediate_non_C_predecessors=preds,foreign_gate=dict(pose=(3,3,0),raw_old_star_reads=sorted(raw_tags),marker_only_old_star_tags=sorted(marker_tags),physical_retirement_full_context_phase=57,physical_owner='successor RAW phase 1, not foreign RAW'),recipe=recipe,poses=poses,conflict=conflict,actual_consistent_prefix_seed=sorted(seed),actual_seed_mass=len(seed),actual_consistent_raw_length=196,old_tag=(0,1),old_tag_genuine_birth=(19,'R'),old_tag_reads_before_deviation=reads[(0,1)],dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_U_age4_renewal_branch.json').write_text(json.dumps(o,indent=2)+'\n')
print('F(3,3,N), previous non-C => original age-four plain-U renewal. Prescribed known extension fails at F phase 14, immutable old C-tail cell (2,4).')
