#include<bits/stdc++.h>
using namespace std;using P=pair<int,int>;
P rot(P p,int h){while(h--)p={p.second,-p.first};return p;} P add(P a,P b){return{a.first+b.first,a.second+b.second};}
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};string names="DCV",words[]={"LLLLRLRRRR","LLLLRLRRRRLRRRR","LLLLRLRRRRLRRLRRRR"},marker="LLLLRLRRRRL";
struct Geo{map<P,int> req;set<P> odd;vector<P> ins,outs;P end;int dh;};Geo G[3];set<P> core;map<P,int> board;map<P,pair<int,int>>tokens;
struct Tr{map<P,int>first,last;set<P>odd;P end;int h;};
Tr tr(string w){Tr t;P p={0,0};int h=0;for(char c:w){int b=c=='L';if(t.last.count(p))assert(t.last[p]!=b);t.first.emplace(p,b);t.last[p]=b;if(t.odd.count(p))t.odd.erase(p);else t.odd.insert(p);h=(h+(b?3:1))%4;p={p.first+dx[h],p.second+dy[h]};}t.end=p;t.h=h;return t;}
long long nodes=0,cap;int dep,fuelcap,bestzero=-1,bestdepth=-1;bool stop=false,hit=false;string path;vector<int>fuels;mt19937 rng;bool randomize=false;
void dfs(P p,int h,int fuel,int zero){if(++nodes>cap){stop=true;return;}if(zero>bestzero){bestzero=zero;cout<<"ZERO_RECORD "<<zero<<" fuel "<<fuel<<" depth "<<path.size()<<" word "<<path<<endl;}if((int)path.size()>bestdepth){bestdepth=path.size();cout<<"DEPTH_RECORD "<<bestdepth<<" fuel "<<fuel<<" word "<<path<<endl;}if(path.size()==dep)return;array<int,3>order={0,1,2};if(randomize)shuffle(order.begin(),order.end(),rng);for(int a:order){auto &g=G[a];vector<pair<P,int>>bu;vector<pair<P,optional<pair<int,int>>>>tu;bool ok=true;int f=fuel;vector<pair<int,int>>parents;
 for(auto[z,b]:g.req){P q=add(p,rot(z,h));auto it=board.find(q);if(it!=board.end()){if(it->second!=b){ok=false;break;}}else{bu.push_back({q,-1});board[q]=b;f+=b;}}
 if(ok&&f<=fuelcap){for(P q:g.ins){q=add(p,rot(q,h));auto it=tokens.find(q);if(it==tokens.end())parents.push_back({-1,-1});else{parents.push_back(it->second);tu.push_back({q,it->second});tokens.erase(it);}}int roots=count(parents.begin(),parents.end(),pair<int,int>{-1,-1});assert(f-fuel==roots);
 for(P q:g.outs){q=add(p,rot(q,h));assert(!tokens.count(q));tu.push_back({q,nullopt});tokens[q]={a,(int)path.size()};}
 for(P q:g.odd){q=add(p,rot(q,h));assert(board.count(q));bu.push_back({q,board[q]});board[q]^=1;}
 path+=names[a];fuels.push_back(roots);
 if(a==2&&parents[0].first==2&&parents[1].first==2){cout<<"BOTH_V_SOURCE "<<path<<" fuel "<<f<<" parents "<<parents[0].second<<" "<<parents[1].second<<endl;stop=hit=true;}
 if(!stop)dfs(add(p,rot(g.end,h)),(h+g.dh)%4,f,roots?0:zero+1);
 fuels.pop_back();path.pop_back();}
 for(auto it=tu.rbegin();it!=tu.rend();++it){if(it->second)tokens[it->first]=*it->second;else tokens.erase(it->first);}for(auto it=bu.rbegin();it!=bu.rend();++it){if(it->second==-1)board.erase(it->first);else board[it->first]=it->second;}if(stop)return;}}
int main(int argc,char**argv){dep=stoi(argv[1]);fuelcap=stoi(argv[2]);cap=stoll(argv[3]);if(argc>4){rng.seed(stoi(argv[4]));randomize=true;}auto m=tr(marker);for(auto[q,c]:m.first){board[q]=c;if(c)core.insert(q);}for(int a=0;a<3;a++){auto r=tr(words[a]),t=tr(words[a]+marker);auto &g=G[a];g.req=t.first;g.odd=r.odd;g.end=r.end;g.dh=r.h;set<P>in,out,nc;for(P q:core)nc.insert(add(r.end,rot(q,r.h)));for(auto[q,c]:t.first)if(c)in.insert(q);out=in;for(P q:r.odd)if(out.count(q))out.erase(q);else out.insert(q);for(P q:core)in.erase(q);for(P q:nc)out.erase(q);for(P q:in){assert(!out.count(q));g.ins.push_back(q);}for(P q:out)g.outs.push_back(q);}dfs({0,0},0,5,0);cout<<"FINISH nodes "<<nodes<<" cap "<<(stop&&!hit)<<" hit "<<hit<<" zero "<<bestzero<<" depth "<<bestdepth<<endl;}
