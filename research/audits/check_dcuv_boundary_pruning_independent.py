"""Fresh complex-coordinate complete-context boundary conflicts for DCUV."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];F=ROOT/'core_periodicity_new/chronology_dcuv'
raw={'D':'LLLLRLRRRR','C':'LLLLRLRRRRLRRRR','V':'LLLLRLRRRRLRRLRRRR','U':'LLLLRLRRRRLRLLLLRRRRLRRLRRRR'}
names=['D','DC','DCC','DCCC','V','VC','VCC','U','UC','UCC'];M='LLLLRLRRRRL'
def conflict(word):
 pos=0j;head=1j;colors={};previous={}
 for t,c in enumerate(word):
  wanted=c=='L'
  if pos in colors and colors[pos]!=wanted:return dict(feasible=False,conflict_read=t,previous_read=previous[pos],cell=[int(pos.real),int(pos.imag)])
  colors[pos]=not wanted;previous[pos]=t;head*=1j if c=='L'else -1j;pos+=head
 raise AssertionError('No boundary conflict')
results={key:{name:conflict(''.join(raw[c]for c in left+right)+M)for name,left,right in items}for key,items in [('DCC_successors',[(n,'DCC',n)for n in names]),('DCCC_predecessors',[(n,n,'DCCC')for n in names])]}
assert results==json.loads((F/'dcc_dccc_boundary_queries.json').read_text())
# Without a right context, a standalone final D remains a genuine exception.
w=''.join(raw[c]for c in 'DCCD')
for suffix in ['', 'L']:
 pos=0j;head=1j;last={}
 for c in w+suffix:
  assert last.get(pos)!=c;last[pos]=c;head*=1j if c=='L'else -1j;pos+=head
out=dict(status='PASS all-ten complete-context DCC successor and DCCC predecessor exclusions',records=results,recurrent_keep=[0,1,4,5,6,7,8,9],scope='An infinite context-complete DCUV tail may restart after a possible initial DCCC, with no DCC. A finite standalone terminal D does not supply the full marker.',sha256=hashlib.sha256((F/'dcc_dccc_boundary_queries.json').read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='records'},indent=2))
