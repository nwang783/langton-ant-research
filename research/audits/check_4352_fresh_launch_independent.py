"""Independent full prepared-field ancestry and finite fresh-cap reconstruction, no author code imports."""
from pathlib import Path
from collections import defaultdict
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];B=ROOT/'nonlinear_global_budget_2026-10-23';U=ROOT/'causal_reduction/unit_scale';D=(1j,1,-1j,-1)
J=json.loads((U/'prepared4352_fresh_launch.json').read_text());N=json.loads((B/'three_standard_band_wave_normal_form.json').read_text());W=json.loads((B/'second_prepared_wave_certificate.json').read_text());H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];word=W['word'];xy=lambda p:(int(p.real),int(p.imag));shift=-70-70j
bulkclasses=set(map(tuple,N['full_black_profiles']));bulk=lambda p:(int(p.real-p.imag),int(p.real)%2)in bulkclasses
base={complex(*q)+shift for q in N['finite_XOR_cap']};edits={complex(*q)for q in J['initial_wave_edits']};pose=complex(*N['pose'][0])+shift;heading=N['pose'][1];assert pose==-2+3j and heading==3

def trace(w,p,h):
 rows=[]
 for i,c in enumerate(w):rows.append((i,p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h

def raydata(w,p,h):
 rows,ep,eh=trace(w,p,h);delta=ep-p;assert eh==h and delta.real==delta.imag and delta.real>0;s=int(delta.real);g=defaultdict(list)
 for i,z,hh,c in rows:
  x,y=xy(z);a=x%s;g[x-y,a].append(((x-a)//s,i,c))
 for ls in g.values():ls.sort(key=lambda z:z[1]-len(w)*z[0]);assert all(a[2]!=b[2]for a,b in zip(ls,ls[1:]))
 return s,g

def future(z,s,g):
 x,y=xy(z);a=x%s;ls=g.get((x-y,a));return bool(ls)and(x-a)//s>=min(k for k,i,c in ls)

def certify(w,p,h,F):
 s,g=raydata(w,p,h);checks=0
 for(t,a),ls in g.items():
  lo=min(k for k,i,c in ls);hi=max(k for k,i,c in ls);nums=set(range(lo,hi+1))
  for z in F:
   x,y=xy(z)
   if(x-y,x%s)==(t,a)and(x-a)//s>=lo:nums.add((x-a)//s)
  nums.add(max(nums)+1)
  for n in nums:
   z=complex(a+s*n,a+s*n-t);want=next(c for k,i,c in ls if k<=n)=='L';assert bulk(z)^(z in F)==want;checks+=1
 return s,g,checks
sw,gw=raydata(word,pose,heading);assert sw==26 and len(gw)==1162 and all(not future(z,sw,gw)for z in edits)
F=base^edits;inv=J['inverse_prefix'];rr,p,h=trace(inv,pose-D[heading],(heading+2)%4)
for i,z,hh,c in rr:assert bulk(z)^(z in F)==(c=='L');F.symmetric_difference_update({z})
assert len(inv)==6812 and [list(xy(p)),h]==J['inverse_tail_pose']
si,gi,ic=certify(J['inverse_tail_word'],p,h,F);assert si==2 and len(gi)==22
_,_,wc=certify(word,pose,heading,base^edits)
forward=''.join('L'if c=='R'else'R'for c in inv[::-1]);assert forward==J['forward_prelude_word'];entry=p-D[h];eh=(h+2)%4;assert [list(xy(entry)),eh]==J['forward_entry_pose']
fr,ep,fh=trace(forward,entry,eh);assert(ep,fh)==(pose,heading)
cur=set(F)
for i,z,hh,c in fr:assert bulk(z)^(z in cur)==(c=='L');cur.symmetric_difference_update({z})
assert cur==base^edits
# Derive strict-past causal standard field directly from H, not inverse-tail desired colors.
phase=28;hr0,delta,dh=trace(H,0j,3);origin=entry-hr0[phase][1];hr,_,_=trace(H,origin,3);assert hr[phase][1:3]==(entry,eh)and delta==-2-2j
expected=''.join('L'if H[(phase-1-i)%104]=='R'else'R'for i in range(104));assert expected==J['inverse_tail_word']
def oldkey(z):
 x,y=xy(z);a=x%2;return(x-y,a),(a-x)//2
rays=defaultdict(list)
for i,z,hh,c in hr:
 cl,k=oldkey(z);rays[cl].append(k+(phase-1-i)//104)
past={cl:max(v)for cl,v in rays.items()};other={q for q in bulkclasses if q[0]>=6};last=bulkclasses-other
assert len(last)==12 and len(other)==24 and set(rays)=={(t,a)for t in range(-8,3)for a in(0,1)}
assert sorted(map(list,other))==J['other_full_black_profiles']
ref=lambda z:(oldkey(z)[0]in other)^bool(sum(oldkey(z)[1]<=th for th in rays[oldkey(z)[0]])%2)
inpast=lambda z:oldkey(z)[0]in past and oldkey(z)[1]<=past[oldkey(z)[0]]
requirements={};preflip=set()
for i,z,hh,c in fr:
 want=(c=='L')^(z in preflip)
 if z in requirements:assert requirements[z]==want
 requirements[z]=want;preflip.symmetric_difference_update({z})
checks=0
for(t,a),ls in gw.items():
 rep=complex(a,a-t);cl,krep=oldkey(rep);lo=min(k for k,i,c in ls);breaks={lo}|{k for k,i,c in ls}
 for th in rays[cl]:
  change=-((th-krep)//13)
  if change>=lo:breaks.add(change)
 for z in preflip|F:
  x,y=xy(z)
  if(x-y,x%26)==(t,a)and(x-a)//26>=lo:breaks.update(((x-a)//26,(x-a)//26+1))
 hi=max(breaks)
 for n in range(lo,hi+2):
  z=rep+n*(26+26j);want=(next(c for k,i,c in ls if k<=n)=='L')^(z in preflip)
  if z in requirements:assert requirements[z]==want
  requirements[z]=want;checks+=1
 # Beyond every actual first-read/color/finite-XOR breakpoint, both fields constant.
 z=rep+(hi+2)*(26+26j);assert ref(z)==(ls[0][2]=='L')
assert all((bulk(z)^(z in F))==b for z,b in requirements.items())
cap={z for z,b in requirements.items()if ref(z)!=b};assert len(cap)==289 and not any(ref(z)or inpast(z)for z in cap)
assert sorted(map(list,map(xy,cap)))==J['fresh_cap']
assert all(not(6<=int(z.real-z.imag)<=16 or 22<=int(z.real-z.imag)<=32)for z in cap)
# Fresh finite additions plus the true causal writer, not XOR edits to settled bulk.
p=entry;h=eh;flips=set()
for c in forward+word*2:
 assert ref(p)^(p in cap)^(p in flips)==(c=='L');flips.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
fixed_middle_erasures={z for z in base if bulk(z)and 6<=int(z.real-z.imag)<=16 and future(z,sw,gw)}
assert len(fixed_middle_erasures)==9 and 16+0j in fixed_middle_erasures
assert (16-(-1))==17 and 2*17==34 and 16-2==14
out=dict(status='PASS independent full4352 causal launch, infinite past/future ownership and exactly289 fresh additions',note_sha256=hashlib.sha256((U/'prepared4352_fresh_launch.md').read_bytes()).hexdigest(),data_sha256=hashlib.sha256((U/'prepared4352_fresh_launch.json').read_bytes()).hexdigest(),forward_entry=[xy(entry),eh],wave_pose=[xy(pose),heading],prelude_length=len(forward),inverse_orbits=len(gi),inverse_tests=ic,wave_orbits=len(gw),wave_tests=wc,all_future_reference_tests=checks,required_initial_cells_checked=len(requirements),fresh_cap=sorted(map(xy,cap)),fresh_additions=len(cap),erasures=0,strict_past_overlap=0,other_writer_read_overlap=0,cap_normal_hull=[min(int(z.real-z.imag)for z in cap),max(int(z.real-z.imag)for z in cap)],cap_u_hull=[min(int(z.real+z.imag)for z in cap),max(int(z.real+z.imag)for z in cap)],literal_control_reads=len(forward)+2*len(word),fixed_middle_wave_erasures=sorted(map(xy,fixed_middle_erasures)),scope='Two full infinite settled SW bands, causal third SW writer phase28, and finite fresh289 additions. No connected finite producer, all-N constant-original family, permanent finite-board4352 or capture counterexample.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('fresh_cap','fixed_middle_wave_erasures')})
