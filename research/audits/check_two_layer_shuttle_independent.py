from pathlib import Path
import sys,json,hashlib
import sympy as S
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'new_constructive_2026-10-23'
ns={'__file__':str(SELF.parent/'check_two_layer_carried_endpoint_independent.py')};exec((SELF.parent/'check_two_layer_carried_endpoint_independent.py').read_text().split('ff=[frame(s)')[0],ns)
C=ns['C'];r,k,i,j=(ns[x]for x in('r','k','i','j'));compile=ns['compile'];domain=ns['domain'];xor=ns['xor'];empty=ns['empty'];literal=ns['literal']
prior=json.loads((SELF.parent/'check_two_layer_carried_endpoint_independent.json').read_text());initial=C.set(prior['complete_returned_relation'])
E='RLLRRRRLLRRRRLLRLRRRRLRRRRLLLLRLRRRRLRLLLLRRRR';assert len(E)==46
fs,p,h,tm,charge=compile([('LRRL',r),(E,1),('LRRL',r),('RRRRLL',1)],p=(0,2));assert len(fs)==60 and p==(0,2)and h==(1,0)and tm==8*r+52 and charge==12
sets=[domain(f)for f in fs];pairs=nonempty=0
for a,(pos,n,tm,ch)in enumerate(fs):
 C.reset_operations();current=initial.intersect(sets[a])
 if n!=1:assert any(S.sympify(z).coeff(i)!=0 for z in pos)
 for b,(q,m,t,_)in enumerate(fs):
  if a==b:continue
  pairs+=1
  if sets[a].intersect(sets[b]).is_empty():continue
  q=tuple(S.sympify(z).subs(i,j)for z in q);t=S.sympify(t).subs(i,j)
  f='[r,k]->{[x,y]:r>=10 and k>=10 and exists(i,j:0<=i<'+str(n)+' and 0<=j<'+str(m)+' and x='+str(pos[0])+' and y='+str(pos[1])+' and x='+str(q[0])+' and y='+str(q[1])+' and '+str(S.expand(t-tm))+'<0)}'
  prev=C.set(f)
  if not prev.is_empty():current=xor(current,prev);nonempty+=1
 bad=sets[a].subtract(current)if ch=='L'else current;assert bad.is_empty(),(a,str(bad))
change=empty
for ds in sets:change=xor(change,ds)
returned=xor(initial,change)
L={(0,3),(0,4),(-1,4),(-1,2)};R={(-1,1),(0,1),(1,1),(2,1),(3,2),(3,3),(0,3),(1,3),(-1,4),(0,4),(1,4),(2,4),(0,5),(1,5)}
def caps(L,R):return C.set('[r,k]->{[x,y]:r>=10 and k>=10 and ('+' or '.join([f'(x={x} and y={y})'for x,y in L]+[f'(x=2r+{x} and y={y})'for x,y in R])+')}')
assert change.is_equal(caps(L,R));assert initial.intersect(change).is_equal(caps({(-1,2)},{(0,1),(1,1)}));assert returned.intersect(caps({(0,3)},set())).is_equal(caps({(0,3)},set()))
ref=json.loads((D/'two_layer_restored_bulk_shuttle.json').read_text());assert returned.is_equal(C.set(ref['complete_returned_relation']))and change.is_equal(C.set(ref['complete_change_relation']));assert pairs==3540 and nonempty==59
# Independently compose physical endpoint visits in a finite word control.
w='LRRL'*10+E+'LRRL'*10+'RRRRLL';p=2j;hh=1+0j;vis=[]
for tick,ch in enumerate(w):
 vis.append((tick,int(p.real),int(p.imag),int(hh.real),int(hh.imag)));hh*=(-1j if ch=='R'else 1j);p+=hh
assert p==2j and hh==1 and any(v[1:]==(0,4,1,0)for v in vis)
note=D/'two_layer_restored_bulk_shuttle.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='83fdd769762b3b87cc50d651bd7d68628eb965c569b9a81e63e4e14d300a00d7'
out=dict(status='PASS all-r,k complete bulk-restored finite shuttle with18 retained cap changes',note_sha256=sha,domain='integer r,k>=10',families=60,ordered_pairs=pairs,nonempty_prior_relations=nonempty,word='(LRRL)^r E46 (LRRL)^r RRRRLL',fixed_E=E,duration='8r+52',endpoint=[0,2,'E'],net_mass=12,clears=[[-1,2],['2r',1],['2r+1',1]],left_toggles=sorted(L),right_toggles_relative_2r=sorted(R),complete_returned_relation=str(returned),complete_change_relation=str(change),scope='Exact continuation of signed complete two-layer returned field. Restored bulk is not a cap reset: second read of immediate repetition asks R at newly black(0,3). No renewal or family capture.',analytic='Independent existential copy chronology checks every prior same-cell read. Complete output equals input XOR18 exact endcap cells, with3clears15adds; all passive remote cells retained.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],pairs,nonempty)
