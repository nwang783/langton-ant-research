#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;using K=uint64_t;using P=pair<int,int>;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
K key(int x,int y){return(K(uint32_t(x))<<32)|uint32_t(y);}
struct Hash{size_t operator()(K k)const{k+=0x9e3779b97f4a7c15ULL;k=(k^(k>>30))*0xbf58476d1ce4e5b9ULL;k=(k^(k>>27))*0x94d049bb133111ebULL;return k^(k>>31);}};
using B=unordered_set<K,Hash>;
void flip(B&b,K k){auto i=b.find(k);if(i==b.end())b.insert(k);else b.erase(i);}
array<int,4> levels(int x,int y){return{x+y,-x+y,-x-y,x-y};}
struct Result{int phi=-100000,t=0,r=0,cap=0,M=0,A=0,x=0,y=0,h=0;};
Result run(P q,int steps){
 const int off=10000,w=20001;array<vector<int>,4>counts,mass;
 for(int r=0;r<4;r++){counts[r].resize(w);mass[r].resize(w);}
 array<int,4>maxs{},qs=levels(q.first,q.second);B b;b.reserve(steps/8);b.insert(key(q.first,q.second));
 int x=0,y=0,h=0;Result best;
 for(int t=0;t<steps;t++){
  K k=key(x,y);bool black=b.count(k);auto ls=levels(x,y);
  for(int r=0;r<4;r++){if(abs(ls[r])>=off-3){cerr<<"row array exceeded\n";exit(2);}counts[r][ls[r]+off]++;mass[r][ls[r]+off]+=black?-1:1;}
  flip(b,k);h=(h+(black?3:1))&3;x+=dx[h];y+=dy[h];ls=levels(x,y);
  for(int r=0;r<4;r++){
   int cap=maxs[r]=max(maxs[r],ls[r]);
   if(cap<4||(r-cap)%2==0||ls[r]>cap-4||qs[r]==cap||qs[r]==cap-1)continue;
   int M=counts[r][cap+off];if(!M)continue;int A=mass[r][cap-1+off];int phi=M-2*A;
   if(phi>best.phi)best={phi,t+1,r,cap,M,A,x,y,h};
  }
 }
 return best;
}
int main(int argc,char**argv){int horizon=argc>1?stoi(argv[1]):200000,prelude=argc>2?stoi(argv[2]):12000;
 B b,seen;vector<P>targets;int x=0,y=0,h=0;
 for(int t=0;t<prelude;t++){K k=key(x,y);if(seen.insert(k).second)targets.emplace_back(x,y);bool black=b.count(k);flip(b,k);h=(h+(black?3:1))&3;x+=dx[h];y+=dy[h];}
 int overall=-999;
 for(int i=0;i<(int)targets.size();i++){
  auto q=targets[i];auto r=run(q,horizon);overall=max(overall,r.phi);
  cout<<"{\"id\":"<<i<<",\"seed\":["<<q.first<<','<<q.second<<"],\"phi\":"<<r.phi<<",\"t\":"<<r.t<<",\"rotation\":"<<r.r<<",\"cap\":"<<r.cap<<",\"M\":"<<r.M<<",\"A\":"<<r.A<<",\"end\":["<<r.x<<','<<r.y<<','<<r.h<<"]}\n";cout.flush();
 }
 cerr<<"checked "<<targets.size()<<" seeds, max "<<overall<<'\n';
}
