#!/usr/bin/env python3
"""Retained ten-read prepared factor refutes input-agnostic unit winding."""
from pathlib import Path
from collections import defaultdict
import json,hashlib
from lifetime_boundary_graph import analyze
from check_extremal_read_coupling import event_word,quotient
R=Path(__file__).resolve().parent;W='RRRRLLLLRL';D=(1,1);C=(-1,-1);I=(-1,0);O=(1,-1)
def add(p,n):return(p[0]+n,p[1]+n)
def run(B,n):
 B=set(B);p=(0,0);h=0;trace=[]
 from check_extremal_read_coupling import D as STEPS
 for t in range(10*n):
  c='L'if p in B else'R';assert c==W[t%10];trace.append({'t':t,'p':p,'hi':h,'turn':c});B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;dx,dy=STEPS[h];p=(p[0]+dx,p[1]+dy)
 return B,p,h,trace

def main():
 f=analyze(W);assert tuple(f['d'])==D and f['input_events']==[5]and f['output_events']==[2]
 assert not f['internal_cycles']and len(f['root_skeleton_cycles'])==1 and f['root_skeleton_cycles'][0]['winding']==3
 E=f['events'];used={tuple(e['p'])for e in E};B,p,h,tr=run({C,I},1);assert B=={add(C,1),O}and p==D and h==0
 # Exact all-N interference proof: every translated future input/output lies
 # on its own distinct full drift class, with just the named read per period.
 HI=[e for e in E if quotient(e['p'],D)[0]==quotient(I,D)[0]];HO=[e for e in E if quotient(e['p'],D)[0]==quotient(O,D)[0]]
 assert [e['t']for e in HI]==[5]and [e['t']for e in HO]==[2]
 assert tuple(HI[0]['p'])==I and tuple(HO[0]['p'])==O
 controls=[]
 for n in [1,2,3,10,31]:
  seed={C}|{add(I,k)for k in range(n)};final,p,h,trace=run(seed,n);expected={add(C,n)}|{add(O,k)for k in range(n)};assert final==expected and p==add((0,0),n)and h==0
  # The next five reads agree, but sixth read at exhausted I+n*d is R, not L.
  pp=p;hh=h;bb=set(final);follow=[]
  from check_extremal_read_coupling import D as STEPS
  for k in range(6):
   c='L'if pp in bb else'R';follow.append({'relative_t':k,'p':pp,'turn':c});assert(c==W[k])==(k<5);bb.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;dx,dy=STEPS[hh];pp=(pp[0]+dx,pp[1]+dy)
  controls.append({'n':n,'full_initial_black':sorted(seed),'full_final_black':sorted(final),'first_deviation_time':10*n+5,'next_reads':follow})
 hist=defaultdict(list)
 for e in E:
  q,k=quotient(e['p'],D);hist[q].append((e['t']-10*k,e['t'],e['c'],e['hi']))
 out={'status':'AUTHOR CHECK PASS; independent audit pending','scope':'Retained prepared factor; one input consumed per period. Not a complete WHITE front or autonomous finite-seed controller.','word':W,'graph':f,'complete_stable_histories':[{'representative':q,'chronological_events':sorted(es)}for q,es in sorted(hist.items())],'literal_two_cell_control':{'full_initial_black':[C,I],'trace':tr,'full_final_black':sorted(B)},'all_n_exact_relation':{'initial':'{(-1,-1)} union {(-1,0)+k*(1,1):0<=k<n}','after_10n':'{(-1,-1)+n*(1,1)} union {(1,-1)+k*(1,1):0<=k<n}','head':'(n,n), N','first_word_deviation':'10n+5, exhausted input is WHITE/R instead of L','induction_reason':'One-period full field relation plus unique input and output full-drift classes. Future input cells and old output cells cannot be read by any other period.'},'finite_controls':controls,'retained_word_source':'../reframe_finite_seed_2026-10-24/minimum_board_word_controls.json','dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['lifetime_boundary_graph.py','check_extremal_read_coupling.py']}}
 (R/'prepared_ten_boundary_winding_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: retained prepared10 has exact boundary winding3; finite fuel relation verified')
if __name__=='__main__':main()
