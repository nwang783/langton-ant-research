// Exact exhaustive prefix search for p(9n)=3p(n), h(9n)=h(n).
// No board or first-L bound. An explicit cap reports UNKNOWN.
#include <iostream>
#include <vector>
#include <array>
#include <string>
#include <unordered_map>
#include <cstdint>
#include <cassert>
#include <cstdlib>
#include <fstream>
using namespace std;
const vector<string> words={"RRLRRRRLR","RRLLRLLLL","RLRRLRRRR","RLRLLLLRL","RLLLLRLLR","LRRLRRLRL","LLLRLLRLR","LLLLRRLLR","LLLLRLRRL","RRRRLRLLR","RRRRLLRRL","RRRLRRLRL","RLLRLLRLR","LRRRRLRRL","LRLRRRRLR","LRLLRLLLL","LLRRLRRRR","LLRLLLLRL"};
struct Pose{int x,y,h;};
vector<Pose> P;vector<int> turn,choices,best;unordered_map<uint64_t,int> lastc;
uint64_t nodes=0,leaves=0,cap=100000000;int depthcap=1000,maxdepth=0,latest=0;bool stopped=false;
const int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
uint64_t key(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
ofstream prefixes;uint64_t roots=0;
void dfs(int n){
 if(n==9){++roots;for(int j=0;j<9;++j){if(j)prefixes<<",";prefixes<<choices[j];}prefixes<<"\n";return;}
 ++nodes;if(n>maxdepth){maxdepth=n;best=choices;}
 if(nodes%10000000==0)cerr<<"PROGRESS "<<nodes<<" depth "<<maxdepth<<" root "<<(choices.empty()?-1:choices[0])<<"\n";
 if(nodes>=cap||n>=depthcap){stopped=true;return;}
 int lo=0,hi=18;if(n){lo=turn[n]==1?0:9;hi=lo+9;}
 for(int wi=lo;wi<hi;++wi){
  if(!n&&((words[wi][0]=='R')!=(wi<9)))continue;
  array<uint64_t,9> keys;array<int,9> old;int made=0;bool okay=true;Pose p=P[9*n];
  for(int j=0;j<9;++j){
   int c=words[wi][j]=='R'?1:2;uint64_t k=key(p.x,p.y);auto it=lastc.find(k);int prior=it==lastc.end()?0:it->second;
   if(prior==c){okay=false;++leaves;latest=max(latest,9*n+j);break;}
   keys[made]=k;old[made]=prior;++made;lastc[k]=c;turn[9*n+j]=c;p.h=(p.h+(c==1?1:3))%4;p.x+=dx[p.h];p.y+=dy[p.h];P[9*n+j+1]=p;
  }
  if(okay){assert(p.x==3*P[n+1].x&&p.y==3*P[n+1].y&&p.h==P[n+1].h);choices.push_back(wi);dfs(n+1);choices.pop_back();}
  for(int j=made-1;j>=0;--j){if(old[j])lastc[keys[j]]=old[j];else lastc.erase(keys[j]);}
  if(stopped)return;
 }
}
int main(int argc,char**argv){prefixes.open("/workspace/shared/langton/causal_reduction/morphic_candidates/free_nine_coarse81_prefixes.csv");if(argc>1)cap=strtoull(argv[1],nullptr,10);if(argc>2)depthcap=atoi(argv[2]);P.resize(9*(depthcap+2));turn.resize(P.size());P[0]={0,0,0};lastc.reserve(100000);dfs(0);
 cout<<"{\n\"status\":\""<<(stopped?"UNKNOWN_CAP":"EXHAUSTED")<<"\",\n\"nodes\":"<<nodes<<",\n\"roots\":"<<roots<<",\n\"conflicts\":"<<leaves<<",\n\"max_macros\":"<<maxdepth<<",\n\"latest_conflict\":"<<latest<<",\n\"best_choices\":[";
 for(size_t i=0;i<best.size();++i){if(i)cout<<",";cout<<best[i];}cout<<"]\n}\n";
}
