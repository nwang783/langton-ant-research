"""Literal conflicts plus exact all-word language equivalence, not sampled words."""
from pathlib import Path
from collections import deque
import json,sys
from check_dcuv_producer_model_independent import ROOT,digest,resolve_file
from check_packet_window_dfa_independent import trace

def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='literal_packet_forbidden_factor_dfa_v1'
 bp=resolve_file(path,J['base_dfa_file']);pp=resolve_file(path,J['forbidden_factor_file'])
 assert digest(bp)==J['base_dfa_sha256'] and digest(pp)==J['forbidden_factor_sha256']
 # Import inside function to avoid the dispatcher's circular import.
 from check_packet_window_dfa_independent import check as basecheck
 basecheck(bp);B=json.loads(bp.read_text());assert J['keep']==B['keep']
 assert J['geometry_file']==B['geometry_file'] and J['geometry_sha256']==B['geometry_sha256']
 pats=sorted(set(tuple(p)for p in json.loads(pp.read_text())));assert pats
 for p in pats:assert p and all(a in J['keep']for a in p)
 assert J['forbidden_factors']==[{'word':list(p),'conflict':trace(p)}for p in pats]
 assert all(trace(p)is not None for p in pats)
 # Independent prefix machine: all states are proper pattern prefixes.
 pref={():0}
 for p in pats:
  for k in range(1,len(p)):pref.setdefault(p[:k],len(pref))
 states=list(pref);ac=[]
 for p in states:
  row=[]
  for a in J['keep']:
   w=p+(a,)
   if any(len(w)>=len(v)and w[-len(v):]==v for v in pats):row.append(-1);continue
   hits=[v for v in states if not v or(len(w)>=len(v)and w[-len(v):]==v)]
   row.append(pref[max(hits,key=len)])
  ac.append(row)
 # The supplied quotient is compared to this independently formed product
 # by reachable synchronous states. This proves equivalence for EVERY word.
 init=(B['initial_class'],0,J['initial_class']);seen={init};todo=deque([init]);arcs=0
 while todo:
  b,p,a=todo.popleft();assert 0<=a<len(J['transitions'])
  for c in range(len(J['keep'])):
   bb=B['transitions'][b][c];ppp=ac[p][c];aa=J['transitions'][a][c];arcs+=1
   legal=bb>=0 and ppp>=0;assert legal==(aa>=0),(b,p,a,c,bb,ppp,aa)
   if legal:
    z=(bb,ppp,aa)
    if z not in seen:seen.add(z);todo.append(z)
 assert {z[2]for z in seen}==set(range(len(J['transitions'])))
 out={'status':'PASS exact all-word necessary-language equivalence and literal first conflicts','patterns':[list(p)for p in pats],'product_comparison_states':len(seen),'comparison_arcs':arcs,'reported_classes':len(J['transitions']),'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,bp,pp)},'scope':'Base necessary packet language intersected with avoidance of literal-impossible complete-context factors; no infinite-language sufficiency or record exclusion.'}
 dest=ROOT/'audits/packet_window_dfa_replays'/(path.stem+'.independent.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);return out
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
