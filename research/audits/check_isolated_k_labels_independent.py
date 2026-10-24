"""No-import exact physical 13-word inventory, current-color convention."""
import hashlib,itertools,json
from pathlib import Path
B=Path('/workspace/shared/langton')
p=B/'computability/singleton_first_block_input.json'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='c67ebdaa29c14c814e8aeb7d42273310f116860fe9f8ff1c7279212a9648f142'
w=json.loads(p.read_text())['word']; assert len(w)==104
legal10={(w+w)[i:i+10] for i in range(104)};assert len(legal10)==84
found={}; physical=0
for letters in itertools.product('LR',repeat=13):
 s=''.join(letters); field={};x=y=0;vx,vy=0,1
 for c in s:
  need=int(c=='L'); q=x,y
  if q in field and field[q]!=need:break
  field[q]=1-need
  vx,vy=(vy,-vx) if c=='R' else (-vy,vx)
  x+=vx;y+=vy
 else:
  physical+=1
  if [s[i:i+10] not in legal10 for i in range(4)]==[False,True,True,False]:found.setdefault(s[1:12],[]).append(s)
expected=dict(json.loads((B/'word_stabilization/isolated_pair_labels13.json').read_text())['patterns'])
assert found==expected,(found,expected)
out={'status':'independent exact inventory passed','binary_words':8192,'physically_feasible_words':physical,'labels':len(found),'contexts':sum(map(len,found.values())),'patterns':found,'scope':'Exactly J-pattern 0110; not an exhaustive inventory of dense mixed K clusters.'}
(B/'audits/check_isolated_k_labels_independent.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
