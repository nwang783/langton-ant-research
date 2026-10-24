from pathlib import Path
import ast,hashlib,json
from collections import Counter
P=Path(__file__).resolve();R=P.parent.parent;S=R/'sources/kehao95-core/one_black/lean/OneBlack/EntryData.lean'
txt=S.read_text();i=txt.index('[',txt.index(':=',txt.index('def pristineLaneTimes')));d=0
for j in range(i,len(txt)):
 d+=(txt[j]=='[')-(txt[j]==']')
 if d==0:rows=ast.literal_eval(txt[i:j+1]);break
directions=(1j,1,-1j,-1)
def move(board,z,h):
 c='L'if z in board else'R';board.symmetric_difference_update({z});h=(h+(-1 if c=='L'else 1))%4
 return z+directions[h],h,c
board=set();z=0j;h=0
for _ in range(9977):z,h,_=move(board,z,h)
entry=z;heading=h;trace=[];seen=set();support=[];copy=board.copy()
for _ in range(104):
 if z not in seen:seen.add(z);support.append(z)
 z,h,c=move(copy,z,h);trace.append(c)
assert h==heading and len(support)==40
drift=z-entry;pristine=board&seen;assert len(pristine)==13
heads=[z for z in support if z+drift not in seen];assert len(heads)==len(rows)==22
def xy(z):return(int(z.real),int(z.imag))
def rotate(z,h):return z*((-1j)**h)
records=[]
for head,row in zip(heads,rows):
 black=pristine|{head+len(row)*drift};p=entry;hh=heading
 for _ in range(row[-1]):p,hh,_=move(black,p,hh)
 turn=(hh-heading)%4;future_drift=rotate(drift,turn)
 active={p+rotate(z-entry,turn)for z in support};required={p+rotate(z-entry,turn)for z in pristine}
 assert black&active==required
 # Exact all-future eligibility, solving z=s+k*d for integer k>=1.
 for b in black-active:
  for s in active:
   u=(b-s)/future_drift
   assert not(u.imag==0 and u.real.is_integer() and u.real>=1)
 start=p;word=[]
 for _ in range(104):p,hh,c=move(black,p,hh);word.append(c)
 assert word==trace and p-start==future_drift
 records.append(dict(head_relative=xy(head-entry),depth=len(row),anchor=row[-1],outgoing_drift=xy(future_drift)))
author=json.loads((R/'nonlinear_global_budget_2026-10-23/probe_pristine_channel_directions.json').read_text())
assert json.loads(json.dumps(records))==author['rows']
stats=Counter(tuple(r['outgoing_drift'])for r in records);assert stats=={(-2,-2):9,(2,-2):5,(-2,2):7,(2,2):1}
assert [r['head_relative']for r in records if r['outgoing_drift']==(2,2)]==[(-2,-8)]
out=dict(status='PASS independent 22 exact stable-anchor directions and complete finite-board terminal guards',incoming_drift=xy(drift),records=records,direction_counts={str(k):v for k,v in stats.items()},entry_data_sha256=hashlib.sha256(S.read_bytes()).hexdigest(),scope='Direct literal anchors and exact extra-black avoidance of every future standard read. Retained all-depth pristine coupling supplies the common post-contact stream. This supports remote singleton stability of any certified capturing finite base on21 non-opposite channels; no exceptional-channel or higher-mass uniform budget.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='records'})
