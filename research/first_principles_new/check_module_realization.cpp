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

int main(int argc,char**argv){int trials=argc>1?stoi(argv[1]):100,T=argc>2?stoi(argv[2]):100000;mt19937_64 rng(718281828);long long total=0;int maxg=0,maxc=0,maxret=0;
for(int tr=0;tr<trials;tr++){Group G;unordered_map<int,bool>B;unordered_map<uint64_t,string>returns;unordered_map<int,int>gc,cc;int s=0;B[G.cell(0)]=0;int p=G.mult(G.mult(G.mult(0,0),0),0);B[G.cell(p)]=0;
for(int t=0;t<T;t++){int c=G.cell(s);if(!B.count(c))B[c]=rng()%2;bool b=B[c];maxg=max(maxg,++gc[s]);maxc=max(maxc,++cc[c]);
if(s && G.ns[s].count==3){int v=G.ns[s].parent,a=G.ns[s].letter;if(b!=a){cout<<"ESCAPE trial "<<tr<<" t "<<t<<endl;return 1;}uint64_t key=uint64_t(v)*2+a;int root=G.cell(v);if(!B.count(root)){cout<<"UNKNOWN_ROOT\n";return 2;}returns[key].push_back(B[root]==a?'B':'G');string r=returns[key];maxret=max(maxret,int(r.size()));if(r!="G"&&r!="B"&&r!="GB"){cout<<"BAD_RETURN_SEQUENCE "<<r<<" trial "<<tr<<" t "<<t<<endl;return 3;}}
B[c]=!b;s=G.mult(s,b);}
total+=T;if(tr%10==0)cout<<"PASS "<<tr<<" steps "<<total<<" maxg "<<maxg<<" maxc "<<maxc<<" maxret "<<maxret<<endl;
}
cout<<"PASS ALL "<<total<<" maxg "<<maxg<<" maxc "<<maxc<<" maxret "<<maxret<<endl;}
