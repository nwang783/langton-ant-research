#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
const string W="LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR";
array<bool,1024> legal{};
map<pair<int,int>,char> lastread;
vector<unsigned long long> counts;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
unsigned long long nodes=0, cap=100000000;
int maxdepth=150,pattern_bits=0;string pattern="RRRLLRLLRLR";
ofstream out;
bool stop=false;
void dfs(string&w,int x,int y,int h,int bits,bool prevbad,int last_pair){
 ++counts[w.size()];if(++nodes>cap){stop=true;return;}
 if(int(w.size())==maxdepth){if(out)out<<w<<'\n';return;}
 pair<int,int> p={x,y};auto it=lastread.find(p);char old=it==lastread.end()?'?':it->second;
 for(char c: {'L','R'}){
  if(c==old)continue;
  int nb=((bits<<1)+(c=='R'))&1023;
  bool bad=w.size()>=9&&!legal[nb];
  bool pair=bad&&prevbad; if(pair && ((bits<<1)+(c=='R'))!=pattern_bits)continue;
  lastread[p]=c;w.push_back(c);int nh=(h+(c=='R'?1:3))%4;
  dfs(w,x+dx[nh],y+dy[nh],nh,nb,bad,pair?(int)w.size()-1:last_pair);
  w.pop_back();if(old=='?')lastread.erase(p);else lastread[p]=old;
  if(stop)return;
 }
}
int main(int argc,char**argv){
 if(argc>1)maxdepth=stoi(argv[1]);
 if(argc>2)pattern=argv[2];
 for(char c:pattern)pattern_bits=(pattern_bits<<1)+(c=='R');
 if(argc>3)cap=stoull(argv[3]);
 if(argc>4)out.open(argv[4]);
 counts.resize(maxdepth+1);
 for(int i=0;i<104;++i){int v=0;for(char c:(W+W).substr(i,10))v=(v<<1)+(c=='R');legal[v]=true;}
 string w;dfs(w,0,0,0,0,false,-1000000);
 cout<<"depth "<<maxdepth<<" sole_K_pattern "<<pattern<<" stopped "<<stop<<" nodes "<<nodes<<'\n';
 for(int i=0;i<=maxdepth;++i)if(i%10==0||i==maxdepth)cout<<i<<' '<<counts[i]<<'\n';
 return stop?1:0;
}
