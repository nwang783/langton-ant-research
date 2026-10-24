#include <bits/stdc++.h>
using namespace std;
struct Move{int x,y,c;};struct Macro{char name;int dx,dy,dh;vector<Move>a;};vector<Macro> ms;
using Key=uint64_t;unordered_map<Key,int> last;Key key(int x,int y){return (Key(uint32_t(x))<<32)|uint32_t(y);}pair<int,int>rot(int x,int y,int h){if(h==0)return {x,y};if(h==1)return {y,-x};if(h==2)return {-x,-y};return {-y,x};}
unsigned long long nodes=0,nodecap=10000000;int depthcap=100,fuelcap=1000;string path;mt19937_64 rng;bool stop=false;int maxdepth=0;long long trials[5]={0},badcount=0;int mins[5]={100,100,100,100,100};string minwords[5];
void dfs(int x,int y,int h,int fuel){
 if(++nodes>nodecap){stop=true;return;}if(path.size()>maxdepth){maxdepth=path.size();if(maxdepth%20==0)cout<<"DEPTH "<<maxdepth<<" fuel "<<fuel<<" nodes "<<nodes<<endl;}if(path.size()==depthcap)return;
 array<int,5> order={0,1,2,3,4};shuffle(order.begin(),order.end(),rng);
 for(int mi:order){auto&m=ms[mi];vector<pair<Key,int>>undo;bool ok=true;int f=fuel;bool bad=false;
  auto[fx,fy]=rot(m.name=='V'?1:0,2,h);auto fi=last.find(key(x+fx,y+fy));if(m.name!='C'&&fi!=last.end())bad=true;
  for(auto&a:m.a){auto[dx,dy]=rot(a.x,a.y,h);auto p=key(x+dx,y+dy);auto it=last.find(p);int old=it==last.end()?-1:it->second;if(old==a.c){ok=false;break;}if(old==-1&&a.c==1&&++f>fuelcap){ok=false;break;}undo.push_back({p,old});last[p]=a.c;}
  if(ok){trials[mi]++;path.push_back(m.name);if(f-fuel<mins[mi]){mins[mi]=f-fuel;minwords[mi]=path;cout<<"MINFUEL "<<m.name<<" "<<mins[mi]<<" "<<path<<endl;}if(m.name!='C' && f==fuel){cout<<"COUNTEREXAMPLE "<<path<<" fuel "<<f<<" nodes "<<nodes<<endl;stop=true;}
   if(!stop){auto[dx,dy]=rot(m.dx,m.dy,h);dfs(x+dx,y+dy,(h+m.dh)%4,f);}path.pop_back();}
  for(auto it=undo.rbegin();it!=undo.rend();++it){if(it->second==-1)last.erase(it->first);else last[it->first]=it->second;}if(stop)return;
 }
}
int main(int argc,char**argv){if(argc>1)rng.seed(stoull(argv[1]));if(argc>2)nodecap=stoull(argv[2]);if(argc>3)depthcap=stoi(argv[3]);if(argc>4)fuelcap=stoi(argv[4]);int n;cin>>n;while(n--){Macro z;int k;cin>>z.name>>z.dx>>z.dy>>z.dh>>k;while(k--){Move a;cin>>a.x>>a.y>>a.c;z.a.push_back(a);}ms.push_back(z);}last.reserve(20000);dfs(0,0,0,0);cout<<"FINISHED nodes "<<nodes<<" stopped "<<stop<<" maxdepth "<<maxdepth<<endl;for(int i=0;i<5;i++)cout<<ms[i].name<<" "<<trials[i]<<" minfuel "<<mins[i]<<" word "<<minwords[i]<<endl;}
