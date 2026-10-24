#include<bits/stdc++.h>
using namespace std;struct P{int x,y;};P rot(P p,int h){h=(h%4+4)%4;if(h==0)return p;if(h==1)return{p.y,-p.x};if(h==2)return{-p.x,-p.y};return{-p.y,p.x};}P add(P a,P b){return{a.x+b.x,a.y+b.y};}P sub(P a,P b){return{a.x-b.x,a.y-b.y};}
bool inside(P p){return p.x>=-32&&p.x<32&&p.y>=-32&&p.y<32;}int qi(P p){assert(inside(p));return(p.x+32)*64+p.y+32;}P dq(int i){return{i/64-32,i%64-32};}bool aligned(P p,int h){return((p.x+p.y-h)&1)==0;}
struct Cell{P p;int c,phase;};struct Macro{P end;int dh;vector<Cell>raw,tar;array<signed char,4096>last,first;};vector<Macro>M;vector<vector<int>>OUT,IN;
uint32_t key(int a,int b,P p,int h){assert(inside(p));return((a*128+b)*4+h)*4096+qi(p);}struct Type{int a,b,h;P p;};Type dec(uint32_t k){P p=dq(k%4096);k/=4096;int h=k%4;k/=4;int b=k%128;return{int(k/128),b,h,p};}
unordered_set<uint32_t>BASE;unordered_set<uint64_t>S;vector<uint64_t>active;
bool ordinary(int a,int b,P p,int h){return inside(p)&&BASE.count(key(a,b,p,h));}
bool has(int a,int b,P p,int h,P q){return ordinary(a,b,p,h)||(inside(p)&&inside(q)&&S.count((uint64_t(key(a,b,p,h))<<12)|qi(q)));}
bool avoids(int a,P p,int h,P q){P z=rot(sub(q,p),-h);return!inside(z)||M[a].first[qi(z)]<0;}
struct Reader{int c,h,color;P p;};map<int,vector<Reader>>READERS;

struct PatchReader{int c,h;P p;uint16_t edges;};map<array<int,4>,vector<PatchReader>>PATCHES;
const vector<PatchReader>&patchreaders(P q1,P q2){array<int,4>k={q1.x,q1.y,q2.x,q2.y};auto it=PATCHES.find(k);if(it!=PATCHES.end())return it->second;set<array<int,4>>poses;for(P q:{q1,q2})for(int c=0;c<(int)M.size();c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){P p=sub(q,rot(z.p,h));if(aligned(p,h))poses.insert({c,h,p.x,p.y});}vector<PatchReader>rr;
 for(auto z:poses){int c=z[0],h=z[1];P p={z[2],z[3]};int mask=0,req=0,out=0,j=0;for(P q:{q1,q2}){P r=rot(sub(q,p),-h);if(inside(r)){int l=M[c].last[qi(r)];if(l>=0){mask|=1<<j;req|=int(M[c].first[qi(r)])<<j;out|=(1-l)<<j;}}j++;}assert(mask);uint16_t ed=0;for(int v=0;v<4;v++)if((v&mask)==req){int w=(v&~mask)|out;ed|=1u<<(4*v+w);}rr.push_back({c,h,p,ed});}return PATCHES.emplace(k,move(rr)).first->second;}
bool reach(uint16_t e,int start,int goal){int r=1<<start;for(int k=0;k<4;k++){int m=r;for(int v=0;v<4;v++)if(r&(1<<v))m|=(e>>(4*v))&15;if(m&(1<<goal))return true;if(m==r)return false;r=m;}return false;}
bool patch_excludes(int a,int b,P p,int h,P q,P x,P y,int start,int goal){if(start==goal)return false;uint16_t edges=0;for(auto r:patchreaders(x,y)){if(!avoids(r.c,r.p,r.h,q)||has(a,r.c,r.p,r.h,q))continue;P rb=rot(sub(p,r.p),-r.h),qr=rot(sub(q,r.p),-r.h);if(has(r.c,b,rb,(h-r.h+4)%4,qr))continue;edges|=r.edges;if(reach(edges,start,goal))return false;}return true;}
struct Proof{int kind=0;P x={0,0},y={0,0};};
Proof certify(uint64_t kk){auto t=dec(kk>>12);P q=dq(kk%4096),p=t.p;int a=t.a,b=t.b,h=t.h;P qb=rot(sub(q,p),-h);int sl=M[a].last[qi(q)],tf=inside(qb)?M[b].first[qi(qb)]:-1;
 if(sl==1||tf==0)return{3,{0,0}}; // post-source or pre-target contradicts black q
 P pa=M[a].end;int ha=M[a].dh;P cb=rot(sub(p,pa),-ha),qc=rot(sub(q,pa),-ha);int cbh=(h-ha+4)%4;bool ok=true;
 vector<tuple<int,P,int,P,int,P>>ds;
 for(int d:IN[b]){int hd=(h-M[d].dh+4)%4;P pd=sub(p,rot(M[d].end,hd));if(!avoids(d,pd,hd,q)||has(a,d,pd,hd,q))continue;P cd=rot(sub(pd,pa),-ha);ds.push_back({d,pd,hd,cd,(hd-ha+4)%4,rot(sub(q,pd),-hd)});}
 for(int c:OUT[a]){if(!avoids(c,pa,ha,q)||has(c,b,cb,cbh,qc))continue;for(auto[d,pd,hd,cd,cdh,qd]:ds)if(!has(c,d,cd,cdh,qc)){ok=false;break;}if(!ok)break;}
 if(ok)return{1,{0,0}};
 for(auto x:M[a].raw){P z=rot(sub(x.p,p),-h);if(!inside(z)||M[b].first[qi(z)]!=x.c)continue;ok=true;
  for(auto r:READERS[qi(x.p)]){if(r.color==x.c||!avoids(r.c,r.p,r.h,q)||has(a,r.c,r.p,r.h,q))continue;P rb=rot(sub(p,r.p),-r.h),qr=rot(sub(q,r.p),-r.h);if(!has(r.c,b,rb,(h-r.h+4)%4,qr)){ok=false;break;}}
  if(ok)return{2,x.p};
 }
 vector<array<int,4>>common;for(auto x:M[a].raw){P z=rot(sub(x.p,p),-h);if(inside(z)){int v=M[b].first[qi(z)];if(v>=0)common.push_back({x.p.x,x.p.y,x.c,v});}}
 for(int i=0;i<(int)common.size();i++)for(int j=i+1;j<(int)common.size();j++){auto x=common[i],y=common[j];int start=(1-x[2])+2*(1-y[2]),goal=x[3]+2*y[3];if(patch_excludes(a,b,p,h,q,{x[0],x[1]},{y[0],y[1]},start,goal))return{4,{x[0],x[1]},{y[0],y[1]}};}
 return{};
}
int main(int argc,char**argv){if(argc!=4){cerr<<"input ordinary_certificate output_prefix\n";return 1;}ifstream f(argv[1]);int n,z;f>>n;M.resize(n);OUT.resize(n);IN.resize(n);
 for(int a=0;a<n;a++){f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].last.fill(-1);M[a].first.fill(-1);while(z--){Cell c;f>>c.p.x>>c.p.y>>c.c;M[a].raw.push_back(c);M[a].last[qi(c.p)]=c.c;}f>>z;while(z--){Cell c;f>>c.p.x>>c.p.y>>c.c>>c.phase;M[a].tar.push_back(c);M[a].first[qi(c.p)]=c.c;}}
 vector<pair<int,int>>pairs;vector<array<int,3>>triples;f>>z;while(z--){int a,b;f>>a>>b;OUT[a].push_back(b);IN[b].push_back(a);pairs.push_back({a,b});}f>>z;while(z--){array<int,3>a;f>>a[0]>>a[1]>>a[2];triples.push_back(a);}
 ifstream cf(argv[2]);string line;while(getline(cf,line)){istringstream ss(line);int a,b,x,y,h;ss>>a>>b>>x>>y>>h;BASE.insert(key(a,b,{x,y},h));}
 set<uint32_t>poses;for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int h=0;h<4;h++)for(auto x:M[a].raw)for(auto y:M[b].tar){P p=sub(x.p,rot(y.p,h));if(aligned(p,h)&&!ordinary(a,b,p,h))poses.insert(key(a,b,p,h));}
 for(auto k:poses){auto t=dec(k);set<int>qs;for(auto x:M[t.a].raw)qs.insert(qi(x.p));for(auto y:M[t.b].tar)qs.insert(qi(add(t.p,rot(y.p,t.h))));for(int q:qs)S.insert((uint64_t(k)<<12)|q);}
 auto clearshort=[&](int a,int b,P p,int h,int c,P pc,int hc){if(ordinary(a,b,p,h))return;vector<uint64_t>del;uint32_t k=key(a,b,p,h);for(int ix=0;ix<4096;ix++){uint64_t kk=(uint64_t(k)<<12)|ix;if(!S.count(kk))continue;P q=dq(ix),qb=rot(sub(q,p),-h);if(M[a].last[ix]==1||(inside(qb)&&M[b].first[qi(qb)]==0))continue;if(c>=0&&!avoids(c,pc,hc,q))continue;del.push_back(kk);}for(auto kk:del)S.erase(kk);};
 size_t candidates=S.size();for(auto[a,b]:pairs)clearshort(a,b,M[a].end,M[a].dh,-1,{0,0},0);for(auto[a,c,b]:triples){P pc=M[a].end,p=add(pc,rot(M[c].end,M[a].dh));clearshort(a,b,p,(M[a].dh+M[c].dh)%4,c,pc,M[a].dh);}size_t shortn=candidates-S.size();active.assign(S.begin(),S.end());sort(active.begin(),active.end());
 set<int>cells;for(auto&m:M)for(auto x:m.raw)cells.insert(qi(x.p));for(int ix:cells){P x=dq(ix);for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto y:M[c].raw){if(M[c].first[qi(y.p)]!=y.c)continue;P p=sub(x,rot(y.p,h));if(aligned(p,h))READERS[ix].push_back({c,h,y.c,p});}}
 cout<<"INITIAL "<<candidates<<" short "<<shortn<<" ordinary "<<BASE.size()<<endl;int round=0;vector<Proof>proof;
 while(true){vector<uint64_t>next,remove;proof.clear();for(auto k:active){auto p=certify(k);if(p.kind){next.push_back(k);proof.push_back(p);}else remove.push_back(k);}cout<<"ROUND "<<round<<" remain "<<next.size()<<" remove "<<remove.size()<<endl;if(remove.empty())break;for(auto k:remove)S.erase(k);active.swap(next);round++;}
 string base=argv[3];ofstream o(base+".tsv");for(int i=0;i<(int)active.size();i++){auto t=dec(active[i]>>12);P q=dq(active[i]%4096);auto p=proof[i];o<<t.a<<' '<<t.b<<' '<<t.p.x<<' '<<t.p.y<<' '<<t.h<<' '<<q.x<<' '<<q.y<<' '<<p.kind<<' '<<p.x.x<<' '<<p.x.y<<' '<<p.y.x<<' '<<p.y.y<<'\n';}
 cout<<"QUERY DC upper to D "<<has(1,0,{2,2},0,{2,3})<<" right to D "<<has(1,0,{3,1},0,{3,2})<<endl;
 ofstream meta(base+".summary.json");meta<<"{\"candidates\":"<<candidates<<",\"shorts\":"<<shortn<<",\"ordinary\":"<<BASE.size()<<",\"kernel\":"<<active.size()<<",\"rounds\":"<<round<<"}\n";
}
