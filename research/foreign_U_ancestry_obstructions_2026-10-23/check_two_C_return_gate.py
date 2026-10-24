"""All-word two-C obstruction for one normalized U/foreign/returned-DC gate.
No trajectory or prefix enumeration; verify literal masks and monotone facts.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
QP=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(QP.read_text())['macro_words'];G8=json.loads(GP.read_text())['geometry'];M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};L={(0,0),(0,1),(1,0),(1,1)};Q=(0,-1);V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(w):
 p=(0,0);h=0;par=set();req={};reads={}
 for t,ch in enumerate(w):
  b=(ch=='L')^(p in par);assert p not in req or req[p]==b;req[p]=b;reads.setdefault(p,[]).append((t,ch));par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
atoms={}
for a in(0,1,2,3):
 w=G[a]['word'];req,_,_,_,reads=derive(w+M);_,par,p,h,_=derive(w);board={q for q,b in req.items()if b}^par;O=board-{place(q,p,h)for q in K};I={q for q,b in req.items()if b}-K
 atoms['DCVU'[a]]=dict(word=w,endpoint=[*p,h],inputs=sorted(I),outputs=sorted(O),requirements=req,reads=reads)
# Bind literal atomic C versus the C pieces of the complete-eight packets.
assert G8[1]['word']==G[0]['word']+G[1]['word']
assert G8[5]['word']==G[2]['word']+G[1]['word']
assert G8[8]['word']==G[3]['word']+G[1]['word']
assert G8[6]['word']==G[2]['word']+G[1]['word']*2
assert G8[9]['word']==G[3]['word']+G[1]['word']*2
assert atoms['U']['reads'][Q]==[(3,'L')]
assert atoms['U']['endpoint']==[0,4,0]
assert all(q[1]>=0 for a in atoms.values()for q in a['outputs'])
assert all(sum(q)>=0 for a in atoms.values()for q in a['outputs'])
# H=y-x is nondecreasing through N/W zero-C epochs.
steps={}
for a in'DVU':
 x,y,h=atoms[a]['endpoint'];assert h==0
 assert y-x>=0
 wx,wy=rot((x,y),3);assert wy-wx>=0
 steps[a]=dict(N_endpoint=[x,y],N_delta_H=y-x,W_endpoint=[wx,wy],W_delta_H=wy-wx)
cx,cy,ch=atoms['C']['endpoint'];assert(cx,cy,ch)==(0,1,3)
# After C2 the heading is S. Every possible zero-C output alignment of Q
# either violates active parity or puts a held old star tag in entry core.
rows=[]
for a in'DVU':
 for z in atoms[a]['outputs']:
  p=sub(Q,rot(z,2));core={place(q,p,2)for q in K};sector=(sum(p)+2)%2
  row=dict(atom=a,output_slot=z,producer_pose=[*p,2],reason='wrong_active_sector'if sector else'held_star_in_entry_core',core_hits=sorted(core&L))
  if not sector:assert core&L
  rows.append(row)
assert len([r for r in rows if r['reason']=='held_star_in_entry_core'])==8
foreign=[]
for a,p in((4,(-3,-3)),(5,(-3,-5)),(6,(-2,-6))):
 w=G[a]['word'];req,_,_,_,reads=derive(w+M);_,_,e,dh,_=derive(w);ep=place(e,p,2);eh=(2+dh)%4;local=rot(sub(Q,p),2)
 assert(ep,eh)==((1,-1),0)
 assert reads[local]==[(len(w)+1,'L')]
 assert req[local]and not any(t<len(w)for t,ch in reads[local])
 assert Q not in{place(q,p,2)for q in K}
 assert not L&{place(q,p,2)for q in req}
 # Returned D10 then C15 really owns the old tag's first physical L.
 dc=G[0]['word']+G[1]['word'];_,_,_,_,dr=derive(dc+M);rslot=rot(sub((1,0),ep),-eh)
 assert dr[rslot][0]==(11,'L')
 foreign.append(dict(word='DCVUFQB'[a],entry_pose=[*p,2],exit_pose=[*ep,eh],required_global_cell=Q,required_local_cell=local,first_requirement_phase=len(w)+1,raw_reads_of_required_cell=[],returned_packet='DC',returned_tag=(1,0),returned_tag_first_L_in_DC=11,returned_C_owned_phase=1))
D=[QP,GP,Path(__file__).resolve(),R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',R/'foreign_U_port_interfaces_2026-10-23/manifest.json']
out=dict(status='AUTHOR_ALL_WORD_TWO_C_FOREIGN_RETURN_OBSTRUCTION_PENDING_INDEPENDENT_AUDIT',scope='A genuine creating U at0,0,N followed by an arbitrary retained-eight connector with EXACTLY TWO C words cannot reach any of three prescribed first foreign gates F/Q/B then returnedDC retiring original tag1,0. No bound on zero-C rail lengths. No exclusion of6,10,...C windings or other gates.',deleted_creator_cell=Q,creator_delete_read=[3,'L'],creator_exit=[0,4,0],zero_C_monotone_steps=steps,S_output_alignment_rows=rows,foreign_gates=foreign,atomic_output_masks={a:x['outputs']for a,x in atoms.items()},dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'two_C_return_gate.json').write_text(json.dumps(out,indent=2)+'\n');print('All three foreign gates excluded for arbitrary exact2C connectors; S table8 active core conflicts')
