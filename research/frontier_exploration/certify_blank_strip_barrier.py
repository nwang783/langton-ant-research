#!/usr/bin/env python3
"""Create/replay a finite invariant of all possible one-sided block excursions.
The generator uses a two-read transition, independent of the literal searcher.
The optional checker independently replays every row with one-step dynamics.
"""
import argparse, hashlib, json, time
from collections import deque
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def pair_visit(mask,W,H,y):
 x=0;dx=1;steps=0;seen=set()
 while 0<=x<W:
  state=(mask,x,y,dx)
  assert state not in seen,'internal repeat';seen.add(state)
  i=x*H+y;a=1-2*((mask>>i)&1);mask^=1<<i;z=y-dx*a;steps+=1
  if not 0<=z<H:return 'vertical',mask,z,steps
  j=x*H+z;b=1-2*((mask>>j)&1);mask^=1<<j;dx=-dx*a*b;y=z;x+=dx;steps+=1
 return ('left' if x<0 else 'right'),mask,y,steps

def literal_visit(mask,W,H,y):
 x=0;heading=1;steps=0;seen=set();vectors=((0,1),(1,0),(0,-1),(-1,0))
 while 0<=x<W and 0<=y<H:
  state=(mask,x,y,heading)
  assert state not in seen,'internal repeat';seen.add(state)
  bit=x*H+y
  heading=(heading+(3 if (mask>>bit)&1 else 1))&3
  mask^=1<<bit;vx,vy=vectors[heading];x+=vx;y+=vy;steps+=1
 return ('vertical' if not 0<=y<H else 'left' if x<0 else 'right'),mask,y,steps

def make(W,H):
 Q=deque([0]);S={0};checks=0;longest=0;ys=range(1,H,2)
 while Q:
  mask=Q.popleft()
  for y in ys:
   side,m,z,steps=pair_visit(mask,W,H,y);checks+=1;longest=max(longest,steps)
   assert side!='right',('not barrier',W,H,mask,y)
   if side=='left' and m not in S:S.add(m);Q.append(m)
 data=''.join(f'{m:x}\n' for m in sorted(S)).encode()
 p=ROOT/f'barrier_h{H}_w{W}.hex';p.write_bytes(data)
 return dict(height=H,width=W,sector='H at x+y odd',entry_rows=list(ys),states=len(S),generator_checks=checks,max_excursion_steps=longest,certificate=p.name,sha256=hashlib.sha256(data).hexdigest())

def replay(meta):
 data=(ROOT/meta['certificate']).read_bytes();assert hashlib.sha256(data).hexdigest()==meta['sha256']
 S={int(z,16) for z in data.splitlines()};assert 0 in S and len(S)==meta['states'];W=meta['width'];H=meta['height'];checks=0;longest=0;left=vertical=0
 assert all(0<=m<1<<(W*H) for m in S)
 for mask in S:
  for y in range(1,H,2):
   a=literal_visit(mask,W,H,y);b=pair_visit(mask,W,H,y);assert a==b,(mask,y,a,b)
   side,m,z,steps=a;checks+=1;longest=max(longest,steps);assert side!='right'
   if side=='left':assert m in S;left+=1
   else:assert side=='vertical';vertical+=1
 return dict(status='PASS',replay_checks=checks,max_excursion_steps=longest,left_returns=left,vertical_exits=vertical)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('H',type=int);p.add_argument('W',type=int);p.add_argument('--replay-only',action='store_true');a=p.parse_args();path=ROOT/f'barrier_h{a.H}_w{a.W}.json';t=time.time()
 if a.replay_only:meta=json.loads(path.read_text())
 else:meta=make(a.W,a.H);path.write_text(json.dumps(meta,indent=2));print('generated',meta,flush=True)
 meta.update(replay(meta));meta['elapsed_seconds']=time.time()-t;path.write_text(json.dumps(meta,indent=2));print(json.dumps(meta,indent=2),flush=True)
