#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;using U=__uint128_t;
struct Hash{size_t operator()(U x)const{return(size_t)x^((size_t)(x>>64)*0x9e3779b97f4a7c15ULL);}};
const string W="LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR";
array<bool,1024>legal{};unordered_set<U,Hash>allowed;map<pair<int,int>,char>lastread;const U mask=(U(1)<<100)-1;int maxdepth=150,gap=140;const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};unsigned long long nodes=0,leaves=0,cap=100000000;bool stop=false;ofstream out;vector<unsigned long long>counts;
void dfs(string&w,int x,int y,int h,U bits,bool prevbad,int lastpair){
 ++counts[w.size()];if(++nodes>cap){stop=true;return;}if((int)w.size()==maxdepth){++leaves;if(out)out<<w<<'\n';return;}
 auto p=make_pair(x,y);auto it=lastread.find(p);char old=it==lastread.end()?'?':it->second;
 for(char c:{'L','R'}){if(c==old)continue;U nb=((bits<<1)+(c=='R'))&mask;if(!allowed.count(nb))continue;bool bad=!legal[(int)(nb&1023)],pair=bad&&prevbad;int depth=w.size();if(pair&&depth-lastpair<gap)continue;lastread[p]=c;w.push_back(c);int nh=(h+(c=='R'?1:3))%4;dfs(w,x+dx[nh],y+dy[nh],nh,nb,bad,pair?depth:lastpair);w.pop_back();if(old=='?')lastread.erase(p);else lastread[p]=old;if(stop)return;}
}
int main(int argc,char**argv){if(argc>1)maxdepth=stoi(argv[1]);gap=maxdepth-10;if(argc>2)cap=stoull(argv[2]);if(argc>3)out.open(argv[3]);counts.resize(maxdepth+1);for(int i=0;i<104;++i){int b=0;for(char c:(W+W).substr(i,10))b=(b<<1)+(c=='R');legal[b]=true;}ifstream in("spaced_pair_words100.recurrent.txt");vector<string>seeds;string w;while(in>>w){seeds.push_back(w);U b=0;for(char c:w)b=(b<<1)+(c=='R');allowed.insert(b);}unsigned done=0;
 for(string w:seeds){lastread.clear();int x=0,y=0,h=0,lastpair=-1000000;bool prevbad=false;U bits=0;for(int i=0;i<100;++i){char c=w[i];auto p=make_pair(x,y);if(lastread.count(p)&&lastread[p]==c)return 2;lastread[p]=c;bits=(bits<<1)+(c=='R');bool bad=i>=9&&!legal[(int)(bits&1023)];if(bad&&prevbad)lastpair=i;prevbad=bad;h=(h+(c=='R'?1:3))%4;x+=dx[h];y+=dy[h];}dfs(w,x,y,h,bits,prevbad,lastpair);++done;if(stop)break;}
 cout<<"depth "<<maxdepth<<" gap "<<gap<<" stopped "<<stop<<" seeds_done "<<done<<" seeds "<<seeds.size()<<" nodes "<<nodes<<" leaves "<<leaves<<'\n';for(int i=100;i<=maxdepth;i+=10)cout<<i<<' '<<counts[i]<<'\n';return stop?1:0;
}
