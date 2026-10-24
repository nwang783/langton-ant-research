// Targeted eight-pair context synthesis, common last map (N,W,S,W).
// Finite-prefix survivors require the exact all-time matrix verifier.
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <string>
#include <cstdint>
#include <chrono>
#include <map>
using namespace std;
struct Word{string s;vector<int> sub;};vector<Word> dom[8];int chosen[8],k=13;
int lastmap[4]={0,3,2,3};const int DX[]={0,1,0,-1},DY[]={1,0,-1,0};
long long nodes=0,capnodes=1000000,reads=0,longest=0,survivors=0;int CAP=3000;bool capped=false;map<pair<int,int>,int> board;
int qid(int h,int d){return 2*h+(((d-h+4)%4)==3);}
void search(vector<pair<int,int>> stack,int x,int y,int h,int t){
 if(capped)return;vector<pair<pair<int,int>,int>> undo;
 auto rollback=[&](){for(auto i=undo.rbegin();i!=undo.rend();++i){if(i->second)board[i->first]=i->second;else board.erase(i->first);}};
 while(!stack.empty()&&t<CAP){
  auto [q,l]=stack.back();stack.pop_back();
  if(l){
   if(chosen[q]<0){for(int wi=0;wi<(int)dom[q].size();wi++){
    if(++nodes>capnodes){capped=true;break;}chosen[q]=wi;auto copy=stack;for(int j=k-1;j>=0;j--)copy.push_back({dom[q][wi].sub[j],l-1});search(move(copy),x,y,h,t);chosen[q]=-1;if(capped)break;
   }rollback();return;}
   for(int j=k-1;j>=0;j--)stack.push_back({dom[q][chosen[q]].sub[j],l-1});continue;
  }
  if(q/2!=h){rollback();return;}int turn=q%2?3:1;auto v=make_pair(x,y);auto it=board.find(v);int old=it==board.end()?0:it->second;
  if(old==turn){rollback();return;}undo.push_back({v,old});board[v]=turn;h=(h+turn)%4;x+=DX[h];y+=DY[h];t++;reads++;longest=max(longest,(long long)t);
 }
 if(t==CAP){survivors++;cout<<"SURVIVOR images";for(int q=0;q<8;q++)cout<<' '<<(chosen[q]<0?"UNASSIGNED":dom[q][chosen[q]].s);cout<<endl;}
 rollback();
}
int main(int argc,char**argv){
 if(argc>1)capnodes=stoll(argv[1]);if(argc>3)CAP=stoi(argv[3]);ifstream f(argv[2]);int a,b;f>>k>>a>>b;vector<string> base[4];for(int d=0;d<4;d++){int n;f>>n;while(n--){string s;f>>s;base[d].push_back(s);}}
 for(int h=0;h<4;h++)for(int c:{1,3}){int d=(h+c)%4,q=qid(h,d);for(auto s:base[d])if(s.back()-'0'==lastmap[d]){Word w;w.s=s;int prev=lastmap[h];for(char ch:s){int dd=ch-'0';w.sub.push_back(qid(prev,dd));prev=dd;}dom[q].push_back(w);}}
 cout<<"DOMAINS";for(auto&v:dom)cout<<' '<<v.size();cout<<endl;
 int completed=0,roots=0;int depth=1,len=k;while(len<CAP){depth++;len*=k;}auto st=chrono::steady_clock::now();
 for(int wi=0;wi<(int)dom[0].size()&&!capped;wi++)if(dom[0][wi].s[0]=='1'){
  roots++;fill(begin(chosen),end(chosen),-1);chosen[0]=wi;search({{0,depth}},0,0,0,0);if(!capped)completed++;
 }
 cout<<"ROOTS completed "<<completed<<" started "<<roots<<endl;
 cout<<"SUMMARY nodes "<<nodes<<" cap "<<capnodes<<" capped "<<capped<<" reads "<<reads<<" longest "<<longest<<" survivors "<<survivors<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;
}
