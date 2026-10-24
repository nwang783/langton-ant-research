"""Exact bit-permutation wrapper for a guarded XOR/reset graph.
CLI MODEL.json PREFIX [interleave|reverse|identity].
Old bit i becomes new bit old_to_new[i]. Underlying literal model is immutable.
"""
from pathlib import Path
import sys,json,hashlib
inp=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]);mode=sys.argv[3]if len(sys.argv)>3 else'interleave';J=json.loads(inp.read_text());n=J['n'];order=[]
if mode=='interleave':
 labels=J.get('producer_label_classes',J.get('producer_labels',J.get('origin_labels',[])));cells={tuple(L['cell']):L for L in labels}
 for i,q in enumerate(J['points']):
  order.append(i)
  if tuple(q)in cells:
   L=cells[tuple(q)];order.extend(range(L['offset'],L['offset']+L['bits']))
   if 'clean_offset'in L:order.append(L['clean_offset'])
 order+= [i for i in range(n)if i not in order]
elif mode=='reverse':order=list(reversed(range(n)))
elif mode=='identity':order=list(range(n))
elif mode.startswith('file:'):order=json.loads(Path(mode.split(':',1)[1]).read_text())
else:raise ValueError(mode)
assert sorted(order)==list(range(n));perm=[order.index(i)for i in range(n)]
def bits(v):return sum(1<<perm[i]for i in range(n)if v>>i&1)
sid,k,v=J['start'];start=[sid,bits(k),bits(v)];T=[]
for fr,to,k,v,f,c,r,g,a in J['transitions']:T.append([fr,to,*map(bits,(k,v,f,c,r)),g,a])
new={'format':'exact_bit_permutation_guarded_reset_v1','unpermuted_model_file':str(inp),'unpermuted_model_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'mode':mode,'old_to_new':perm,'n':n,'poses':J.get('poses',[]),'points':J.get('points',[]),'out':J['out'],'start':start,'reentry':J['reentry'],'transitions':T}
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {J['out']+1} {len(T)} {len(J['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for r in T:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
# Directly verify inversion for EVERY field, not merely sampled states.
def inv(v):return sum(1<<i for i in range(n)if v>>perm[i]&1)
assert [start[0],inv(start[1]),inv(start[2])]==J['start']
for a,b in zip(T,J['transitions']):assert [*a[:2],*map(inv,a[2:7]),*a[7:]]==b
print(json.dumps({'status':'EXACT_BIT_BIJECTION','variables':n,'transitions':len(T),'old_to_new':perm}))
