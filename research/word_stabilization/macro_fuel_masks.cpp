#include <bits/stdc++.h>
using namespace std;
struct Move{int x,y,c,fi=-1;};
struct Macro{char name;int dx,dy,dh;vector<Move> a;};
vector<Macro> ms;
map<char,map<unsigned,int>> masks;

unordered_map<long long,int> last;
long long key(int x,int y){return ((long long)x<<32)^(unsigned int)y;}
pair<int,int> rot(int x,int y,int h){if(h==0)return {x,y};if(h==1)return {y,-x};if(h==2)return {-x,-y};return {-y,x};}
long long nodes;int fuelcap,depthcap;string path,best;int minfuel[1001];string minword[1001];
void dfs(int x,int y,int h,int fuel){
 ++nodes;int n=path.size();if(fuel<minfuel[n]){minfuel[n]=fuel;minword[n]=path;}
 if(n>best.size()){best=path;cout<<"RECORD "<<nodes<<" depth "<<n<<" fuel "<<fuel<<" word "<<path<<endl;}
 if(n==depthcap)return;
 for(auto&m:ms){
  vector<pair<long long,int>> undo; bool ok=true;int f=fuel;unsigned mask=0;
  for(auto&a:m.a){auto[dx,dy]=rot(a.x,a.y,h);auto p=key(x+dx,y+dy);auto it=last.find(p);int old=it==last.end()?-1:it->second;if(old==a.c){ok=false;break;}if(old==-1&&a.c==1){if(a.fi>=0)mask|=1u<<a.fi;if(++f>fuelcap){ok=false;break;}}undo.push_back({p,old});last[p]=a.c;}
  if(ok){masks[m.name][mask]++;auto[dx,dy]=rot(m.dx,m.dy,h);path.push_back(m.name);dfs(x+dx,y+dy,(h+m.dh)%4,f);path.pop_back();}
  for(auto it=undo.rbegin();it!=undo.rend();++it){if(it->second==-1)last.erase(it->first);else last[it->first]=it->second;}
 }
}
int main(int argc,char**argv){fuelcap=argc>1?stoi(argv[1]):10;depthcap=argc>2?stoi(argv[2]):100;int m;cin>>m;while(m--){Macro z;int n;cin>>z.name>>z.dx>>z.dy>>z.dh>>n;while(n--){Move a;cin>>a.x>>a.y>>a.c;z.a.push_back(a);}int fi=0;set<pair<int,int>>seen;for(auto&a:z.a){if(!seen.count({a.x,a.y})&&a.c==1)a.fi=fi++;seen.insert({a.x,a.y});}ms.push_back(z);}fill(minfuel,minfuel+1001,INT_MAX);dfs(0,0,0,0);for(auto&[k,mp]:masks){cout<<"MASKS "<<k<<endl;for(auto&[mask,c]:mp)cout<<mask<<" "<<c<<endl;}cout<<"DONE nodes "<<nodes<<" maxdepth "<<best.size()<<" cap "<<depthcap<<endl;for(int i=1;i<=best.size();i++)cout<<"MIN "<<i<<" "<<minfuel[i]<<" "<<minword[i]<<endl;}
