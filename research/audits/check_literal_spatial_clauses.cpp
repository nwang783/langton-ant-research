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
int main(int argc,char**argv){try{if(argc!=5)throw runtime_error("usage: checker literal_input certificate marks output");ifstream in(argv[1]);int n;in>>n;vector<string>w(n),ext(n);vector<Trace>raw,tar;for(int a=0;a<n;a++){in>>w[a]>>ext[a];raw.push_back(trace(w[a]));tar.push_back(trace(w[a]+ext[a]));if(!raw.back().good||!tar.back().good)throw runtime_error("invalid own word");}
 int np;in>>np;vector<vector<int>>outs(n),ins(n);set<pair<int,int>> gp;for(int i=0;i<np;i++){int a,b;in>>a>>b;if(trace(w[a]+w[b]+ext[b]).good)gp.insert({a,b});}for(auto[a,b]:gp){outs[a].push_back(b);ins[b].push_back(a);}
 const int B=32,W=64;size_t size=(size_t)W*W*4*n*n;vector<uint64_t>S((size+63)/64);long long num=0;
 auto idx=[&](int a,int b,P p,int h)->size_t{if(a<0||a>=n||b<0||b>=n||h<0||h>=4||p.x< -B||p.x>=B||p.y< -B||p.y>=B)return size;return ((((size_t)(p.x+B)*W+p.y+B)*4+h)*n+a)*n+b;};
 auto has=[&](int a,int b,P p,int h){size_t k=idx(a,b,p,h);return k<size&&((S[k/64]>>(k%64))&1);};
 auto normhas=[&](int a,P p,int h,int b,P q,int k){return has(a,b,rot(q-p,-h),(k-h+4)%4);};
 string line;ifstream cert(argv[2]);while(getline(cert,line)){istringstream ss(line);int a,b,x,y,h,kind;ss>>a>>b>>x>>y>>h>>kind;size_t k=idx(a,b,{x,y},h);if(!ss||k==size||has(a,b,{x,y},h)||((x+y-h)%2)!=0)throw runtime_error("bad key");S[k/64]|=1ULL<<(k%64);num++;}cert.close();
 long long shorts=0,triples=0;for(auto[a,b]:gp){if(has(a,b,raw[a].end,raw[a].h))throw runtime_error("gap one");shorts++;for(int c:outs[b])if(trace(w[a]+w[b]+w[c]+ext[c]).good){P p=raw[a].end+rot(raw[b].end,raw[a].h);int h=(raw[a].h+raw[b].h)%4;if(has(a,c,p,h))throw runtime_error("gap two");triples++;}}
 map<P,vector<Reader>>cache;auto readers=[&](P q)->const vector<Reader>&{auto it=cache.find(q);if(it!=cache.end())return it->second;vector<Reader>v;for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto[z,cell]:raw[c].cells){P p=q-rot(z,h);if((p.x+p.y-h)%2==0)v.push_back({c,h,p,cell.first,cell.last,cell.n});}return cache.emplace(q,move(v)).first->second;};
 long long counts[4]={0},nr=0,nn=0,transitions=0;cert.open(argv[2]);long long row=0;while(getline(cert,line)){row++;istringstream ss(line);int a,b,h,kind;P p,q[2];ss>>a>>b>>p.x>>p.y>>h>>kind>>q[0].x>>q[0].y;ss>>q[1].x>>q[1].y;if(kind<1||kind>3)throw runtime_error("unknown rule");counts[kind]++;
 if(kind==1){P pc=raw[a].end;int hc=raw[a].h;for(int c:outs[a])for(int d:ins[b]){int hd=(h-raw[d].h+4)%4;P pd=p-rot(raw[d].end,hd);nn++;if(!has(a,d,pd,hd)&&!normhas(c,pc,hc,b,p,h)&&!normhas(c,pc,hc,d,pd,hd))throw runtime_error("neighbor row "+to_string(row));}}
 else if(kind==2){auto sa=raw[a].cells.find(q[0]);auto tb=tar[b].cells.find(rot(q[0]-p,-h));if(sa==raw[a].cells.end()||tb==tar[b].cells.end()||sa->second.last!=tb->second.first)throw runtime_error("barrier mismatch");int letter=sa->second.last;for(auto r:readers(q[0])){if(r.n%2==0||r.first==letter)continue;if(r.first!=r.last)throw runtime_error("odd chronology");nr++;if(!has(a,r.c,r.p,r.h)&&!normhas(r.c,r.p,r.h,b,p,h))throw runtime_error("odd reader row "+to_string(row));}}
 else{if(q[0]==q[1])throw runtime_error("same cells");int start=0,goal=0;for(int j=0;j<2;j++){auto sa=raw[a].cells.find(q[j]);auto tb=tar[b].cells.find(rot(q[j]-p,-h));if(sa==raw[a].cells.end()||tb==tar[b].cells.end())throw runtime_error("missing cell");start|=(1-sa->second.last)<<j;goal|=tb->second.first<<j;}int graph[4]={0};
 // Duplicating a reader touching both cells is harmless: the graph is a union.
 for(int j=0;j<2;j++)for(auto r:readers(q[j])){nr++;if(has(a,r.c,r.p,r.h)||normhas(r.c,r.p,r.h,b,p,h))continue;for(int input=0;input<4;input++){int state=input;bool ok=true;for(auto[z,bit]:raw[r.c].visits){P cell=r.p+rot(z,r.h);for(int k=0;k<2;k++)if(cell==q[k]){if(((state>>k)&1)!=bit){ok=false;break;}state^=1<<k;}if(!ok)break;}if(ok){graph[input]|=1<<state;transitions++;}}}
 int reach=1<<start;for(int k=0;k<4;k++)for(int s=0;s<4;s++)if(reach&(1<<s))reach|=graph[s];if(reach&(1<<goal))throw runtime_error("two cell reachable row "+to_string(row));}
 if(row%500000==0)cerr<<"verified "<<row<<" / "<<num<<"\n";
 }
 long long marks=0,queries=0;ifstream mf(argv[3]);int b;P q;while(getline(mf,line)){istringstream ms(line);int phase=-1;ms>>b>>q.x>>q.y;if(!ms)throw runtime_error("bad mark row");ms>>phase;auto it=raw[b].cells.find(q);if(it==raw[b].cells.end()||it->second.first!=1)throw runtime_error("mark not raw first L");if(phase>=0&&phase!=it->second.phase)throw runtime_error("mark phase mismatch");marks++;for(int a=0;a<n;a++)for(int h=0;h<4;h++)for(auto[z,cell]:raw[a].cells){P p=z-rot(q,h);if((p.x+p.y-h)%2)continue;queries++;if(!has(a,b,p,h))throw runtime_error("unproved mark "+to_string(b));}}
 ofstream out(argv[4]);out<<"{\n\"status\":\"PASS independent literal least-gap certificate\",\n\"words\":"<<n<<",\"pairs\":"<<gp.size()<<",\"triples\":"<<triples<<",\"clauses\":"<<num<<",\"neighbor_clauses\":"<<counts[1]<<",\"odd_reader_clauses\":"<<counts[2]<<",\"two_cell_clauses\":"<<counts[3]<<",\"neighbor_options\":"<<nn<<",\"reader_options\":"<<nr<<",\"literal_two_cell_transitions\":"<<transitions<<",\"raw_marks\":"<<marks<<",\"mark_overlap_queries\":"<<queries<<"\n}\n";cout<<"PASS "<<num<<" clauses, "<<marks<<" marks\n";
 }catch(exception&e){cerr<<"FAILED: "<<e.what()<<"\n";return 1;} }
