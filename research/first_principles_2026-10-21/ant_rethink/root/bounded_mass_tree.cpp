// Enumerate every physical finite turn word that can run with complete black
// mass <= K at all times. All coordinates and all finite seeds are covered.
// A branch is feasible iff turns alternate at every physical cell and
// initial_first_L_count + maximum_prefix_R_minus_L <= K.
// Termination at each K uses the separate no-bounded-mass-orbit theorem.
// A resource stop, if added by a caller, must not count as completion.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
using Pt=pair<int,int>;
struct Hash{size_t operator()(Pt p)const{return uint64_t(uint32_t(p.first))*0x9e3779b97f4a7c15ULL^uint32_t(p.second);}};
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
unordered_map<Pt,int,Hash> next_color;
vector<Pt> first_black;
vector<Pt> longest_seed;
string word,longest_word;
uint64_t nodes=0,leaves=0;
int max_length=0,K;
void dfs(int x,int y,int h,int m,int g,int peak){
 ++nodes;
 if((int)word.size()>max_length){max_length=word.size();longest_word=word;longest_seed=first_black;}
 Pt p={x,y};auto it=next_color.find(p);bool fresh=it==next_color.end();int known=fresh?-1:it->second;
 bool extended=false;
 for(int black=0;black<2;black++){
  if(!fresh&&black!=known)continue;
  int new_m=m+(fresh&&black),new_g=g+(black?-1:1),new_peak=max(peak,new_g);
  if(new_m+new_peak>K)continue;
  extended=true;next_color[p]=1-black;word+=black?'L':'R';
  if(fresh&&black)first_black.push_back(p);
  int hh=(h+(black?3:1))%4;
  dfs(x+dx[hh],y+dy[hh],hh,new_m,new_g,new_peak);
  if(fresh&&black)first_black.pop_back();word.pop_back();
  if(fresh)next_color.erase(p);else next_color[p]=known;
 }
 if(!extended)++leaves;
}
int main(int argc,char**argv){if(argc!=2){cerr<<"usage bounded_mass_tree K\n";return 2;}K=stoi(argv[1]);
 dfs(0,0,0,0,0,0);
 cout<<"{\"K\":"<<K<<",\"complete\":true,\"nodes\":"<<nodes<<",\"leaves\":"<<leaves<<",\"max_surviving_updates\":"<<max_length<<",\"forced_exceedance_by\":"<<max_length+1<<",\"word\":\""<<longest_word<<"\",\"seed\":[";
 for(int j=0;j<(int)longest_seed.size();j++){if(j)cout<<',';cout<<'['<<longest_seed[j].first<<','<<longest_seed[j].second<<']';}
 cout<<"]}\n";
}
