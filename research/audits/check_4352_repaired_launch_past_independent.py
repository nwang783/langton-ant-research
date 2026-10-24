"""Exact complete causal launch field and one-bit repaired inverse staircase.
No author code imports. All full-field equality classes are checked.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale'
L=json.loads((U/'prepared4352_fresh_launch.json').read_text());A=json.loads((U/'prepared4352_repaired_launch_past.json').read_text());W=json.loads((ROOT/'nonlinear_global_budget_2026-10-23/second_prepared_wave_certificate.json').read_text())['word'];H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];D=(1j,1,-1j,-1)
xy=lambda p:(int(p.real),int(p.imag))
def trace(w,p,h):
 rows=[]
 for i,c in enumerate(w):rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h
def key(p):
 x,y=xy(p);return(x-y,x%78),x//78
full=set();rays=defaultdict(set);F=set()
def lower(p):
 cl,k=key(p);full.symmetric_difference_update({cl});rays[cl].symmetric_difference_update({k-1})
def color(p):
 cl,k=key(p);return(cl in full)^(sum(k<=a for a in rays[cl])%2)^(p in F)
# Build actual infinite strict-past standard history at phase28, from literal
# forward H reads, rather than using desired inverse-tail initial colors.
entry=-24-17j;hentry=3;hr,delta,hh=trace(H,0j,3);assert delta==-2-2j and hh==3
origin=entry-hr[28][1];hr,_,_=trace(H,origin,3);assert hr[28][1:3]==(entry,hentry)
for i,q,h,c in hr:
 nmax=(27-i)//104;cut=q+nmax*delta
 for r in range(39):lower(cut+2*r*(1+1j))
for t,a in map(tuple,L['other_full_black_profiles']):
 for r in range(a,78,2):full.symmetric_difference_update({(t,r)})
F={complex(*p)for p in L['fresh_cap']};assert len(F)==289
p=entry;h=hentry
for c in L['forward_prelude_word']:
 assert color(p)==(c=='L');F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert(p,h)==(-2+3j,3)
repair=14-7j;assert color(repair);F.symmetric_difference_update({repair})
# Whole-plane exact equality with the supplied serialized field: all modulus78
# classes, all thresholds and ALL finite XOR points, including untouched cells.
B=A['initial_board'];assert B['modulus']==78;afull=set(map(tuple,B['full']));arays={tuple(c):set(v)for c,v in B['upper_rays']};af={complex(*p)for p in B['finite_xor']}
classes=set(full)|set(rays)|afull|set(arays)|{key(p)[0]for p in F|af};equalitytests=0
for cl in classes:
 tests={0}
 for t in rays.get(cl,set())|arays.get(cl,set()):tests.update((t-1,t,t+1))
 for q in F|af:
  cc,k=key(q)
  if cc==cl:tests.update((k-1,k,k+1))
 tests.update((min(tests)-1,max(tests)+1))
 t,a=cl
 for k in tests:
  q=complex(a+78*k,a+78*k-t);want=(cl in afull)^(sum(k<=z for z in arays.get(cl,()))%2)^(q in af);assert color(q)==want;equalitytests+=1
# Entire future4352 READ ownership, not a finite window.
wr,ep,eh=trace(W,-2+3j,3);assert ep==24+29j and eh==3
readhits=[]
for i,q,h,c in wr:
 z=repair-q
 if z.real==z.imag and int(z.real)%26==0 and z.real>=0:readhits.append((i,int(z.real)//26))
assert not readhits
wave_full=set(full);wave_rays={cl:set(v)for cl,v in rays.items()};wave_F=set(F)
# Unique inverse orbit from the correct reversed boundary pose.
p=-1+3j;h=1;first=None
for i,c in enumerate(A['word']):
 assert color(p)==(c=='L')
 if i<len(L['inverse_prefix'])and c!=L['inverse_prefix'][i]and first is None:first=(i,xy(p),h,L['inverse_prefix'][i],c)
 F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert len(A['word'])==1605 and(p,h)==(17-4j,0)and first==(1599,(14,-7),0,'L','R')
# Complete field equality after the prefix follows from the independently
# checked initial whole-plane equality and identical actual cell toggles.
# Individual finite-XOR encodings need not coincide across ray normal forms.
# Exact every-future-read RL staircase. Read classes21 and22 are disjoint;
# split r modulo78, then only threshold/finite exceptions can change color.
tests=0
for q,want in ((17-4j,False),(18-4j,True)):
 for residue in range(78):
  z=q+residue*(1+1j);cl,k0=key(z);critical={0}
  for t in rays.get(cl,()):
   for n in(t-k0-1,t-k0,t-k0+1):
    if n>=0:critical.add(n)
  for f in F:
   cc,k=key(f)
   if cc==cl:
    for n in(k-k0-1,k-k0,k-k0+1):
     if n>=0:critical.add(n)
  critical.add(max(critical)+1)
  for n in critical:assert color(z+78*n*(1+1j))==want;tests+=1
# Independently assemble the separately supplied complete return-end limit:
# all completed positive4352 copies, remote past15324 copies, passive helpers.
full=set(wave_full);rays=defaultdict(set,{cl:set(v)for cl,v in wave_rays.items()});F=set(wave_F)
for t in(89,-57):
 counts=defaultdict(int)
 for i,q,h,c in trace(H,complex(0,-t),1)[0]:
  xx,yy=xy(q);counts[xx-yy,xx%2]+=1
 for(t0,a),cnt in counts.items():
  if cnt%2:
   for r in range(a,78,2):full.symmetric_difference_update({(t0,r)})
for i,q,h,c in wr:
 for r in range(3):lower(q+26*r*(1+1j))
returnword=json.loads((U/'prepared4352_output_return_wave.json').read_text())['word']
for i,q,h,c in trace(returnword,117+111j,0)[0]:lower(q+78*(1+1j))
p=117+111j;h=0
for i in range(17358):
 c=returnword[i%len(returnword)];assert color(p)==(c=='L'),(i,xy(p),h,c)
 F.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert(p,h)==(14-8j,2)and returnword[17358%len(returnword)]=='L'and not color(p)
for i,q,h,c in wr:
 z=p-q;assert not(z.real==z.imag and int(z.real)%26==0 and z.real>=0)
out=dict(status='PASS independent complete one-bit-repaired4352 launch field and unique inverse RL staircase',source_sha256=hashlib.sha256((U/'prepared4352_repaired_launch_past.json').read_bytes()).hexdigest(),full_field_equality_classes=len(classes),full_field_equality_tests=equalitytests,repair=xy(repair),repair_future4352_unread=True,inverse_prefix_reads=1605,first_divergence=first,staircase_entry=((17,-4),0),staircase_drift=(1,1),exact_staircase_tests=tests,return_end_prescribed_reads=17358,next_deficit=((14,-8),2,'L','R'),scope='Exact supplied complete field only. Unique inverse RL tail rules out standard104 ancestry for this unchanged repaired field; no other future-unread edits, producer, finite staircase, or finite-seed noncapture is excluded.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
