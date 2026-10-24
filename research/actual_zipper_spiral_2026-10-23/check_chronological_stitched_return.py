"""Exact entire-board two-pass replay, with charged guide and lifetime ownership."""
from return_guide_geometry import *

def path_word(vs,first_r):
 es=[(v[0]-u[0],v[1]-u[1])for u,v in zip(vs,vs[1:])];w='R'*first_r+'L'
 for a,b in zip(es,es[1:]):
  cr=a[0]*b[1]-a[1]*b[0];assert cr in(-1,0,1);w+='R'*(1+cr)+'L'
 return w

def ordered_path(cells,k,start):
 g={}
 for c in cells:
  u,v=endpoints(c,k);g.setdefault(u,[]).append((v,c));g.setdefault(v,[]).append((u,c))
 assert len(g[start])==1 and all(len(n)<=2 for n in g.values())
 out=[start];last=None;u=start;edges=[]
 while True:
  ns=[x for x in g[u]if x[0]!=last]
  if not ns:break
  assert len(ns)==1;v,c=ns[0];edges.append(c);out.append(v);last,u=u,v
 assert set(edges)==cells and len(out)==len(set(out))
 return out

def run(q,witness=False):
 B,p,h,w1,P,C,G,K,U=setup_guide(q);k=wwhich(p,h);M=len(B);initial=set(B);entry=(p,h);labels={c:('input'if c in P else 'stitch'if c in C else 'guide',0,c)for c in B};t=0;maxmass=M;stages=[];R1ids=set();R1cells=set()
 def replay(name,word):
  nonlocal B,p,h,t,maxmass
  before=len(B);r=0;L=R=0;birth=[0,0];erase=[0,0];Ew=0;deaths={};exc=[];stageborn=set();startpose=(p,h)
  for j,c in enumerate(word):
   actual='L'if p in B else'R';assert actual==c,(q,name,j,p,h,c,actual)
   ev=[connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk))for kk in(0,1)];t+=1
   if c=='R':
    R+=1;r+=1;labels[p]=(name,t,p);stageborn.add(labels[p])
    if name=='first_R':R1ids.add(labels[p]);R1cells.add(p)
    for kk in(0,1):birth[kk]+=ev[kk]
   else:
    L+=1;life=labels.pop(p);deaths[life[0]]=deaths.get(life[0],0)+1;ex=r>=3 or ev[k]
    if ex:Ew+=1;exc.append({'time_in_stage':j+1,'r':r,'w_nonbridge':ev[k],'life_class':life[0],'cell':p})
    if name in('first_R','second_R'):assert r<=2 and not ev[k],('not ordinary',q,name,j,r,ev[k])
    if name=='first_R':assert life[0]=='input'
    if name=='second_R':assert life[0]in('first_R','stitch','transport_R')
    for kk in(0,1):erase[kk]+=ev[kk]
    r=0
   p,h=step(B,p,h);maxmass=max(maxmass,len(B))
  assert word[-1]=='L'and r==0
  out={'stage':name,'T':len(word),'L':L,'R':R,'gain':len(B)-before,'mass_before':before,'mass_after':len(B),'births_w_z':birth,'erasures_w_z':erase,'w_exceptional_blocks':Ew,'exceptions':exc,'deaths_by_origin':deaths,'entry_pose':startpose,'exit_pose':(p,h),'word':word,'ranks_after':[rank(B,kk)for kk in(0,1)]}
  stages.append(out);return out
 initialranks=[rank(B,kk)for kk in(0,1)]
 replay('first_R',w1);assert len(R1ids)==len(R1cells);output=R1cells|C;vs=ordered_path(output,k,xy((1,-1)))
 # All guide cells were present from the first cut. No further board is added.
 w2='RL'+path_word(K,0)+'RRRRL';transport=replay('transport_R',w2)
 assert transport['w_exceptional_blocks']==2 and [x['r']for x in transport['exceptions']]==[1,4]
 assert R1ids<=set(labels.values()),('first output not preserved',q)
 assert cursors(p,h)[1]==xy((1,-1)) and (p,h)==((0,3),0)
 second=replay('second_R',path_word([((X+Y-2)//4,(X-Y)//4)for X,Y in vs],2)+'RLL');assert not(R1ids&set(labels.values()))
 assert second['deaths_by_origin']=={'first_R':len(R1ids),'stitch':q-1,'transport_R':2}
 n=12*((q+1)//2)**2
 assert M==4*n-9*q+43 and len(G)==2*n-10*q+43
 assert [x['gain']for x in stages]==[q-2,9-q,q-2]
 assert [x['T']for x in stages]==[4*n+q,4*n-21*q+91,4*n+5*q-2]
 assert not component(B,k,cursors(p,h)[1]),('second epoch not maximal',q)
 origins={}
 for c,life in labels.items():origins.setdefault(life[0],set()).add(c)
 comps=[];left=set(B)
 while left:
  c=next(iter(left));comp=component(B,k,endpoints(c,k)[0]);comps.append({'mass':len(comp),'origin_counts':{cl:len(comp&ss)for cl,ss in origins.items()if comp&ss}});left-=comp
 out={'q':q,'scale':12,'n_coarse':n,'initial_mass':M,'initial_partition':{'input':len(P),'stitch':len(C),'guide':len(G)},'initial_ranks_w_z':initialranks,'stages':stages,'T':t,'max_mass':maxmass,'final_mass':len(B),'final_origin_counts':{cl:len(ss)for cl,ss in origins.items()},'initial_cells_still_black':{'input':len(B&P),'stitch':len(B&C),'guide':len(B&G)},'final_w_components':sorted(comps,key=lambda x:-x['mass']),'first_R_lifetimes_all_preserved_until_second':True,'first_R_lifetimes_all_consumed_in_second':True}
 if witness:out.update({'initial_black_cells':sorted(initial),'initial_pose':entry,'final_black_cells':sorted(B),'final_pose':(p,h),'final_lifetime_labels':[(c,labels[c])for c in sorted(B)]})
 return out

if __name__=='__main__':
 out=[]
 for q in(3,5,7,9,15):
  x=run(q,witness=q in(3,5));out.append(x);print({'q':q,'M':x['initial_mass'],'gains':[s['gain']for s in x['stages']],'wE':[s['w_exceptional_blocks']for s in x['stages']],'events':[(s['births_w_z'],s['erasures_w_z'])for s in x['stages']],'final_origins':x['final_origin_counts'],'final_components':[c['mass']for c in x['final_w_components']]},flush=True)
  if q in(3,5):Path('chronological_stitched_return_witness_q%d.json'%q).write_text(json.dumps(x,indent=2)+'\n')
 Path('chronological_stitched_return_controls.json').write_text(json.dumps([{k:v for k,v in x.items()if k not in('initial_black_cells','initial_pose','final_black_cells','final_pose','final_lifetime_labels')}for x in out],indent=2)+'\n')
