"""Literal complete-field controls for the frozen two-phase affine family."""
from pathlib import Path
import json,hashlib,sys
from check4352_noncrossing_producer import V,H
P=Path(__file__).resolve().parent;J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text())
def run(m):
 v=lambda a:a[0]*m+a[1]
 B={(v(x),v(y))for x,y in J['seed_families']};initial=set(B);p=(v(J['initial_pose']['x_N_constant']),v(J['initial_pose']['y_N_constant']));h=3;t=0;first={};history='LRLRRRRLLL';factors={(H*2)[i:i+10]for i in range(104)};bad=history not in factors;K=0;stages=[]
 for s in J['stages']:
  assert p==(v(s['start_x_N_constant']),v(s['start_y_N_constant']))and h==s['heading']and t==v(s['start_time_N_constant'])
  for _ in range(v(s['count_N_constant'])):
   for c in s['word']:
    assert(p in B)==(c=='L'),(m,t,p,h,c)
    first.setdefault(p,c);history=(history+c)[-10:];nb=history not in factors;K+=bad and nb;bad=nb
    B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);t+=1
  stages.append({'kind':s['kind'],'time':t,'pose':[p,h],'mass':len(B),'K':K})
 assert t==129780*m+455161 and(p,h)==((117,111),0)and len(B)==12660*m+37419 and K==13269*m+86411
 assert {q for q,c in first.items()if c=='L'}==initial
 return {'M':m,'status':'PASS','original_mass':len(initial),'steps':t,'pose':[p,h],'mass':len(B),'K':K,'stages':stages,'full_final_field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()}
if __name__=='__main__':
 out=run(int(sys.argv[1])if len(sys.argv)>1 else 1)
 (P/f"prepared4352_two_phase_M{out['M']}.json").write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
