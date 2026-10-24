// Independent literal least-gap checker for capped-C protected clauses.
#include <bits/stdc++.h>
using namespace std;
struct P{int x,y;bool operator<(const P&o)const{return tie(x,y)<tie(o.x,o.y);}bool operator==(const P&o)const{return x==o.x&&y==o.y;}};
P operator+(P a,P b){return{a.x+b.x,a.y+b.y};}P operator-(P a,P b){return{a.x-b.x,a.y-b.y};}P rot(P p,int h){for(int j=0;j<(h%4+4)%4;j++)p={p.y,-p.x};return p;}const P dir[4]={{0,1},{1,0},{0,-1},{-1,0}};
struct Cell{int first,last,count;};struct Trace{map<P,Cell> cells;vector<pair<P,int>> events;P end;int heading=0;bool valid=true;};
Trace trace(string s){Trace t;t.end={0,0};for(char ch:s){int b=ch=='L';auto it=t.cells.find(t.end);if(it==t.cells.end())t.cells[t.end]={b,b,1};else{if(it->second.last==b)t.valid=false;it->second.last=b;it->second.count++;}t.events.push_back({t.end,b});t.heading=(t.heading+(b?3:1))%4;t.end=t.end+dir[t.heading];}return t;}
using B=tuple<int,int,int,int,int>;using K=tuple<int,int,int,int,int,int,int>;using CK=tuple<int,int,int,int,int,int,int,int>;
struct Row{int a,b,h,k,kind;P p,q,x,y;};struct Reader{int a,h;P p;};
int main(int argc,char**argv){try{
 if(argc!=6)throw runtime_error("literal ordinary protected counted output");ifstream f(argv[1]);int n;f>>n;assert(n==8);vector<string>w(n),ext(n);vector<Trace>raw,ctx;int cs[8]={0,1,0,1,2,0,1,2};
 for(int a=0;a<n;a++){f>>w[a]>>ext[a];raw.push_back(trace(w[a]));ctx.push_back(trace(w[a]+ext[a]));if(!raw.back().valid||!ctx.back().valid)throw runtime_error("invalid literal");}
 vector<vector<int>>after(n),before(n);for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(trace(w[a]+w[b]+ext[b]).valid){after[a].push_back(b);before[b].push_back(a);}
 set<B>ordinary;set<K>base;set<CK>relation;vector<Row>rows;string line;
 ifstream of(argv[2]);while(getline(of,line)){if(line.empty())continue;istringstream s(line);int a,b,x,y,h;s>>a>>b>>x>>y>>h;ordinary.emplace(a,b,x,y,h);}
 ifstream pf(argv[3]);while(getline(pf,line)){if(line.empty())continue;istringstream s(line);int a,b,x,y,h,qx,qy;s>>a>>b>>x>>y>>h>>qx>>qy;base.emplace(a,b,x,y,h,qx,qy);}
 ifstream cf(argv[4]);while(getline(cf,line)){istringstream s(line);Row r;s>>r.a>>r.b>>r.p.x>>r.p.y>>r.h>>r.q.x>>r.q.y>>r.k>>r.kind>>r.x.x>>r.x.y>>r.y.x>>r.y.y;if(!s||r.a<0||r.a>=n||r.b<0||r.b>=n||r.h<0||r.h>=4||r.k<0||r.k>4)throw runtime_error("row");if(!relation.emplace(r.a,r.b,r.p.x,r.p.y,r.h,r.q.x,r.q.y,r.k).second)throw runtime_error("duplicate");rows.push_back(r);}
 auto cap=[](int k){return min(k,4);};
 auto count_possible=[&](int a,int h,int k){return k==4||(k>=cs[a]&&(k+h)%4==0);};
 auto geometry_possible=[&](int a,P p,int h,int k){if(k==4)return true;int r=k-cs[a];if(r<0)return false;if(r>=2)return true;P target={2*p.x,2*p.y};target=target+rot({-1,-1},h);P exit={2*raw[a].end.x,2*raw[a].end.y};exit=exit+rot({-1,-1},raw[a].heading);P diff=rot(target-exit,-raw[a].heading);if(diff.x%2||diff.y%2)return false;int x=diff.x/2,y=diff.y/2;if(r==0)return x>=0&&y>=x&&(x+y)%2==0&&(x!=0||y%4==0);int X=x-1,Y=y-1;return Y>=0&&X<=Y&&(X+Y)%2==0&&(Y!=0||X%4==0);};
 auto has=[&](int a,int b,P p,int h,P q,int k){return !count_possible(a,h,k)||!geometry_possible(a,p,h,k)||ordinary.count({a,b,p.x,p.y,h})||base.count({a,b,p.x,p.y,h,q.x,q.y})||relation.count({a,b,p.x,p.y,h,q.x,q.y,k});};
 auto normalized=[&](int a,P p,int h,int b,P z,int j,P q,int k){return has(a,b,rot(z-p,-h),(j-h+4)%4,rot(q-p,-h),k);};
 auto avoids=[&](int a,P p,int h,P q){return !ctx[a].cells.count(rot(q-p,-h));};
 auto black_possible=[&](int a,int b,P p,int h,P q){auto u=raw[a].cells.find(q),v=ctx[b].cells.find(rot(q-p,-h));return (u==raw[a].cells.end()||u->second.last==0)&&(v==ctx[b].cells.end()||v->second.first==1);};
 long long shortchecks=0;
 for(int a=0;a<n;a++)for(int b:after[a]){P p=raw[a].end;int h=raw[a].heading;for(auto r:rows)if(r.a==a&&r.b==b&&r.p==p&&r.h==h&&r.k==cs[a]){shortchecks++;if(black_possible(a,b,p,h,r.q))throw runtime_error("gap one");}
 for(int c:after[b])if(trace(w[a]+w[b]+w[c]+ext[c]).valid){P z=p+rot(raw[b].end,h);int j=(h+raw[b].heading)%4;for(auto r:rows)if(r.a==a&&r.b==c&&r.p==z&&r.h==j&&r.k==cap(cs[a]+cs[b])){shortchecks++;if(black_possible(a,c,z,j,r.q)&&avoids(b,p,h,r.q))throw runtime_error("gap two");}}}
 map<P,vector<Reader>>cache;auto readers=[&](P x)->const vector<Reader>&{auto it=cache.find(x);if(it!=cache.end())return it->second;vector<Reader>rs;for(int a=0;a<n;a++)for(int h=0;h<4;h++)for(auto [z,c]:raw[a].cells){P p=x-rot(z,h);if((p.x+p.y-h)%2==0)rs.push_back({a,h,p});}return cache.emplace(x,move(rs)).first->second;};
 long long kinds[5]={},options=0,transitions=0;
 for(auto r:rows){if(r.kind<1||r.kind>4)throw runtime_error("kind");kinds[r.kind]++;
 if(r.kind==3){if(count_possible(r.a,r.h,r.k)&&geometry_possible(r.a,r.p,r.h,r.k))throw runtime_error("bad kinematic exclusion");}
 else if(r.kind==1){P pc=raw[r.a].end;int hc=raw[r.a].heading;for(int c:after[r.a])for(int d:before[r.b]){int hd=(r.h-raw[d].heading+4)%4;P pd=r.p-rot(raw[d].end,hd);if(!avoids(c,pc,hc,r.q)||!avoids(d,pd,hd,r.q))continue;for(int u=0;u<=4;u++){if(cap(cs[r.a]+u+cs[d])!=r.k)continue;options++;if(!has(r.a,d,pd,hd,r.q,cap(cs[r.a]+u))&&!normalized(c,pc,hc,r.b,r.p,r.h,r.q,cap(u+cs[d]))&&!normalized(c,pc,hc,d,pd,hd,r.q,u))throw runtime_error("neighbor");}}}
 else if(r.kind==2){auto u=raw[r.a].cells.find(r.x),v=ctx[r.b].cells.find(rot(r.x-r.p,-r.h));if(u==raw[r.a].cells.end()||v==ctx[r.b].cells.end()||u->second.last!=v->second.first)throw runtime_error("barrier");for(auto s:readers(r.x)){auto cc=raw[s.a].cells.at(rot(r.x-s.p,-s.h));if(cc.count%2==0||cc.first==u->second.last||!avoids(s.a,s.p,s.h,r.q))continue;for(int k=0;k<=4;k++)for(int l=0;l<=4;l++)if(cap(k+l)==r.k){options++;if(!has(r.a,s.a,s.p,s.h,r.q,k)&&!normalized(s.a,s.p,s.h,r.b,r.p,r.h,r.q,l))throw runtime_error("odd reader");}}}
 else{if(r.x==r.y)throw runtime_error("equal cells");P cells[2]={r.x,r.y};int start=0,goal=0;for(int j=0;j<2;j++){auto u=raw[r.a].cells.find(cells[j]),v=ctx[r.b].cells.find(rot(cells[j]-r.p,-r.h));if(u==raw[r.a].cells.end()||v==ctx[r.b].cells.end())throw runtime_error("missing color");start|=(1-u->second.last)<<j;goal|=v->second.first<<j;}uint32_t graph[20]={};for(int k=0;k<4;k++)for(int c=0;c<4;c++)graph[4*k+c]|=1U<<(4*(k+1)+c);
 set<tuple<int,int,int,int>>used;for(P x:cells)for(auto s:readers(x)){if(!used.emplace(s.a,s.p.x,s.p.y,s.h).second||!avoids(s.a,s.p,s.h,r.q))continue;for(int k=0;k<=4;k++){if(has(r.a,s.a,s.p,s.h,r.q,k))continue;bool possible=false;for(int l=0;l<=4;l++)if(cap(k+l)==r.k&&!normalized(s.a,s.p,s.h,r.b,r.p,r.h,r.q,l))possible=true;if(!possible)continue;options++;for(int color=0;color<4;color++){int next=color;bool ok=true;for(auto [z,bit]:raw[s.a].events){P p=s.p+rot(z,s.h);for(int j=0;j<2;j++)if(p==cells[j]){if(((next>>j)&1)!=bit){ok=false;break;}next^=1<<j;}if(!ok)break;}if(ok){graph[4*k+color]|=1U<<(4*cap(k+cs[s.a])+next);transitions++;}}}}
 uint32_t reach=1U<<(4*cs[r.a]+start);for(int i=0;i<20;i++)for(int v=0;v<20;v++)if(reach&(1U<<v))reach|=graph[v];if(reach&(1U<<(4*r.k+goal)))throw runtime_error("two-cell reachable");}
 }
 ofstream out(argv[5]);out<<"{\"status\":\"PASS independent counted protected least-gap replay\",\"clauses\":"<<rows.size()<<",\"ordinary\":"<<ordinary.size()<<",\"protected_base\":"<<base.size()<<",\"short_checks\":"<<shortchecks<<",\"neighbor\":"<<kinds[1]<<",\"odd_reader\":"<<kinds[2]<<",\"kinematic\":"<<kinds[3]<<",\"two_cell\":"<<kinds[4]<<",\"options\":"<<options<<",\"literal_transitions\":"<<transitions<<"}\n";cout<<"PASS "<<rows.size()<<" clauses\n";
 }catch(exception&e){cerr<<"FAIL "<<e.what()<<'\n';return 1;}}
