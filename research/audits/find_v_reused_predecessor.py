"""Find a finite physical control: lift freshness alone is not physical freshness.
This searches arbitrary turn prefixes, NOT five-macro prefixes.
"""
from pathlib import Path
from collections import deque
import json
R=Path('/workspace/shared/langton');data=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text());V=data['V']['word'];D=((0,1),(1,0),(0,-1),(-1,0))
p=(0,0);h=0;initial={};parity={}
for c in V:
 b=c=='L'
 if p not in initial:initial[p]=b
 else:assert initial[p]^parity[p]==b
 parity[p]=not parity.get(p,False)
 h=(h+(1 if c=='R' else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
q=(1,2)
def red(w):
 s=[]
 for a in w:
  if s and s[-1][0]==a:
   x=s.pop()[1]+1
   if x<4:s.append((a,x))
  else:s.append((a,1))
 return tuple(s)
def same(a,b):
 d=red(''.join(c*3 for c in a[::-1])+b)
 return any(d==red(('RLLL'*k if k>=0 else 'LRRR'*(-k))) for k in range(-len(d)-1,len(d)+2))
queue=deque([((0,0),0,initial,'')]);nodes=0
while queue:
 p,h,colors,back=queue.popleft();nodes+=1
 prev=(p[0]-D[h][0],p[1]-D[h][1])
 for curr in ([colors[prev]] if prev in colors else [False,True]):
  before=not curr;c='L' if before else 'R';ph=(h-(-1 if before else 1))%4
  nc=colors.copy();nc[prev]=before;nb=back+c
  if prev==q:
   prefix=nb[::-1]
   # Previous q read is first prefix read. V nose is its phase13.
   if not same('',prefix+V[:13]):
    word=prefix+V
    # Independently replay the word from the actual prehistory starting pose.
    seen={};seed=set();last={};pp=prev;hh=ph;vis=[]
    for t,letter in enumerate(word):
     b=letter=='L'
     if pp not in seen:
      seen[pp]=b
      if b:seed.add(pp)
     assert seen[pp]==b
     if pp==q:vis.append((t,letter))
     seen[pp]=not b;hh=(hh+(1 if letter=='R' else -1))%4;pp=(pp[0]+D[hh][0],pp[1]+D[hh][1])
    out=dict(status='finite physical witness',scope='arbitrary turn prefix, not a five-macro prefix',prefix=prefix,V=V,whole_word=word,start_pose=[prev,ph],entry_pose_V=[[0,0],0],target=q,target_visits=vis,initial_black=sorted(seed),previous_tip_coset_is_different=True,search_nodes=nodes)
    (R/'audits/v_reused_arbitrary_prefix.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit
  elif len(nb)<30:
   queue.append((prev,ph,nc,nb))
 if nodes>2000000:raise RuntimeError('search cap')
