#!/usr/bin/env python3
"""Literal canonical post-capture singleton reversal on the complete394 family.
Discovery only unless a separately specified exact tail/affine check is run.
"""
from pathlib import Path
import json, hashlib, sys, time
ROOT=Path('/workspace/shared/langton'); OUT=Path(__file__).parent
J=json.loads((ROOT/'causal_reduction/unit_scale/prepared4352_capture_manifest.json').read_text())
V=((0,1),(1,0),(0,-1),(-1,0))
def ev(a,m):return a[0]*m+a[1]
def step(B,p,h):
 c='L' if p in B else 'R';B.symmetric_difference_update({p});h=(h+(-1 if c=='L' else 1))%4;v=V[h]
 return (p[0]+v[0],p[1]+v[1]),h,c

def prefix(m):
 B={(ev(x,m),ev(y,m)) for x,y in J['seed_families']};init=set(B);z=J['initial_pose'];p=(ev(z['x_N_constant'],m),ev(z['y_N_constant'],m));h=z['heading'];reads=set();t=0
 for s in J['stages']:
  assert p==(ev(s['start_x_N_constant'],m),ev(s['start_y_N_constant'],m)) and h==s['heading']
  for _ in range(ev(s['count_N_constant'],m)):
   for c in s['word']:
    reads.add(p);p,h,actual=step(B,p,h);assert actual==c;t+=1
 assert p==(ev(J['end_pose_x_M_constant'],m),ev(J['end_pose_y_M_constant'],m)) and h==J['end_heading']
 return B,p,h,reads,t,init

def canonical():
 B=set();p=(0,0);h=0
 for _ in range(9977):p,h,_=step(B,p,h)
 entry=p;eh=h;H='';S=set();bb=set(B);q=p;hh=h
 for _ in range(104):S.add(q);q,hh,c=step(bb,q,hh);H+=c
 base=B&S
 return base,entry,eh,H

def period_suffix(word, n=300000):
 w=word[-n:];L=len(w);pi=[0]*L
 for i in range(1,L):
  j=pi[i-1]
  while j and w[i]!=w[j]:j=pi[j-1]
  if w[i]==w[j]:j+=1
  pi[i]=j
 return L-pi[-1]

def main(m=1,K=50,extra=0,steps=1000000):
 started=time.time();B,p,h,reads,t,init=prefix(m);base,entry,eh,H=canonical();tail=J['tail_word'];phase=next(i for i in range(104) if tail[i:]+tail[:i]==H)
 for c in tail[:phase]:reads.add(p);p,h,cc=step(B,p,h);assert cc==c;t+=1
 assert h==eh
 anchor=p;head=(p[0]-2,p[1]-8);obs=(head[0]-2*(11+K+extra),head[1]-2*(11+K+extra))
 assert obs not in reads and obs not in B and obs not in init
 original_mass=len(init)+1;B.add(obs)
 # Adding obs here is exactly equivalent to adding it to original seed because no earlier read owns it.
 out=[];poses=[];sample=[];last='';snaps=[]
 for i in range(steps):
  if i%100000==0:sample.append([i,list(p),h,len(B)])
  p,h,c=step(B,p,h);out.append(c)
 w=''.join(out);P=period_suffix(w);sample.append([steps,list(p),h,len(B)])
 report={'scope':__doc__,'M':m,'K':K,'extra':extra,'steps_after_canonical_boundary':steps,'canonical_phase':phase,'canonical_anchor':anchor,'canonical_time':t,'satellite_initial_cell':obs,'original_mass':original_mass,'original_prefix_unchanged':True,'suffix_period':P,'final_pose':[p,h],'final_mass':len(B),'samples':sample,'elapsed':time.time()-started,'word_sha256':hashlib.sha256(w.encode()).hexdigest()}
 if P<len(w)//2:
  i=len(w)-1
  while i>=P and w[i]==w[i-P]:i-=1
  st=i-P+1;report.update(periodic_sample_begin=st,period_word=w[st:st+P])
 name=f'return15324_M{m}_K{K}_extra{extra}'
 (OUT/(name+'.json')).write_text(json.dumps(report,indent=2)+'\n')
 (OUT/(name+'.word.txt')).write_text(w)
 (OUT/(name+'.final.json')).write_text(json.dumps({'black':sorted(B),'pose':[p,h]}))
 print(json.dumps({k:v for k,v in report.items() if k!='period_word'},indent=2))
if __name__=='__main__':main(*[int(x) for x in sys.argv[1:]])
