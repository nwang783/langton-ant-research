#!/usr/bin/env python3
"""Author exact local gap controls; no whole-front realization is asserted."""
import json,sys
from itertools import product
from pathlib import Path
from check_extremal_read_coupling import ROOT,D,event_word
sys.path.insert(0,str(ROOT/'computability'))
from check_rigid_reachability import State,forward,backward

def table(kind,T):
 counts={'raw':0,'endpoint':0,'color_consistent':0};accepted=[];rejections=[]
 for bb in product('RL',repeat=T):
  w=''.join(bb)
  if kind=='target' and (w[0]!='R' or w[-1]!='R'):continue
  if kind=='source' and not w.startswith('RL'):continue
  counts['raw']+=1;ev,d,h=event_word(w)
  if d!=(0,0) or h!=(2 if kind=='target' else 0):continue
  counts['endpoint']+=1
  seen={};ok=True;witness=None
  for e in ev:
   q=e['p']
   if q in seen and seen[q]==e['c']:ok=False;witness={'time':e['t'],'cell':q,'same_consecutive_color':e['c']};break
   seen[q]=e['c']
  if not ok or seen.get((0,0))!='R':
   rejections.append({'word':w,'conflict':witness or {'endpoint_color_expected':'R','actual':seen.get((0,0))}});continue
  counts['color_consistent']+=1;accepted.append(w+'L')
 return dict(kind=kind,gap=T,counts=counts,accepted=accepted,rejections=rejections)

def minimum(w):
 ev,_,_=event_word(w);seen={};seed=set()
 for e in ev:
  if e['p'] not in seen:
   if e['c']=='L':seed.add(e['p'])
  else:assert seen[e['p']]!=e['c']
  seen[e['p']]=e['c']
 return seed

def main():
 tables=[table(k,T) for k in ('target','source') for T in (4,8)]
 assert all(not a['accepted'] for a in tables)
 word='RRRLRRLRRLRRLLRLLRLLRLLL';seed=minimum(word);base=State(frozenset(seed),(0,0),0)
 s=backward(base);start=s;trace=[];H={}
 # One actual predecessor and one actual successor retain the marked endpoints
 # strictly inside this complete finite factor; neither endpoint is truncated.
 for t in range(26):
  c='L' if s.p in s.black else 'R';e={'t':t,'p':s.p,'h':s.h,'c':c};trace.append(e);H.setdefault(s.p,[]).append(e);s=forward(s)
 assert ''.join(e['c'] for e in trace[1:25])==word
 target=H[(0,0)];source=H[(0,1)]
 assert [(e['t'],e['c'],e['h']) for e in target]==[(1,'R',0),(13,'L',2)]
 assert [(e['t'],e['c'],e['h']) for e in source]==[(12,'R',1),(24,'L',1)]
 assert trace[12]['p']==(0,1) and trace[13]['p']==(0,0)
 result={'scope':'Exact short-gap exclusion plus actual finite sharp control; author-only.','tables':tables,'sharp_control':{'length':26,'initial_black':sorted(start.black),'initial_position':start.p,'initial_heading':start.h,'word':''.join(e['c'] for e in trace),'trace':trace,'final_black':sorted(s.black),'final_position':s.p,'final_heading':s.h,'source_history':source,'target_history':target,'source_age':12,'target_age':12,'read_interval_spanning_both':23,'limitation':'First/last are over this actual finite factor, not the complete infinite future. No periodic or regenerating claim.'}}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'tables':tables,'sharp_seed_mass':len(start.black),'sharp_word':result['sharp_control']['word'],'source':source,'target':target},indent=2))
if __name__=='__main__':main()
