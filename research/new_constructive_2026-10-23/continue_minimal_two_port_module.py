#!/usr/bin/env python3
"""Canonical natural continuation of the exact minimal-input two-port module.
No new bits, caps, field crop or controller. Each M denotes a different finite seed.
"""
from pathlib import Path
import json,hashlib,sys,time
P=Path('/workspace/shared/langton');O=Path(__file__).parent
J=json.loads((P/'causal_reduction/unit_scale/prepared4352_capture_manifest.json').read_text());V=((0,1),(1,0),(0,-1),(-1,0))
def step(B,p,h):
 c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4;v=V[h];return(p[0]+v[0],p[1]+v[1]),h,c

def force(w,p,h):
 initial=set();seen={};flip=set();p0=p;h0=h
 for i,c in enumerate(w):
  if p in seen:assert seen[p][0]!=c,(i,p,c,seen[p])
  elif c=='L':initial.add(p)
  seen[p]=(c,i);flip.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
 return initial,initial^flip,p,h

def suffixperiod(word):
 w=word[-300000:];pi=[0]*len(w)
 for i in range(1,len(w)):
  j=pi[i-1]
  while j and w[i]!=w[j]:j=pi[j-1]
  if w[i]==w[j]:j+=1
  pi[i]=j
 return len(w)-pi[-1]

def main(m=1,steps=1000000):
 started=time.time();W=J['stages'][11]['word'];T=J['stages'][12]['word'];R=J['stages'][13]['word'];Z=J['stages'][14]['word'];w='RLL'+W*(3*m+4)+T+R*m+Z[:17395]
 initial,B,p,h=force(w,(-2,2),0);assert (p,h)==((9,-10),3);assert{q for q in B if sum(q)<=0}=={(-2,2),(10,-10)}
 for c in'RR':p,h,cc=step(B,p,h);assert cc==c
 assert(p,h)==((10,-9),1)
 origsuffix=Z[17395+2:];out=[];dev=None;samples=[]
 for i in range(steps):
  if i%100000==0:samples.append([i,list(p),h,len(B)])
  p,h,c=step(B,p,h);out.append(c)
  if i<len(origsuffix) and dev is None and c!=origsuffix[i]:dev={'offset_after_RR':i,'absolute_time':len(w)+2+i,'original_wanted':origsuffix[i],'minimal_actual':c}
 word=''.join(out);per=suffixperiod(word);report={'scope':__doc__,'M':m,'initial_mass':len(initial),'exact_module_length':len(w),'at_exit_mass':len(force(w,(-2,2),0)[1]),'forced_RR_reentry_pose':[[10,-9],1],'natural_steps_after_reentry':steps,'first_difference_from_original394_response':dev,'suffix_period':per,'final_pose':[p,h],'final_mass':len(B),'samples':samples,'elapsed':time.time()-started}
 if per<150000:
  i=len(word)-1
  while i>=per and word[i]==word[i-per]:i-=1
  st=i-per+1;report['periodic_sample_begin']=st;report['candidate_word']=word[st:st+per]
 (O/f'minimal_two_port_M{m}.json').write_text(json.dumps(report,indent=2)+'\n');(O/f'minimal_two_port_M{m}.final.json').write_text(json.dumps({'black':sorted(B),'pose':[p,h]}));(O/f'minimal_two_port_M{m}.initial.json').write_text(json.dumps({'black':sorted(initial),'pose':[[-2,2],0]}));print(json.dumps({k:v for k,v in report.items()if k!='candidate_word'},indent=2))
if __name__=='__main__':main(*map(int,sys.argv[1:]))
