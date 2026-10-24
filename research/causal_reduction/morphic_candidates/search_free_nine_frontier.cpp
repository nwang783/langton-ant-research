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
#include <unordered_set>
#include <algorithm>
using namespace std;
const vector<string> words={"RRLRRRRLR","RRLLRLLLL","RLRRLRRRR","RLRLLLLRL","RLLLLRLLR","LRRLRRLRL","LLLRLLRLR","LLLLRRLLR","LLLLRLRRL","RRRRLRLLR","RRRRLLRRL","RRRLRRLRL","RLLRLLRLR","LRRRRLRRL","LRLRRRRLR","LRLLRLLLL","LLRRLRRRR","LLRLLLLRL"};
struct Pose{int x,y,h;};
vector<Pose> P;vector<int> turn,choices,best;unordered_map<uint64_t,int> lastc;
uint64_t nodes=0,leaves=0,cap=100000000;int depthcap=1000,maxdepth=0,latest=0;bool stopped=false;
const int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
uint64_t key(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}

uint64_t tailnodes=0,hits=0,roots=0,states=0;int horizon=81;bool found=false;
struct Ev{int cell,c;};
vector<array<vector<Ev>,9>> ev;
vector<vector<int>> alive;
vector<unordered_set<string>> cache;
vector<int> color;
bool tail(int n){
 ++tailnodes;
 if(n>maxdepth){maxdepth=n;best=choices;}
 if(n==horizon){found=true;return true;}
 if(tailnodes>=cap){stopped=true;return true;}
 string k;for(int i:alive[n])k.push_back(char(color[i]));
 if(cache[n].count(k)){++hits;return false;}
 for(int o=0;o<9;++o){
  array<pair<int,int>,9> undo;int made=0;bool okay=true;
  for(auto e:ev[n][o]){if(color[e.cell]==e.c){okay=false;++leaves;break;}undo[made++]={e.cell,color[e.cell]};color[e.cell]=e.c;}
  if(okay){choices.push_back((turn[n]==1?0:9)+o);bool yes=tail(n+1);choices.pop_back();if(yes){for(int j=made-1;j>=0;--j)color[undo[j].first]=undo[j].second;return true;}}
  for(int j=made-1;j>=0;--j)color[undo[j].first]=undo[j].second;
 }
 cache[n].insert(move(k));++states;return false;
}
void fixed_coarse(){
 ++roots;
 unordered_map<uint64_t,int> ids;vector<uint64_t> locations;vector<int> last;
 ev.clear();ev.resize(horizon);alive.clear();alive.resize(horizon);cache.clear();cache.resize(horizon);
 for(int n=9;n<horizon;++n)for(int o=0;o<9;++o){Pose p={3*P[n].x,3*P[n].y,P[n].h};int wi=(turn[n]==1?0:9)+o;
  for(char ch:words[wi]){int c=ch=='R'?1:2;uint64_t kk=key(p.x,p.y);int idx;auto it=ids.find(kk);if(it==ids.end()){idx=ids.size();ids[kk]=idx;locations.push_back(kk);last.push_back(n);}else idx=it->second;
   last[idx]=n;ev[n][o].push_back({idx,c});p.h=(p.h+(c==1?1:3))%4;p.x+=dx[p.h];p.y+=dy[p.h];}
  assert(p.x==3*P[n+1].x&&p.y==3*P[n+1].y&&p.h==P[n+1].h);
 }
 color.assign(ids.size(),0);for(size_t i=0;i<locations.size();++i){auto it=lastc.find(locations[i]);if(it!=lastc.end())color[i]=it->second;for(int n=9;n<=last[i];++n)alive[n].push_back(i);}
 tail(9);
 if(roots%100==0)cerr<<"ROOT "<<roots<<" tailnodes "<<tailnodes<<" states "<<states<<" hits "<<hits<<" max "<<maxdepth<<"\n";
 if(found)stopped=true;
}
void dfs(int n){
 if(n==9){fixed_coarse();return;}

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
int main(int argc,char**argv){if(argc>1)cap=strtoull(argv[1],nullptr,10);if(argc>2)depthcap=atoi(argv[2]);P.resize(9*(depthcap+2));turn.resize(P.size());P[0]={0,0,0};lastc.reserve(100000);dfs(0);
 cout<<"{\n\"status\":\""<<(found?"SAT_PREFIX":stopped?"UNKNOWN_CAP":"EXHAUSTED")<<"\",\n\"nodes\":"<<nodes<<",\n\"tail_nodes\":"<<tailnodes<<",\n\"roots\":"<<roots<<",\n\"states\":"<<states<<",\n\"cache_hits\":"<<hits<<",\n\"conflicts\":"<<leaves<<",\n\"max_macros\":"<<maxdepth<<",\n\"latest_conflict\":"<<latest<<",\n\"best_choices\":[";
 for(size_t i=0;i<best.size();++i){if(i)cout<<",";cout<<best[i];}cout<<"]\n}\n";
}
