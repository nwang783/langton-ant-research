from check_three_positive_passes import *
import sys
sys.path.insert(0,'/workspace/shared/langton/computability')
from periodic_tail_checker import first_mismatch,State
H104=json.load(open('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json'))['word'];phase={H104[i:]+H104[:i]:i for i in range(104)}
z=json.load(open(OUT/'THREE_POSITIVE_PASSES_CHECKED.json'));out=[]
for c in z['cases']:
 q=c['q'];B=set(map(tuple,c['full_final_field']));p,h=tuple(c['final_pose'][0]),c['final_pose'][1];A3={tuple(x)for x,o,b in c['full_final_lifetime_labels']if o=='third_positive_ordinary'};word='';dead=[];tests=0
 for t in range(100000):
  if len(word)>=208 and word[-104:]==word[-208:-104]and word[-104:]in phase:
   i=phase[word[-104:]];w=H104[i:]+H104[:i];tests+=1;bad=first_mismatch(State(frozenset(B),p,h),w)
   if bad is None:
    rec=dict(q=q,capture_after_third=t,pose=[p,h],word=word,period=w,tail_full_black=sorted(B),third_R_consumed=dead,tests=tests);out.append(rec);print({k:rec[k]for k in['q','capture_after_third','pose','third_R_consumed','tests']},flush=True);break
  ch='L'if p in B else'R'
  if ch=='L':
   if p in A3:dead.append([t,p]);A3.remove(p)
   B.remove(p);h=(h-1)%4
  else:B.add(p);h=(h+1)%4
  word+=ch;p=(p[0]+D[h][0],p[1]+D[h][1])
 else:out.append(dict(q=q,status='100000 limit, inconclusive'));print(out[-1])
(OUT/'THREE_PASS_TAIL_DISCOVERY.json').write_text(json.dumps(out,indent=2)+'\n')
