#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <chrono>
using namespace std;
struct Word { string s;vector<int> sub; };
vector<Word> dom[8];int k,a,b,root,firststate,chosen[8];long long nodes=0,capnodes=20000000,reads=0,longest=0,survivors=0;bool capped=false;int completed=0,startordinal=0,ordinal=0;const int CAP=3000,SZ=2048;int8_t board[SZ*SZ];const int DX[4]={0,1,0,-1},DY[4]={1,0,-1,0};
void search(vector<pair<int,int>> stack,int x,int y,int h,int t){
 if(capped)return;vector<pair<int,int>> undo;
 auto rollback=[&](){for(auto i=undo.rbegin();i!=undo.rend();++i)board[i->first]=i->second;};
 while(!stack.empty() && t<CAP){
  auto [q,l]=stack.back();stack.pop_back();
  if(l){
   if(chosen[q]<0){
    for(int wi=0;wi<(int)dom[q].size();wi++){
     if(q==firststate && dom[q][wi].sub[0]!=root)continue;
     if(++nodes>capnodes){capped=true;break;}
     chosen[q]=wi;auto copy=stack;for(int j=k-1;j>=0;j--)copy.push_back({dom[q][wi].sub[j],l-1});search(move(copy),x,y,h,t);chosen[q]=-1;if(capped)break;
    }
    rollback();return;
   }
   const auto &w=dom[q][chosen[q]];for(int j=k-1;j>=0;j--)stack.push_back({w.sub[j],l-1});continue;
  }
  if(q/2!=h){rollback();return;}
  int turn=q%2?3:1,addr=(x+1024)*SZ+y+1024;
  if(x<=-1024||x>=1024||y<=-1024||y>=1024){cerr<<"GEOMETRY BOUND\n";exit(2);}
  if(board[addr]==turn){rollback();return;}
  undo.push_back({addr,board[addr]});board[addr]=turn;h=(h+turn)%4;x+=DX[h];y+=DY[h];t++;reads++;longest=max(longest,(long long)t);
 }
 if(t==CAP){survivors++;cout<<"SURVIVOR root "<<root<<" images";for(int q=0;q<8;q++)cout<<' '<<(chosen[q]<0?"UNASSIGNED":dom[q][chosen[q]].s);cout<<endl;}
 rollback();
}
int main(int argc,char**argv){
 if(argc>1)capnodes=stoll(argv[1]);if(argc>3)startordinal=stoi(argv[3]);ifstream f(argc>2?argv[2]:"rectangular_axis_turn_k13_domains.txt");f>>k>>a>>b;vector<string> base[4];
 for(int q=0;q<4;q++){int n;f>>n;while(n--){string w;f>>w;base[q].push_back(w);}}
 for(int q=0;q<8;q++)for(const auto&s:base[2*((q/2)%2)+q%2]){Word w;w.s=s;int h=q/2;for(char c:s){w.sub.push_back(2*h+(c=='L'));h=(h+(c=='L'?3:1))%4;}dom[q].push_back(w);}
 auto st=chrono::steady_clock::now();int depth=2;long long len=long(k)*k;while(len<CAP){depth+=2;len*=k*k;}
 for(root=0;root<4&&!capped;root++)for(int wi=0;wi<(int)dom[root].size();wi++){
  if(ordinal++<startordinal){completed++;continue;}
  fill(begin(chosen),end(chosen),-1);chosen[root]=wi;firststate=dom[root][wi].sub[0];search({{root,depth}},0,0,root/2,0);if(capped)break;completed++;cout<<"PROGRESS completed "<<completed<<" nodes "<<nodes<<" longest "<<longest<<" survivors "<<survivors<<endl;
 }
 cout<<"SUMMARY completed_root_images "<<completed<<" nodes "<<nodes<<" cap "<<capnodes<<" capped "<<capped<<" reads "<<reads<<" longest "<<longest<<" survivors "<<survivors<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;
}
