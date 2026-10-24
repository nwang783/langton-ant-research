"""Actual16-cell VC-young-pair control, with full strict record core/creation cuts."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';RP=R/'chronology_dcuv/delayed_height_probe/u1_residue_cegar/root_out.json';G=json.loads(GP.read_text())['geometry'];RJ=json.loads(RP.read_text());A=RJ['core_offsets'];T={(a,h):t for a,h,t in RJ['created_peaks']}
ids=[5,5,5,4,0,7];DIR=((0,1),(1,0),(0,-1),(-1,0));K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
word=''.join(G[a]['word']for a in ids)+G[7]['marker'];p=(0,0);h=0;seen={};par={};first={}
for t,ch in enumerate(word):
 b=(ch=='L')^par.get(p,False);assert p not in seen or seen[p]==b
 seen[p]=b;first.setdefault(p,t);par[p]=not par.get(p,False);h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h])
seed={p for p,b in seen.items()if b};assert len(seed)==16 and K<=seed
P={(1,0),(2,0),(4,0),(2,-1),(3,-1)};upper={(4,0),(2,-1),(3,-1)}
Board=set(seed);L={q:('entry',None)for q in seed-K};p=(0,0);h=0;clock=0;t=0;rows=[];held={};S=28
for j,a in enumerate(ids):
 core={add(p,rot(q,h))for q in K};assert core.isdisjoint(L)and Board==core|set(L)
 I=[add(p,rot(q,h))for q in G[a]['inputs']];births=[L[q]for q in I];ages=[None if v[1]is None else clock-v[1]for v in births];entry=2*sum(p)+A[h];peak=2*sum(p)+T[a,h]
 if j<len(ids)-1:assert max(entry,peak)<S
 else:
  assert p==(0,-1)and h==1 and peak==S
  assert [v[0]for v in births]==[0,0,'entry','entry','entry']and ages==[3,3,None,None,None]
 if j>0:
  assert all(q in L and L[q]==held[q]for q in P)
  if j<len(ids)-1:
   ctx={add(p,rot(q[:2],h))for q in G[a]['requirements']};assert ctx.isdisjoint(P)
 rows.append(dict(index=j,packet=a,pose=[*p,h],C_clock=clock,raw_time=t,input_cells=I,input_births=births,input_ages=ages,entering_core_value=entry,created_peak=peak))
 for q in I:del L[q]
 for q in G[a]['outputs']:
  z=add(p,rot(q,h));assert z not in L;L[z]=(j,clock)
 for ch in G[a]['word']:
  assert(ch=='L')==(p in Board)
  if p in Board:Board.remove(p)
  else:Board.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h]);t+=1
 clock+=G[a]['name'].count('C')
 if j==0:
  held={q:L[q]for q in P};assert all(held[q][0]=='entry'for q in upper)
for ch in G[7]['marker']:
 assert(ch=='L')==(p in Board)
 if p in Board:Board.remove(p)
 else:Board.add(p)
 h=(h+(-1 if ch=='L'else 1))%4;p=add(p,DIR[h]);t+=1
assert t==166 and clock==3
upper_activations=[dict(cell=q,height=sum(q),I28_activation=28+2*sum(q))for q in sorted(upper)]
J=dict(status='AUTHOR_ACTUAL_VC_YOUNG3_JOINT5_WITH_FULL_CORE_CREATION_CUTS_PASS',scope='One actual16-cell word; all3upper target inputs are entry-old and FUND the event. Not an unfunded U1 record, min-age improvement, closure, or fresh-root theorem.',word=ids,seed=sorted(seed),mass=len(seed),reads_including_final_marker=t,source_included_C_age=3,strict_C_count=2,protected_points=sorted(P),older_upper_points=sorted(upper),target_record_score=28,max_earlier_core_or_created=24,rows=rows,upper_initial_activation_values=upper_activations,missing_premise='In a full unfunded U1 prefix these same3upper identities must instead be genuinely produced before sourceVC, by at least2 C increments; this direct word does not supply that past.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,RP,Path(__file__).resolve()]})
(R/'chronology_dcuv/young_U_VC_literal_control.json').write_text(json.dumps(J,indent=2)+'\n');print(dict(word=ids,mass=len(seed),reads=t,record_pairs=[(q['entering_core_value'],q['created_peak'])for q in rows],upper_activations=upper_activations))
