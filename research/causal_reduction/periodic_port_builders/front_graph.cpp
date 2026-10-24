#include <algorithm>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Step {int64_t next;int shift;char turn;};
int main(int argc,char**argv){
 int H=argc>1?atoi(argv[1]):10,W=argc>2?atoi(argv[2]):2;
 uint32_t masks[2]={(uint32_t)(argc>3?atoi(argv[3]):0),(uint32_t)(argc>4?atoi(argv[4]):819)};
 int bits=H*W,ports=4*H*W;uint64_t M=1ULL<<bits,N=2*ports*M;assert(N<=200000000);
 vector<uint8_t> done(N);uint64_t cycles=0,maxpath=0;auto start=chrono::steady_clock::now();
 auto step=[&](uint32_t s){
  uint32_t board=s&(M-1),q=s>>bits;int head=q%ports,phase=q/ports,h=head%4,cell=head/4,x=cell/H,y=cell%H;
  uint32_t bit=1u<<(x*H+y);bool black=board&bit;board^=bit;h=(h+(black?3:1))%4;
  const int DX[]={0,1,0,-1},DY[]={1,0,-1,0};x+=DX[h];y+=DY[h];int shift=0;
  if(y<0||y>=H||x<0)return Step{-1,0,black?'L':'R'};
  if(x>=W){phase^=1;board>>=H;board|=masks[phase]<<(H*(W-1));--x;shift=1;}
  return Step{int64_t((uint64_t(phase*ports+(x*H+y)*4+h)<<bits)|board),shift,black?'L':'R'};
 };
 cout<<"{\"H\":"<<H<<",\"W\":"<<W<<",\"input_masks\":["<<masks[0]<<","<<masks[1]<<"],\"states\":"<<N<<",\"cycles\":[";
 for(uint64_t seed=0;seed<N;++seed){
  if(done[seed])continue;vector<uint32_t>path;int64_t s=seed;
  while(s>=0&&!done[s]){done[s]=1;path.push_back(s);s=step(s).next;}
  maxpath=max(maxpath,uint64_t(path.size()));
  if(s>=0&&done[s]==1){
   auto it=find(path.begin(),path.end(),uint32_t(s));assert(it!=path.end());uint64_t drift=0;string word;
   for(auto j=it;j!=path.end();++j){auto z=step(*j);drift+=z.shift;word+=z.turn;}
   assert(drift>0);if(cycles++)cout<<",";
   cout<<"{\"entry_id\":"<<s<<",\"period\":"<<word.size()<<",\"drift\":"<<drift<<",\"word\":\""<<word<<"\"}";
  }
  for(auto v:path)done[v]=2;
 }
 cout<<"],\"cycle_count\":"<<cycles<<",\"max_transient_path\":"<<maxpath<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"status\":\"COMPLETE_FINITE_INTERFACE_GRAPH\"}\n";
}
