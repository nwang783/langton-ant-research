"""Literal seven-word marker/core bridge and one finite D-return obstruction.
No prefix enumeration or search: seven supplied words and one explicit DVFD.
"""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
P=R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json';J=json.loads(P.read_text());G=J['macro_words'];LABELS='DCVUFQB';M='LLLLRLRRRRL';K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};V=((0,1),(1,0),(0,-1),(-1,0))
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def place(q,p,h):return add(p,rot(q,h))
def derive(word):
 p=(0,0);h=0;par=set();req={};reads=[]
 for i,ch in enumerate(word):
  need=(ch=='L')^(p in par);assert p not in req or req[p]==need,(i,p)
  req[p]=need;reads.append(p);par.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h])
 return req,par,p,h,reads
req,*_=derive(M);assert{q for q,b in req.items()if b}==K
literal=[]
for i,g in enumerate(G):
 w=g['word'];joined=w+M;req,_,_,_,_=derive(joined);_,par,p,h,_=derive(w);board={q for q,b in req.items()if b}^par;core={place(q,p,h)for q in K};assert core<=board
 assert joined.startswith(g['start_marker'])and joined[len(w):].startswith(g['end_marker'])
 marks=[j for j in range(len(w)+1)if joined[j:j+len(M)]==M];assert marks==[0,len(w)]
 assert K<={q for q,b in req.items()if b};inputs={q for q,b in req.items()if b}-K;outputs=board-core
 literal.append(dict(label=LABELS[i],word=w,length=len(w),actual_start_marker=g['start_marker'],actual_end_marker=g['end_marker'],endpoint=[*p,h],entry_extra_black=sorted(inputs),exit_residual=sorted(outputs),mass_gain=w.count('R')-w.count('L'),M11_occurrences_with_actual_right_marker=marks,core_verified=True))
# Explicit finite return witness, with all marker context physically replayed.
ids=[0,2,4,0];raw=''.join(G[i]['word']for i in ids);full=raw+M;req,_,_,_,_=derive(full);seed={q for q,b in req.items()if b};assert len(seed)==23
board=set(seed);p=(0,0);h=0;time=0;cuts=[];wordcuts=[]
for i in ids:
 core={place(q,p,h)for q in K};assert core<=board
 cuts.append(dict(label=LABELS[i],tick=time,head=[*p,h],mass=len(board),active_core=sorted(core)))
 wordcuts.append(time)
 for ch in G[i]['word']:
  assert(ch=='L')==(p in board)
  board.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h]);time+=1
raw_end=dict(tick=time,head=[*p,h],mass=len(board),black=sorted(board))
assert time==94 and len(board)==29
for ch in M:
 assert(ch=='L')==(p in board)
 board.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p=add(p,V[h]);time+=1
for k,i in enumerate(ids):
 st=wordcuts[k];assert full[st:].startswith(G[i]['start_marker']);assert full[st+len(G[i]['word']):].startswith(M)
allmarks=[i for i in range(len(raw)+1)if full[i:i+len(M)]==M];assert allmarks==[0,10,28,84,94]
assert cuts[3]['head']==[-2,2,2]and cuts[3]['mass']==29
# Frozen quotient compatibility is a separate finite graph statement; no
# claim that this short physical seed realizes a particular150-history class.
paths=[([s],[])for s in range(J['classes'])]
for lab in ids:
 paths=[(vs+[v],ls+[lab])for vs,ls in paths for u,k,v in J['quotient_edges']if u==vs[-1]and k==lab]
assert len(paths)==77
D=[P,Path(__file__).resolve(),R/'word_stabilization/no_d_packet_fuel_manifest.json']
out=dict(status='AUTHOR_LITERAL_RETURN_BRIDGE_AND_MASS_OBSTRUCTION_PENDING_INDEPENDENT_AUDIT',scope='Seven supplied raw words have a common actual M11 core and are first-return words to M11 with actual right context. Finite23-cell DVFD+M11 control increases D-entry mass23→29 and flips N→S with zero literal C. Obstructs monotone-mass/literal-C-clock return shortcuts only, not seven-word finiteness or a general potential.',literal_words=literal,common_marker=M,common_core=sorted(K),control=dict(labels='DVFD',raw=raw,full_with_right_marker=full,seed=sorted(seed),cuts=cuts,raw_end=raw_end,marker_end=dict(tick=time,head=[*p,h],mass=len(board)),M11_occurrences=allmarks,D_return_raw_turns=84,D_return_start=[0,0,0],D_return_end=[-2,2,2],D_entry_mass_before=23,D_entry_mass_after=29,literal_C_count=0),quotient_DVFD_paths_count=len(paths),one_quotient_path=paths[0][0],quotient_scope='Label path compatibility only; no identification of physical seed with a particular historical quotient class.',dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(H/'marker_and_D_return.json').write_text(json.dumps(out,indent=2)+'\n');print('DVFD seed23 -> secondD mass29, nextDpose(-2,2,S), quotient paths77')
