from pathlib import Path
from collections import Counter,defaultdict
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();files={'prepared_F48_realizes_the_even_one_use_LL_portal.md':'54c369d6','check_prepared_F48_even_one_use_portal.py':'84563e36','check_prepared_F48_even_one_use_portal.json':'bf0c5abc','prepared_F49_external_entry_scope_addendum.md':'068c75e4','check_prepared_F49_portal_external_entry.py':'7256b253','check_prepared_F49_portal_external_entry.json':'a8533d94'}
for f,h in files.items():assert sha(D/f).startswith(h)
H='NESW';V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];targets={0j:'NNSS',1+0j:'EE',1+1j:'SN',1j:'EWWE'};controls=[]
for n,file in[(48,'check_prepared_F48_even_one_use_portal.json'),(49,'check_prepared_F49_portal_external_entry.json')]:
 J=json.loads((D/file).read_text());w=J['word'];B={complex(*p)for p in J['initial_black']};initial=set(B);p=complex(*J['start'][0]);h=H.index(J['start'][1]);hist=defaultdict(list);edges=Counter();reads=[]
 for t,c in enumerate(w):
  e=J['trace'][t];assert sorted(map(xy,B))==e['black_before']and xy(p)==e['cell']and H[h]==e['incoming']
  assert(p in B)==(c=='L');old=p;hist[p].append((t,H[h],c));B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];edges[old,p]+=1
  assert sorted(map(xy,B))==e['black_after']and xy(p)==e['next_cell']and H[h]==e['next_incoming'];reads.append((xy(old),c))
 assert len(w)==n and len(initial)==n-36 and len(B)==16 and p==2j and h==0 and p in B and max(map(len,hist.values()))==4
 assert sorted(map(xy,B))==J['final_black']
 for q,hh in targets.items():
  assert q not in initial and q not in B and ''.join(e[1]for e in hist[q])==hh and ''.join(e[2]for e in hist[q])==('RL'*(len(hh)//2))
  if n==49:
   for t,_,_ in hist[q]:assert t>0 and J['trace'][t-1]['next_cell']==xy(q)
 assert edges[1+2j,1+1j]==1 and edges[1+0j,1-1j]==1 and[edges[e]for e in[(1+1j,1j),(1j,0j),(0j,1+0j)]]==[2,2,2]
 assert reads[n-25:n-20]==[([0,1],'L'),([0,0],'L'),([1,0],'L'),([1,1],'L'),([0,1],'R')]
 controls.append(dict(length=n,seed=sorted(map(xy,initial)),final=sorted(map(xy,B)),factor_cell_count=len(hist),max_reads=4,target_histories={str(xy(q)):hist[q]for q in targets},edges=[(xy(a),xy(b),v)for(a,b),v in edges.items()]))
assert controls[0]['final']==controls[1]['final']and controls[0]['factor_cell_count']==34
O=dict(status='PASS two genuine connected prepared finite even-one-use portal factors',files={f:sha(D/f)for f in files},script=sha(S),controls=controls,scope='F48 supplies all12 target reads; F49 adds actual external BLACK-firstL at(0,-1), supplying every targetR0. Entire boards retained. Complete histories only over the finite factor, not a full translating quotient. EndpointBLACK prevents immediate repeatedF48 R. No globallyWHITE, max-stream boundary, controller, renewal or odd-fuel theorem.')
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(sha(S.with_suffix('.json')))
