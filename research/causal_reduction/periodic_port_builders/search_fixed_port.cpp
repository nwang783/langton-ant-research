#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>
using namespace std;
constexpr int H=12,SW=8,W=1024; int entry=6,exitrow=5;using Seed=array<uint16_t,SW>;
struct Run{int good,span,steps,reason;long long score;};
Run run(const Seed&seed,bool literal=false){
 array<uint16_t,W>B{};copy(seed.begin(),seed.end(),B.begin());int R[]={entry},S[]={exitrow};int x=0,y=entry,h=1,good=0,span=0;const int DX[]={0,1,0,-1},DY[]={1,0,-1,0};string word;
 for(int t=0;t<200000;++t){
  bool black=B[x]&(1<<y);B[x]^=1<<y;h=(h+(black?3:1))%4;x+=DX[h];y+=DY[h];span=max(span,x);if(literal)word+=black?'L':'R';
  int reason=0;
  if(y<0||y>=H)reason=1;else if(x>=W)reason=2;else if(x<0){
   if(y!=S[good%1]||h!=3)reason=3;
   else{if(literal)cout<<"EXCURSION "<<good<<" "<<word<<"\n";word.clear();++good;x=0;y=R[good%1];h=1;if(good==300)reason=4;}
  }
  if(reason){if(literal)cout<<"STOP "<<reason<<" at "<<x<<","<<y<<","<<h<<"\n";return {good,span,t+1,reason,1000000LL*good+1000LL*span+(t%1000)};}
 }
 return{good,span,200000,5,1000000LL*good+1000LL*span+999};
}
int main(int argc,char**argv){int trials=argc>1?atoi(argv[1]):1000000;if(argc>2)entry=atoi(argv[2]);if(argc>3)exitrow=atoi(argv[3]);mt19937_64 rng(4251009+entry*19+exitrow);vector<pair<long long,Seed>>pool;Run best{-1,0,0,0,0};Seed bestseed{};
 for(int it=0;it<trials;++it){
  Seed seed{};
  if(pool.empty()||rng()%12==0){for(auto&col:seed)col=rng()&4095;}
  else{seed=pool[rng()%min<size_t>(pool.size(),20)].second;int edits=1+(rng()%6==0?rng()%12:0);for(int j=0;j<edits;++j)seed[rng()%SW]^=1<<(rng()%H);}
  auto r=run(seed);
  if(r.score>best.score||best.good<0){best=r;bestseed=seed;cout<<"BEST "<<it<<" good "<<r.good<<" span "<<r.span<<" steps "<<r.steps<<" reason "<<r.reason<<" seed";for(auto c:seed)cout<<" "<<c;cout<<endl;}
  if(pool.size()<64||r.score>pool.back().first){pool.emplace_back(r.score,seed);sort(pool.begin(),pool.end(),[](auto&a,auto&b){return a.first>b.first;});pool.erase(unique(pool.begin(),pool.end(),[](auto&a,auto&b){return a.second==b.second;}),pool.end());if(pool.size()>64)pool.resize(64);}
  if(r.reason==4||r.reason==5){cout<<"HORIZON_CANDIDATE\n";break;}
 }
 cout<<"FINAL seed";for(auto c:bestseed)cout<<" "<<c;cout<<"\n";run(bestseed,true);
}
