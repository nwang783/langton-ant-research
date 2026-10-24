"""Independent complete current-color closure for a fixed joint freshness kernel.
No imported transition code or saved traces. Every geometric/colored transfer is
reconstructed from the four literal words. This is a finite overapproximation,
not a finite trajectory experiment.
"""
import json,time,hashlib
from pathlib import Path
from collections import deque
R=Path('/workspace/shared/langton'); P=R/'word_stabilization'
DATA=R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'
WORDS={a:v['word'] for a,v in json.load(open(DATA)).items() if a in 'UVQB'}
MARKFILE=P/'cfree_kernel_current_marks.json'; marks={a:set(map(tuple,v)) for a,v in json.load(open(MARKFILE)).items()}
VECTORS=[(0,1),(1,0),(0,-1),(-1,0)]
def rotate(p,h):return p if h==0 else (-p[0],-p[1])
LITERAL={}
for a,w in WORDS.items():
 x=y=h=0; reads=[]; seen={}; first={}
 for c in w:
  q=x,y; b=int(c=='L'); assert q not in seen or seen[q]!=b
  reads.append((q,b));first.setdefault(q,b);seen[q]=b
  h=(h+(1 if c=='R' else -1))%4;dx,dy=VECTORS[h];x+=dx;y+=dy
 assert h in (0,2) and (x+y)%4==0
 assert all(first[p]==1 for p in marks[a])
 LITERAL[a]=(reads,(x,y,h))

def check(goal,target):
 patch=[(target[0]+dx,target[1]+dy) for dy in range(-2,3) for dx in range(-2,3)]
 bit={p:1<<i for i,p in enumerate(patch)}; qb=bit[target]
 heads=set()
 for h in (0,2):
  for reads,_ in LITERAL.values():
   for z,_ in reads:
    zx,zy=rotate(z,h)
    for px,py in patch:
     p=(px-zx,py-zy,h)
     if (p[0]+p[1])%4==0:heads.add(p)
 heads=sorted(heads,reverse=True); hid={h:i for i,h in enumerate(heads)}; OUT=len(heads)
 transfers={};sources=set();reentry=set()
 for pose,sid in hid.items():
  px,py,h=pose
  for a,(reads,(dx,dy,dh)) in LITERAL.items():
   dx,dy=rotate((dx,dy),h); end=px+dx,py+dy,(h+dh)%4
   inputs={};outputs={};markmask=0
   for z,colour in reads:
    zx,zy=rotate(z,h);bb=bit.get((px+zx,py+zy),0)
    if bb:inputs.setdefault(bb,colour);outputs[bb]=1-colour
   rm=sum(inputs); requirement=sum(bb for bb,c in inputs.items() if c); result=sum(bb for bb,c in outputs.items() if c)
   for z in marks[a]:
    zx,zy=rotate(z,h);markmask|=bit.get((px+zx,py+zy),0)
   to=hid.get(end,OUT)
   transfers[sid,a]=(to,rm,requirement,result,markmask)
   if rm&qb and result&qb:sources.add((to,rm,result))
   preh=(h-dh)%4; ddx,ddy=rotate(LITERAL[a][1][:2],preh)
   if (px-ddx,py-ddy,preh) not in hid:reentry.add(sid)
 queue=deque(sources); reached=set(sources); edges=0
 while queue:
  sid,known,black=queue.popleft()
  if sid==OUT:
   candidates=((to,known,black) for to in reentry)
  else:
   candidates=[]
   for a in WORDS:
    to,rm,req,result,mm=transfers[sid,a]
    isgoal=(heads[sid]==(0,0,0) and a==goal)
    if not isgoal and (rm&qb or known&mm):continue
    if (black^req)&known&rm:continue
    assert not isgoal,('ABSTRACT REUSE',goal,target,sid,known,black)
    candidates.append((to,known|rm,(black&~rm)|result))
  for t in candidates:
   edges+=1
   if t not in reached:reached.add(t);queue.append(t)
 return dict(macro=goal,site=target,heads=len(heads),sources=len(sources),reentry=len(reentry),states=len(reached),accepted_transfers=edges)

if __name__=='__main__':
 start=time.time();rows=[]
 for a in WORDS:
  for q in sorted(marks[a]):
   row=check(a,q);rows.append(row);print(row,flush=True)
 expected=json.load(open(P/'cfree_kernel_rounds.json'))[-1]
 assert expected['assumed']==expected['surviving']==json.load(open(MARKFILE))
 old={(r['macro'],tuple(r['site'])):int(r['stdout'].split('EXCLUDED ')[1].split()[0]) for r in expected['results']}
 assert all(row['states']==old[row['macro'],tuple(row['site'])] for row in rows)
 result={'status':'all stable joint freshness targets excluded by independent current-color closure','target_count':len(rows),'marks':{a:sorted(v) for a,v in marks.items()},'word_sha256':{a:hashlib.sha256(w.encode()).hexdigest() for a,w in WORDS.items()},'rows':rows,'seconds':time.time()-start}
 (R/'audits/cfree_kernel_independent.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS',len(rows),result['seconds'],flush=True)
