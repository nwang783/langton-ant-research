from pathlib import Path
from fractions import Fraction
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'fresh_RAW_U_LEFT_all_length_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json'
assert sha(MF)=='aa6a04d0e64f7cf2c7bd4d7a7e4e3632b2ab3d166d4c3554d4fc47ed3611fd1a'
for key,base in [('files',D),('dependencies',R)]:
 for f,h in json.loads(MF.read_text())[key].items():assert sha(base/f)==h
J=json.loads((D/'fresh_U_LEFT_all_length.json').read_text())
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet')]
I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert sum(map(len,I.values()))==8 and not I['C']
def chord(a,p=0j,h=0):z=tr(W[a],p,h);return center(p,h),center(z['p'],z['h'])
def ownercheck(a,inp,row):
 tick=next(i for i,(q,h,c)in enumerate(tr(W[a]+M)['reads'])if q==inp)
 own=row['physical_first_L_owner'];assert own['context_tick0']==tick and own['turn']=='L'
 if tick>=len(W[a]):assert tick==len(W[a])+1 and own['owner']=='next actual word RAW'
left={0j,1j};right=1+0j;source=tr(W['U']);ek={source['p']+rot(source['h'])*q for q in K};assert (source['p'],source['h'])==(4j,0)
for q,t in [(0j,4),(1j,19),(1+0j,9)]:assert source['last'][q]==('R',t)and q not in ek
old=chord('U');assert old==(-1-1j,-1+7j)
counts=[];tables=[]
for tags,key in [(left,'all64_LEFT_first_loss_roles'),({right},'all32_prior_a_loss_roles')]:
 ref={(tuple(r['tag']),r['atom'],tuple(r['slot']),r['entry'][2]):r for r in J[key]};seen=set();ct=Counter();gates=[]
 for tag in tags:
  for a in'DCVU':
   ctx=tr(W[a]+M)
   for inp in I[a]:
    for h in range(4):
     p=tag-rot(h)*inp;ky=(tuple(xy(tag)),a,tuple(xy(inp)),h);r=ref[ky];seen.add(ky);assert r['entry']==xy(p)+[h];ownercheck(a,inp,r)
     if(int(p.real+p.imag)+h)%2:why='sector'
     elif tags==left:
      if any((q-p)/rot(h)in K or ctx['req'].get((q-p)/rot(h))is False for q in left):why='held_LEFT_CORE_or_WHITE'
      elif meet(*old,*chord(a,p,h))is not None:why='nonadjacent_source_U_contact'
      else:why='sole_N_U_gate';gates.append((a,p,h))
     else:
      if any((q-p)/rot(h)in K for q in left|{right}):why='held_CURRENT_in_ENTRY_CORE'
      elif any((q-p)/rot(h)in ctx['req']for q in left):why='not_complete_context_MISS_LEFT'
      elif meet(*old,*chord(a,p,h))is not None:why='nonadjacent_source_U_contact'
      else:why='right_N_gate';gates.append((a,p,h))
     assert r['classification']==why,(r,why);ct[why]+=1
     if why.endswith('source_U_contact'):assert(p,h)!=(source['p'],source['h'])
 assert seen==set(ref);counts.append(dict(ct));tables.append(gates)
assert Counter(tables[0])=={('U',1-1j,0):2}
assert set(tables[1])=={('D',1-1j,0),('V',1-3j,0),('U',2-2j,0),('U',2-4j,0)}
ctx=tr(W['U']+M,1-1j,0);assert next((i,c)for i,(q,h,c)in enumerate(ctx['reads'])if q==right)==(11,'R')
assert [next((i,c)for i,(q,h,c)in enumerate(ctx['reads'])if q==q0)for q0 in sorted(left,key=lambda q:q.imag)]==[(14,'L'),(13,'L')]
for a,p,h in tables[1]:
 z=tr(W[a],p,h);assert (z['p'],z['h'])in [(2+0j,0),(2+2j,0)]
 q=next((i,c)for i,(q,hh,c)in enumerate(tr(W[a]+M,p,h)['reads'])if q==right);assert q[1]=='L'
# Reconstruct current-edge coverage, including new EXIT CORE captures.
edge=lambda q:(2*q-1-1j,2*q+1+1j)if int(q.real+q.imag)%2==0 else(2*q-1+1j,2*q+1-1j)
bar=[]
for a in'DCVU':
 b,e=chord(a);v=e-b;ctx=tr(W[a]+M);raw=tr(W[a]);ec={raw['p']+rot(raw['h'])*q for q in K};roles={}
 for x in range(math.floor((min(b.real,e.real)-1)/2),math.ceil((max(b.real,e.real)+1)/2)+1):
  for y in range(math.floor((min(b.imag,e.imag)-1)/2),math.ceil((max(b.imag,e.imag)+1)/2)+1):
   q=complex(x,y);u,w=edge(q);hit=meet(u,w,b,e)
   if hit is None:continue
   if hit[0]=='OVERLAP':
    k='real'if v.real else'imag';ts=sorted([Fraction(int(getattr(u-b,k)),int(getattr(v,k))),Fraction(int(getattr(w-b,k)),int(getattr(v,k)))]);inside=max(0,ts[0])<min(1,ts[1])
   else:inside=0<hit[1]<1
   if not inside:continue
   role='entry_CORE'if q in K else'TRUE_residual_input'if q in I[a]else'before_WHITE'if ctx['req'].get(q)is False else'BAD';assert role!='BAD';roles[tuple(xy(q))]=role
 ref=next(z for z in J['RAW_barrier']if z['ordinary_RAW']==a);assert roles=={tuple(z['cell']):z['actual_before_role']for z in ref['all_open_chord_edge_contacts']}
 for c,core in [(b,K),(e,ec)]:
  incident={complex(x,y)for x in range(int(c.real)//2-2,int(c.real)//2+3)for y in range(int(c.imag)//2-2,int(c.imag)//2+3)if c in edge(complex(x,y))};assert len(incident)==4 and incident<=core
 for q in ec-K:assert q in ctx['req']and(q in I[a]if ctx['req'][q]else q not in I[a])
 bar.append([a,len(roles)])
# Actual source/consumer midpoints and exact principal-angle identity.
B=-1+3j;E=1+1j;gate=chord('U',1-1j,0);assert set(edge(1j))=={B,E}and gate==(1-3j,1+5j)
assert center(tr(W['U'][:20])['p'],tr(W['U'][:20])['h'])==B
z=tr(W['U'][:13],1-1j,0);assert center(z['p'],z['h'])==E
assert meet(B,old[1],B,E)==(0,0)and meet(gate[0],E,B,E)==(1,1)
beta=math.atan(1/3);theta=dict(D=math.pi/4,C=math.pi/4,V=math.pi/2-beta,U=math.pi/2)
for a in'DCVU':
 for b in'DCVU':
  z=tr(W[a]);v=chord(a)[1]-chord(a)[0];u=chord(b,z['p'],z['h'])[1]-chord(b,z['p'],z['h'])[0];actual=math.atan2((u/v).imag,(u/v).real);assert abs(actual-(theta[b]-theta[a]+(math.pi/2 if a=='C'else 0)))<1e-12
closing=[math.atan2((b/a).imag,(b/a).real)for a,b in [(gate[1]-gate[0],B-E),(B-E,old[1]-B)]];assert all(abs(x-y)<1e-12 for x,y in zip(closing,[math.pi/4,-math.pi/4]))
for a in'DVU':z=tr(W[a]);assert z['h']==0 and z['p'].real>=0 and z['p'].imag>0
# Fresh full-field replay, retaining SAME physical births at every actual cut.
C=J['positive_regression'];assert C['word']=='UQUCCV'and C['all_physical_reads']==179
raw=''.join(W[a]for a in C['word'])+M;z=tr(raw);assert not z['bad'];seed={q for q,b in z['req'].items()if b};assert sorted(map(xy,seed))==C['complete_seed']and len(seed)==31
board={q:('initial',tuple(xy(q)))for q in seed};p=0j;h=0;t=0;tags={};rec=[]
for k,a in enumerate(C['word']):
 if k==2:tags={p+rot(h)*q:t+source['last'][q][1]for q in left};assert xy(p)+[h]==C['source_entry']and t==C['source_start_tick0']
 for c in W[a]:
  assert (p in board)==(c=='L')
  if c=='L':del board[p]
  else:board[p]=t
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
 if k>=2:
  ec={p+rot(h)*q for q in K};assert all(board.get(q)==birth and q not in ec for q,birth in tags.items());r=C['source_and_later_RAW_cut_states'][k-2];assert r['head']==xy(p)+[h]and r['actual_RAW_cut_tick0']==t;rec.append([k,t,xy(p)+[h]])
for c in M:
 assert(p in board)==(c=='L')
 if c=='L':del board[p]
 else:board[p]=t
 h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
assert t==179
out=dict(status='PASS fresh RAW U SAME LEFT at every simple completed ordinary cut, no later foreign',manifest=sha(MF),script=sha(S),counts=counts,RAW_barrier=bar,regression=rec,analytic_review=[
'All64 LEFT roles and all32 prior-a roles independently rebuilt from literal RAW+actualM. The sole noncontact LEFT gate U1,-1N includes BOTH simultaneous true inputs. No input is mistaken for entry-color contradiction. Every physical deletion or new EXIT CORE absorption is covered; alive CORE is a CURRENT loss rather than physical death.',
'The source w finalR19 has actual fine center B-1,3 after birth, and consumer before ownL13 has center E1,1. Source remainder and consumer prefix meet the SAME w physical edge only at the specified endpoints. Held-w plus the fresh RAW current-edge barrier clears every intervening chord and endpoint, so source-relative prefix simplicity gives a genuine Jordan closure, not a historical wire.',
'All16 ordinary principal joins telescope with no hidden half-turn. Both source and gate tangents are N; open turnKpi/2 and closing joins +pi/4,-pi/4 give K=+/-4. Nonnegative actual C count forces4. There is no foreign after source, but an arbitrary earlier foreign is allowed.',
'Gate firstR11 requires original a1,0 physically dead before ENTRY. Its first earlier CURRENT loss is therefore before the LEFT gate, including marker-only capture. While LEFT held, complete consumer context must MISS both LEFT originals; its true inputs would otherwise be an earlier pair loss. Four remaining N ports have m=0mod4, 0<=m<=4. At0 they lie below sourceEXIT0,4N; at4 every exit has x2,y0or2 and no C remains, so monotone zero-C N increments cannot reach gate1,-1. The a marker-only deletion is a later actual read2, not an invented extra word.',
'Original a, w and left r identities are actual RAW outputs, not full-eight ages or initial prepared bits. UC/UCC tails count as subsequent real Cs. The full31-black179-read UQUCCV regression retains selected post-Q U LEFT at every real cut, with all source and terminal fields present.',
'The conclusion is only CURRENT at simple completed cuts and hence ENTRY of global first-contact. A contact atom may take LEFT as TRUE inputs and destroy them; no through-contact persistence, terminal-contact exclusion, all-tail simplicity, second foreign or capture claim follows.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
