"""Exact tagged U-star/cycle interfaces across one foreign word and return.
Only literal finite alignments and 72 prescribed local suffixes; no prefix scan.
Prepared suffix controls do NOT certify an earlier U creator for their tags.
"""
from pathlib import Path
from collections import Counter
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
MP=R/'word_stabilization/no_d_packet_fuel_marks.json'
J=json.loads(QP.read_text());G=J['macro_words'];G8=json.loads(GP.read_text())['geometry'];MARKS=json.loads(MP.read_text())['packets']
M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}
L={(0,0),(0,1),(1,0),(1,1)};Z={(1,0),(1,1),(2,0),(2,1)}
V=((0,1),(1,0),(0,-1),(-1,0));LABELS='DCVUFQB';IDS=(0,1,4,5,6,7,8,9)
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  need=(ch=='L')^(p in par);assert p not in req or req[p]==need,(t,p)
  req[p]=need;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
# Each protected tag has a genuine fresh physical R birth in creating U.
_,_,_,_,ur=derive(G[3]['word'])
source_tag_births=[]
for q in sorted(L|Z):
 assert ur[q][-1][1]=='R'
 source_tag_births.append(dict(cell=q,last_creating_U_read=ur[q][-1]))
for s in(7,8,9):
 assert L|Z<=set(map(tuple,G8[s]['outputs']))
 _,_,_,_,reads=derive(G8[s]['word'])
 assert all(t<len(G[3]['word'])for q in L|Z for t,ch in reads[q])
# The only candidate foreign entry center on the old creating-U chord is its
# endpoint. Different physical pose forbids zero-gap adjacency; a nonempty
# intervening retained-eight path cannot return to that already visited center.
def entry_repeats_old_source(p,h):
 c=add((2*p[0],2*p[1]),rot((-1,-1),h))
 if c[0]==-1 and -1<=c[1]<=7:
  assert(p,h)==((-1,3),2)and c==(-1,7)
  return True
 return False
interfaces={}
for held,name,target in((L,'star',L),(L|Z,'intact_cycle',Z)):
 rows=[];cases={}
 for a in(4,5,6):
  w=G[a]['word'];req,_,_,_,reads=derive(w+M);I={q for q,b in req.items()if b}-K;white={q for q,b in req.items()if not b}
  base=next(z for z in MARKS if z['name']==LABELS[a]);fm={tuple(q[:2])for q in base['raw_marks']}
  ctxonly={q for q in I if reads[q][0][0]>=len(w)};assert len(ctxonly)==1
  qmarker=next(iter(ctxonly));assert reads[qmarker][0]==(len(w)+1,'L')
  _,_,ep,dh,_=derive(w);exitcore={place(q,ep,dh)for q in K};assert qmarker in exitcore and qmarker==place((-1,0),ep,dh)
  first_C_marks=next(z for z in MARKS if z['name']==LABELS[a]+'C')['raw_marks']
  assert [*qmarker,len(w)+1] in first_C_marks
  for z in sorted(target):
   for q in sorted(I):
    for h in range(4):
     p=sub(z,rot(q,h));core={place(x,p,h)for x in K};W={place(x,p,h)for x in white};II={place(x,p,h)for x in I}
     why='sector'if(sum(p)+h)%2 else'held_core'if held&core else'held_before_white'if held&W else'entry_repeats_old_U_center'if entry_repeats_old_source(p,h)else'candidate'
     row=dict(foreign=LABELS[a],pose=[*p,h],aligned_tag=z,input_slot=q,reason=why);rows.append(row)
     if why!='candidate':continue
     key=(a,*p,h);tags=II&held;raw=[];spill=[]
     for tag in sorted(tags):
      local=rot(sub(tag,p),-h);ts=reads[local];first=ts[0];assert first[1]=='L'
      raw_reads=[(t,ch)for t,ch in ts if t<len(w)]
      if raw_reads:
       raw.append(dict(cell=tag,foreign_local_cell=local,first_L_phase=first[0],raw_reads=raw_reads,raw_exit_black=not(len(raw_reads)%2),is_base_fuel_mark=local in fm))
      else:
       assert local==qmarker
       spill.append(dict(cell=tag,foreign_local_cell=local,first_L_full_context_phase=first[0],owner='successor raw word phase1, NOT foreign raw',successor_phase=1,foreign_raw_exit_black=True,in_foreign_exit_core=True))
     cases[key]=dict(foreign=LABELS[a],pose=[*p,h],target_tags=sorted(tags&target),held_input_tags=sorted(tags),raw_retirements=raw,marker_spillover=spill,untouched_through_foreign_RAW=sorted(held-{tuple(r['cell'])for r in raw}),base_fuel_marks_hitting_held=sorted({place(q,p,h)for q in fm}&held))
 out=dict(alignment_count=len(rows),counts=dict(Counter(r['reason']for r in rows)),unique_gate_count=len(cases),gates=list(cases.values()),rows=rows)
 assert len(rows)==752
 interfaces[name]=out
assert interfaces['star']['unique_gate_count']==69
assert interfaces['intact_cycle']['unique_gate_count']==29
star=interfaces['star']['gates'];cyc=interfaces['intact_cycle']['gates']
assert Counter((c['foreign'],len(c['raw_retirements']),len(c['marker_spillover']))for c in star)==Counter({(a,1,0):16 for a in'FQB'})+Counter({(a,2,0):3 for a in'FQB'})+Counter({(a,0,1):4 for a in'FQB'})
raw_ports={tuple(r['foreign_local_cell'])for c in star for r in c['raw_retirements']}
assert raw_ports=={(-1,2),(-2,2),(-3,3),(-4,3),(-5,2),(-5,1)}
assert{r['first_L_phase']for c in star for r in c['raw_retirements']}=={13,16,34,35,37,38}
assert all(not r['raw_exit_black']and not r['is_base_fuel_mark']for c in star for r in c['raw_retirements'])
assert all(not c['base_fuel_marks_hitting_held']for c in star)
for c in cyc:
 consumed={tuple(r['cell'])for r in c['raw_retirements']}|{tuple(r['cell'])for r in c['marker_spillover']}
 assert 2<=len(consumed&Z)<=3
 assert len({tuple(r['cell'])for r in c['raw_retirements']}&Z)>=2
 assert Z-consumed
cycle_no_D_cuts=[dict(foreign=c['foreign'],pose=c['pose'],fresh_mark_hits=c['base_fuel_marks_hitting_held'])for c in cyc if c['base_fuel_marks_hitting_held']]
assert len(cycle_no_D_cuts)==2
# A local postforeign return interface, with all four old physical tags still
# black/outside core. No old-U-chord exclusion is available across a foreign.
post={};postrows=[]
for a in IDS:
 for z in sorted(L):
  for q in G8[a]['inputs']:
   for h in range(4):
    p=sub(z,rot(q,h));core={place(x,p,h)for x in K};W={place(x[:2],p,h)for x in G8[a]['requirements']if not x[2]}
    why='sector'if(sum(p)+h)%2 else'held_core'if L&core else'held_before_white'if L&W else'candidate'
    postrows.append(dict(packet=G8[a]['name'],pose=[*p,h],aligned_tag=z,input_slot=q,reason=why))
    if why=='candidate':post[a,*p,h]=dict(packet=G8[a]['name'],pose=[*p,h])
assert len(postrows)==368 and len(post)==24
suffix_controls=[]
for a,x,y,h in sorted(post):
 for f in(4,5,6):
  fw=G[f]['word'];_,_,ep,dh,_=derive(fw);fh=(h-dh)%4;fp=sub((x,y),rot(ep,fh));freq,_,_,_,fr=derive(fw+M)
  assert not L&{place(q,fp,fh)for q in fr}
  assert not entry_repeats_old_source(fp,fh)
  word=fw+G8[a]['word']+M;req,_,_,_,_=derive(word)
  globalreq={place(q,fp,fh):b for q,b in req.items()}
  assert all(globalreq.get(q,True)for q in L)
  seed={q for q,b in globalreq.items()if b}|L;board=set(seed);p=fp;hh=fh;first={}
  for tick,ch in enumerate(word):
   assert(ch=='L')==(p in board)
   if p in L and p not in first:first[p]=(tick,ch)
   board.symmetric_difference_update({p});hh=(hh+(-1 if ch=='L'else 1))%4;p=add(p,V[hh])
  assert len(first)==1 and all(t>=len(fw)and ch=='L'for t,ch in first.values())
  suffix_controls.append(dict(foreign=LABELS[f],foreign_pose=[*fp,fh],returned_packet=G8[a]['name'],returned_pose=[x,y,h],prepared_seed=sorted(seed),prepared_seed_mass=len(seed),first_tag_reads=[dict(cell=q,global_suffix_phase=t,returned_packet_phase=t-len(fw),turn=ch)for q,(t,ch)in first.items()],scope='Actual finite prepared suffix only. Distinguished tags are present black cells; NO earlier creating-U history is certified.'))
assert len(suffix_controls)==72
D=[QP,GP,MP,R/'word_stabilization/no_d_packet_fuel_manifest.json',R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/manifest.json',Path(__file__).resolve()]
out=dict(status='AUTHOR_EXACT_FOREIGN_U_TAG_INTERFACES_PENDING_INDEPENDENT_AUDIT',scope='Necessary interfaces for current fresh U-born residual tags at the FIRST foreign F/Q/B after an uninterrupted retained-eight interval; held star L, and optionally intact Z, at foreign entry. Only the foreign ENTRY center is cut using earlier simple-center history. No old simplicity or permanence is assumed across foreign. Postreturn72 controls certify only prepared suffixes, not U-born ancestry.',source_tag_births=source_tag_births,interfaces=interfaces,common_raw_star_ports=sorted(raw_ports),star_raw_first_L_phases=[13,16,34,35,37,38],cycle_no_D_freshness_cuts=cycle_no_D_cuts,postreturn=dict(rows=postrows,gates=list(post.values()),prepared_suffix_controls=suffix_controls),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'foreign_U_ports.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:(v['counts'],v['unique_gate_count'])for k,v in interfaces.items()});print('postreturn gates24; prepared suffixes72; no U ancestry assertion')
