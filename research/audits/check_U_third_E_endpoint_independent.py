from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_U_third_E_endpoint_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='0e82a78e6b7e4a9ec9e0e34396e8298024b64d95518de0c2e90744061738b194'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'third_E_endpoints.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,cross,xy,meet=[ns[k]for k in('W','M','K','tr','G','rot','center','cross','xy','meet')]
raw=lambda seq:''.join(W[a]for a in seq)
A=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows']
for target in'DCVU':
 row=next(r for r in A if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='U'and r['contact_atom']==target)
 assert[k for k in row['allowed_C_counts_before_contact_ENTRY']if(2-k)%4==1]==[1]
# Closed exact head box, outgoing old endpoint convention, and active sector.
a=center(0,0);b=center(G['U']['p'],G['U']['h']);geos=[];keep=[]
for target in'DCVU':
 c=center(0,1);d=center(G[target]['p']*rot(1),(G[target]['h']+1)%4)
 corners=[(a+s*(b-a)-c-t*(d-c))/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))+1):
  for y in range(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners))+1):
   if(x+y+1)%2:continue
   p=complex(x,y);hit=meet(a,b,c+2*p,d+2*p)
   if hit is None or not(0<=hit[0]<1 and 0<hit[1]<=1):continue
   f=tr(W[target]+M);cuts=[]
   for q in(0j,1j):
    loc=(q-p)/rot(1)
    if loc in K or f['req'].get(loc)is False:cuts.append(q)
   z=(target,(x,y,1),str(hit[0]),str(hit[1]),bool(cuts));geos.append(z)
   if not cuts:keep.append((target,p))
assert len(geos)==18 and len(keep)==4
assert set(geos)=={(r['third'],tuple(r['third_pose']),r['old_s'],r['third_t'],bool(r['SAME_LEFT_contradictions']))for r in J['all18_exact_E_contact_geometries']}
assert {(a,tuple(xy(p)))for a,p in keep}=={('D',(-1,0)),('V',(-3,0)),('U',(-4,-1)),('U',(-2,-1))}
def perms(d,v,u):
 counts=[d,v,u];out=[]
 def rec(s):
  if not sum(counts):out.append(s);return
  for k,c in enumerate('DVU'):
   if counts[k]:counts[k]-=1;rec(s+c);counts[k]+=1
 rec('');return out
rows={0:[],1:[]};words={0:[],1:[]}
for b3,p3 in keep:
 for b1,b2 in product('DCVU',repeat=2):
  n=1-(b1+b2).count('C')
  if n not in(0,1):continue
  for foreign in'FQB':
   h=(-n)%4;z=tr(raw(foreign+b1+b2),h=h);p=p3-z['p'];assert z['h']==1
   key=(b1,b2,b3,foreign,tuple(xy(p)+[h]));rows[n].append(key);x,y=xy(p)
   candidates=[]
   if n==0:
    # y bounds every count. x then enforces the actual N endpoint.
    for d in range(max(y-4+1,0)):
     for v in range(max((y-4)//3+1,0)):
      rest=y-4-d-3*v
      if d+v!=x or rest<0 or rest%4:continue
      for run in perms(d,v,rest//4):
       if run and run[-1]not in('VU'if foreign in'FQ'else'U'):continue
       candidates.append('U'+run+foreign+b1+b2+b3)
   else:
    assert y<=6
    # At y=6 UC's W run has exactly one D/V, necessarily first; all later U.
    if y==6:
     for first in'DV':
      pfirst=tr(raw('UC'+first))['p'];assert pfirst.imag==6
      diff=int(pfirst.real)-x
      if diff<0 or diff%4:continue
      run=first+'U'*(diff//4)
      if run[-1]not in('VU'if foreign in'FQ'else'U'):continue
      seq='UC'+run+foreign+b1+b2+b3
      assert tr(raw('UC'+run))['p']==p and tr(raw('UC'+run))['h']==h
      candidates.append(seq)
   for seq in candidates:
    t=tr(raw(seq)+M);assert t['bad']is not None
    words[n].append((key,seq,t['bad'][:2],xy(t['bad'][2]),t['bad'][3]))
for n,num,wn in((0,72,13),(1,108,16)):
 assert len(rows[n])==num and len(words[n])==wn
 rr=J['all72_zero_preFOREIGN_C_endpoint_cases'if n==0 else'all108_one_preFOREIGN_C_endpoint_cases']
 assert set(rows[n])=={(r['first'],r['second'],r['third'],r['foreign'],tuple(r['foreign_pose']))for r in rr}
 wr=J['all13_zero_C_endpoint_exhaustive_whole_words_fail'if n==0 else'all16_one_C_endpoint_exhaustive_whole_words_fail']
 assert {(k,s)for k,s,*_ in words[n]}=={((r['first'],r['second'],r['third'],r['foreign'],tuple(r['foreign_pose'])),r['whole_actual_word'])for r in wr}
 for r in wr:
  t=tr(raw(r['whole_actual_word'])+M);bad=t['bad'];assert bad[0]==r['conflict']['conflict_read']and bad[1]==r['conflict']['previous_read']
# Geometry and true completion prerequisites, not a history-length cutoff.
assert tr(raw('U'))['p']==4j and tr(raw('UC'))['p']==5j and tr(raw('UC'))['h']==3
assert tr(raw('CU')+M)['bad']is not None
for base in'DVU':
 assert G[base]['p'].imag in(1,3,4)and(G[base]['p']*rot(3)).imag in(1,1,0)
assert G['C']['p']==1j
out=dict(status='PASS old-U THIRD E-facing global-first-contact slice only',manifest=sha(D/'manifest.json'),geometries=18,LEFT_compatible=4,inverse_endpoint_counts=[72,108],exact_failed_words=[13,16],all_failed_words=words,analytic_scope=[
'Total actual C count K=1 comes from signed arbitrary-tail angular bounds and target E heading; true preforeign count n=0 or1. Complete young foreign STAR-MISS plus stopping at alleged global first-contact ENTRY licenses SAME original LEFT currentness. No postforeign age law.',
'Old source parameter s<1 assigns outgoing vertices correctly; new t>0 excludes preexisting entry contact. All18 nonparallel exact heads and14 LEFT core/first-R contradictions reconstructed.',
'At n0 creator must be plain U, and the arbitrary N run is completely bounded by exact x/y equations. At n1 UCC cannot finish. Plain U requires a later N base before its first C, and a nonempty W run beginning D/V, giving yA>=7 against all inverse yA<=6. Actual creatorUC exits0,5,W and equality forces exactly firstD/V then arbitrary U rail, with its length fixed by x. Actual last-V/U foreign restrictions retained.',
'All13+16 whole words independently reconstructed and fail literal repeated-color constraints within real RAW or supplied actual M. No depth cap, no hypothetical source completion, no extension to other headings, tail indices or third simplicity.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
