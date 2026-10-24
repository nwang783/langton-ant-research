import json,sys
from pathlib import Path
D=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h]
def check(w):
 last={};seed=set();p=(0,0);h=0;t=0;out=[];trace=[]
 for j,k in enumerate(w):
  r=D[k];fresh=[];reads=[];start=p;hh=h;target=(1,2) if k=='V' else (0,2);dx,dy=rot(target,h);target=(p[0]+dx,p[1]+dy);prior=last.get(target)
  for z in r['trace']:
   dx,dy=rot(z['p'],h);q=p[0]+dx,p[1]+dy;c=z['c'];old=last.get(q)
   assert not old or old[1]!=c,(j,k,t,q,old,c)
   if old is None and c=='L':fresh.append(q);seed.add(q)
   last[q]=(t,c,j,z['i']);trace.append([t,*q,c,j,k,z['i']]);reads.append((q,old));t+=1
  out.append({'index':j,'macro':k,'pose':[*p,h],'new_fuel':fresh,'target':target,'target_previous':prior,'past_fuel':len(seed)})
  dx,dy=rot(r['end_pose'][:2],h);p=p[0]+dx,p[1]+dy;h=(h+r['end_pose'][2])%4
 # Independent literal all-seed simulation verifies exact turn word.
 B=set(seed);p=(0,0);h=0;vectors=((0,1),(1,0),(0,-1),(-1,0));whole=''.join(D[k]['word'] for k in w)
 for t,c in enumerate(whole):
  assert (p in B)==(c=='L'),(t,p,c)
  B.symmetric_difference_update([p]);h=(h+(1 if c=='R' else -1))%4;p=p[0]+vectors[h][0],p[1]+vectors[h][1]
 return {'word':w,'fuel':len(seed),'time':len(whole),'seed':sorted(seed),'blocks':out,'trace':trace}
if __name__=='__main__':
 w=sys.argv[1];r=check(w)
 print('fuel',r['fuel'],'time',r['time'])
 for z in r['blocks']:print(z['macro'],len(z['new_fuel']),'targetprior',z['target_previous'])
 Path(__file__).with_name('verified_'+w+'.json').write_text(json.dumps(r,indent=2))
