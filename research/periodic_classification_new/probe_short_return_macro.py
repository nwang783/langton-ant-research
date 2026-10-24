#!/usr/bin/env python3
"""Author local first-return control. Exhausts 4/8-step physical returns only.
No white-front exclusion is inferred from this finite local computation.
"""
from itertools import product
from pathlib import Path
import json,subprocess
D=[(0,1),(1,0),(0,-1),(-1,0)]
ps=[]
for h0 in (0,2):
 for L in (4,8):
  for cs in product((1,-1),repeat=L):
   p=(0,0);h=h0;last={};tr=[];ok=True
   for t,c in enumerate(cs):
    if p in last and last[p]==c:ok=False;break
    last[p]=c;tr.append((p,c));h=(h+c)%4;v=D[h];p=(p[0]+v[0],p[1]+v[1])
    if p==(0,0) and t<L-1:ok=False;break
   if ok and p==(0,0):ps.append(dict(h0=h0,h1=h,L=L,word=''.join('R' if c==1 else'L' for c in cs),trace=tr))
U=sorted({p for a in ps for p,c in a['trace']});ix={p:i for i,p in enumerate(U)}
for a in ps:
 a['guard']=a['black']=a['xor']=0
 for p,c in a['trace']:
  b=1<<ix[p]
  if not a['guard']&b:a['guard']|=b;a['black']|=b if c==-1 else 0
  a['xor']^=b
print(json.dumps(dict(cells=len(U),macros=len(ps),positions=U,programs=[{k:v for k,v in a.items() if k!='trace'} for a in ps])),flush=True)
root=Path(__file__).parent
(root/'short_return_macros.json').write_text(json.dumps(dict(positions=U,programs=ps),indent=2)+'\n')
entries=',\n'.join('{'+','.join(map(str,[a['h0']//2,a['h1']//2,a['L'],a['guard'],a['black'],a['xor']]))+'}' for a in ps)
cpp=r'''#include <cstdio>
#include <cstdint>
#include <vector>
#include <algorithm>
struct M{int h0,h1,L;uint32_t guard,black,xr;};
M ms[]={ENTRIES};
int main(){const int B=BITS,N=(1<<B)*2;std::vector<int> nxt(N,-1),len(N),dist(N,-1),count4(N),stack;std::vector<unsigned char> col(N);int arcs=0,maxD=0,best=-1,cycles=0;
for(int m=0;m<(1<<B);m++)for(int h=0;h<2;h++){int u=m*2+h;for(int z=0;z<(int)(sizeof(ms)/sizeof(M));z++){auto a=ms[z];if(a.h0==h&&((uint32_t)m&a.guard)==a.black){if(nxt[u]>=0){printf("DUPLICATE %d\n",u);return 1;}nxt[u]=((m^a.xr)*2+a.h1);len[u]=a.L;arcs++;}}}
for(int start=0;start<N;start++){if(col[start])continue;int u=start;stack.clear();while(u>=0&&!col[u]){col[u]=1;stack.push_back(u);u=nxt[u];}if(u>=0&&col[u]==1){cycles++;printf("CYCLE %d\n",u);return 2;}for(auto i=stack.rbegin();i!=stack.rend();i++){u=*i;int v=nxt[u];dist[u]=v<0?0:1+dist[v];count4[u]=v<0?0:(len[u]==4)+count4[v];col[u]=2;if(dist[u]>maxD){maxD=dist[u];best=u;}}}
printf("{\"states\":%d,\"edges\":%d,\"cycles\":%d,\"max_short_run\":%d,\"best_state\":%d,\"macro_path\":[",N,arcs,cycles,maxD,best);int u=best;while(nxt[u]>=0){printf("[%d,%d,%d]%s",u,len[u],nxt[u],nxt[nxt[u]]>=0?",":"");u=nxt[u];}printf("]}\n");
// Minimum average cost of any short-run block followed by a >=12 gap.
double val=12;int bu=-1,bk=0,bt=12;for(int u0=0;u0<N;u0++){int t=0,k=0,u=u0;while(nxt[u]>=0){t+=len[u];k++;u=nxt[u];double a=double(t+12)/(k+1);if(a<val){val=a;bu=u0;bk=k;bt=t+12;}}}printf("{\"least_block_ratio\":%.12f,\"numerator\":%d,\"denominator\":%d,\"best_state\":%d}\n",val,bt,bk+1,bu);
}'''.replace('ENTRIES',entries).replace('BITS',str(len(U)))
(root/'probe_short_return_macro.cpp').write_text(cpp)
subprocess.run(['g++','-O3','-std=c++17',str(root/'probe_short_return_macro.cpp'),'-o','/tmp/langton_short_return_macro'],check=True)
subprocess.run(['/tmp/langton_short_return_macro'],check=True)
