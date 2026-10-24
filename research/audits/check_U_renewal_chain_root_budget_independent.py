from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();C=ROOT/'core_periodicity_new';B=C/'U_renewal_chain_root_budget_frozen_20261023_1907'
m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['path']).read_bytes()).hexdigest()==f['sha256']
deps={'genealogy_role_speed_frozen_20261023_0840/manifest.json':'c15e71ce948a16c32fc1dbc8ddb443eec3be99e89f209904a9bcb7cfb1ac8be5','causal_cycle_renewal_20261023_1841/manifest.json':'27db0bc457534074587a988c16bbf57c994464656df7c9aa06427ab23203d7d4','U_renewal_exact_clock_frozen_20261023_1902/manifest.json':'91f5cb870b1dacd19c793820cef537c1410bca05c8b71294d80a2ccc823b7fd6'}
for p,h in deps.items():assert hashlib.sha256((C/p).read_bytes()).hexdigest()==h
K={q for q,b in walk(mark)[2].items()if b};I={};O={}
for s in (7,8,9):
 e,h,_,f=walk(raws[s]);black={q for q,b in walk(raws[s]+mark)[2].items()if b};I[s]=black-K;O[s]=(black^f)-{e+rotation(q,h)for q in K}
 assert {2+0j,2+1j}<=O[s] and 3j in I[s]
 assert {3-1j+v for v in (-1+4j,2j,3j)}=={2+3j,3+1j,3+2j}
 assert {3-1j+v for v in (-1+1j,-1+2j)}=={2+0j,2+1j}
ids=(0,1,4,5,6,7,8,9);ix={s:k for k,s in enumerate(ids)}
p=C/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';clauses={tuple(map(int,l.split()[:8]))for l in p.read_text().splitlines()}
rows=[];allowed=[]
for s in (7,8,9):
 for t in (7,8,9):
  qs=[(ix[s],ix[t],3,-1,0,*xy(q),4)for q in sorted(O[s]&{2+0j,2+1j},key=lambda v:v.imag)]
  ex=[q in clauses for q in qs];assert ex[0]==ex[1];rows.append(dict(source=s,target=t,queries=qs,excluded=ex))
  if not any(ex):allowed.append((s,t))
assert set(allowed)=={(7,7),(7,8),(8,7),(9,7)}
# Exact integer algebra, not a finite test used as a universal premise:
# 3j <= M+floor((8j+5)/3) iff 9j-3M <= 8j+5 iff j<=3M+5.
checks=0
for M in range(0,64):
 for j in range(1,3*M+12):
  assert(3*j<=M+(8*j+5)//3)==(j<=3*M+5);checks+=1
out=dict(status='PASS independent spatial chain bound and permanent-cycle consequence',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),dependencies=deps,typed_rows=rows,unexcluded_edges=allowed,arithmetic_controls=checks,bound='At a reset finite chain-head entry, M=max root x. No renewal if M<3; otherwise at most3M+5 links. All produced or entry upper d identities were current at preceding chain C=4j-4, so current-root radius applies.',graph_argument='Directed first-break links have in/out degree at most one, increase time, and no infinite path by the spatial bound. Infinite U events therefore imply infinitely many finite chains. Each last cycle is never first-broken and all four exact identities stay current. Distinct permanent cycles have disjoint physical cells by fresh-output semantics.',scope='Finite entry boards inside retained-eight histories only. No bound on independent chain births, initial mass-only bound, general merger, or capture. No lower-parent selected-role inequality is used.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(allowed)
