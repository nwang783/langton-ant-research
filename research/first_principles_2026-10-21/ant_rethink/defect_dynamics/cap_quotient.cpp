#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0},OFF=2048,W=4096;
array<signed char,W*W> board;
struct Counts {long long M=0;array<long long,4>delta{};};
struct Best{long long value=-999999;string word;vector<pair<int,int>>seed;Counts counts;};
uint64_t nodes=0,checks=0;int depth_cap,seed_cap;
array<Best,64> best;
string word;vector<pair<int,int>> seed;
void dfs(int x,int y,int h,int depth,Counts c){
 ++nodes;
 if(x+y<=-4&&c.M){
  ++checks;long long phi=c.M-2*c.delta[1];int n=seed.size();
  if(phi>best[n].value)best[n]={phi,word,seed,c};
 }
 if(depth==depth_cap)return;
 int at=(y+OFF)*W+x+OFF,old=board[at],level=x+y;
 for(int black=0;black<2;black++){
  if((old>=0&&old!=black)||(old<0&&level==-1&&black))continue;
  bool fresh_black=old<0&&black;if(fresh_black&&int(seed.size())==seed_cap)continue;
  int nh=(h+(black?3:1))&3,nx=x+dx[nh],ny=y+dy[nh];
  if(nx+ny>0)continue;
  Counts d=c;
  if(level>=-3){int j=-level;d.delta[j]+=black?-1:1;if(j==0)d.M++;}
  if(fresh_black)seed.emplace_back(x,y);
  board[at]=!black;word+=black?'L':'R';dfs(nx,ny,nh,depth+1,d);word.pop_back();board[at]=old;
  if(fresh_black)seed.pop_back();
 }
}
int main(int argc,char**argv){depth_cap=argc>1?atoi(argv[1]):40;int heading=argc>2?atoi(argv[2]):3;seed_cap=argc>3?atoi(argv[3]):40;int start_depth=argc>4?atoi(argv[4]):4;
 if(seed_cap>63||depth_cap+start_depth>=OFF-5)return 2;board.fill(-1);dfs(0,-start_depth,heading,0,{});
 cout<<"{\"max_length\":"<<depth_cap<<",\"heading\":"<<heading<<",\"start_depth\":"<<start_depth<<",\"seed_cap\":"<<seed_cap<<",\"nodes\":"<<nodes<<",\"completed\":"<<checks<<",\"best_by_seed_count\":[";
 bool comma=false;for(int n=0;n<=seed_cap;n++)if(best[n].value>-999999){if(comma)cout<<',';comma=true;auto&b=best[n];cout<<"{\"black_count\":"<<n<<",\"phi\":"<<b.value<<",\"M\":"<<b.counts.M<<",\"delta_A\":"<<b.counts.delta[1]<<",\"word\":\""<<b.word<<"\",\"seed\":[";bool cm=false;for(auto[x,y]:b.seed){if(cm)cout<<',';cm=true;cout<<'['<<x<<','<<y<<']';}cout<<"]}";}cout<<"]}\n";
}
