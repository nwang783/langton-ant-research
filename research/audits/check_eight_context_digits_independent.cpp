#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
// This search resolves each next read directly from its four base-13 digits,
// not from the author's recursive expansion stack. The domain was regenerated
// independently from every literal turn word using current colors.
struct Image{string word;array<int,13> state;};
vector<Image> domain[8];int chosen[8];int root,first;
constexpr int SIDE=8192,CENTER=4096,LIMIT=3000;
int8_t colors[SIDE*SIDE]; // 0 unassigned; 1 current white; 2 current black
int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
uint64_t tries=0,readcount=0,rejected=0,survivors=0;int longest=0;
vector<array<int,4>> digits;
void search(int time,int x,int y,int heading){
 vector<pair<int,int8_t>> undo;
 auto rollback=[&](){for(auto it=undo.rbegin();it!=undo.rend();++it)colors[it->first]=it->second;};
 while(time<LIMIT){
  int q=root;
  for(int depth=0;depth<4;depth++){
   if(chosen[q]<0){
    for(int w=0;w<int(domain[q].size());w++){
     if(q==first && domain[q][w].state[0]!=root)continue;
     tries++;chosen[q]=w;search(time,x,y,heading);chosen[q]=-1;
    }
    rollback();return;
   }
   q=domain[q][chosen[q]].state[digits[time][depth]];
  }
  if(q/2!=heading){rejected++;rollback();return;}
  int bit=q%2;int index=(x+CENTER)*SIDE+y+CENTER;int8_t old=colors[index];
  if(old!=0 && old!=bit+1){rejected++;rollback();return;}
  undo.push_back({index,old});colors[index]=2-bit;
  heading=(heading+(bit?3:1))%4;x+=dx[heading];y+=dy[heading];
  time++;readcount++;if(time>longest)longest=time;
 }
 survivors++;cout<<"SURVIVOR root "<<root<<endl;rollback();
}
int main(int argc,char**argv){
 if(argc!=2)return 2;ifstream in(argv[1]);int k,a,b;in>>k>>a>>b;if(k!=13||a!=3||b!=5)return 2;
 vector<string> base[4];
 for(auto &v:base){int count;in>>count;while(count--){string s;in>>s;v.push_back(s);}}
 for(int q=0;q<8;q++)for(auto s:base[(q/2%2)*2+q%2]){
  Image im;im.word=s;int h=q/2;
  for(int i=0;i<13;i++){im.state[i]=2*h+(s[i]=='L');h=(h+(s[i]=='L'?3:1))%4;}
  domain[q].push_back(im);
 }
 for(int t=0;t<LIMIT;t++)digits.push_back({t/2197,(t/169)%13,(t/13)%13,t%13});
 auto start=chrono::steady_clock::now();int completed=0;
 for(root=0;root<4;root++)for(int w=0;w<int(domain[root].size());w++){
  fill(begin(chosen),end(chosen),-1);chosen[root]=w;first=domain[root][w].state[0];search(0,0,0,root/2);completed++;
  cout<<"ROOT "<<completed<<" state "<<root<<" word "<<domain[root][w].word<<" tries "<<tries<<" reads "<<readcount<<" rejected "<<rejected<<" longest "<<longest<<" survivors "<<survivors<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<endl;
 }
 cout<<"COMPLETE roots "<<completed<<" tries "<<tries<<" reads "<<readcount<<" rejected "<<rejected<<" longest "<<longest<<" survivors "<<survivors<<endl;
}
