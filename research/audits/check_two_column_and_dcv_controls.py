"""Independent small literal controls; unbounded ladder proof is analytic."""
from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton');vec=[1j,1,-1j,-1];ladder=[]
for d in range(151):
 B={complex(-1,y)for y in range(-2*d,0)};p=0j;h=1
 word='RRLL'*d+'RRRR'+'LLRR'*d+'LR';seen=[]
 for turn in word:
  assert p.real in (-1,0);assert (p in B)==(turn=='L');seen.append(p)
  B.symmetric_difference_update({p});h=(h+(1 if turn=='R'else -1))%4;p+=vec[h]
 assert (p,h)==(1+1j,1) and {q for q in B if q.real==0}=={1j,-(2*d+1)*1j}
 for turn in 'RRRL':
  assert (p in B)==(turn=='L');B.symmetric_difference_update({p});h=(h+(1 if turn=='R'else -1))%4;p+=vec[h]
 assert p==-1+1j;ladder.append(d)
controls=json.loads((R/'word_stabilization/dcv_vtip_reuse_controls.json').read_text());W={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR'};M='LLLLRLRRRRL';reports=[]
for row in controls['controls']:
 word=''.join(W[a]for a in row['macros']);assert word==row['raw_word'];assert M==row['actual_right_marker'];B={complex(x,y)for x,y in row['seed']};p=0j;h=0;seen=[];tip=complex(*row['target_tip'])
 for i,turn in enumerate(word+M):
  assert (p in B)==(turn=='L');
  if i<len(word)and p==tip:seen.append([i,turn])
  B.symmetric_difference_update({p});h=(h+(1 if turn=='R'else -1))%4;p+=vec[h]
  if i+1==len(word):assert [int(p.real),int(p.imag),h]==row['raw_endpoint']
 assert seen==row['target_tip_reads'];assert len(row['seed'])==row['entry_mass_with_marker']
 for a in W:
  colors={};p=0j;h=0
  for turn in word+W[a]+M:
   if p in colors:assert colors[p]==turn
   colors[p]='L'if turn=='R'else'R';h=(h+(1 if turn=='R'else -1))%4;p+=vec[h]
  assert row['one_macro_extensions'][a]
 reports.append({'macros':row['macros'],'entry_mass':len(row['seed']),'tip_reads':seen})
out={'status':'PASS independent literal controls','two_column_depths':ladder,'dcv_reuse_controls':reports,'scope':'Two-column all-depth theorem relies on the separate analytic forced-ladder proof; DCV controls are finite counterexamples to tip freshness only.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],reports)
