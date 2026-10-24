#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
const string W="LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR";
array<bool,1024>legal{};array<bool,2048>allowed{};array<ofstream,2048>out;ofstream common;map<pair<int,int>,char>lastread;vector<unsigned long long>counts;array<unsigned long long,2048>leaves{};unsigned long long nodes=0,none=0,cap=500000000;int depthlim=150;bool stop=false;const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
void dfs(string&w,int x,int y,int h,int bits,bool prevbad,int selected){++counts[w.size()];if(++nodes>cap){stop=true;return;}if(int(w.size())==depthlim){if(selected<0){common<<w<<'\n';none++;}else{out[selected]<<w<<'\n';leaves[selected]++;}return;}pair<int,int>p={x,y};auto it=lastread.find(p);char old=it==lastread.end()?'?':it->second;for(char c:{'L','R'}){if(c==old)continue;int full=(bits<<1)+(c=='R'),nb=full&1023;bool bad=w.size()>=9&&!legal[nb],pair=bad&&prevbad;int chosen=selected;if(pair){if(!allowed[full]||(selected>=0&&selected!=full))continue;chosen=full;}lastread[p]=c;w.push_back(c);int nh=(h+(c=='R'?1:3))%4;dfs(w,x+dx[nh],y+dy[nh],nh,nb,bad,chosen);w.pop_back();if(old=='?')lastread.erase(p);else lastread[p]=old;if(stop)return;}}
int main(int argc,char**argv){if(argc>1)depthlim=stoi(argv[1]);if(argc>2)cap=stoull(argv[2]);string dir=argc>3?argv[3]:"monochromatic_union";vector<string>patterns={"LLLRRRRLRLL","LLRLRLLRRLL","LLRLRRRRLLL","LLRRLRLLRRL","LRRLRRRRLRL","LRRLRRRRLRR","RLRLLRLLRRR","RRRLLRLLRLR","RRRLRLLRRRR","RRRLRRRRLRL","RRRLRRRRLRR","RRRRLRLLRLL"};for(auto p:patterns){int v=0;for(char c:p)v=(v<<1)+(c=='R');allowed[v]=true;out[v].open(dir+"/"+p+".txt");if(!out[v])return 2;}common.open(dir+"/NO_K.txt");if(!common)return 2;for(int i=0;i<104;i++){int v=0;for(char c:(W+W).substr(i,10))v=(v<<1)+(c=='R');legal[v]=true;}counts.resize(depthlim+1);string w;dfs(w,0,0,0,0,false,-1);cout<<"complete "<<!stop<<" depth "<<depthlim<<" nodes "<<nodes<<" noK "<<none<<'\n';for(auto p:patterns){int v=0;for(char c:p)v=(v<<1)+(c=='R');cout<<p<<' '<<leaves[v]<<'\n';}return stop?1:0;}
