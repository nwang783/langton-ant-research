from pathlib import Path
exec((Path(__file__).resolve().parent/'literal_helpers.py').read_text())
for s in(7,8,9):
 R=set(map(tuple,G[s]['outputs']));got={}
 for a in IDS:
  for h in range(4):
   for z in R:
    for inp in G[a]['inputs']:
     p=sub(z,rot(inp,h));ins={place(q,p,h)for q in G[a]['inputs']};ctx={place(q[:2],p,h)for q in G[a]['requirements']};cc=chords(a,p,h)
     if(sum(p)+h)%2 or ctx&(R-ins):continue
     # Source full adjacency exception can occur; preserve it precisely.
     ep=tuple(G[s]['endpoint'][:2]);eh=G[s]['endpoint'][2];src=chords(s);bad=False
     for i,ch in enumerate(src):
      for j,new in enumerate(cc):
       hit=contact(*ch,*new)
       if hit and not(i==len(src)-1 and j==0 and(p,h)==(ep,eh)and hit==[[str(ch[1][0]),str(ch[1][1])]]):bad=True
     if bad:continue
     got[(a,p,h)]=(sorted(ins&R),sorted(ins-R))
 print('SOURCE',s,'CANDIDATES',len(got))
 for (a,p,h),data in sorted(got.items()):print(G[a]['name'],p,h,'old',data[0],'outside',data[1])
