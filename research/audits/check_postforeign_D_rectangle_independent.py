from pathlib import Path
from fractions import Fraction as F
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'postforeign_D_rectangle_shadow_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='14ed9c10bcfb93e156435ee8811f38788f2397fbf5468a515ec53acece388082';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,rot,K,xy,pieces,meet,G=[ns[k]for k in('W','M','tr','rot','K','xy','pieces','meet','G')];raw=lambda ts:''.join(W[a]for a in ts);J=json.loads((D/'rectangle_shadow.json').read_text());reads={a:tr(W[a])['reads']for a in'DCV'}
# Affine complex heads(coeffa,coeffb,constant); every rail power endpoint is derived from actual literal displacement.
add=lambda x,y:tuple(a+b for a,b in zip(x,y));mul=lambda v,z:tuple(a*z for a in v);cn=lambda z:(0j,0j,complex(z));p=cn(0);h=0;heads=[]
for atom,count in [('D',(1,0,1)),('C',(0,0,1)),('D',(0,1,0)),('C',(0,0,1)),('D',(1,0,1)),('C',(0,0,1)),('D',(0,1,0))]:
 heads.append((p,h));g=G[atom];p=add(p,mul(count,rot(h)*g['p']));h=(h+g['h'])%4
assert(p,h)==(cn(-1),1)
expected=[((0j,0j,0j),0),((1+1j,0j,1+1j),0),((1+1j,0j,1+2j),3),((1+1j,-1+1j,1+2j),3),((1+1j,-1+1j,2j),2),((0j,-1+1j,-1+1j),2),((0j,-1+1j,-1),1)]
assert heads==expected
# Exact all-index minimum substitutions, independent of the author's prose bounds.
bounds=[]
for i,(hp,hh)in enumerate(heads):
 atom='C'if i%2 else'D'
 for tick,(q,_,turn)in enumerate(reads[atom]):
  off=q*rot(hh);x,y=int(off.real),int(off.imag)
  if i==0:assert x>=-1 and y>=-1
  elif i==1:assert 1+y>=0
  elif i==2:assert 2+y>=1
  elif i==3:assert 3+y>=2
  elif i==4:assert 3+y>=2
  elif i==5:assert 2+y>=0
  else:assert 1+y>=-1 and 2+y>=0
  bounds.append((i,tick,x,y,turn))
assert len(bounds)==85
for z,(i,t,x,y,ch)in zip(J['all85_exact_stage_read_offsets'],bounds):assert z['tick0']==t and z['rotated_offset']==[x,y]and z['turn']==ch
old=pieces('D')[0];final=(-3+1j,3-1j);assert meet(*old,*final)==(F(1,2),F(1,2))
shadows=[]
for A,birth,q,reader,ph in [('F',47,-2-1j,'D',-2+1j),('Q',57,-1-2j,'V',-1+0j),('B',67,-1-2j,'V',-1+0j)]:
 aa=tr(W[A]);at=aa['p']+rot(aa['h'])*q;ek={aa['p']+rot(aa['h'])*k for k in K};assert aa['last'][at]==('R',birth)and at not in ek
 assert tr(W[A]+M)['last'][at]==('R',birth)
 rr=tr(W[reader],ph,1);vis=[(i,c)for i,(z,h,c)in enumerate(rr['reads'])if z==q];assert vis[0]==(8,'R')
 row=next(r for r in J['all3_genuine_foreign_output_guard_transforms']if r['A']==A);assert row['foreign_output_local']==xy(at)and row['output_in_postforeign_D_frame']==xy(q)and row['source_tick0']==birth
 shadows.append((A,birth,xy(at),xy(q),reader,8))
def owner(ts,t):
 for j,a in enumerate(ts):
  if t<len(W[a]):return dict(atom=a,atom_index0=j,tick0=t,read1=t+1)
  t-=len(W[a])
 return dict(atom='actual following word',tick0=t,read1=t+1)
for key in('all216_finite_rectangle_regressions','all12_VCC_pose_return_regressions'):
 for r in J[key]:
  ts=r['word'];z=tr(raw(ts)+M);t,prev,q,ch=z['bad'];assert r['conflict_owner']==owner(ts,t)and r['previous_owner']==owner(ts,prev)
  if key.startswith('all216'):
   a,b=r['a'],r['b'];body='D'*(a+1)+'C'+'D'*b+'C'+'D'*(a+1)+'C'+'D'*b+'V';assert ts.endswith(body)and tr(raw(body[:-1]))['p']==-1 and tr(raw(body[:-1]))['h']==1
for r in J['two_genuine_U_entry_fourth_V_positive_prefixes']:
 ts=r['word'];z=tr(raw(ts)+M);assert z['bad']is None;seed={q for q,v in z['req'].items()if v};assert sorted(map(xy,seed))==r['complete_seed'];p=0j;h=0;B=set(seed)
 for c in raw(ts)+M:assert(c=='L')==(p in B);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=ns['V'][h]if'V'in ns else[1j,1,-1j,-1][h]
 assert xy(p)+[h]==list(r['actual_next_prefix_exit'])
out=dict(status='PASS all-length named postforeign D-rectangle last-R shadow obstruction only',manifest_sha256=sha(MF),script_sha256=sha(S),affine_RAW_offsets=85,actual_foreign_shadows=shadows,finite_regressions=216,other_prescribed_controls=12,positive_U_entry_prefixes=2,analytic_review=['Actual affine heads follow by literal D and C displacements with full orientations. Index endpoints j=0/a or0/b-1 give all RAW read bounds for every a>=0,b>=1, not an empirical length cutoff. The lastV proper midpoint crossing is fixed independently of parameters.','Q/B actual last-R shadow is below every earlier body read; finalV firstR8 requires itWHITE. F actual lastR shadow is left of allN reads and below every later pre-lastE read; the finalE D firstR8 requires itWHITE. These identities remain physically BLACK because there was no read, including any marker reads already present inside subsequent RAWs.','All216 finite regressions and12 VCC owner cases were independently recomputed; both genuine UQ/UB VCCV complete positive boards remain valid. The proof uses no postforeign maturation or external-current-to-death shortcut.','Only this D-only proper-crossing template is excluded. Mixed V/U rails may restore the shadow, and neither the historical4C theorem nor arbitrary-tail simplicity is inferred.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
