"""Exploratory exact two-packet ledger with inherited signed transfer exclusions.
No generated rank or UNSAT alone is a global capture theorem.
"""
import json,collections
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
D=[1j,1,-1j,-1];P=Path(__file__).parent
G=json.load(open(P/'dcv_residual_core_resources.json'))['geometry']; gr=json.load(open(P/'seven_sub_dcv_grammar.json')); keep={0,1,4,5,6}
F={tuple(map(int,l.split()[:5])) for l in open(P/'seven_sub_dcv_star4_kernel.tsv')};H={tuple(map(int,l.split()[:7])) for l in open(P/'dcv_protected_patch2_kernel.tsv')}
xy=lambda z:[int(z.real),int(z.imag)]
def posekey(a,b,z,h):return (a,b,int(z.real),int(z.imag),h%4)
def rot(z,h):return z*(-1j)**h
def trace(w):
 z=0j;h=0;first={};last={};odd=set()
 for c in w:
  if last.get(z)==c:return None
  first.setdefault(z,c=='L');last[z]=c;odd.symmetric_difference_update({z});h=(h+(1 if c=='R' else -1))%4;z+=D[h]
 return z,h,first,odd
core={z for z,c in trace('LLLLRLRRRRL')[2].items() if c}
M=[]
for a,b in gr['pairs']:
 if a not in keep or b not in keep:continue
 name=G[a]['name']+'|'+G[b]['name'];word=gr['macros'][a]['word']+gr['macros'][b]['word'];r=trace(word);t=trace(word+'LLLLRLRRRRL');assert r and t
 p=0j;h=0;ins={};outs={};parts=[]
 for j,c in enumerate((a,b)):
  parts.append((c,p,h))
  for k,z in enumerate(G[c]['inputs']):
   z=p+rot(complex(*z),h)
   if z in outs:del outs[z]
   else:assert z not in ins;ins[z]=(j,k)
  for k,z in enumerate(G[c]['outputs']):
   z=p+rot(complex(*z),h);assert z not in outs;outs[z]=(j,k)
  p+=rot(complex(*G[c]['endpoint'][:2]),h);h=(h+G[c]['endpoint'][2])%4
 ei={z for z,c in t[2].items() if c}-core;eo=({z for z,c in t[2].items() if c}^r[3])-{p+rot(z,h) for z in core}
 assert set(ins)==ei and set(outs)==eo
 M.append({'name':name,'word':word,'endpoint':xy(p)+[h],'parts':[[c,*xy(z),h] for c,z,h in parts],'inputs':[xy(z)+list(meta) for z,meta in sorted(ins.items(),key=lambda x:xy(x[0]))],'outputs':[xy(z)+list(meta) for z,meta in sorted(outs.items(),key=lambda x:xy(x[0]))]})
T=[];why=collections.Counter();raw=0
for a,A in enumerate(M):
 for k,o in enumerate(A['outputs']):
  q=complex(*o[:2]);start=o[2]
  for b,B in enumerate(M):
   for j,i in enumerate(B['inputs']):
    end=i[2]
    for h in range(4):
     p=q-rot(complex(*i[:2]),h)
     if (int(p.real+p.imag)-h)%2:continue
     raw+=1;blocked=False
     for ai,(aa,ax,ay,ah) in enumerate(A['parts']):
      ap=complex(ax,ay)
      for bi,(bb,bx,by,bh) in enumerate(B['parts']):
       bp=p+rot(complex(bx,by),h);bh=(bh+h)%4;dp=rot(bp-ap,-ah);dh=(bh-ah)%4
       if posekey(aa,bb,dp,dh) in F:blocked=True;why['ordinary']+=1;break
       qq=rot(q-ap,-ah)
       if ai>=start and bi<=end and (*posekey(aa,bb,dp,dh),*xy(qq)) in H:blocked=True;why['protected']+=1;break
      if blocked:break
     if not blocked:T.append([a,k,b,j,*xy(p),h])
ins=[(a,k) for a,A in enumerate(M) for k in range(len(A['inputs']))];outs=[(a,k) for a,A in enumerate(M) for k in range(len(A['outputs']))];I={v:k for k,v in enumerate(ins)};O={v:k+len(ins) for k,v in enumerate(outs)};n=len(ins)+len(outs)
rows=[];rhs=[]
for a,k,b,j,x,y,h in T:
 row=np.zeros(n);row[I[b,j]]=1;row[O[a,k]]=-1;rows.append(row);rhs.append(0)
for a,A in enumerate(M):
 row=np.zeros(n)
 for k in range(len(A['inputs'])):row[I[a,k]]=-1
 for k in range(len(A['outputs'])):row[O[a,k]]=1
 rows.append(row);rhs.append(-1)
r=linprog(np.ones(n),A_ub=rows,b_ub=rhs,bounds=(0,None),method='highs')
result={'status':'exploratory','compounds':M,'transfer_edges':T,'raw_transfer_poses':raw,'exclusions':dict(why),'linear_rank':r.message}
if r.success:result['linear_weights']={'inputs':[[a,k,float(r.x[I[a,k]])] for a,k in ins],'outputs':[[a,k,float(r.x[O[a,k]])] for a,k in outs]}
(P/'dcv_compound_resources.json').write_text(json.dumps(result,indent=2));print('compounds',len(M),'inputs',len(ins),'outputs',len(outs),'raw',raw,'remain',len(T),'exclusions',why,'linear',r.message)
