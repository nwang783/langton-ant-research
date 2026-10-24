#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
static uint64_t cell(int x,int y) {return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
struct Node {int parent; unsigned char letter,count;};
int main(int argc,char**argv){
 int trials=argc>1?stoi(argv[1]):500, T=argc>2?stoi(argv[2]):200000; uint64_t rngseed=argc>3?stoull(argv[3]):20261022;
 mt19937_64 rng(rngseed); int global=0; long long steps=0;
 for(int trial=0;trial<trials;trial++){
  int radius=trial==0?0:array<int,9>{2,3,5,8,12,20,30,50,100}[(trial-1)%9];
  int density=trial==0?0:array<int,7>{5,10,20,35,50,65,85}[((trial-1)/9)%7];
  unordered_set<uint64_t> B; vector<pair<int,int>> initial;
  if(trial)for(int x=-radius;x<=radius;x++)for(int y=-radius;y<=radius;y++)if(int(rng()%100)<density){B.insert(cell(x,y));initial.push_back({x,y});}
  vector<Node> nodes{{-1,2,0}}; vector<int> count{0},first{0},last{0}; unordered_map<uint64_t,int> intern;
  nodes.reserve(T);count.reserve(T);first.reserve(T);last.reserve(T);intern.reserve(T);B.reserve(T);
  int x=0,y=0,h=0,s=0,local=0;string word;word.reserve(T);vector<int> history;history.reserve(T);
  int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
  for(int t=0;t<T;t++){
   history.push_back(s);if(count[s]==0)first[s]=t;last[s]=t;
   local=max(local,++count[s]);
   if(count[s]>global){
    global=count[s];vector<int> times;for(int i=0;i<=t;i++)if(history[i]==s)times.push_back(i);
    cout<<"MAX "<<global<<" trial "<<trial<<" radius "<<radius<<" density "<<density<<" mass "<<initial.size()<<" t "<<t<<" first "<<first[s]<<" wordlen "<<t-first[s]<<" visits";for(int z:times)cout<<" "<<z;cout<<endl;
    ofstream out("/workspace/shared/langton/first_principles_new/free_product_witness_"+to_string(global)+".txt");
    out<<"rngseed "<<rngseed<<" trial "<<trial<<" t "<<t<<" start "<<first[s]<<"\nseed "<<initial.size()<<"\n";for(auto p:initial)out<<p.first<<" "<<p.second<<"\n";
    out<<"visits";for(int z:times)out<<" "<<z;out<<"\nword "<<word.substr(first[s])<<"\n";
   }
   bool black=B.count(cell(x,y));int letter=black?1:0;word.push_back(black?'L':'R');
   if(black)B.erase(cell(x,y));else B.insert(cell(x,y));h=(h+(black?3:1))%4;x+=dx[h];y+=dy[h];
   int parent=s,n=1;if(nodes[s].letter==letter){parent=nodes[s].parent;n=nodes[s].count+1;}
   if(n==4)s=parent;else{uint64_t key=uint64_t(parent)*8+letter*4+n;auto z=intern.find(key);if(z==intern.end()){s=nodes.size();intern[key]=s;nodes.push_back({parent,(unsigned char)letter,(unsigned char)n});count.push_back(0);first.push_back(0);last.push_back(0);}else s=z->second;}
  }
  steps+=T;
  if(trial%10==0)cout<<"DONE "<<trial<<" local "<<local<<" global "<<global<<" steps "<<steps<<endl;
 }
}
