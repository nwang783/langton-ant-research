import json,sys
from pathlib import Path
p=sys.argv[1];allowed=sys.argv[2];q=json.load(open('shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'));words=dict(zip('DCVUFQB',[m['word']for m in q['macro_words']]))
def good(w):
 h=0;p=0j;last={}
 for c in w:
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R' else -1))%4;p+=(1j,1,-1j,-1)[h]
 return True
M=[]
for a in allowed:
 if a=='C':continue
 for k in range(4):
  w=words[a]+words['C']*k
  if good(w+'LLLLRLRRRRL'):M.append({'word':w,'start_marker':w[:11],'end_marker':'LLLLRLRRRRL','name':a+'C'*k})
result={'classes':1,'macro_words':M,'quotient_edges':[(0,i,0)for i in range(len(M))],'scope':'Arbitrary physically feasible maximal C-run packets over '+allowed+' with final M11 context; next packet begins non-C.'}
Path(p+'_port_quotient.json').write_text(json.dumps(result,indent=2));print(p,len(M),[m['name']for m in M])
