#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <chrono>
#include <unordered_map>
using namespace std;
struct Word { vector<int> turn, sub; };
vector<Word> dom[4]; int k,a,b,root,chosen[4],firststate;vector<int> coarse;
long long nodes=0,capnodes=1000000000,leaves=0,good=0,late=0;bool capped=false;int completed=0;
const int DX[4]={0,1,0,-1},DY[4]={1,0,-1,0},SZ=512;int8_t board[SZ*SZ];
uint64_t code(int x,int y){return (uint64_t(uint32_t(x))<<32)^uint32_t(y);}
void fullcheck(){
 leaves++;int depth=2;long long len=long(k)*k;while(len<10000){len*=k*k;depth+=2;}
 unordered_map<uint64_t,pair<int,int>> last;int x=0,y=0,h=root/2;long long fuel=0;
 for(int t=0;t<10000;t++){
  int q=root;long long div=len/k;
  while(div){int digit=(t/div)%k;q=dom[q][chosen[q]].sub[digit];div/=k;}
  int turn=q%2?3:1;auto xy=code(x,y);auto it=last.find(xy);
  if(it!=last.end() && it->second.first==turn){late=max(late,(long long)t);cout<<"LEAF "<<root<<" conflict "<<t<<" previous "<<it->second.second<<" xy "<<x<<","<<y<<" turn "<<turn<<" images";for(int v=0;v<4;v++){cout<<' ';for(int c:dom[v][chosen[v]].turn)cout<<(c==1?'R':'L');}cout<<'\n';return;}
  if(it==last.end() && turn==3)fuel++;last[xy]={turn,t};h=(h+turn)%4;x+=DX[h];y+=DY[h];
 }
 good++;cout<<"SURVIVOR root "<<root<<" fuel "<<fuel<<" images";for(int z=0;z<4;z++){cout<<' ';for(int c:dom[z][chosen[z]].turn)cout<<(c==1?'R':'L');}cout<<endl;
}
void dfs(int t,int x,int y,int h){
 if(capped)return;if(t==k){fullcheck();return;}
 int q=coarse[t],lo=chosen[q],hi=lo+1;bool fresh=lo<0;if(fresh){lo=0;hi=dom[q].size();}
 for(int wi=lo;wi<hi;wi++){
  if(q==firststate && dom[q][wi].sub[0]!=root)continue;
  if(++nodes>capnodes){capped=true;return;}
  vector<pair<int,int>> undo;int xx=x,yy=y,hh=h;bool ok=true;
  for(int turn:dom[q][wi].turn){int addr=(xx+256)*SZ+yy+256;if(board[addr]==turn){ok=false;break;}undo.push_back({addr,board[addr]});board[addr]=turn;hh=(hh+turn)%4;xx+=DX[hh];yy+=DY[hh];}
  if(ok){if(fresh)chosen[q]=wi;dfs(t+1,xx,yy,hh);if(fresh)chosen[q]=-1;}
  for(auto i=undo.rbegin();i!=undo.rend();++i)board[i->first]=i->second;if(capped)return;
 }
}
int main(int argc,char**argv){
 if(argc>1)capnodes=stoll(argv[1]);ifstream f("rectangular_axis_turn_domains.txt");f>>k>>a>>b;
 for(int q=0;q<4;q++){int n;f>>n;while(n--){string w;f>>w;Word v;for(int j=0;j<k;j++){int c=w[j]=='R'?1:3;v.turn.push_back(c);v.sub.push_back(2*((q/2+j)%2)+(c==3));}dom[q].push_back(v);}}
 auto st=chrono::steady_clock::now();
 for(root=0;root<4 && !capped;root++)for(int i=0;i<(int)dom[root].size();i++){
  fill(begin(chosen),end(chosen),-1);chosen[root]=i;coarse=dom[root][i].sub;firststate=coarse[0];dfs(0,0,0,root/2);if(capped)break;completed++;
 }
 cout<<"SUMMARY completed_root_images "<<completed<<" nodes "<<nodes<<" cap "<<capnodes<<" capped "<<capped<<" leaves "<<leaves<<" survivors "<<good<<" latest_deep_conflict "<<late<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;
}
