import json,pathlib,re
P=pathlib.Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));allout=[]
for entry,exitrow in[(6,5),(4,5)]:
 text=(P/f'fixed_port_{entry}_{exitrow}.log').read_text();seed=list(map(int,re.search(r'FINAL seed(.*)',text).group(1).split()))
 B={(x,y)for x,m in enumerate(seed)for y in range(12)if m>>y&1};x=0;y=entry;h=1;times=0;out=[];states=[set(B)];word=''
 for t in range(200000):
  b=(x,y)in B;word+='L'if b else'R';B.symmetric_difference_update({(x,y)});h=(h+(-1 if b else 1))%4;dx,dy=D[h];x+=dx;y+=dy
  if x<0 or y<0 or y>=12:
   if (x,y,h)!=(-1,exitrow,3):break
   before=states[-1];row=dict(index=len(out),length=len(word),mass=len(B),mass_change=len(B)-len(before),max_black_x=max(x for x,y in B),net_changed=len(B^before),word=word,board=sorted(B))
   out.append(row);states.append(set(B));word='';x=0;y=entry;h=1
 repairs=[]
 for i,A in enumerate(states):
  for j,Bb in enumerate(states[i+1:],i+1):
   delta=A^Bb
   if delta:repairs.append(dict(i=i,j=j,min_x=min(x for x,y in delta),max_x=max(x for x,y in delta),changed=len(delta)))
 r=dict(entry=entry,exit=exitrow,seed=seed,initial_mass=len(states[0]),completed=len(out),stop=(x,y,h),steps=t+1,returns=out,checkpoint_pairs=repairs);allout.append(r)
 print(entry,exitrow,'mass',r['initial_mass'],'returns',[(a['mass_change'],a['max_black_x'])for a in out])
(P/'fixed_port_prefix_controls.json').write_text(json.dumps(allout,indent=2))
