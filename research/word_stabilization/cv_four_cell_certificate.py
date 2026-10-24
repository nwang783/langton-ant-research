"""Four-cell finite inductive certificate for fresh V nose, using full colors."""
import json,collections
WORDS={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'}
D=((0,1),(1,0),(0,-1),(-1,0));P=((1,1),(1,2),(2,1),(2,2));I={p:i for i,p in enumerate(P)};QBIT=2
CENTERS=((0,-1),(0,0),(1,-1),(1,0));HEADS=tuple((a,b,h) for a,b in CENTERS for h in range(4));OUT=(9,9,9)
def pose(a,b,h):
 f=D[h];r=D[(h+1)%4];return ((-1+2*a-6*b-f[0]+r[0])//2,(1+6*a+2*b-f[1]+r[1])//2,h)
def trace(head,word):
 x,y,h=pose(*head);rr=[]
 for c in word:
  if (x,y) in I:rr.append((1<<I[x,y],c=='L'))
  h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return rr
T={};BOUNDARY=[];S=set();INITIAL=set()
for head in HEADS:
 a,b,h=head;da,db=((1,0),(0,-1),(-1,0),(0,1))[h]
 if (a-da,b-db) not in CENTERS:BOUNDARY.append(head)
 for k,w in WORDS.items():
  end=(a,b,(h-1)%4) if k=='C' else (a+da,b+db,h);end=end if end in HEADS else OUT
  seq=trace(head,w);T[head,k]=end,seq
  nr=[c for bit,c in seq if bit==QBIT]
  if nr and not nr[-1]:
   for color in range(16):
    v=color
    for bit,c in seq:
     if bool(v&bit)!=c:break
     v^=bit
    else:INITIAL.add((end,v))
S=set(INITIAL);todo=collections.deque(S)
def succ(s):
 head,color=s
 if head==OUT:return [(h,color) for h in BOUNDARY]
 ans=[]
 for k in WORDS:
  end,seq=T[head,k];goal=head==(0,0,0) and k=='V'
  if not goal and any(bit==QBIT for bit,c in seq):continue
  v=color
  for bit,c in seq:
   if bool(v&bit)!=c:break
   v^=bit
  else:
   assert not goal,('Counterexample',s)
   ans.append((end,v))
 return ans
while todo:
 for ns in succ(todo.popleft()):
  if ns not in S:S.add(ns);todo.append(ns)
assert INITIAL<=S and all(ns in S for s in S for ns in succ(s))
print('Full-color reachable states',len(S),'initial',len(INITIAL))
rows=[]
for head in (*HEADS,OUT):
 colors=sorted(v for h,v in S if h==head);mask=sum(1<<v for v in colors)
 print(head,hex(mask),colors);rows.append({'head':head,'allowed_colors':colors,'bitset':mask})
with open('/workspace/shared/langton/word_stabilization/cv_four_cell_certificate.json','w') as f:json.dump({'patch':P,'color_bit_order':['(1,1)','(1,2)','(2,1)','(2,2)'],'initial':sorted(INITIAL),'boundary':BOUNDARY,'reachable':rows},f,indent=2)
