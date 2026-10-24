#!/usr/bin/env python3
"""Independent full turn-word enumeration, complex headings and current colors."""
from pathlib import Path
import itertools,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'causal_reduction/matrix_candidates/rectangular_axis_turn_k13_domains.txt'
tok=source.read_text().split();k,a,b=map(int,tok[:3]);i=3;saved=[];actual=[]
for q in range(4):
 n=int(tok[i]);i+=1;saved.append(tok[i:i+n]);i+=n
 start=1j if q//2==0 else 1
 out=start*(-1j if q%2==0 else 1j)
 target=complex(a*out.real,b*out.imag)
 accepted=[]
 for turns in itertools.product('RL',repeat=k):
  z=0j;v=start;colors={};ok=True
  for turn in turns:
   bit=int(turn=='L')
   if z in colors and colors[z]!=bit:ok=False;break
   colors[z]=1-bit;v*=(-1j if turn=='R' else 1j);z+=v
  if ok and z==target and v==out:accepted.append(''.join(turns))
 assert sorted(saved[-1])==sorted(accepted),(q,len(saved[-1]),len(accepted))
 actual.append(accepted)
out=Path(__file__).with_suffix('.txt')
with out.open('w') as f:
 f.write(f'{k} {a} {b}\n')
 # Keep independent R-before-L enumeration, not source ordering.
 for words in actual:f.write(str(len(words))+'\n'+'\n'.join(words)+'\n')
result=dict(status='COMPLETE DOMAIN MATCH',counts=list(map(len,actual)),words_tested_per_context=2**k,independent_domain_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),source_domain_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
