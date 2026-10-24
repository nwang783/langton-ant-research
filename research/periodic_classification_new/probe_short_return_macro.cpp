#include <cstdio>
#include <cstdint>
#include <vector>
#include <algorithm>
struct M{int h0,h1,L;uint32_t guard,black,xr;};
M ms[]={{0,0,4,50688,0,50688},
{0,1,4,101376,100352,101376},
{0,1,4,3168,1024,3168},
{0,0,4,1584,1584,1584},
{0,0,8,59136,8960,42240},
{0,0,8,837120,802816,787968},
{0,1,8,1674240,34816,1575936},
{0,1,8,236544,98304,168960},
{0,1,8,7392,7296,5280},
{0,1,8,3174,1094,3078},
{0,0,8,1587,1568,1539},
{0,0,8,1848,1072,1320},
{1,1,4,3168,0,3168},
{1,0,4,1584,560,1584},
{1,0,4,50688,1024,50688},
{1,1,4,101376,101376,101376},
{1,1,8,7392,6272,5280},
{1,1,8,3174,70,3078},
{1,0,8,1587,544,1539},
{1,0,8,1848,48,1320},
{1,0,8,59136,9984,42240},
{1,0,8,837120,803840,787968},
{1,1,8,1674240,35840,1575936},
{1,1,8,236544,99328,168960}};
int main(){const int B=21,N=(1<<B)*2;std::vector<int> nxt(N,-1),len(N),dist(N,-1),count4(N),stack;std::vector<unsigned char> col(N);int arcs=0,maxD=0,best=-1,cycles=0;
for(int m=0;m<(1<<B);m++)for(int h=0;h<2;h++){int u=m*2+h;for(int z=0;z<(int)(sizeof(ms)/sizeof(M));z++){auto a=ms[z];if(a.h0==h&&((uint32_t)m&a.guard)==a.black){if(nxt[u]>=0){printf("DUPLICATE %d\n",u);return 1;}nxt[u]=((m^a.xr)*2+a.h1);len[u]=a.L;arcs++;}}}
for(int start=0;start<N;start++){if(col[start])continue;int u=start;stack.clear();while(u>=0&&!col[u]){col[u]=1;stack.push_back(u);u=nxt[u];}if(u>=0&&col[u]==1){cycles++;printf("CYCLE %d\n",u);return 2;}for(auto i=stack.rbegin();i!=stack.rend();i++){u=*i;int v=nxt[u];dist[u]=v<0?0:1+dist[v];count4[u]=v<0?0:(len[u]==4)+count4[v];col[u]=2;if(dist[u]>maxD){maxD=dist[u];best=u;}}}
printf("{\"states\":%d,\"edges\":%d,\"cycles\":%d,\"max_short_run\":%d,\"best_state\":%d,\"macro_path\":[",N,arcs,cycles,maxD,best);int u=best;while(nxt[u]>=0){printf("[%d,%d,%d]%s",u,len[u],nxt[u],nxt[nxt[u]]>=0?",":"");u=nxt[u];}printf("]}\n");
// Minimum average cost of any short-run block followed by a >=12 gap.
double val=12;int bu=-1,bk=0,bt=12;for(int u0=0;u0<N;u0++){int t=0,k=0,u=u0;while(nxt[u]>=0){t+=len[u];k++;u=nxt[u];double a=double(t+12)/(k+1);if(a<val){val=a;bu=u0;bk=k;bt=t+12;}}}printf("{\"least_block_ratio\":%.12f,\"numerator\":%d,\"denominator\":%d,\"best_state\":%d}\n",val,bt,bk+1,bu);
}