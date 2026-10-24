#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <chrono>
#include <unordered_map>
using namespace std;
struct Word { vector<int> d; };
vector<Word> dom[4];int k,a,b;int chosen[4];long long nodes=0,capnodes=50000000,leaves=0,good=0,late=0;int completed=0;long long depthnodes[100]{};bool capped=false;
const int DX[4]={0,1,0,-1},DY[4]={1,0,-1,0};
const int SZ=512; int8_t board[SZ*SZ];
vector<int> coarse;
long long code(int x,int y){return static_cast<long long>((static_cast<uint64_t>(static_cast<uint32_t>(x))<<32)^static_cast<uint32_t>(y));}
void fullcheck(int h0) {
 leaves++;int depth=1;long long len=k;while(len<10000){len*=k;depth++;}
 unordered_map<long long,pair<int,int>> last;int x=0,y=0,h=h0;long long fuel=0;
 for(int t=0;t<10000;t++){
  int z=1;long long div=len/k;
  while(div){int digit=(t/div)%k;z=dom[z][chosen[z]].d[digit];div/=k;}
  int turn=(z-h+4)%4;auto xy=code(x,y);auto it=last.find(xy);
  if(it!=last.end() && it->second.first==turn){late=max(late,(long long)t);
   cout<<"LEAF "<<h0<<" conflict "<<t<<" previous "<<it->second.second<<" xy "<<x<<","<<y<<" turn "<<turn<<" images";
   for(int v=0;v<4;v++){cout<<' ';for(int dd:dom[v][chosen[v]].d)cout<<dd;}cout<<'\n';return;}
  if(it==last.end() && turn==3)fuel++;
  last[xy]={turn,t};h=z;x+=DX[z];y+=DY[z];
 }
 good++;cout<<"SURVIVOR "<<h0<<" fuel "<<fuel<<" images";
 for(int z=0;z<4;z++){cout<<' ';for(int d:dom[z][chosen[z]].d)cout<<d;}cout<<endl;
}
void dfs(int t,int x,int y,int h,int h0) {
 if(capped)return;
 if(t==k){fullcheck(h0);return;}
 int z=coarse[t];int lo=chosen[z],hi=lo+1;bool fresh=lo<0;if(fresh){lo=0;hi=dom[z].size();}
 for(int wi=lo;wi<hi;wi++){
  depthnodes[t]++;if(++nodes>capnodes){capped=true;return;}
  vector<pair<int,int>> undo;int xx=x,yy=y,hh=h;bool ok=true;
  for(int d:dom[z][wi].d){
   int turn=(d-hh+4)%4;int addr=(xx+256)*SZ+yy+256;
   if(turn!=1 && turn!=3){ok=false;break;}
   if(board[addr]==turn){ok=false;break;}
   undo.push_back({addr,board[addr]});board[addr]=turn;
   xx+=DX[d];yy+=DY[d];hh=d;
  }
  if(ok){if(fresh)chosen[z]=wi;dfs(t+1,xx,yy,hh,h0);if(fresh)chosen[z]=-1;}
  for(auto i=undo.rbegin();i!=undo.rend();++i)board[i->first]=i->second;
  if(capped)return;
 }
}
int main(int argc,char**argv){
 if(argc>1)capnodes=stoll(argv[1]);ifstream f("rectangular_k17_domains.txt");f>>k>>a>>b;
 for(int z=0;z<4;z++){int n;f>>n;while(n--){string w;f>>w;Word v;for(char c:w)v.d.push_back(c-'0');dom[z].push_back(v);}}
 auto st=chrono::steady_clock::now();
 for(int i=0;i<(int)dom[1].size() && !capped;i++)for(int h:{0,2}){
  fill(begin(chosen),end(chosen),-1);chosen[1]=i;coarse=dom[1][i].d;dfs(0,0,0,h,h);
  if(capped)break;completed++;
 }
 cout<<"COMPLETED root headings "<<completed<<" out of "<<dom[1].size()*2<<endl;cout<<"DEPTHS";for(int j=0;j<k;j++)cout<<" "<<depthnodes[j];cout<<endl;
 cout<<"SUMMARY nodes "<<nodes<<" cap "<<capnodes<<" capped "<<capped<<" leaves "<<leaves<<" survivors "<<good<<" latest_deep_conflict "<<late<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;
}
