"""Exact endpoint-driven Q renewal branch with EMPTY prebreaker N stage.
No generic ant prefix search or all-branch exclusion. All83 whole words fail.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py');lit=importlib.util.module_from_spec(s);s.loader.exec_module(lit)
G=json.load(open(R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'))['geometry'];W={g['name']:g['word']for g in G};W.update({a:q['word']for a,q in zip('DCVUFQB',json.load(open(R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'))['macro_words'])})
def perms(d,v,u):return sorted(set(permutations('D'*d+'V'*v+'U'*u)))
def close(a):return list(a[:-1])+[a[-1]+'C']
def pose(word):
 p=(0,0);h=0
 for c in word:
  h=(h+(1 if c=='R'else-1))%4;z=lit.DIRS[h];p=(p[0]+z[0],p[1]+z[1])
 return(*p,h)
rows=[];solutions=[]
for dS in range(8):
 for vS in range(3):
  for uS in range(2):
   if dS+3*vS+4*uS>7:continue
   m=7-dS-3*vS-4*uS
   for vE in range(m+1):
    dE=m-vE;num=5+dS+vS-dE-3*vE
    if num<0 or num%4:continue
    uE=num//4
    if not(dS+vS+uS)or not(dE+vE+uE):continue
    solutions.append((dS,vS,uS,dE,vE,uE))
    for S in perms(dS,vS,uS):
     if S[0]!='D':continue
     for E in perms(dE,vE,uE):
      T=['UC','D','DC']+close(S)+close(E)+['U','U','U','Q','C']
      pre=''.join(W[a]for a in T[:-5]);assert pose(pre)==(3,-1,0)
      word=''.join(W[a]for a in T)+lit.M;tr=lit.trace(word)
      row=dict(S=S,E=E,tokens=T,result=tr);rows.append(row)
      if tr['feasible']:print('POSITIVE',T,flush=True)
print('solutions',len(solutions),solutions)
print('rows',len(rows),'positive',sum(r['result']['feasible']for r in rows))
print('conflicts',Counter((r['result']['conflict_read'],r['result']['previous_read'],tuple(r['result']['cell']))for r in rows if not r['result']['feasible']))
Path(__file__).with_name('Q_UC_D_empty_N_connector_family.json').write_text(json.dumps(dict(count_solutions=solutions,rows=rows),indent=2))
