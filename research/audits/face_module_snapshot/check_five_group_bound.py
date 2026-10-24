"""Same interface as check_six_cell_bound.py, counting only each canonical group state.
A last-boundary alias of the tracked cell does not count as this group state.
"""
"""Finite overapproximation of all reads of a parent face's two interior cells.
The parent and its two children are explicit; four grandchildren are abstract
modules whose completed-return language is {empty,G,B,GB}. Their interiors
cannot touch either tracked cell. Arbitrary exterior resets of the parent
boundary are permitted between calls. Thus any bound here follows from the
module lemma and module geometry, not from a depth cutoff in the ant.
"""
from itertools import product
# parent, root, first interior, second interior, sign, child IDs
mods=[(1,0,2,3,0,1,2),(0,2,4,5,1,3,4),(2,3,6,7,1,5,6)]
# Abstract grandchildren: parent, root, sign
leaves={3:(2,4,0),4:(4,5,0),5:(3,6,0),6:(6,7,0)}
maxima=[0,0];states=0;terminal=0;witness=[None,None]; conditioned=[[0,0],[0,0]]; initial=(0,0)
def read(colors,cell,counts,canonical=False):
 colors[cell]^=1
 if canonical and cell in (2,3):counts[cell-2]+=1

def walk(colors,ledgers,stack,calls,counts,events):
 global states,terminal
 states+=1
 while stack:
  mod,pc=stack[-1]
  if mod>=3:
   p,w,a=leaves[mod];assert colors[w]==a
   read(colors,w,counts)
   st=ledgers[mod-3]
   # A nonreturning leaf can always terminate the observed portion here.
   stop(counts,events+[(mod,'nonreturn')])
   if st==2:return
   assert colors[p]==a,('wrong leaf parent',mod,colors,events)
   for out in ('G','B') if st==0 else ('B',):
    c=colors.copy();l=ledgers.copy();n=counts.copy();ss=stack[:-1].copy()
    if out=='B':c[w]=a
    read(c,p,n);l[mod-3]=1 if out=='G' else 2
    walk(c,l,ss,calls,n,events+[(mod,out)])
   return
  p,w,x,y,a,c1,c2=mods[mod]
  if pc==-1:
   assert colors[w]==a
   read(colors,w,counts,canonical=True);stack[-1]=(mod,0)
  elif pc in (0,1):
   cell,child=(x,c1) if pc==0 else (y,c2)
   if colors[cell]==a:
    read(colors,cell,counts,canonical=(mod==0));stack[-1]=(mod,pc+1)
   else:stack.append((child,-1))
  else:
   assert colors[p]==a,('wrong explicit parent',mod,colors,events)
   read(colors,p,counts);stack.pop()
 if calls<3:
  colors[0]=colors[1]=0
  walk(colors,ledgers,[(0,-1)],calls+1,counts,events+[(0,'exterior reset')])
 else:
  raise AssertionError(('three parent returns',events))

def stop(counts,events):
 global terminal
 terminal+=1
 for i,n in enumerate(counts):
  conditioned[i][initial[i]]=max(conditioned[i][initial[i]],n)
  if n>maxima[i]:maxima[i]=n;witness[i]=events
for bits in product(range(2),repeat=6):
 initial=bits[:2]
 walk([0,0]+list(bits),[0]*4,[(0,-1)],1,[0,0],[])
assert maxima==[4,5],maxima
assert conditioned==[[4,4],[5,4]],conditioned
print('PASS: all64 initial local color states, four arbitrary grandchild return interfaces; max reads',maxima,'states',states,'terminal traces',terminal)
print('Witness first interior:',witness[0])
print('Witness second interior:',witness[1])

print("Conditioned on tracked initial color [same,opposite]:",conditioned)
