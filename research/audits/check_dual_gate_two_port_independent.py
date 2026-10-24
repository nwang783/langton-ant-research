from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];U=R/'causal_reduction/unit_scale';S=R/'spatial_cursor_2026-10-23';m=json.loads((U/'prepared4352_capture_manifest.json').read_text());D=(1j,1,-1j,-1);rot=lambda z,h:z*((-1j)**h);xy=lambda z:(int(z.real),int(z.imag))
def trace(word,p,h):
 rows=[]
 for c in word:
  rows.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h
# Check both coupled vertices and midpoint identities at every heading/turn.
for h in range(4):
 for c in 'RL':
  p=2-3j;z=p+rot(-.5-.5j,h);w=p+rot(.5-.5j,h);g=(h+(1 if c=='R'else-1))%4;q=p+D[g];zz=q+rot(-.5-.5j,g);ww=q+rot(.5-.5j,g)
  assert w-z==rot(1,h) and z+(z+rot(1+1j,h))==2*p and w+(w+rot(-1+1j,h))==2*p
  if c=='R':assert zz-z==rot(1+1j,h)and ww==w
  else:assert ww-w==rot(-1+1j,h)and zz==z
st={s['kind']:s for s in m['stages']};W=st['wave']['word'];T=st['source-transition']['word'];P=st['return-wave']['word'];Z=st['launch-end-response']['word'][:17395];H=m['stages'][0]['word'];small={-1+2j,-1+3j}
wr,we,wh=trace(W,-2+3j,3);tr,te,th=trace(T,102+107j,3);pr,pe,ph=trace(P,117+111j,0);zr,ze,zh=trace(Z,117+111j,0)
u=lambda z:int(z.real+z.imag)
assert(we,wh)==(24+29j,3)and(te,th)==(117+111j,0)and(pe,ph)==(39+33j,0)
assert min(u(q)for q,h,c in wr)==1 and min(u(q)for q,h,c in tr)==182 and min(u(q)for q,h,c in pr)==26
assert min(u(q)for q,h,c in zr[:-1])>=1 and zr[-1]==(10-10j,2,'R')and(ze,zh)==(9-10j,3)
assert all(q not in small for q,h,c in wr+zr)
# Exact all-M support minima: W shifts+52 per copy, T+156M,
# P starts+156M and shifts-156 each copy, so min P^M=182.
assert 26+156==182
# Independent integer-bit adjacent bad-ten counter, ignoring initial windows.
def code(w):
 x=0
 for c in w:x=2*x+(c=='R')
 return x
F={code((H*2)[i:i+10])for i in range(104)};assert len(F)==84
def cost(word,prefix=''):
 bits=code(prefix[-10:]);n=min(len(prefix),10);k=0
 for c in word:
  v=2*bits+(c=='R');n+=1
  if n>=11:k+=(v>>1 not in F and v&1023 not in F)
  bits=v&1023
 return k
costs=[cost(W,'RLL'),cost(W,W),cost(T,W),cost(P,T),cost(P,P),cost(Z,P)]
assert costs==[1973,1972,75515,7358,7353,8418]
assert costs[0]+3*costs[1]+costs[2]+costs[3]-costs[4]+costs[5]==91827 and 3*costs[1]+costs[4]==13269
controls=[]
for k in(1,2):
 body=W*(3*k+4)+T+P*k+Z;rr,p,h=trace(body,-2+3j,3);first={};bits={}
 for q,h,c in rr:
  if q not in first:first[q]=c=='L';bits[q]=c=='L'
  assert bits[q]==(c=='L');bits[q]=not bits[q]
 A={q for q,v in first.items()if v};assert not(A&small)and all(u(q)>0 for q in A)
 initial=A|small;board=set(initial);full='RLL'+body;p=-2+2j;h=0;cuts=[]
 for t,c in enumerate(full):
  assert(p in board)==(c=='L')
  if u(p)<=0:assert u(p)==0;cuts.append((t,xy(p),h,c))
  if 0<t<len(full)-1:assert u(2*(p+rot(-.5-.5j,h)))>=2
  board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 assert cuts==[(0,(-2,2),0,'R'),(len(full)-1,(10,-10),2,'R')]
 assert {q for q in board if u(q)<=0}=={-2+2j,10-10j}and(p,h)==(9-10j,3)
 assert len(full)==192957+28380*k and cost(full)==91827+13269*k
 controls.append(dict(M=k,mass=len(initial),duration=len(full),internal_K=cost(full),cut_events=cuts))
assert [x['mass']for x in controls]==[5925,7266]
out=dict(status='PASS independent dual-cursor coupling, exact all-M two-port support/count deduction and fresh finite-board controls',bindings={f:hashlib.sha256((S/f).read_bytes()).hexdigest()for f in('coupled_dual_cursors_and_gate_memory.md','fixed_exterior_two_port_excursion.md')},source_manifest_sha256=hashlib.sha256((U/'prepared4352_capture_manifest.json').read_bytes()).hexdigest(),local_cases=8,K_costs=costs,controls=controls,scope='Global occupied-fence shielding only until its first actual L gate; mixed fences require genuine Jordan curve, permanent current edges and28 buffer. Two-port family has growing initial mass; exact timing/cost obstruction only, not untimed qualitative or finite-seed noncapture.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(controls)
