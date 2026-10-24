from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
p=SELF.parent/'check_returned_V_source_reduction_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
walk,W,M,xy,raw,ctx,I,outputs,S,K=[ns[x]for x in('walk','W','M','xy','raw','ctx','I','outputs','S','K')]
D=ROOT/'returned_V_source_residual_guards_2026-10-23';ref=json.loads((D/'V_residual_guards.json').read_text());cat=json.loads((ROOT/'seven_word_spatial_return_2026-10-23/first_returned_atom_contact.json').read_text())['old_source_contact_cases']
held={0,1};deleted=1+1j;bud=2+2j
for n in('V','VC','VCC'):
 assert[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==deleted]==[(6,'R'),(10,'L')]
 assert deleted not in outputs[n]and deleted not in{raw[n]['p']+q*(-1j)**raw[n]['h']for q in K}
 assert[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==bud][-1]==(16,'R')
# Reconstruct genuine atomic outputs, retaining C's complete marker context.
ar={n:walk(W[n])for n in'DCVU'};ac={n:walk(W[n]+M)for n in'DCVU'}
ao={n:({q for q,b in ac[n]['req'].items()if b}^ar[n]['odd'])-{ar[n]['p']+q*(-1j)**ar[n]['h']for q in K}for n in'DCVU'}
assert all(q.imag>=0 and q.real+q.imag>=0 for s in ao.values()for q in s)
roles=[];origins=[]
for h in(2,1):
 for n in'DCVU':
  for q in sorted(ao[n],key=xy):
   entry=deleted-q*(-1j)**h;end=entry+ar[n]['p']*(-1j)**h;hits=held&{entry+z*(-1j)**h for z in ac[n]['req']}
   if(int(entry.real+entry.imag)+h)%2:why='sector'
   elif hits:why='held_r_B_context'
   elif h==1 and n=='C':why='C4_too_late'
   else:why='E3';origins.append((n,q,entry,end));assert h==1
   roles.append((h,n,xy(q),xy(entry),xy(end),why))
assert len(roles)==38 and set((n,e,z)for n,q,e,z in origins)=={('V',3j,3+2j),('U',3j,4+3j)}
def counts(delta):
 dx,dy=xy(delta);down=-dy;out=[]
 for v in range(max(0,down+1)):
  d=down-v;rem=dx-d-3*v
  if d>=0 and rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
def exclude(end,target,f):
 assert end!=target
 sol=counts(target-end)
 assert all(u==0 and(v==0 or f=='B')for d,v,u in sol)
 return sol
sixes={167,168,169,211,212,213};tens={173,174,175,214,215,216,217,218,219,220};twos={221,222};rr=[];de=[];be=[];hh=[]
for ix in sorted(sixes|tens|twos):
 r=cat[ix];assert r['source_atom']=='V'and r['source_to_foreign_C_age']==3
 f=r['foreign'];ret=r['returned_atom'];p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2];assert h==1
 comb=walk(W[f]+W[ret]+M);assert comb['feasible'];mask={p+q*(-1j)**h:b for q,b in comb['req'].items()};core={p+q*(-1j)**h for q in K}
 if ix in sixes:
  assert mask[deleted]and deleted not in core
  fore=walk(W[f]+M);assert fore['req'][(deleted-p)*1j]is True
  for n,q,e,end in origins:de.append((ix,n,xy(end),exclude(end,p,f)))
  kind='source_deleted_11'
 elif ix in tens:
  assert mask[bud]is False and bud not in core
  for n in'DVU':
   for q in I[n]:
    entry=bud-q*(-1j);end=entry+raw[n]['p']*(-1j);be.append((ix,n,xy(q),xy(entry),xy(end),exclude(end,p,f)))
  kind='exit_bud'
 else:
  assert mask[1j]is False;H={4j-q for q in S};whites={q for q,b in mask.items()if not b};assert H&whites=={-2+3j,-2+4j,-1+4j,3j}
  for n in('V','VC'):
   assert S<=outputs[n]
   assert[(i,c)for i,(q,h,c)in enumerate(raw[n]['reads'])if q==1j][-1]==(11,'R')
  qlocal=(3j-p)*1j;first=next((i,c)for i,(q,h,c)in enumerate(comb['reads'])if q==qlocal);assert first[0]==(90 if f=='Q'else 100)
  hh.append((ix,sorted(map(xy,H)),first));kind='forced_A_cleanup_fresh_guard'
 rr.append((ix,kind))
assert len(de)==12 and len(be)==80 and len(hh)==2
mins=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())['slots'];assert min(v['certified_minimum_C_age']for v in mins.values())==2
for label,t,q in [('VCDCDUCDUFV',97,-1),('VCCVCDVUQU',198,3+3j)]:
 word=''.join(W[n]for n in label);r=walk(word);assert not r['feasible']and(r['i'],r['q'])==(t,q)
 if t==198:
  good=walk(word[:t]);B={z for z,b in good['req'].items()if b};p=0j;h=0
  for c in word[:t]:assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
  assert p==q and p in B and word[t]=='R'
mp=D/'manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='0135df7ffcc4c40e8bc5ae1b480bf12a4ad79e29c593506d08c3872f72eb6173'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in ref['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
out={'status':'PASS all18 old-V residual first-returned-contact labels; with signed94 closes all112 old-V labels','manifest_sha256':mh,'all38_atomic_deleted_guard_rebirth_roles':roles,'two_possible_E3_origins':[(n,xy(q),xy(e),xy(end))for n,q,e,end in origins],'twelve_deleted_guard_endpoint_obligations':de,'eighty_exit_bud_endpoint_obligations':be,'two_fresh_helper_guards':hh,'disjoint_cases':rr,'analytic':['All three genuine containing source families preserve the base identities and source deletion. The deleted cell is no longer an entry identity or active core cell. N0 y>=3 and W1 H>=3 exclude early origins; both S2 and E3 atomic output roles include actual C tails. Held r/B are current only in the old-eight prefix.','The only two surviving genuine E3 origins cannot reach any of their foreign targets by arbitrary E zero-C runs having an allowed last full V/U packet. There is no missing earlier S run: the origin itself is already at clock3 and all remaining packets must have zero C.','The genuine exit bud cannot retire before clock3. All eight D/V/U input placements at that clock are retained, including upper and marker-only absorption. Positive-C full clearers cannot finish before the foreign. None of eighty endpoint obligations meets actual foreign adjacency; empty continuations are separately ruled out by unequal endpoints.','The final two cases genuinely force old-A cleanup at V/VC(0,4,S), clock2. Its six newly born base identities survive until foreign3 by the correct universal minimum TWO, not the selected-slot minimum three. The pulled-back combined before-mask conflicts with new A_H. No identity is presumed to survive the foreign itself.'],'scope':'Only chronological FIRST new contact of the immediate returned atom cannot have outgoing old V source. D/C-source cases and later contacts remain; no returned simplicity, second-foreign iteration, seven-word termination or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
