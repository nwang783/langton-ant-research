import importlib.util,json
from fractions import Fraction as F
p='/workspace/shared/langton/causal_archive_spatial_lifetime_2026-10-23/check_thin_chord_lifetime.py';s=importlib.util.spec_from_file_location('tc',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
cache={};rows=[]
for a in m.IDS:
 for o in m.G[a]['outputs']:
  for b in m.IDS:
   for x,y,color,*_ in m.G[b]['requirements']:
    i=(x,y)
    for h in range(4):
     head=m.sub(o,m.rot(i,h))
     if(sum(head)+h)%2:continue
     r=m.rot((-1,-1),h);d=(head[0]+(r[0]+1)//2,head[1]+(r[1]+1)//2)
     if d not in cache:cache[d]=len(m.candidate_entries(d))
     M=cache[d];geometric=0 if d==(0,0)else 4*M+11;res=(-h)%4;bound=0 if d==(0,0)else geometric-((geometric-res)%4)
     rows.append(dict(source=a,output=o,target=b,slot=i,before_color=color,heading=h,head=head,d=d,M=M,geometric=geometric,bound=bound))
maxg=max(r['geometric']for r in rows);maxb=max(r['bound']for r in rows)
print('rows',len(rows),'deltas',len(cache),'M',max(cache.values()),'geometric',maxg,'rounded',maxb)
print('maximizers',[r for r in rows if r['bound']==maxb])
c=(F(-1,2),F(-1,2));off=[]
for b in m.IDS:
 for x,y,*_ in m.G[b]['requirements']:
  for h in range(4):
   rr=m.rot((c[0]-x,c[1]-y),h);dd=m.sub(rr,c);off.append((max(map(abs,dd)),b,(x,y),h,dd))
print('maxctxoffset',max(z[0]for z in off));print([str(z)for z in off if z[0]==max(z[0]for z in off)][:10])
json.dump(dict(count=len(rows),distinct_deltas=len(cache),maxM=max(cache.values()),geometric=maxg,rounded=maxb,maximizers=[r for r in rows if r['bound']==maxb],rows=rows,candidates=[dict(delta=d,M=v,sites=m.candidate_entries(d))for d,v in sorted(cache.items())]),open('/workspace/shared/langton/causal_archive_frontier_2026-10-23/probe_context_horizon.json','w'),indent=2)
