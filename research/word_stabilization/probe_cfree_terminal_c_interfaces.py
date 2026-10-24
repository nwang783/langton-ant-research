import json,itertools
from verify_macro_word import D,rot,check
M={a:set(map(tuple,ps))for a,ps in json.load(open('cfree_kernel_current_marks.json')).items()}
q=(-1,0);AA='UVQB'
def tr(s,p,h):return{(p[0]+rot(z,h)[0],p[1]+rot(z,h)[1])for z in s}
F={a:{tuple(z['p'])for z in D[a]['trace']}for a in AA}
def cen(p,h):x,y=rot((-1,1),h);return 2*p[0]+x,2*p[1]+y
def end(a,p,h):dx,dy=rot(D[a]['end_pose'][:2],h);return((p[0]+dx,p[1]+dy),(h+D[a]['end_pose'][2])%4)
def prev(a,p,h):h=(h-D[a]['end_pose'][2])%4;dx,dy=rot(D[a]['end_pose'][:2],h);return((p[0]-dx,p[1]-dy),h)
def feasible(w):
 try:check(w);return True
 except AssertionError:return False
sources=[]
for a in AA:
 last={tuple(z['p']):z['c']for z in D[a]['trace']}
 for z,c in last.items():
  if c!='R':continue
  for h in(0,2):
   dx,dy=rot(z,h);p=(q[0]-dx,q[1]-dy)
   if sum(p)%4==0:sources.append((a,p,h))
for left_depth,right_depth in[(1,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3)]:
 early=[];late=[]
 for a,p,h in sources:
  for suf in itertools.product(AA,repeat=left_depth-1):
   w=a+''.join(suf)
   if not feasible(w):continue
   pp,hh=p,h;fs=set();cs=set();valid=True
   for j,b in enumerate(w):
    ff=tr(F[b],pp,hh)
    if j and q in ff:valid=False;break
    fs|=ff;cs.add(cen(pp,hh));pp,hh=end(b,pp,hh)
   if valid:early.append((w,p,h,fs,cs))
 for pre in itertools.product(AA,repeat=right_depth):
  w=''.join(pre)
  if not feasible(w+'C'):continue
  pp,hh=(0,0),0;poses=[]
  for a in w[::-1]:pp,hh=prev(a,pp,hh);poses.append((a,pp,hh))
  marks=set();cs=set();valid=True
  for a,p,h in poses:
   if q in tr(F[a],p,h):valid=False;break
   marks|=tr(M[a],p,h);cs.add(cen(p,h))
  if valid:late.append((w,marks,cs))
 survive=[]
 for w,p,h,fs,cs in early:
  for v,ms,ds in late:
   if not fs&ms and not cs&ds:survive.append((w,p,h,v))
 print(left_depth,right_depth,'early',len(early),'late',len(late),'survivors',len(survive),survive[:12],flush=True)
