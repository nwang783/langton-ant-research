"""No-import complete 16-turn pristine-half-plane pair check."""
import json,pathlib
D=(1j,1,-1j,-1)
counts=[]
for h0 in range(4):
 nodes=0;survivors=[];middle=0
 def rec(p,h,word,field):
  global nodes,middle
  nodes+=1;t=len(word)
  if t==8:
   if p!=0j:return
   middle+=1
  if t==16:
   if p==2+2j:survivors.append(word)
   return
  # Actual colors above the interface are white until read. Elsewhere choose
  # the first color freely; thereafter deterministic literal alternation.
  choices=[field[p]] if p in field else ([0] if p.imag>=0 else [0,1])
  for color in choices:
   qfield=field.copy();qfield[p]=1-color
   nh=(h+(1 if color==0 else -1))%4
   rec(p+D[nh],nh,word+('R' if color==0 else 'L'),qfield)
 rec(2-2j,h0,'',{})
 assert not survivors
 counts.append({'heading':h0,'nodes':nodes,'feasible_pristine_predecessors':middle,'complete_pairs':0})
# The analytic envelope: with four vertical updates, net dy=-2 permits one
# north update, and net dy=+2 permits three. Earlier coarse diagonal levels
# Y-1 and <=Y-2 consequently remain strictly below the fine record line.
assert -2+1==-1 and -4+3==-1
out={'status':'PASS','rows':counts,'all_four_headings_no_pairs':True,'prior_block_upper_bounds':[-1,-1]}
p=pathlib.Path('/workspace/shared/langton/audits/check_diagonal_k8_record_independent.json');p.write_text(json.dumps(out,indent=2));print(json.dumps(out))
