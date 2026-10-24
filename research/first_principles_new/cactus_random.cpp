#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
struct Node {int parent,depth;unsigned char letter,count;};
struct Group{
 vector<Node> ns{{-1,0,2,0}};unordered_map<uint64_t,int> cache;unordered_map<int,int> cosets;
 int mult(int s,int letter){int parent=s,n=1;if(ns[s].letter==letter){parent=ns[s].parent;n=ns[s].count+1;}if(n==4)return parent;uint64_t key=uint64_t(parent)*8+letter*4+n;auto z=cache.find(key);if(z!=cache.end())return z->second;int t=ns.size();cache[key]=t;ns.push_back({parent,ns[parent].depth+1,(unsigned char)letter,(unsigned char)n});return t;}
 int u(int s,int sign){int a=sign>0?0:1,b=1-a;s=mult(s,a);for(int i=0;i<3;i++)s=mult(s,b);return s;}
 int cell(int s){auto z=cosets.find(s);if(z!=cosets.end())return z->second;int a=u(s,1),b=u(s,-1),target=s;if(ns[a].depth<ns[target].depth)target=a;if(ns[b].depth<ns[target].depth)target=b;if(target!=s)return cosets[s]=cell(target);int best=s;if(ns[a].depth==ns[s].depth)best=min(best,a);if(ns[b].depth==ns[s].depth)best=min(best,b);return cosets[s]=best;}
};
int main(int argc,char**argv){int trials=argc>1?stoi(argv[1]):100,T=argc>2?stoi(argv[2]):100000;mt19937_64 rng(3141592653);int maxg=0,maxc=0;
for(int trial=0;trial<trials;trial++) {Group G;unordered_map<int,bool>B;unordered_map<int,int>counts,ccounts,first;string w;vector<int>hist;int s=0;
for(int t=0;t<T;t++){int c=G.cell(s);hist.push_back(s);if(!counts[s])first[s]=t;
if(++counts[s]>maxg){maxg=counts[s];cout<<"GMAX "<<maxg<<" trial "<<trial<<" t "<<t<<" span "<<t-first[s]<<endl;ofstream o("/workspace/shared/langton/first_principles_new/cactus_group_witness_"+to_string(maxg)+".txt");o<<w.substr(first[s])<<"\n";}
if(++ccounts[c]>maxc){maxc=ccounts[c];cout<<"CMAX "<<maxc<<" trial "<<trial<<" t "<<t<<endl;}
if(!B.count(c)) B[c]=rng()%2;bool bit=B[c];B[c]=!bit;w.push_back(bit?'L':'R');s=G.mult(s,bit);
}
if(trial%10==0)cout<<"DONE "<<trial<<" g "<<maxg<<" c "<<maxc<<" nodes "<<G.ns.size()<<endl;}
}
