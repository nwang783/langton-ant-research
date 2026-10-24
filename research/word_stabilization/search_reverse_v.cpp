#include <bits/stdc++.h>
using namespace std;
struct Read {int x,y; char c;};
struct Macro {char name; string word; vector<Read> tr; int dx,dy,dh;};
struct Pose {int x,y,h;};
vector<Macro> macros;
unordered_map<uint64_t,char> firstread;
uint64_t key(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
pair<int,int> rot(int x,int y,int h){switch(h&3){case 0:return{x,y};case 1:return{y,-x};case 2:return{-x,-y};default:return{-y,x};}}
vector<pair<uint64_t,char>> undo_log;
mt19937_64 rng;
long long total=0,remaining=0;int maxdepth=80,cap=200,maxseen=0;string revword;bool found=false;int fuel_now=0;
const uint64_t goal=key(1,2);
Macro make(char name,string word){Macro m{name,word,{},0,0,0};int x=0,y=0,h=0;int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};for(char c:word){m.tr.push_back({x,y,c});h=(h+(c=='R'?1:3))%4;x+=dx[h];y+=dy[h];}m.dx=x;m.dy=y;m.dh=h;return m;}
bool prepend(const Macro&m,Pose cur,Pose&pre,bool&touch){pre.h=(cur.h-m.dh+4)%4;auto[d,e]=rot(m.dx,m.dy,pre.h);pre.x=cur.x-d;pre.y=cur.y-e;touch=false;for(auto it=m.tr.rbegin();it!=m.tr.rend();++it){auto[x,y]=rot(it->x,it->y,pre.h);uint64_t p=key(pre.x+x,pre.y+y);auto old=firstread.find(p);if(old!=firstread.end()&&old->second==it->c)return false;char oldc=old==firstread.end()?char(0):old->second;undo_log.push_back({p,oldc});fuel_now+=(it->c=='L')-(oldc=='L');firstread[p]=it->c;if(p==goal)touch=true;}return true;}
void undo(size_t mark){while(undo_log.size()>mark){auto[p,c]=undo_log.back();undo_log.pop_back();fuel_now+=(c=='L')-(firstread[p]=='L');if(c)firstread[p]=c;else firstread.erase(p);}}
void dfs(Pose cur,int dep){if(found||remaining<=0)return;--remaining;++total;maxseen=max(maxseen,dep);if(dep>=maxdepth)return;vector<pair<double,int>> choices;for(int i=0;i<5;i++){auto&m=macros[i];int h=(cur.h-m.dh+4)%4;auto[dx,dy]=rot(m.dx,m.dy,h);int x=cur.x-dx,y=cur.y-dy;double noise=double(rng()%10000)/1000.0;double score=0.12*(abs(x-1)+abs(y-2))+noise;choices.push_back({score,i});}sort(choices.begin(),choices.end());for(auto [score,i]:choices){if(remaining<=0||found)break;size_t mark=undo_log.size();Pose pre;bool touch;bool ok=prepend(macros[i],cur,pre,touch);if(ok){int fuel=fuel_now;if(fuel<=cap){revword.push_back(macros[i].name);if(touch){found=true;string w=revword;reverse(w.begin(),w.end());w+='V';cout<<"FOUND "<<w<<" fuel "<<fuel<<" depth "<<dep+2<<" pose "<<pre.x<<","<<pre.y<<","<<pre.h<<"\n"<<flush;}else dfs(pre,dep+1);revword.pop_back();}}undo(mark);}}
int main(int argc,char**argv){
macros.push_back(make('C',"LLLLRLRRRRLRRRR"));
macros.push_back(make('U',"LLLLRLRRRRLRLLLLRRRRLRRLRRRR"));
macros.push_back(make('V',"LLLLRLRRRRLRRLRRRR"));
macros.push_back(make('Q',"LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRRLRRRR"));
macros.push_back(make('B',"LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR"));
int runs=argc>1?stoi(argv[1]):100;long long budget=argc>2?stoll(argv[2]):100000;maxdepth=argc>3?stoi(argv[3]):80;cap=argc>4?stoi(argv[4]):200;firstread.reserve(5000);auto &v=macros[2];for(auto it=v.tr.rbegin();it!=v.tr.rend();++it)firstread[key(it->x,it->y)]=it->c;for(auto[p,c]:firstread)fuel_now+=(c=='L');for(int run=0;run<runs&&!found;run++){rng.seed(0x712abefULL+run*1987231ULL);remaining=budget;dfs({0,0,0},0);if(run%10==0)cout<<"RUN "<<run<<" nodes "<<total<<" maxdepth "<<maxseen<<"\n"<<flush;}cout<<"DONE nodes "<<total<<" found "<<found<<" maxdepth "<<maxseen<<"\n";}
