#!/usr/bin/env python3
"""Independent literal/complex-coordinate checker of right-extendible packet pairs.
No generator geometry, saved trace, feasibility, or marks are imported.
"""
import json,itertools,hashlib,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];START=time.time()
W={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR','Q':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR','B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
source=json.loads((ROOT/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text());assert all(W[a]==source[a]['word']for a in W)
O=(1,-1j,-1,1j);HI={o:h for h,o in enumerate(O)}
def literal(raw):
 p=0j;o=1;first={};last={};valid=True
 for a in raw:
  for c in W[a]:
   if last.get(p)==c:valid=False
   first.setdefault(p,c);last[p]=c;o*=(-1j if c=='R'else 1j);p+=1j*o
 return valid,first,last,p,o
# Exact grammar ingredients, independent of saved necessary-grammar tables.
assert not literal('CCCCC')[0]
for a in 'UVQB':
 assert not literal(a+'CCCC')[0]
 for b in 'UVQB':
  assert not literal(a+'CCC'+b)[0]
  if b!='V':
   assert not literal(a+'C'+b)[0] and not literal(a+'CC'+b)[0]
P={chr(97+3*i+k):a+'C'*k for i,a in enumerate('UVQB')for k in range(3)}
F={};FIRST={};LAST={};END={};MARK={};EXTFIRST={}
for a,raw in P.items():
 ok,first,last,p,o=literal(raw);assert ok
 F[a]=set(first);FIRST[a]=first;LAST[a]=last;END[a]=(p,o)
 if len(raw)>1:
  _,af,_,ap,ao=literal(raw[0]);q=ap-ao
  assert q not in af and first[q]=='L';MARK[a]=q
 EXTFIRST[a]=literal(raw+'V')[1]
def key(a,b,p,o):
 assert p.real==int(p.real) and p.imag==int(p.imag)
 return(a,b,int(p.real),int(p.imag),HI[o])
def relative(a,p,o,b,q,v):return key(a,b,(q-p)/o,v/o)
def sector(p,o):return (int(p.real+p.imag)-HI[o])%2==0
def legal_packets(w):
 if any(len(P[a])>1 and P[b][0]!='V'for a,b in zip(w,w[1:])):return False
 raw=''.join(P[a]for a in w)
 if len(P[w[-1]])>1:raw+='V'
 return literal(raw)[0]
CAND=set()
for a,b,o in itertools.product(P,P,O):
 for q,z in itertools.product(F[a],F[b]):
  p=q-o*z
  if sector(p,o):CAND.add(key(a,b,p,o))
GOOD2={a+b for a,b in itertools.product(P,repeat=2)if legal_packets(a+b)}
SHORT=set()
for a,b in itertools.product(P,repeat=2):
 p,o=END[a]
 if a+b in GOOD2:SHORT.add(key(a,b,p,o))
 for c in P:
  if legal_packets(a+c+b):SHORT.add(key(a,b,p+o*END[c][0],o*END[c][1]))
path=ROOT/'word_stabilization/spatial_packet_kernel.json';cert=json.loads(path.read_text());assert cert['words']==P
rows=cert['kernel'];S0={tuple(row[:5])for row in rows};assert len(S0)==len(rows)==40508
extensions=[['a','e',-1,5,2,['extended-equal-read',0,1]],['d','e',0,4,2,['extended-equal-read',0,0]]]
assert set(map(tuple,cert['unexcluded_completed_C_input_pairs']))=={tuple(x[:5])for x in extensions}
rows=rows+extensions
complete_path=ROOT/'word_stabilization/spatial_packet_kernel_complete.json';complete=json.loads(complete_path.read_text())
assert complete['words']==P and not complete['unexcluded_completed_C_input_pairs']
assert {tuple(z[:5]):z[5]for z in complete['kernel']}=={tuple(z[:5]):z[5]for z in rows}
assert len(complete['kernel'])==40510
S={tuple(row[:5])for row in rows};assert len(S)==40510 and S<=CAND and not(S&SHORT)
assert len(CAND)==cert['candidate_count']==42211 and len(SHORT&CAND)==cert['short_pair_count']==55
counts={'neighbors':0,'equal-read':0,'extended-equal-read':0};reader_tests=neighbor_tests=0;reader_cache={}
print('geometry/base cases pass',len(CAND),len(S),len(GOOD2),flush=True)
for rowindex,row in enumerate(rows):
 a,b,x,y,h,reason=row;p=complex(x,y);o=O[h];kind=reason[0];counts[kind]+=1
 if kind=='neighbors':
  cp,co=END[a]
  for c,d in itertools.product(P,repeat=2):
   if a+c not in GOOD2 or d+b not in GOOD2:continue
   do=o/END[d][1];dp=p-do*END[d][0]
   options=(key(a,d,dp,do),relative(c,cp,co,b,p,o),relative(c,cp,co,d,dp,do));neighbor_tests+=1
   assert any(v in S for v in options),(row,c,d,options)
 else:
  q=complex(reason[1],reason[2]);local=(q-p)/o
  first=EXTFIRST[b]if kind=='extended-equal-read'else FIRST[b]
  if kind=='extended-equal-read':assert len(P[b])>1
  assert q in LAST[a] and local in first and LAST[a][q]==first[local],row
  if q not in reader_cache:
   readers=set()
   for c,co in itertools.product(P,O):
    for z in F[c]:
     cp=q-co*z
     if sector(cp,co):readers.add((c,cp,co))
   reader_cache[q]=readers
  for c,cp,co in reader_cache[q]:
   reader_tests+=1
   assert key(a,c,cp,co)in S or relative(c,cp,co,b,p,o)in S,(row,c,cp,co)
 if rowindex%5000==0:print('clauses',rowindex,'seconds',round(time.time()-START,2),flush=True)
# Every possible earlier physical read of the first-C input is excluded.
targets=set()
for a,b,o in itertools.product(P,MARK,O):
 for q in F[a]:
  p=q-o*MARK[b]
  if sector(p,o):targets.add(key(a,b,p,o))
assert targets<=S
out={'status':'Independent complete packet-pair certificate passed','packet_words':P,'candidate_pairs':len(CAND),'short_feasible_pairs':len(SHORT&CAND),'forbidden_pairs':len(S),'proof_kinds':counts,'neighbor_options_checked':neighbor_tests,'intermediate_reader_options_checked':reader_tests,'completed_C_marker_pair_types':len(targets),'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'complete_certificate_sha256':hashlib.sha256(complete_path.read_bytes()).hexdigest(),'extension_clauses':extensions,'seconds':time.time()-START,'scope':'Packet factors beginning non-C with required V continuation after every nonempty C suffix; each completed C-run first input is fresh relative to that cut. No global ant-to-five-language premise.'}
Path(__file__).with_name('spatial_packets_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
