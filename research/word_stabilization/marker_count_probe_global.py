import sys,random,json
D=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h]
M={}
for z in D['C']['trace'][:12]:M.setdefault(tuple(z['p']),z['c']=='L')
MP=[[(rot(p,h),c)for p,c in M.items()]for h in range(4)]
def markers(B):
 return [(x,y,h)for x,y in B for h in range(4)if(x+y+h)%2==0 and all((((x+dx,y+dy)in B)==c) for(dx,dy),c in MP[h])]
rng=random.Random(72);out={}
for k,d in D.items():
 first={};odd=set()
 for z in d['trace']:first.setdefault(tuple(z['p']),z['c']=='L');odd.symmetric_difference_update([tuple(z['p'])])
 xmin=min(x for x,y in first)-3;xmax=max(x for x,y in first)+3;ymin=min(y for x,y in first)-3;ymax=max(y for x,y in first)+3
 unknown=[(x,y)for x in range(xmin,xmax+1)for y in range(ymin,ymax+1)if(x,y)not in first]
 forced={p for p,c in first.items()if c};maxdiff=-99;wit=None
 for trial in range(10000):
  p=rng.choice([.1,.2,.3,.4,.5,.6,.7,.8,.9]);B=forced|{q for q in unknown if rng.random()<p};a=markers(B);b=markers(B^odd);delta=len(b)-len(a)
  if delta>maxdiff:maxdiff=delta;wit={'seed':sorted(B),'before':a,'after':b};print(k,trial,'maxdelta',delta,flush=True)
  if delta>=2:break
 out[k]={'maxdelta':maxdiff,'witness':wit}
json.dump(out,open('/workspace/shared/langton/word_stabilization/marker_count_probe_global.json','w'),indent=2)
