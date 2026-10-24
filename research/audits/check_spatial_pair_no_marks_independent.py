#!/usr/bin/env python3
"""Independent finite proof checker for the all-gap spatial-pair induction.
Literal words, complex-coordinate geometry, and arbitrary-color feasibility.
Does not import generator, saved trace positions, or its feasibility checker.
"""
import json,hashlib,itertools
from pathlib import Path
R=Path(__file__).resolve().parents[1];CF='UVQB';ALL=CF+'C'
W={'C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR','Q':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR','B':'LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR'}
source=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text());assert all(W[a]==source[a]['word'] for a in ALL)
marks=json.loads((R/'word_stabilization/cfree_kernel_current_marks.json').read_text());M={a:{complex(*q)for q in marks[a]}for a in CF}
F={};FIRST={};LAST={};END={}
for a,w in W.items():
 p=0j;v=1j;first={};last={}
 for c in w:
  assert p not in last or last[p]!=c
  first.setdefault(p,c);last[p]=c;v*=(-1j if c=='R' else 1j);p+=v
 F[a]=set(first);FIRST[a]=first;LAST[a]=last;END[a]=(p,v/1j)
assert all(END[a][1] in (1,-1) for a in CF)
def tup(a,b,p,o):return(a,b,int(p.real),int(p.imag),0 if o==1 else 2)
def rel(a,p,o,b,q,v):return tup(a,b,(q-p)/o,v/o)
def feasible(word):
 p=0j;v=1j;seen={}
 for a in word:
  for c in W[a]:
   if seen.get(p)==c:return False
   seen[p]=c;v*=(-1j if c=='R' else 1j);p+=v
 return True
CAND=set()
for a,b,o in itertools.product(CF,ALL,(1,-1)):
 for q,z in itertools.product(F[a],F[b]):
  p=q-o*z
  if int(p.real+p.imag)%4==0:CAND.add(tup(a,b,p,o))
SHORT=set();good2=set()
for a,b in itertools.product(CF,ALL):
 p,o=END[a]
 if feasible(a+b):good2.add(a+b);SHORT.add(tup(a,b,p,o))
 for c in CF:
  if feasible(a+c+b):SHORT.add(tup(a,b,p+o*END[c][0],o*END[c][1]))
cert=json.loads((R/'word_stabilization/spatial_pair_kernel_no_marks.json').read_text())
S={tuple(row[:5])for row in cert['kernel']};assert len(S)==len(cert['kernel']) and S<=CAND and not(S&SHORT)
counts={'marked':0,'neighbors':0,'equal-read':0};reader_tests=neighbor_tests=0
for row in cert['kernel']:
 a,b,x,y,h,reason=row;p=complex(x,y);o=1 if h==0 else -1;kind=reason[0]
 assert kind in counts and kind!='marked';counts[kind]+=1
 if kind=='marked':
  assert b in CF and any(p+o*q in F[a] for q in M[b])
 elif kind=='neighbors':
  cp,co=END[a]
  for c,d in itertools.product(CF,repeat=2):
   if a+c not in good2 or d+b not in good2:continue
   do=o/END[d][1];dp=p-do*END[d][0]
   options=(tup(a,d,dp,do),rel(c,cp,co,b,p,o),rel(c,cp,co,d,dp,do));neighbor_tests+=1
   assert any(q in S for q in options),(row,c,d,options)
 else:
  q=complex(reason[1],reason[2]);local=(q-p)/o
  assert q in LAST[a] and local in FIRST[b] and LAST[a][q]==FIRST[b][local]
  readers=set()
  for c,co in itertools.product(CF,(1,-1)):
   for z in F[c]:
    cp=q-co*z
    if int(cp.real+cp.imag)%4==0:readers.add((c,cp,co))
  for c,cp,co in readers:
   reader_tests+=1
   assert tup(a,c,cp,co) in S or rel(c,cp,co,b,p,o)in S,(row,c,cp,co)
# Independently enumerate EVERY old footprint overlapping the terminal C input.
targets=set()
for a,o in itertools.product(CF,(1,-1)):
 for q in F[a]:
  p=q-o*complex(-1,0)
  if int(p.real+p.imag)%4==0:targets.add(tup(a,'C',p,o))
assert targets<=S
assert len(CAND)==cert['candidate_count'] and len(SHORT&CAND)==cert['short_pair_count']
fresh={}
for b in ALL:
 fresh[b]=[]
 for local,letter in FIRST[b].items():
  if letter!='L':continue
  pairs=set()
  for a,o in itertools.product(CF,(1,-1)):
   for old in F[a]:
    p=old-o*local
    if int(p.real+p.imag)%4==0:pairs.add(tup(a,b,p,o))
  if pairs<=S:fresh[b].append([int(local.real),int(local.imag)])
out={'fresh_first_L_sites':fresh,'status':'Independent literal all-gap induction certificate passed','candidate_pairs':len(CAND),'short_feasible_pairs':len(SHORT&CAND),'stable_forbidden_pairs':len(S),'proof_kinds':counts,'neighbor_options_checked':neighbor_tests,'intermediate_reader_options_checked':reader_tests,'terminal_C_input_pairs':len(targets),'all_terminal_input_pairs_excluded':True,'certificate_sha256':hashlib.sha256((R/'word_stabilization/spatial_pair_kernel_no_marks.json').read_bytes()).hexdigest(),'scope':'Every feasible C-free U/V/Q/B prefix followed by terminal C has a previously unread first-C input. No marked-site theorem is used; only literal colors and strict least-gap descent.'}
Path(__file__).with_name('spatial_pair_no_marks_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
