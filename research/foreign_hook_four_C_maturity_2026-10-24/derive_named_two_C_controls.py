from pathlib import Path
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def perms(d,v,u):
 if not d+v+u:yield'';return
 if d:
  for t in perms(d-1,v,u):yield'D'+t
 if v:
  for t in perms(d,v-1,u):yield'V'+t
 if u:
  for t in perms(d,v,u-1):yield'U'+t
rows=[];pos=[];counts=[]
for A,goals in [('Q',[(-3,-1),(-4,-2)]),('B',[(-2,-2),(-3,-3)])]:
 for N,(x0,y0)in[('',(0,0)),('D',(1,1)),('V',(1,3)),('U',(0,4))]:
  for x,y in goals:
   M=x0-1-x
   if M<0:continue
   for dw in range(M+1):
    for vw in range((M-dw)//3+1):
     for uw in range((M-dw-3*vw)//4+1):
      ss=M-dw-3*vw-4*uw
      for vs in range(ss+1):
       ds=ss-vs;z=y0+1+dw+vw-ds-3*vs-y
       if z<0 or z%4:continue
       us=z//4;counts.append((A,N,(x,y),dw,vw,uw,ds,vs,us))
       for X in perms(dw,vw,uw):
        for Y in perms(ds,vs,us):
         tail=N+'C'+X+'C'+Y+'U'
         for P in('','U'):
          T=P+A+tail;tr=l.trace(''.join(W[a]for a in T)+l.M);r=dict(A=A,N=N,target=(x,y,2),W=X,S=Y,pre=P,word=T,trace=tr);rows.append(r)
          if tr['feasible']:pos.append(r);print('POSITIVE',T,'target',x,y,'mass',sum(c=='L'for c,t in tr['first'].values()))
print('counts',len(counts),'words',len(rows),'positive',len(pos));print(Counter((r['A'],r['N'],r['pre'])for r in pos))
(Path(__file__).resolve().parent/'named_two_C_controls.json').write_text(json.dumps(dict(counts=counts,wordcases=rows,positive=pos),indent=2)+'\n')
