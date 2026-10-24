#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
using namespace std;using U=__uint128_t;
constexpr int H=10,W=12;const int DX[]={0,1,0,-1},DY[]={1,0,-1,0};uint64_t nodes,cap=100000000;int bound,split;bool hitcap=false;string word;U finalseed;string finalword;int finalsplit;
bool dfs(int x,int y,int h,int phase,int depth,U known,U black,U seed){
 if(++nodes>cap){hitcap=true;return false;}
 if(x<0){
  if(h!=3||y!=(phase==1?9:5))return false;
  if(phase==2){finalseed=seed;finalword=word;finalsplit=split;return true;}
  split=word.size();return dfs(0,8,1,2,depth,known,black,seed);
 }
 if(x>=W||y<0||y>=H||depth>=bound)return false;
 int dist=x+1+abs(y-(phase==1?9:5))+(phase==1?6:0);if(depth+dist>bound)return false;
 U bit=U(1)<<(x*H+y);int first=(black&bit)?1:0,last=first;if(!(known&bit)){first=0;last=1;}
 for(int b=first;b<=last;++b){int hh=(h+(b?3:1))%4;U bb=b?(black&~bit):(black|bit),ss=seed;if(!(known&bit)&&b)ss|=bit;word+=b?'L':'R';if(dfs(x+DX[hh],y+DY[hh],hh,phase,depth+1,known|bit,bb,ss))return true;word.pop_back();if(hitcap)return false;}
 return false;
}
int main(){for(bound=16;bound<=80;bound+=4){nodes=0;hitcap=false;word.clear();bool yes=dfs(0,4,1,1,0,3,0,3);cout<<"BOUND "<<bound<<" NODES "<<nodes<<" STATUS "<<(yes?"FOUND":hitcap?"CAP":"EXHAUSTED")<<endl;if(yes){cout<<"WORDS LL "<<finalword.substr(0,finalsplit)<<" "<<finalword.substr(finalsplit)<<"\nSEED";for(int x=0;x<W;++x)for(int y=0;y<H;++y)if(finalseed&(U(1)<<(x*H+y)))cout<<" "<<x<<","<<y;cout<<endl;break;}if(hitcap)break;}}
