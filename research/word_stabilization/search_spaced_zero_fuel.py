from pathlib import Path
from collections import defaultdict
import json,random,time
random.seed(20261022);start=time.time();Q=json.load(open('spaced_two_marker_port_quotient.json'));P=json.load(open('spaced_two_marker_actual_ports.json'));M=json.load(open('spaced_two_marker_macros.json'))['macros'];A=defaultdict(list)
for u,a,v in Q['quotient_edges']:A[u].append((a,v))
REP={}
for i,c in enumerate(P['classes']):REP.setdefault(c,i)
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(w):
 p=0j;h=0;F={};L={}
 for c in w:
  assert L.get(p)!=c
  F.setdefault(p,c);L[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=complex(*D[h])
 return F,L,p,h
T=[]
for z in M:
 f,l,p,h=trace(z['word']);ff,ll,pp,hh=trace(z['word']+z['end_marker']);T.append([(tuple((q*((-1j)**r),c)for q,c in ff.items()),tuple((q*((-1j)**r),c)for q,c in l.items()),p*((-1j)**r),h)for r in range(4)])
classes=list(REP);random.shuffle(classes);nodes=0;tests=0;least=1000;best=None;stop=False
for c0 in classes:
 idx=REP[c0];pre=P['port_histories'][idx][:-12];field={};p=0j;h=0
 for c in pre:assert field.get(p)!=c;field[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=complex(*D[h])
 seen=set();word=[];local=0
 def dfs(c,p,h,depth):
  global nodes,tests,least,best,stop,local
  nodes+=1;local+=1
  if local>1500 or depth>=24:return
  options=A[c][:];random.shuffle(options)
  for a,dest in options:
   f,l,dp,dh=T[a][h];ff=[(p+q,z)for q,z in f]
   if any(field.get(q)==z for q,z in ff):continue
   if M[a]['K_end_indices']:
    tests+=1;fresh=[q for q,z in ff if z=='L'and q not in seen]
    if len(fresh)<least:
     least=len(fresh);best={'start_port':idx,'initial_class':c0,'prehistory':pre,'macros':word+[a],'fresh_count':least};print('BEST',least,'nodes',nodes,'word',word+[a],flush=True)
    if not fresh:stop=True;return
   changes=[];added=[]
   for q,z in l:
    q+=p;changes.append((q,field.get(q)));field[q]=z
    if q not in seen:seen.add(q);added.append(q)
   word.append(a);dfs(dest,p+dp,(h+dh)%4,depth+1);word.pop()
   for q,z in changes:
    if z is None:del field[q]
    else:field[q]=z
   for q in added:seen.remove(q)
   if stop or local>1500:return
 dfs(c0,p,h,0)
 if stop or nodes>=500000:break
out={'status':'physical zero-new-entry-black bad-macro witness found'if stop else'bounded search inconclusive','nodes':nodes,'bad_macro_tests':tests,'least_new_fuel':least,'best':best,'seconds':time.time()-start};Path('spaced_zero_fuel_search.json').write_text(json.dumps(out,indent=2));print(out)
