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
rows={};counts=[];positive=[]
for A,goals in [('Q',[(-1,-5),(0,-4)]),('B',[(0,-6),(1,-5)])]:
 for wb,wx in [('D',-1),('V',-3)]:
  for nb,nx,ny in [('D',1,1),('V',1,3)]:
   for tx,ty in goals:
    M=1+ny-ty
    for ds in range(M+1):
     for vs in range((M-ds)//3+1):
      for us in range((M-ds-3*vs)//4+1):
       z=M-ds-3*vs-4*us
       for de in range(z+1):
        ve=z-de;num=tx-wx-nx+ds+vs-de-3*ve
        if num<0 or num%4:continue
        ue=num//4;counts.append((A,wb,nb,(tx,ty),ds,vs,us,de,ve,ue))
        for S in perms(ds,vs,us):
         for E in perms(de,ve,ue):
          tail='C'+wb+'C'+S+'C'+E+'C'+nb+'U'
          for pre in('','U'):
           T=pre+A+tail
           if T in rows:continue
           tr=l.trace(''.join(W[a]for a in T)+l.M);r=dict(word=T,FOREIGN=A,Wbase=wb,S=S,E=E,Nbase=nb,target=(tx,ty,0),pre=pre,trace=tr);rows[T]=r
           if tr['feasible']:positive.append(r);print('POSITIVE',T,'mass',sum(c=='L'for c,t in tr['first'].values()))
print('exact count records',len(counts),'whole words',len(rows),'positive',len(positive));print(Counter((r['pre'],r['FOREIGN'])for r in positive))
(Path(__file__).resolve().parent/'named_clock4_controls.json').write_text(json.dumps(dict(counts=counts,words=rows,positive=positive),indent=2)+'\n')
