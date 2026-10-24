// Independent proof checker. Input is literal owned words, actual right contexts,
// and an overapproximating allowed successor graph. No discovery-engine imports.
#include <bits/stdc++.h>
using namespace std;
struct P {int x,y; bool operator<(const P&o)const{return tie(x,y)<tie(o.x,o.y);} bool operator==(const P&o)const{return x==o.x&&y==o.y;} };
P operator+(P a,P b){return{a.x+b.x,a.y+b.y};} P operator-(P a,P b){return{a.x-b.x,a.y-b.y};}
P rot(P p,int h){h=(h%4+4)%4;while(h--){p={p.y,-p.x};}return p;}
const P dirs[4]={{0,1},{1,0},{0,-1},{-1,0}};
struct Cell{int first,last,n,phase;};
struct Trace{map<P,Cell> cells;vector<pair<P,int>> visits;P end;int h;bool good;};
Trace trace(const string&w){Trace t;t.end={0,0};t.h=0;t.good=true;int i=0;for(char c:w){int bit=c=='L';auto it=t.cells.find(t.end);if(it==t.cells.end())t.cells[t.end]={bit,bit,1,i};else{if(it->second.last==bit)t.good=false;it->second.last=bit;it->second.n++;}t.visits.push_back({t.end,bit});t.h=(t.h+(bit?3:1))%4;t.end=t.end+dirs[t.h];i++;}return t;}
struct Reader{int c,h;P p;int first,last,n;};
using K=tuple<int,int,int,int,int,int,int>;
using B=tuple<int,int,int,int,int>;
int main(int argc,char**argv){try{
 if(argc!=5)throw runtime_error("literal input, ordinary certificate, protected certificate, output");
 ifstream f(argv[1]);int n;f>>n;vector<string>w(n),ext(n);vector<Trace>raw,tar;
 for(int i=0;i<n;i++){f>>w[i]>>ext[i];raw.push_back(trace(w[i]));tar.push_back(trace(w[i]+ext[i]));if(!raw.back().good||!tar.back().good)throw runtime_error("own literal conflict");}
 int count;f>>count;set<pair<int,int>>gp;while(count--){int a,b;f>>a>>b;if(trace(w[a]+w[b]+ext[b]).good)gp.insert({a,b});}
 vector<vector<int>>out(n),in(n);for(auto[a,b]:gp){out[a].push_back(b);in[b].push_back(a);}
 set<B>base;string line;ifstream bf(argv[2]);while(getline(bf,line)){istringstream s(line);int a,b,x,y,h;s>>a>>b>>x>>y>>h;base.emplace(a,b,x,y,h);}
 struct Row{int a,b,h,kind;P p,q,x,y;};vector<Row>rows;set<K>relation;ifstream cf(argv[3]);
 while(getline(cf,line)){istringstream s(line);Row r;s>>r.a>>r.b>>r.p.x>>r.p.y>>r.h>>r.q.x>>r.q.y>>r.kind>>r.x.x>>r.x.y>>r.y.x>>r.y.y;if(!s||r.a<0||r.b<0||r.a>=n||r.b>=n||r.h<0||r.h>3||(r.p.x+r.p.y-r.h)%2)throw runtime_error("bad row");if(!relation.emplace(r.a,r.b,r.p.x,r.p.y,r.h,r.q.x,r.q.y).second)throw runtime_error("duplicate");rows.push_back(r);}
 auto blackok=[&](int a,int b,P p,int h,P q){auto x=raw[a].cells.find(q),y=tar[b].cells.find(rot(q-p,-h));return(x==raw[a].cells.end()||x->second.last==0)&&(y==tar[b].cells.end()||y->second.first==1);};
 auto avoids=[&](int a,P p,int h,P q){return tar[a].cells.count(rot(q-p,-h))==0;};
 auto has=[&](int a,int b,P p,int h,P q){return base.count(B(a,b,p.x,p.y,h))||relation.count(K(a,b,p.x,p.y,h,q.x,q.y));};
 auto normalized=[&](int a,P p,int h,int b,P r,int k,P q){return has(a,b,rot(r-p,-h),(k-h+4)%4,rot(q-p,-h));};
 // Complete literal adjacent/triple controls, not the discovery grammar lists.
 long long shorttests=0;for(auto[a,b]:gp){P p=raw[a].end;int h=raw[a].h;for(auto&r:rows)if(r.a==a&&r.b==b&&r.p==p&&r.h==h){shorttests++;if(blackok(a,b,p,h,r.q))throw runtime_error("realized gap1");}
  for(int c:out[b])if(trace(w[a]+w[b]+w[c]+ext[c]).good){P p2=p+rot(raw[b].end,h);int h2=(h+raw[b].h)%4;for(auto&r:rows)if(r.a==a&&r.b==c&&r.p==p2&&r.h==h2){shorttests++;if(blackok(a,c,p2,h2,r.q)&&avoids(b,p,h,r.q))throw runtime_error("realized gap2");}}}
 map<P,vector<Reader>>cache;auto readers=[&](P q)->const vector<Reader>&{auto i=cache.find(q);if(i!=cache.end())return i->second;vector<Reader>v;for(int a=0;a<n;a++)for(int h=0;h<4;h++)for(auto[z,c]:raw[a].cells){P p=q-rot(z,h);if((p.x+p.y-h)%2==0)v.push_back({a,h,p,c.first,c.last,c.n});}return cache.emplace(q,move(v)).first->second;};
 long long kinds[5]={}, options=0, transitions=0;int index=0;
 for(auto r:rows){index++;if(r.kind<1||r.kind>4)throw runtime_error("unknown rule");kinds[r.kind]++;
  auto discharge=[&](Reader s){return !avoids(s.c,s.p,s.h,r.q)||has(r.a,s.c,s.p,s.h,r.q)||normalized(s.c,s.p,s.h,r.b,r.p,r.h,r.q);};
  if(r.kind==3){if(blackok(r.a,r.b,r.p,r.h,r.q))throw runtime_error("false black contradiction");}
  else if(r.kind==1){P pc=raw[r.a].end;int hc=raw[r.a].h;for(int c:out[r.a])for(int d:in[r.b]){int hd=(r.h-raw[d].h+4)%4;P pd=r.p-rot(raw[d].end,hd);options++;if(!avoids(c,pc,hc,r.q)||!avoids(d,pd,hd,r.q))continue;if(!has(r.a,d,pd,hd,r.q)&&!normalized(c,pc,hc,r.b,r.p,r.h,r.q)&&!normalized(c,pc,hc,d,pd,hd,r.q))throw runtime_error("neighbor row "+to_string(index));}}
  else if(r.kind==2){auto a=raw[r.a].cells.find(r.x),b=tar[r.b].cells.find(rot(r.x-r.p,-r.h));if(a==raw[r.a].cells.end()||b==tar[r.b].cells.end()||a->second.last!=b->second.first)throw runtime_error("unequal barrier");int bit=a->second.last;for(auto s:readers(r.x)){if(s.n%2==0||s.first==bit)continue;options++;if(s.first!=s.last||!discharge(s))throw runtime_error("odd reader row "+to_string(index));}}
  else{if(r.x==r.y)throw runtime_error("duplicate color cells");P q[2]={r.x,r.y};int start=0,goal=0;for(int j=0;j<2;j++){auto a=raw[r.a].cells.find(q[j]),b=tar[r.b].cells.find(rot(q[j]-r.p,-r.h));if(a==raw[r.a].cells.end()||b==tar[r.b].cells.end())throw runtime_error("missing color cell");start|=(1-a->second.last)<<j;goal|=b->second.first<<j;}int graph[4]={};
   for(int j=0;j<2;j++)for(auto s:readers(q[j])){options++;if(discharge(s))continue;for(int v=0;v<4;v++){int state=v;bool ok=true;for(auto[z,bit]:raw[s.c].visits){P a=s.p+rot(z,s.h);for(int k=0;k<2;k++)if(a==q[k]){if(((state>>k)&1)!=bit){ok=false;break;}state^=1<<k;}if(!ok)break;}if(ok){graph[v]|=1<<state;transitions++;}}}
   int reach=1<<start;for(int k=0;k<4;k++)for(int v=0;v<4;v++)if(reach&(1<<v))reach|=graph[v];if(reach&(1<<goal))throw runtime_error("reachable two-cell target row "+to_string(index));
  }
 }
 ofstream o(argv[4]);o<<"{\"status\":\"PASS independent protected least-gap replay\",\"clauses\":"<<rows.size()<<",\"ordinary_clauses\":"<<base.size()<<",\"short_tests\":"<<shorttests<<",\"neighbor\":"<<kinds[1]<<",\"odd_reader\":"<<kinds[2]<<",\"direct_black\":"<<kinds[3]<<",\"two_cell\":"<<kinds[4]<<",\"options\":"<<options<<",\"literal_color_transitions\":"<<transitions<<"}\n";cout<<"PASS "<<rows.size()<<" protected clauses\n";
 }catch(exception&e){cerr<<"FAIL: "<<e.what()<<'\n';return 1;}}
