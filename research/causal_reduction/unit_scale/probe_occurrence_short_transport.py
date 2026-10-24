"""Charge-free occurrence-dependent unit transports with lengths1,5,9.
This tests the minimal one/two-square-return mechanism, not longer words.
"""
import itertools,pathlib,json,hashlib,time
from search_heading_transport import legal_image
import probe_occurrence_transport as searcher

def main():
 st=time.monotonic();dom=[[],[]]
 for k in [1,5,9]:
  for z in itertools.product('RL',repeat=k):
   w=''.join(z)
   if legal_image(w,(1,0,1)):dom[0].append(w)
   if legal_image(w,(-1,0,3)):dom[1].append(w)
 results=[];records=[]
 for root in [0,1]:
  a,b=searcher.search(root,dom);results.append(a);records.extend(dict(root=root,**z) for z in b)
 p=pathlib.Path(__file__);raw=(json.dumps(records,sort_keys=True,separators=(',',':'))+'\n').encode();p.with_suffix('.records.json').write_bytes(raw)
 out=dict(scope='arbitrary occurrence choices of ALL legal unit/final-heading-preserving transports of lengths1,5,9; no charge condition; T(0)=0, at least one nonidentity',domains=dom,prefix_cap=searcher.CAP,node_cap=searcher.NODECAP,results=results,seconds=time.monotonic()-st,records_sha256=hashlib.sha256(raw).hexdigest())
 p.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
