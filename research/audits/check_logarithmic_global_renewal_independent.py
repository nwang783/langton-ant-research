from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'global_cycle_birth_2026-10-23'
ns={'__file__':str(SELF.with_name('check_cycle_birth_finite_fuel_independent.py'))};exec(Path(ns['__file__']).read_text().split('cells=')[0],ns)
wvertex,component,rank,connected,ends,isbirth,step=(ns[k]for k in('wvertex','component','rank','connected','ends','isbirth','step'))
stats=Counter();runs=[]
def control(B0,p,h,T):
 B=set(B0);m=len(B);wv=wvertex(p,h);lattice=int(wv.real+wv.imag)%4;beta=rank(B,lattice);A=H=E=O=NB=Birth=0;r=0;hadbirth=False;C=component(B,lattice,wv)[1];blockmass=m;epochmass=m;epn=0;word=''
 for tick in range(1,T+1):
  if p not in B:
   hb=isbirth(B,p,lattice);bb=isbirth(B,p);H+=hb;Birth+=bb;hadbirth|=hb;r+=1;assert r<=4
   if r==4:A+=1;assert bb
   p,h,ch=step(B,p,h)
  else:
   q=p;nb=connected(B-{q},lattice,*ends(q,lattice));NB+=nb;exception=(r==4 or hadbirth or nb);p,h,ch=step(B,p,h);assert len(B)-blockmass==r-1
   if exception:
    E+=1;assert len(B)<=3*epochmass+3;epochmass=len(B);epn=0;assert epochmass<=(m+2)*3**E-2
   else:
    O+=1;epn+=1;actual=component(B,lattice,wvertex(p,h))[1];expected=component(C-{q},lattice,wvertex(p,h))[1];assert q in C and actual==expected and len(actual)<=len(C)-1 and epn<=epochmass;stats['exact_ordinary_edge_sets']+=1
   C=component(B,lattice,wvertex(p,h))[1];blockmass=len(B);r=0;hadbirth=False
  word+=ch;assert A==sum(word[i:i+4]=='RRRR'for i in range(max(0,len(word)-3)))
  assert rank(B,lattice)==beta+H-NB and E<=beta+A+2*H and A+2*H<=3*Birth
  assert O<=(m+2)*(3**(E+1)-1)//2-2*(E+1)
  assert tick<=4*O+5*E+4<=2*(m+2)*(3**(E+1)-1)-3*E-4<=6*(m+2)*3**E<=6*(m+2)*3**(beta+A+2*H)
  stats['physical_prefix_checks']+=1
 stats['runs']+=1;stats['exceptional_blocks']+=E;stats['w_births']+=H;stats['both_graph_birth_updates']+=Birth
 runs.append({'m':m,'beta':beta,'T':T,'A':A,'H':H,'B':Birth,'exceptional':E,'ordinary':O})
cells=[-1-1j,-1,0,1,1j,1+1j]
for mask in range(64):
 B={q for i,q in enumerate(cells)if mask>>i&1}
 for h in range(4):control(B,0j,h,64)
control(set(),0j,0,1000)
control({complex(x,y)for x in range(-3,4)for y in range(-3,4)if(x+2*y)%3==0}|{100+100j,101+100j,100+101j,101+101j},0j,0,128)
note=D/'logarithmic_global_renewal.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='55899d2fabd3e720bb9f9046c284c2c2de7edbd85f8e1a53b5a263598d2d82f3'
out={'status':'PASS unrestricted logarithmic global actual-renewal lower bound','note_sha256':sha,'counts':dict(stats),'controls':runs,'analytic':['Any R run is at most4 because four R restore the physical pose but make its read cell black. An interval beginning mid-run causes no exception: its remaining ordinary L edge was already present at the interval block entry.','Ordinary R^r L blocks have r<=3, no w cycle birth, and bridge L deletion. The exact signed component inheritance applies independently of non-RRRR z-cycle births.','Exceptional complete blocks are at most A + H + (beta+H), using GLOBAL w rank for nonbridge L deletions. A/H in a terminal unfinished run only make this upper bound weaker.','Complete masses satisfy M_next<=3M+3 and M_j<=(m+2)3^j-2. Summing n_j<=M_j yields T<=4 sum n+5E+4<=2(m+2)(3^(E+1)-1)-3E-4<=6(m+2)3^E. All abandoned passive components remain charged to M.','Each contained RRRR has a distinct fourth update creating a z unit cycle; each H is a cycle-birth update. Therefore A+2H<=3B, even if one update contributes to both. The logarithmic B bound is only for T>0; negative short-time lower bounds are harmless.'],'bounds':['T <= 6(m+2)3^(beta+A+2H)','A+2H >= log_3(T/(6(m+2)))-beta','B >= (log_3(T/(6(m+2)))-beta)/3 for T>0'],'scope':'Actual finite-support arbitrary-word intervals, not positive-density defects, original-mass total complexity, capture, or a finite state summary.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats)
