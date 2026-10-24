#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
const string W="LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRR";
set<string> whitelist;
map<pair<int,int>,char> lastread;
vector<string> words150, starts, survivors;
int bad_count=1;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};

void enumerate(string &w,int x,int y,int h,int target,int mode){
 if(int(w.size())==target){
  if(mode==0)words150.push_back(w);
  else if(mode==1)starts.push_back(w);
  else survivors.push_back(w);
  return;
 }
 const pair<int,int> p={x,y};
 auto it=lastread.find(p); char old=it==lastread.end()?'?':it->second;
 for(char c: {'L','R'}){
  if(c==old)continue;
  bool legal=true;
  if(w.size()>=9)legal=whitelist.count(w.substr(w.size()-9)+c);
  if(mode==2 && w.size()>=10 && w.size()<size_t(10+bad_count)){if(legal)continue;}
  else if(!legal)continue;
  lastread[p]=c; w.push_back(c);
  int nh=(h+(c=='R'?1:3))%4;
  enumerate(w,x+dx[nh],y+dy[nh],nh,target,mode);
  w.pop_back();
  if(old=='?')lastread.erase(p);else lastread[p]=old;
 }
}
int main(int argc,char**argv){
 for(int i=0;i<104;++i)whitelist.insert((W+W).substr(i,10));
 string z; enumerate(z,0,0,0,150,0);
 map<string,set<string>> pred;set<string> vertices;
 for(auto&w:words150){pred[w.substr(1)].insert(w.substr(0,149));vertices.insert(w.substr(1));vertices.insert(w.substr(0,149));}
 set<string> reach;vector<string> stack;
 for(int i=0;i<104;++i){string v=(W+W+W).substr(i,149);reach.insert(v);stack.push_back(v);}
 while(!stack.empty()){
  auto v=stack.back();stack.pop_back();
  for(auto&u:pred[v])if(reach.insert(u).second)stack.push_back(u);
 }
 lastread.clear();enumerate(z,0,0,0,10,1);
 for(int k=1;k<=12;++k){
  bad_count=k; survivors.clear();lastread.clear();enumerate(z,0,0,0,159+k,2);
  size_t successes=0;
  string example;
  for(auto&w:survivors)if(reach.count(w.substr(w.size()-149))){++successes;example=w;}
  cout<<"consecutive_bad "<<k<<" survivors "<<survivors.size()<<" successes "<<successes<<"\n"<<flush;
  if(successes){cout<<"example "<<example<<"\n";break;}
 }
 return 0;
}
