"""Targeted full-board collector countercontrol; does not assume fragmentation."""
from check_spiral import *
from check_renewal_archive import component

def collector_vertices(q,scale=4):
 runends=[(0,0)];at=(0,0)
 for j in range(1,q+1):
  dx,dy=D[(j-1)%4];at=(at[0]+scale*((j+1)//2)*dx,at[1]+scale*((j+1)//2)*dy);runends.append(at)
 normal=[(d[1],-d[0])for d in [D[j%4]for j in range(q)]]
 corners=[(runends[0][0]+normal[0][0],runends[0][1]+normal[0][1])]
 for j in range(1,q):
  a,b=runends[j];u,v=normal[j-1];x,y=normal[j];corners.append((a+u+x,b+v+y))
 a,b=runends[-1];u,v=normal[-1];corners.append((a+u,b+v))
 out=[corners[0]]
 for dest in corners[1:]:
  while out[-1]!=dest:
   a,b=out[-1];c,d=dest;assert a==c or b==d
   out.append((a+(c>a)-(c<a),b+(d>b)-(d<b)))
 assert len(set(out))==len(out)
 return out

def cells_of(vs):
 v=list(map(xy,vs));return {((u[0]+w[0])//4,(u[1]+w[1])//4)for u,w in zip(v,v[1:])}

def run(q,joined):
 B,p,h,vs,pathcells,word=setup(q,4)
 P=set(B);collector=cells_of(collector_vertices(q));assert P.isdisjoint(collector)
 connector=cells_of([(0,0),(-1,0),(-1,-1),(0,-1)])if joined else set()
 assert connector.isdisjoint(P|collector)
 B|=collector|connector;B0=set(B);M=len(B);n=len(P)
 active0=len(component(B,0,cursors(p,h)[1]));passive0=M-active0
 preB=B|{(0,1)};assert (0,1)not in B;preP,preH=step(preB,(0,1),2);assert(preB,preP,preH)==(B,p,h)
 births=[0,0];erasures=[0,0];events=[];L=R=0;r=0;initialrank=[rank(B,kk)for kk in(0,1)]
 marked={v for cell in B for v in endpoints(cell,0)}|{cursors(p,h)[1]};initialmarked=set(marked)
 def ccount(board,verts):
  g={v:set()for v in verts}
  for e in board:
   u,v=endpoints(e,0);g[u].add(v);g[v].add(u)
  seen=set();cc=0
  for v in verts:
   if v in seen:continue
   cc+=1;seen.add(v);todo=[v]
   for z in todo:
    for w in g[z]:
     if w not in seen:seen.add(w);todo.append(w)
  return cc
 initialcomponents=ccount(B,marked)
 for t,c in enumerate(word):
  assert ('L'if p in B else'R')==c,('read',q,joined,t,p,h,c)
  kind=[]
  for kk in (0,1):
   yes=connected(B-{p}if c=='L'else B,kk,*endpoints(p,kk))
   (erasures if c=='L'else births)[kk]+=yes
   if yes:kind.append(('erasure'if c=='L'else'birth')+str(kk))
  if c=='L':
   assert p==pathcells[L];assert not connected(B-{p},0,*endpoints(p,0))
   active_before=len(component(B,0,cursors(p,h)[1]))
   L+=1
  else:R+=1;r+=1
  before_current_active=len(component(B,0,cursors(p,h)[1]))
  if c=='R':
   marked.update(endpoints(p,0))
   if 'birth0'in kind:
    assert connected(B-{pathcells[L]},0,*endpoints(p,0))
  oldp=p;p,h=step(B,p,h)
  if c=='L':
   active_after=len(component(B,0,cursors(p,h)[1]));assert active_after==n-L
   if kind:events.append({'t':t,'read':c,'cell':oldp,'kind':kind,'block_r':r,'active_before':active_before,'active_after':active_after})
   r=0
  elif kind:events.append({'t':t,'read':c,'cell':oldp,'kind':kind,'old_input_suffix_before_block':n-L,'current_full_active_mass_before_write':before_current_active,'current_full_active_mass_after_write':len(component(B,0,cursors(p,h)[1])),'w_birth_cycle_avoids_departing_bridge':'birth0'in kind})
 assert L==n and len(B)-M==q-2
 comps=[];seen=set()
 for cell in B:
  if cell in seen:continue
  cc=component(B,0,endpoints(cell,0)[0]);seen|=cc;comps.append(len(cc))
 assert len(comps)==1 and comps[0]==len(B)
 newvertices=len(marked-initialmarked);finalcomponents=ccount(B,marked)
 assert finalcomponents-initialcomponents==newvertices+births[0]-(q-2)
 pruned=active0-n;initialdormant=M-active0
 assert len(B)==initialdormant+pruned+n+(q-2)
 return {'q':q,'joined_initial_collector':joined,'n_old_path_edges':n,'collector_edges':len(collector),'connector_edges':len(connector),'initial_mass':M,'initial_active_mass':active0,'initial_passive_mass':passive0,'initial_rank':initialrank,'updates':len(word),'signed_turn':q-1,'mass_gain':q-2,'final_mass':len(B),'final_active_mass':0,'final_dormant_component_masses':sorted(comps,reverse=True),'final_rank':[rank(B,kk)for kk in(0,1)],'births':births,'erasures':erasures,'pruned_old_active_mass':pruned,'new_marked_w_vertices':newvertices,'initial_marked_w_components':initialcomponents,'final_marked_w_components':finalcomponents,'events':events}

if __name__=='__main__':
 out=[run(q,j)for q in(1,2,3,4,8,16,32)for j in(False,True)]
 Path(__file__).with_name('collector_controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps([{k:v for k,v in d.items()if k!='events'}for d in out],indent=2))
