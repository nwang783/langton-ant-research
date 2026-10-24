from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];P=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind={'maximal_flow2_flow3_departure_segments.md':'b955fed15a4e99779763667a44e3bbf32e06b184758f9977d42465f91130c50b','first_R_departure_cycle_local_multiplicities.py':'118bb587fb1bb556f831c0735aa7aae5a826a718372ceb529ad96149cf420650','first_R_departure_cycle_local_multiplicities.json':'a8d67cb9e730bd6f7a84c7d5a5d992c65d5438b9bfc71a3db269fa5bc8c010a7','flow3_source_sink_segment_open_mode.py':'a68ce0f831bd40d364b9a38fe2242660a598564bf7f04914669a94df49e873e6','flow3_source_sink_segment_open_mode.json':'037b9c35cb583f99a385957bb0ea34e5fa03ee8324f9cb0305807cd2806f664d'}
for f,h in bind.items():assert sha(P/f)==h
H='NESW';V=(1j,1,-1j,-1);out=lambda w,r:(w[r]+(1 if r%2==0 else-1))%4
faces={'NW':-.5+.5j,'NE':.5+.5j,'SW':-.5-.5j,'SE':.5-.5j}
def levels(w,anchor):
 rel=[]
 for h,v in enumerate(V):rel.append((v/2-1j*v/2,v/2+1j*v/2,sum(out(w,r)==h for r in range(len(w)))-w.count((h+2)%4)))
 val={faces[anchor]:0}
 for _ in range(4):
  for a,b,k in rel:
   if a in val:val.setdefault(b,val[a]-k)
   if b in val:val.setdefault(a,val[b]+k)
 assert len(val)==4 and all(val[a]-val[b]==k for a,b,k in rel)
 return {k:val[v]for k,v in faces.items()}
def st(w):return ''.join(H[h]for h in w)
def row(w,turn):
 dep=2 if turn=='R'else 0
 ins=[r for r,h in enumerate(w)if h==1];outs=[r for r in range(len(w))if out(w,r)==dep]
 return {'history':st(w),'in':ins,'out':outs,'external_in':[r for r in range(len(w))if r not in ins],'external_out':[r for r in range(len(w))if r not in outs]}
rr=[];ll=[]
for n in range(1,5):
 for w in product((1,3),repeat=n):
  if w[0]==1:rr.append(row(w,'R'))
  elif levels(w,'NE')['SW']==0:ll.append(row(w,'L'))
assert len(rr)==15 and len(ll)==6
assert {r['history'] for r in ll}=={'WWE','WWEW','WEE','WEEW','WWEE','WEEE'}
assert all(len(r['in'])==len(r['out'])for r in ll)
f2={r['history']:r for r in rr+ll if len(r['in'])==len(r['out'])==2}
expected={'EEWW':([0,1],[0,3]),'EWWE':([0,3],[0,1]),'WEE':([1,2],[0,1]),'WEEW':([1,2],[0,1]),'WWEE':([2,3],[0,3])}
assert set(f2)==set(expected)
for w,(a,b)in expected.items():assert f2[w]['in']==a and f2[w]['out']==b
f3={r['history']:r for r in rr+ll if len(r['in'])==len(r['out'])==3}
assert {w:(r['in'],r['out'])for w,r in f3.items()}=={'EEEW':([0,1,2],[0,2,3]),'EWEE':([0,2,3],[0,1,2]),'WEEE':([1,2,3],[0,1,3])}
starts={n:{r['history']:(len(r['in']),len(r['out']))for r in rr if len(r['out'])==n and len(r['in'])!=n}for n in(2,3)}
ends={n:{r['history']:(len(r['in']),len(r['out']))for r in rr if len(r['in'])==n and len(r['out'])!=n}for n in(2,3)}
assert starts[2]=={'EW':(1,2),'EEE':(3,2),'EWW':(1,2),'EEEE':(4,2)}
assert ends[2]=={'EE':(2,1),'EEW':(2,1),'EWE':(2,3),'EWEW':(2,4)}
assert starts[3]=={'EWE':(2,3),'EWWW':(1,3)} and ends[3]=={'EEE':(3,2),'EEWE':(3,1)}
# Exact telescoping coefficients: first-copy departures are R0; middle-copy endpoint ranks are L1.
for r in rr+ll:
 if r['history']in f3:
  assert r['out'][0]==0 and r['in'][0]==(1 if r in ll else 0)
  assert (r['in'][1],r['out'][1])==((1,2)if r['history']=='EEEW'else(2,1))
for r in rr:
 if r['history']in starts[3]:assert r['out'][0]==0 and r['out'][1]==1
 if r['history']in ends[3]:assert r['in'][0]==0 and r['in'][1]==1
# Flow four and exact rank matching after quarter rotation.
f4=[r for r in rr+ll if 4 in(len(r['in']),len(r['out']))]
assert {(r['history'],len(r['in']),len(r['out']))for r in f4}=={('EWEW',2,4),('EEEE',4,2)}
sw=tuple(H.index(c)for c in'EWEW');tw=tuple(H.index(c)for c in'SSSS')
assert [r for r in range(4)if out(sw,r)==2]==[0,1,2,3] and [r for r,h in enumerate(tw)if h==2]==[0,1,2,3]
assert [r for r,h in enumerate(sw)if h==1]==[0,2] and [r for r in range(4)if out(tw,r)==3]==[0,2]
# Source/sink open mode: independent full ordinal network and every zero-use internal port.
o=json.loads((P/'flow3_source_sink_segment_open_mode.json').read_text());hh={tuple(r['cell']):tuple(H.index(c)for c in r['history'])for r in o['named_histories']};tt={tuple(r['cell']):r['clocks']for r in o['named_histories']}
ed=[];oi=[];ii=[]
for p,w in hh.items():
 assert all(b-a>=4 for a,b in zip(tt[p],tt[p][1:]))
 for h,v in enumerate(V):
  q=(p[0]+int(v.real),p[1]+int(v.imag));a=[r for r in range(len(w))if out(w,r)==h]
  if q in hh:
   b=[r for r,x in enumerate(hh[q])if x==h];assert len(a)==len(b)
   for j,(u,z)in enumerate(zip(a,b),1):assert tt[q][z]==tt[p][u]+1;ed.append((p,u,q,z,j))
  else:oi.extend((p,r,q,H[h],j,tt[p][r])for j,r in enumerate(a,1))
  q=(p[0]-int(v.real),p[1]-int(v.imag))
  if q not in hh:ii.extend((q,p,r,H[h],j,tt[p][r])for j,r in enumerate([r for r,x in enumerate(w)if x==h],1))
assert len({t for ts in tt.values()for t in ts})==13
assert sorted(ed)==sorted((tuple(x['source']),x['source_rank'],tuple(x['target']),x['target_rank'],x['ordinal'])for x in o['all_internal_edges'])
assert sorted(oi)==sorted((tuple(x['source']),x['rank'],tuple(x['target']),x['heading'],x['ordinal'],x['departure_time'])for x in o['all_outgoing_open_ports'])
assert sorted(ii)==sorted((tuple(x['source']),tuple(x['target']),x['rank'],x['heading'],x['ordinal'],x['arrival_time'])for x in o['all_incoming_open_ports'])
# Complete opposite-square single-port inventory and chronology, independently of author inventory.
u=[];helper=[]
for n in range(1,5):
 for w in product((0,2),repeat=n):
  if w.count(2)==sum(out(w,r)==3 for r in range(n))==1:u.append(w)
  if w.count(0)==sum(out(w,r)==3 for r in range(n))==1:helper.append(w)
assert set(map(st,u))=={'S','NNNS','NSNN'}
pre=[w for w in u if next(r for r in range(len(w))if out(w,r)==3)<w.index(2)]
assert list(map(st,pre))==['NNNS'] and levels(pre[0],'NW')['SE']==2
helper=[w for w in helper if w.index(0)<next(r for r in range(len(w))if out(w,r)==3)]
assert set(map(st,helper))=={'NSS','NSSS'}
for w in helper:
 assert w.index(0)==0 and next(r for r in range(len(w))if out(w,r)==3)==2
 z=levels(w,'SW');assert z['NW']==z['SE']==1 and z['NE']==2-len(w)
res={'status':'PASS with actual b-cycle/constant-selected-C scope','bindings':bind,'right_rows':rr,'left_rows':ll,'flow2':f2,'flow3':f3,'starts':starts,'ends':ends,'open_events':13,'internal_edges':len(ed),'open_out':len(oi),'open_in':len(ii),'analytic_review':[
'LEFT flatness was independently derived by solving all four physical stream equations, rather than assuming rank2. It yields exactly six histories from every WHITE length1..4 binary heading word. The local alphabet applies to an actual b-cycle, whose selected C height is constant by signed monotonicity, or an explicitly constant-selected-C path. Arbitrary b-tree paths are NOT classified by these six rows.',
'All constant-flow alphabets, change endpoints, complete incoming/outgoing ordinal sets and exterior ports were reconstructed. Every flow3 interior preserves the adjacent C=c and low L=c-3 components by the signed G3 local identity. Without one-use edges the rerouting endpoints EWWW/EEWE cannot occur; the remaining endpoints are actual odd source/sink, and no other three-use port allows hidden continuation. Distinct maximal segments therefore name distinct full paths, not independent new output credits.',
'The first-copy joins yield T0(t)-T0(s)=m minus internal LEFT(T1-T0); the middle-copy endpoint ranks are exactly1 in all four endpoint types, and internal passage rank1->2 or2->1 gives m+sum epsilon Delta. Subtraction yields the displayed exact identity with full physical times/voltages. No repaired passage is asserted to be an uninterrupted cursor path.',
'Flow4 is exactly EWEW followed by the rotated EEEE=SSSS, with all four same-ordinal transfers retained. Only R0/R2 are persistent flow2 strands; L1/L3 are actual extra channels. Essential embedded unit-circle simplicity forbids three identical successive turns, so the two RIGHT block turns have LEFT neighbors. This is not a physical erasure.',
'An all-at-least3 b-cycle is all3 and has all LEFT corners negative. For its LRL triple, let alpha=Bprev.R0. Actual first b edges give A.R0=alpha+1 and B.L1=alpha+2, hence B.R2>=alpha+6. The opposite U.W output is alpha-1 and its S input is B.R2+1. All single-port histories therefore reduce to NNNS, whose diagonally adjacent C is c+2. Local C maximality forbids LRL, irrespective of the middle RIGHT sign. Equal turns plus no three same turns force RRLL, contradicting signed positive RRLL winding against actual b winding-1. Only existence of a one-OR-two-use edge follows.',
'The explicit13-event source/negative-left/sink/helper network has all complete named histories, internal physical ordinal edges, gaps>=4, distinct clocks and open/zero-use ports checked. Its helper N first at alpha+3 and W departure at alpha+a-1 must be separated by two reads, so a>=12. NSS/NSSS force opposite L=c-4/c-5. This remains only a partial event network, not a literal seed factor, complete front, or completion claim.',
'Actual same-cell first-return paths must connect consecutive physical reads, a stronger obligation than open rank-time feasibility. The previously signed fixed-five-corner flow2 obstruction is retained, but other varying flow2 modes and the general one-use question remain open.'
]}
S.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(res['status']);print(sha(S),sha(S.with_suffix('.json')))
