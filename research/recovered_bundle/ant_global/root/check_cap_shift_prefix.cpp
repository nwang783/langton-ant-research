// Exhaust all physical finite words with an initially white A row.
// Each other first read branches; subsequent reads use literal toggled cells.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
using namespace std;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0},OFF=128,W=256;
array<signed char,W*W> board;
struct Counts {long long M=0,LC=0;array<long long,4>delta{};};
uint64_t nodes=0,checks=0;long long maxS=-999999;int depth_cap;
array<long long,17> best;array<string,17> bestword;
string word;vector<pair<int,int>> seed;
void dfs(int x,int y,int h,int depth,Counts c){
 ++nodes;
 int index=x+y<=-4?16:-4*(x+y)+h;
 long long test=7*c.delta[1]-4*c.delta[2]+c.delta[3]-8*c.M+c.LC;
 if(test>best[index]){best[index]=test;bestword[index]=word;}
 if(x+y<=-4&&c.M){
  ++checks;long long S=7*c.delta[1]-4*c.delta[2]+c.delta[3]-8*c.M+c.LC;
  if(S>maxS)maxS=S;
  if(S>0){cerr<<"COUNTEREXAMPLE "<<word<<" S="<<S<<" M="<<c.M<<" delta="<<c.delta[1]<<","<<c.delta[2]<<","<<c.delta[3]<<" seed:";for(auto p:seed)cerr<<" ("<<p.first<<","<<p.second<<")";cerr<<'\n';exit(1);}
 }
 if(depth==depth_cap)return;
 int at=(y+OFF)*W+x+OFF,old=board[at],level=x+y;
 for(int black=0;black<2;black++){
  if((old>=0&&old!=black)||(old<0&&level==-1&&black))continue;
  int nh=(h+(black?3:1))&3,nx=x+dx[nh],ny=y+dy[nh];
  if(nx+ny>0)continue;
  Counts d=c;
  if(level>=-3){int j=-level;d.delta[j]+=black?-1:1;if(j==0)d.M++;if(j==3&&black&&h==0)d.LC++;}
  bool add=old<0&&black;if(add)seed.emplace_back(x,y);
  board[at]=!black;word+=black?'L':'R';dfs(nx,ny,nh,depth+1,d);word.pop_back();board[at]=old;
  if(add)seed.pop_back();
 }
}
int main(int argc,char**argv){depth_cap=argc>1?atoi(argv[1]):32;int heading=argc>2?atoi(argv[2]):3;best.fill(-999999);board.fill(-1);dfs(0,-4,heading,0,{});cout<<"{\"max_length\":"<<depth_cap<<",\"heading\":"<<heading<<",\"nodes\":"<<nodes<<",\"completed_prefixes\":"<<checks<<",\"max_S\":"<<maxS<<"}\n";for(int j=0;j<17;j++)if(best[j]>-999999)cout<<j<<" "<<best[j]<<" "<<bestword[j]<<"\n";}
