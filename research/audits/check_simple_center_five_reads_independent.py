from pathlib import Path
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/simple_center_five_read_frozen_20261023_1621';M=json.loads((B/'manifest.json').read_text())
for x in M['files']:assert hashlib.sha256((B/x['frozen']).read_bytes()).hexdigest()==x['sha256']
J=json.loads((B/'02_simple_center_five_read_control.json').read_text())['control'];word=[7,1,0,9,5];assert J['word']==word
raw=''.join(raws[x]for x in word);seed={q for q,c in walk(raw+mark)[2].items()if c};assert len(seed)==18 and set(map(xy,seed))==set(map(tuple,J['seed']))
field=set(seed);res={q:('entry',xy(q))for q in seed-K};p=0j;h=0;tick=clock=0;arcs=[];hits=[]
for pi,src in enumerate(word):
 core={p+rotation(q,h)for q in K};assert field==core|set(res)and not core&set(res)
 assert all((p+rotation(q,h)in field)==col for q,col in G[src][2].items())
 for q in G[src][3]:res.pop(p+rotation(q,h))
 for q in G[src][4]:
  z=p+rotation(q,h);assert z not in res;res[z]=(pi,xy(q),clock)
 for at,w in [('D'if base[src]==0 else'V'if base[src]==4 else'U',raws[base[src]])]+[('C',C)]*counts[src]:
  a=2*p+rotation(-1-1j,h)
  for c in w:
   assert(p in field)==(c=='L')
   if p==4j:hits.append([tick,c,h])
   field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h];tick+=1
  arcs.append((a,2*p+rotation(-1-1j,h)));clock+=at=='C'
 assert field==set(res)|{p+rotation(q,h)for q in K}and not set(res)&{p+rotation(q,h)for q in K}
assert tick==154 and(p,h)==(-1+5j,0)and clock==4 and 4j not in seed
assert hits==[[24,'R',0],[28,'L',0],[32,'R',0],[40,'L',2],[152,'R',2]]
nonadj=0
for j,(b0,b1)in enumerate(arcs):
 for i,(a0,a1)in enumerate(arcs[:j]):
  if j==i+1:assert a1==b0 and (det(a1-a0,b1-b0)!=0 or (a1-a0).real*(b1-b0).real+(a1-a0).imag*(b1-b0).imag>0)
  else:assert not meet(a0,a1,b0,b1);nonadj+=1
for c in mark:assert(p in field)==(c=='L');field.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
assert len(arcs)==9 and nonadj==28
out=dict(status='PASS independent actual18-cell simple-center five-read control',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),word=word,seed=sorted(map(xy,seed)),raw_turns=154,actual_marker=11,raw_exit=[-1,5,0],atomic_chords=9,nonadjacent_pairs=nonadj,cell=[0,4],read_history=hits,scope='Refutes cap4 from center simplicity only. No renewal, capture, or optimal read-cap claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
