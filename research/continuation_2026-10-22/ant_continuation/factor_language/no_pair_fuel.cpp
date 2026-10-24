#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
struct V{string word,choices;array<int,2> next={-1,-1};};
vector<V> vertices;
map<pair<int,int>,char> lastread;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
int capmass=20,maxdepth=2000,longest=0;
unsigned long long nodes=0,capnodes=20000000;
bool stopped=false;string best;
void dfs(string&w,int vid,int x,int y,int h,int mass){
 if(++nodes>capnodes){stopped=true;return;}
 if(int(w.size())>longest){longest=w.size();best=w;}
 if(int(w.size())>=maxdepth){stopped=true;return;}
 auto p=make_pair(x,y);auto it=lastread.find(p);char old=it==lastread.end()?'?':it->second;
 for(char c:vertices[vid].choices){
  if(c==old)continue;
  int nm=mass+(old=='?'&&c=='L');if(nm>capmass)continue;
  lastread[p]=c;w+=c;int nh=(h+(c=='R'?1:3))%4;
  dfs(w,vertices[vid].next[c=='R'],x+dx[nh],y+dy[nh],nh,nm);
  w.pop_back();if(old=='?')lastread.erase(p);else lastread[p]=old;
  if(stopped)return;
 }
}
int main(int argc,char**argv){
 if(argc<3)return 2;capmass=stoi(argv[2]);if(argc>3)maxdepth=stoi(argv[3]);
 ifstream f(argv[1]);string w,c;unordered_map<string,int>ids;
 while(f>>w>>c){ids[w]=vertices.size();vertices.push_back({w,c,{-1,-1}});}
 for(auto&v:vertices)for(char c:v.choices)v.next[c=='R']=ids.at(v.word.substr(1)+c);
 for(int vid=0;vid<int(vertices.size());++vid){
  lastread.clear();int x=0,y=0,h=0,m=0;w=vertices[vid].word;
  for(char c:w){auto p=make_pair(x,y);if(!lastread.count(p)&&c=='L')++m;lastread[p]=c;h=(h+(c=='R'?1:3))%4;x+=dx[h];y+=dy[h];}
  if(m<=capmass)dfs(w,vid,x,y,h,m);
  if(stopped)break;
 }
 cout<<"mass "<<capmass<<" longest "<<longest<<" stopped "<<stopped<<" nodes "<<nodes<<"\nbest "<<best<<"\n";
 return stopped?1:0;
}
