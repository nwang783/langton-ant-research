from pathlib import Path
import json,itertools,hashlib
P=Path(__file__).resolve().parents[1]/'core_periodicity_new/chronology_dcuv';O=P/'recurrent8_kernels';G=json.loads((P/'literal_residual_geometry.json').read_text())['geometry'];ids=[0,1,4,5,6,7,8,9];words=[G[a]['word']for a in ids];M='LLLLRLRRRRL';dirs=[(0,1),(1,0),(0,-1),(-1,0)]
def trace(w):
 p=(0,0);h=0;first={};last={}
 for t,c in enumerate(w):
  if last.get(p)==c:return None
  first.setdefault(p,(int(c=='L'),t));last[p]=c;h=(h+(1 if c=='R'else-1))%4;d=dirs[h];p=(p[0]+d[0],p[1]+d[1])
 return p,h,first,last
literal=[str(len(ids))]+[w+' '+M for w in words]+['64']+[f'{a} {b}'for a in range(8)for b in range(8)];(O/'literal8.input').write_text('\n'.join(literal)+'\n');lines=['8']
for w in words:
 p,h,_,last=trace(w);_,_,first,_=trace(w+M);lines.append(f'{p[0]} {p[1]} {h} {len(last)}');lines.extend(f'{x} {y} {int(c=="L")}'for (x,y),c in sorted(last.items()));lines.append(str(len(first)));lines.extend(f'{x} {y} {c} {t}'for (x,y),(c,t)in sorted(first.items()))
meta={}
for n in [2,3]:
 tuples=[t for t in itertools.product(range(8),repeat=n)if trace(''.join(words[a]for a in t)+M)is not None];lines.append(str(len(tuples)));lines.extend(' '.join(map(str,t))for t in tuples);meta[str(n)]=len(tuples)
(O/'kernel8.input').write_text('\n'.join(lines)+'\n');(O/'mapping.json').write_text(json.dumps({'new_to_original':ids,'retained_original_ids':ids,'adjacency_counts':meta,'literal_input_sha256':hashlib.sha256((O/'literal8.input').read_bytes()).hexdigest(),'generic_input_sha256':hashlib.sha256((O/'kernel8.input').read_bytes()).hexdigest()},indent=2)+'\n');print(meta)
