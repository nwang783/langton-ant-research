from pathlib import Path
from collections import defaultdict
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];R=ROOT/'nonlinear_global_budget_2026-10-23';U=ROOT/'causal_reduction/unit_scale';D=(1j,1,-1j,-1)
J=json.loads((U/'LLR_inverse_completion_certificate.json').read_text());N=json.loads((R/'prepared_wave_five_band_normal_form.json').read_text());W=json.loads((R/'prepared_travelling_wave_certificate.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
xy=lambda p:(int(p.real),int(p.imag));bulkclasses=set(map(tuple,N['full_black_orbit_profiles']));bulk=lambda p:(int(p.real-p.imag),int(p.real)%2)in bulkclasses
base=set(map(lambda z:complex(*z),N['finite_XOR_cap']));edits=set(map(lambda z:complex(*z),J['initial_wave_XOR_edits']));assert len(edits)==21 and len(base)==2

def trace(word,p,h):
 rows=[]
 for i,c in enumerate(word):
  rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h

def raydata(word,p,h):
 rows,ep,eh=trace(word,p,h);delta=ep-p;assert eh==h and delta.real==delta.imag and delta.real>0;k=int(delta.real);G=defaultdict(list)
 for i,z,hh,c in rows:
  x,y=xy(z);a=x%k;G[x-y,a].append(((x-a)//k,i,c))
 for ls in G.values():
  ls.sort(key=lambda z:z[1]-len(word)*z[0]);assert all(a[2]!=b[2]for a,b in zip(ls,ls[1:]))
 return k,G

def future(p,k,G):
 x,y=xy(p);a=x%k;ls=G.get((x-y,a));return bool(ls)and(x-a)//k>=min(row[0]for row in ls)

def certify(word,p,h,F):
 k,G=raydata(word,p,h);checks=0
 for(t,a),ls in G.items():
  lo=min(z[0]for z in ls);hi=max(z[0]for z in ls);nums=set(range(lo,hi+1))
  for z in F:
   x,y=xy(z)
   if(x-y,x%k)==(t,a)and(x-a)//k>=lo:nums.add((x-a)//k)
  nums.add(max(nums)+1)
  for n in nums:
   first=next(c for kk,i,c in ls if kk<=n);z=complex(a+k*n,a+k*n-t);assert bulk(z)^(z in F)==(first=='L'),(z,first);checks+=1
 return k,G,checks
kw,Gw=raydata(W['word'],-6-6j,0)
assert all(not future(z,kw,Gw)for z in edits)
F=base^edits;inv=J['inverse_prefix'];rows,p,h=trace(inv,-6-7j,2)
for i,z,hh,c in rows:
 assert bulk(z)^(z in F)==(c=='L');F.symmetric_difference_update({z})
assert (p,h)==(4+1j,0)and len(inv)==24
ki,Gi,icheck=certify(J['inverse_tail_word'],p,h,F);assert ki==2 and len(Gi)==22
_,_,wcheck=certify(W['word'],-6-6j,0,base^edits)
forward=''.join('L'if c=='R'else'R'for c in inv[::-1]);assert forward==J['forward_prelude_word'];entry=p-D[h];eh=(h+2)%4;fr,ep,fh=trace(forward,entry,eh);cur=set(F)
for i,z,hh,c in fr:
 assert bulk(z)^(z in cur)==(c=='L');cur.symmetric_difference_update({z})
assert(ep,fh)==(-6-6j,0)and cur==base^edits
assert sorted(map(list,map(xy,F)))==J['forward_entry_cap_vs_full_bulk']
# Full standard strict past at the actual boundary, from fresh canonical physical H.
hr,_,_=trace(H,-15-16j,3);phase=55;copy=-11;tau=104*copy+phase
assert hr[phase][1]+copy*(-2-2j)==entry and hr[phase][2]==eh
expectedI=''.join('L'if H[(phase-1-i)%104]=='R'else'R'for i in range(104));assert expectedI==J['inverse_tail_word']
old=lambda q:((int(q.real-q.imag),int(q.real)%2),(int(q.real)%2-int(q.real))//2)
rays=defaultdict(list);past={}
for i,z,hh,c in hr:
 cl,k=old(z);end=k+(tau-1-i)//104;rays[cl].append(end);past[cl]=max(past.get(cl,end),end)
last={cl for cl in bulkclasses if -2<=cl[0]<=8};other=bulkclasses-last;assert len(last)==12 and len(other)==48
ref=lambda z:((int(z.real-z.imag),int(z.real)%2)in other)^bool(sum(old(z)[1]<=th for th in rays[old(z)[0]])%2)
inpast=lambda z:old(z)[0]in past and old(z)[1]<=past[old(z)[0]]
# Compare the reference with ALL future-required cells of bridge then wave.
pre_first={};preflip=set()
for i,z,hh,c in fr:
 if z not in pre_first:pre_first[z]=c=='L'
 assert pre_first[z]^(z in preflip)==(c=='L');preflip.symmetric_difference_update({z})
requirements=dict(pre_first);checks=0
for(t,a),ls in Gw.items():
 rep=complex(a,a-t);cl,krep=old(rep);lo=min(k for k,i,c in ls);breaks={lo}|{k for k,i,c in ls if k>=lo}
 for th in rays[cl]:
  change=-((th-krep)//7)
  if change>=lo:breaks.add(change)
 for z in preflip|F:
  if(int(z.real-z.imag),int(z.real)%14)==(t,a)and int(z.real)//14>=lo:breaks.add(int(z.real)//14);breaks.add(int(z.real)//14+1)
 hi=max(breaks)
 for n in range(lo,hi+2):
  z=rep+n*(14+14j);desired=(next(c for kk,i,c in ls if kk<=n)=='L')^(z in preflip)
  if z in requirements:assert requirements[z]==desired
  requirements[z]=desired;checks+=1
 assert all(kk<=hi for kk,i,c in ls)
 z=rep+(hi+2)*(14+14j);assert ref(z)==(ls[0][2]=='L') # identical constant tails beyond every breakpoint
mismatch={z for z,b in requirements.items()if ref(z)!=b};erasures={z for z in mismatch if ref(z)};pastoverlap={z for z in mismatch if inpast(z)}
# Existence of this full inverse ancestry independently implies no mismatch on strict past.
assert not pastoverlap
# Verify chosen full field and reference+required toggles agree on every tested required cell.
assert all((bulk(z)^(z in F))==b for z,b in requirements.items())
cap_author=json.loads((U/'prepared1564_fresh_launch_cap.json').read_text())
assert sorted(map(list,map(xy,mismatch)))==cap_author['fresh_cap']
assert sorted(map(list,other))==cap_author['other_full_black_profiles']
assert all(-2<=int(z.real-z.imag)<=8 for z in mismatch)
assert all(not ref(z) and not inpast(z) for z in mismatch)
# Actual pruned causal field, not the fully settled five-band comparison field.
flips=set();pp=entry;hh=eh
for c in forward+W['word']*2:
 assert ref(pp)^(pp in mismatch)^(pp in flips)==(c=='L')
 flips.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=D[hh]
counts={'extra_wave_edits':len(edits),'extra_wave_additions':sum(not bulk(z)for z in edits),'extra_wave_erasures':sum(bulk(z)for z in edits),'forward_bulk_cap_size':len(F),'forward_bulk_cap_additions':sum(not bulk(z)for z in F),'forward_bulk_cap_erasures':sum(bulk(z)for z in F),'actual_writer_required_toggles':len(mismatch),'actual_writer_required_additions':len(mismatch-erasures),'actual_writer_required_erasures':len(erasures),'actual_writer_strict_past_overlap':len(pastoverlap)}
out={'status':'PASS independent prepared standard ancestry, complete wave-future ownership and actual writer-boundary cap','source_sha256':hashlib.sha256((U/'LLR_inverse_completion_certificate.json').read_bytes()).hexdigest(),'inverse_prefix':inv,'forward_prefix':forward,'inverse_tail_pose':[[4,1],0],'forward_entry_pose':[[4,0],2],'canonical_H_phase':phase,'canonical_H_copy':copy,'canonical_H_time':tau,'inverse_orbits':len(Gi),'inverse_critical_checks':icheck,'wave_orbits':len(Gw),'wave_critical_checks':wcheck,'all_future_reference_checks':checks,'counts':counts,'actual_writer_required_toggles':sorted(map(xy,mismatch)),'actual_writer_erasures':sorted(map(xy,erasures)),'actual_writer_past_overlap':sorted(map(xy,pastoverlap)),'scope':'Four other FULL infinite prepared standard bands plus a causal final SW standard writer and the explicit necessary finite cap. No connected seven-flight finite producer is asserted. The future wave still needs197N+1 current black supply.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
