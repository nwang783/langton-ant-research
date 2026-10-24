#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
struct Node {int parent,depth;unsigned char letter,count;};
struct Group{
 vector<Node> ns{{-1,0,2,0}};unordered_map<uint64_t,int> cache;unordered_map<int,int> cosets;
 int mult(int s,int letter){int parent=s,n=1;if(ns[s].letter==letter){parent=ns[s].parent;n=ns[s].count+1;}if(n==4)return parent;uint64_t key=uint64_t(parent)*8+letter*4+n;auto z=cache.find(key);if(z!=cache.end())return z->second;int t=ns.size();cache[key]=t;ns.push_back({parent,ns[parent].depth+1,(unsigned char)letter,(unsigned char)n});return t;}
 int u(int s,int sign){int a=sign>0?0:1,b=1-a;s=mult(s,a);for(int i=0;i<3;i++)s=mult(s,b);return s;}
 int cell(int s){auto z=cosets.find(s);if(z!=cosets.end())return z->second;int a=u(s,1),b=u(s,-1),target=s;if(ns[a].depth<ns[target].depth)target=a;if(ns[b].depth<ns[target].depth)target=b;if(target!=s)return cosets[s]=cell(target);int best=s;if(ns[a].depth==ns[s].depth)best=min(best,a);if(ns[b].depth==ns[s].depth)best=min(best,b);return cosets[s]=best;}
};

uint64_t xy(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
int main(int argc,char**argv){int trials=argc>1?stoi(argv[1]):100,T=argc>2?stoi(argv[2]):100000;mt19937_64 rng(192837465);long long steps=0;
for(int tr=0;tr<trials;tr++) {Group G;unordered_set<uint64_t>B;vector<pair<int,int>>seed;int radius=tr?array<int,9>{2,3,5,8,12,20,30,50,100}[(tr-1)%9]:0,density=tr?array<int,7>{5,10,20,35,50,65,85}[((tr-1)/9)%7]:0;
if(tr)for(int x=-radius;x<=radius;x++)for(int y=-radius;y<=radius;y++)if(int(rng()%100)<density){B.insert(xy(x,y));seed.push_back({x,y});}
unordered_map<int,int>lamp; unordered_map<int,int>lastbit,lasttime;unordered_map<uint64_t,int>lastphys;int x=0,y=0,h=0,s=0;string word;int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
for(int t=0;t<T;t++){int c=G.cell(s);if(!lamp.count(c))lamp[c]=rng()%2; bool b=lamp[c]; lamp[c]=1-b;if(lastbit.count(c) && lastphys.count(xy(x,y)) && lastphys[xy(x,y)]!=c){cout<<"INTERLEAVE trial "<<tr<<" t "<<t<<" previouscosettime "<<lasttime[c]<<" word "<<word.substr(lasttime[c])<<(b?'L':'R')<<endl;ofstream out("/workspace/shared/langton/first_principles_new/abstract_interleaving_witness.txt"); out<<word.substr(lasttime[c])<<(b?'L':'R')<<"\n"; return 0;}lastphys[xy(x,y)]=c;if(lastbit.count(c)&&lastbit[c]==b){cout<<"LIFT_FAILURE trial "<<tr<<" t "<<t<<" previous "<<lasttime[c]<<" seedmass "<<seed.size()<<" word "<<word.substr(lasttime[c])<<(b?'L':'R')<<endl;ofstream o("/workspace/shared/langton/first_principles_new/lift_failure.txt");for(auto p:seed)o<<p.first<<" "<<p.second<<"\n";return 1;}lastbit[c]=b;lasttime[c]=t;word.push_back(b?'L':'R');if(b)B.erase(xy(x,y));else B.insert(xy(x,y));h=(h+(b?3:1))%4;x+=dx[h];y+=dy[h];s=G.mult(s,b);}
steps+=T;if(tr%10==0)cout<<"PASS "<<tr<<" steps "<<steps<<endl;}
cout<<"PASS ALL "<<steps<<endl;}
