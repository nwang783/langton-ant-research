#include <bits/stdc++.h>
using namespace std;
struct Read{int x,y,c;};struct Macro{char name;int dx,dy,dh;vector<Read> a;};
struct Last{int c,owner;};vector<Macro> ms;unordered_map<uint64_t,Last> board;string path,best;mt19937_64 rng;long long seen=0,cap;int maxword=300,bestdepth=-1;
uint64_t key(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
pair<int,int> rot(int x,int y,int h){if(h==0)return{x,y};if(h==1)return{y,-x};if(h==2)return{-x,-y};return{-y,x};}
struct Undo{uint64_t k;bool present;Last old;};
bool stop=false; map<tuple<int,int,int>,int> poses; const int DX[4]={0,1,0,-1},DY[4]={1,0,-1,0}; tuple<int,int,int> cp(int x,int y,int h){return {2*x+DX[h]-DX[(h+1)%4],2*y+DY[h]-DY[(h+1)%4],h};}
void dfs(int x,int y,int h,int active,int maxdepth,int block){
 if(stop||++seen>cap){stop=true;return;}
 if(maxdepth>bestdepth){bestdepth=maxdepth;best=path;cout<<"DEPTH "<<bestdepth<<" macros "<<path.size()<<" nodes "<<seen<<" word "<<path<<endl;}
 if(false){cout<<"HEIGHT8 COUNTEREXAMPLE "<<path<<endl;stop=true;return;}
 if((int)path.size()>=maxword)return;
 array<int,5> ord={0,1,2,3,4};shuffle(ord.begin(),ord.end(),rng);
 for(int j:ord){auto&m=ms[j];int act=active,md=maxdepth;bool ok=true;vector<Undo> undo;
  for(auto&a:m.a){auto[dx,dy]=rot(a.x,a.y,h);auto k=key(x+dx,y+dy);auto it=board.find(k);bool exists=it!=board.end();Last old=exists?it->second:Last{-1,-1};
   if(old.c==a.c){ok=false;break;}undo.push_back({k,exists,old});
   if(a.c==0)board[k]={0,act};else{act=exists?old.owner+1:0;board[k]={1,-1};md=max(md,act);}
  }
  if(ok){auto[dx,dy]=rot(m.dx,m.dy,h);int nh=(h+m.dh)%4,nb=block+(m.name!='C');auto cc=cp(x+dx,y+dy,nh);path+=m.name;auto it=poses.find(cc);if(it!=poses.end()&&it->second!=nb){cout<<"ORIENTED CENTER RETURN "<<path<<endl;stop=true;}else{bool fresh=it==poses.end();if(fresh)poses[cc]=nb;dfs(x+dx,y+dy,nh,act,md,nb);if(fresh)poses.erase(cc);}path.pop_back();}
  for(auto it=undo.rbegin();it!=undo.rend();++it){if(it->present)board[it->k]=it->old;else board.erase(it->k);}
  if(stop)return;
 }
}
int main(int argc,char**argv){rng.seed(argc>1?stoull(argv[1]):1);cap=argc>2?stoll(argv[2]):1000000;maxword=argc>3?stoi(argv[3]):300;int count;cin>>count;while(count--){Macro m;int n;cin>>m.name>>m.dx>>m.dy>>m.dh>>n;while(n--){Read r;cin>>r.x>>r.y>>r.c;m.a.push_back(r);}ms.push_back(m);}poses[cp(0,0,0)]=0;dfs(0,0,0,0,0,0);cout<<"DONE nodes "<<seen<<" maximum "<<bestdepth<<" word "<<best<<endl;}
