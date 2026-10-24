#!/usr/bin/env python3
"""Exact one-period interfaces among all cyclic cuts of three supplied words.
A legal pair is only a finite factor. It is not a recurrent controller.
"""
import json,time,hashlib
from pathlib import Path
from check_extremal_read_coupling import ROOT,event_word,D
G=ROOT/'nonlinear_global_budget_2026-10-23';OUT=Path(__file__).resolve().parent
WORDS={'S104':json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word'],'P1564':json.loads((G/'prepared_travelling_wave_certificate.json').read_text())['word'],'Q4352':json.loads((G/'second_prepared_wave_certificate.json').read_text())['word']}
LOW=-100;PITCH=201

def rot(q,r):
 x,y=q
 if r==0:return x,y
 if r==1:return y,-x
 if r==2:return -x,-y
 return -y,x

def bit(q):
 x,y=q;assert LOW<=x<=100 and LOW<=y<=100
 return 1<<((y-LOW)*PITCH+x-LOW)

def profiles(w):
 ev,d,h=event_word(w);N=len(w);out=[]
 for i in range(N):
  p=ev[i]['p'];r=(-ev[i]['hi'])%4;di=rot(d,r);first={};last={}
  for j in list(range(i,N))+list(range(i)):
   q=ev[j]['p'];q=(q[0]-p[0]+(d[0] if j<i else 0),q[1]-p[1]+(d[1] if j<i else 0));q=rot(q,r);c=w[j]
   if q in last:assert last[q]!=c
   else:first[q]=c
   last[q]=c
  Ib=Iw=Ob=Ow=0
  for q,c in first.items():
   if c=='L':Ib|=bit(q)
   else:Iw|=bit(q)
  for q,c in last.items():
   qe=(q[0]-di[0],q[1]-di[1])
   if c=='R':Ob|=bit(qe)
   else:Ow|=bit(qe)
  out.append((Ib,Iw,Ob,Ow,di,len(first)))
 return out

def literal_pair(a,i,b,j):
 A=WORDS[a];B=WORDS[b];w=A[i:]+A[:i]+B[j:]+B[:j];ev,d,h=event_word(w);seen={};seed=[]
 for e in ev:
  q=e['p'];c=e['c']
  if q in seen:
   if seen[q][0]==c:return {'legal':False,'first_conflict':{'time':e['t'],'cell':q,'requested':c,'previous_read_time':seen[q][1],'previous_read_turn':seen[q][0]}}
  elif c=='L':seed.append(q)
  seen[q]=(c,e['t'])
 return {'legal':True,'word_lengths':[len(A),len(B)],'initial_heading':0,'initial_position':[0,0],'minimum_black':sorted(seed),'minimum_black_count':len(seed),'final_position':d,'final_heading':h,'final_black':sorted(q for q,(c,t)in seen.items()if c=='R')}

def main():
 t=time.time();Ps={}
 for n,w in WORDS.items():
  Ps[n]=profiles(w);print('profiles',n,len(Ps[n]),'seconds',time.time()-t,flush=True)
 reports=[];edges={}
 for a,A in Ps.items():
  for b,B in Ps.items():
   if a==b:continue
   legal=[]
   for i,(_,_,Ob,Ow,_,_) in enumerate(A):
    for j,(Ib,Iw,_,_,_,_) in enumerate(B):
     if not ((Ob&Iw)or(Ow&Ib)):legal.append([i,j])
   edges[a+'->'+b]=legal
   witness=literal_pair(a,*legal[0][:1],b,legal[0][1]) if legal else None
   if witness:assert witness['legal']
   r={'source':a,'target':b,'all_phase_pairs':len(A)*len(B),'legal_pairs':len(legal),'witness_phases':legal[0]if legal else None,'witness':witness,'canonical_cut_pair':literal_pair(a,0,b,0)};reports.append(r)
   print('pair',a,b,len(legal),'/',len(A)*len(B),'seconds',time.time()-t,flush=True)
 result={'scope':__doc__,'word_hashes':{n:hashlib.sha256(w.encode()).hexdigest()for n,w in WORDS.items()},'common_boundary_heading':0,'coordinate_encoding':{'low':LOW,'pitch':PITCH,'bounds_check':'Every input/output coordinate asserted inside encoding; bound is storage only, not a search cutoff.'},'reports':reports,'elapsed':time.time()-t}
 (OUT/'all_cut_wave_interfaces.json').write_text(json.dumps(result,indent=2)+'\n');(OUT/'all_cut_wave_interface_edges.json').write_text(json.dumps(edges,separators=(',',':'))+'\n')
 print('DONE',time.time()-t,flush=True)
if __name__=='__main__':main()
