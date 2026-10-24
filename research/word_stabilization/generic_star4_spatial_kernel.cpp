#include <bits/stdc++.h>
using namespace std;
struct P{int x,y;};
P rot(P p,int h){h=(h%4+4)%4;if(h==0)return p;if(h==1)return{p.y,-p.x};if(h==2)return{-p.x,-p.y};return{-p.y,p.x};}
P add(P a,P b){return{a.x+b.x,a.y+b.y};} P sub(P a,P b){return{a.x-b.x,a.y-b.y};}
struct Cell{int x,y,c,phase;};struct Macro{P end;int dh;vector<Cell>raw,tar;array<signed char,4096>first,rawlast;};
static const uint32_t SZ=1u<<28;vector<uint64_t>CAND(SZ/64),S(SZ/64);vector<uint32_t>active;
uint32_t key(int a,int b,int x,int y,int h){return (((((uint32_t)a*128+b)*4+h)*64+(x+32))*64+(y+32));}
bool inside(int x,int y){return x>=-32&&x<32&&y>=-32&&y<32;}
bool bit(const vector<uint64_t>&v,uint32_t k){return(v[k>>6]>>(k&63))&1;}
void setbit(vector<uint64_t>&v,uint32_t k){v[k>>6]|=1ull<<(k&63);}void clearbit(vector<uint64_t>&v,uint32_t k){v[k>>6]&=~(1ull<<(k&63));}
bool has(int a,int b,P p,int h){return inside(p.x,p.y)&&bit(S,key(a,b,p.x,p.y,h));}
bool aligned(P p,int h){return((p.x+p.y-h)&1)==0;}
struct Type{int a,b,h;P p;};Type decode(uint32_t k){Type t;t.p.y=int(k%64)-32;k/=64;t.p.x=int(k%64)-32;k/=64;t.h=k%4;k/=4;t.b=k%128;t.a=k/128;return t;}
struct Reader{int c,h,color;P p;};vector<Macro>M;vector<vector<int>>OUT,IN;map<pair<int,int>,vector<Reader>>READERS;
struct Proof{int kind=0,x=0,y=0,x2=0,y2=0;};

struct PatchReader{int c,h;P p;uint16_t edges;};
map<array<int,4>,vector<PatchReader>> PATCHES;
const vector<PatchReader>& patchreaders(P q1,P q2){
 array<int,4>k={q1.x,q1.y,q2.x,q2.y};auto it=PATCHES.find(k);if(it!=PATCHES.end())return it->second;
 set<array<int,4>>poses;for(P q:{q1,q2})for(int c=0;c<(int)M.size();c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){P p=sub(q,rot({z.x,z.y},h));if(aligned(p,h))poses.insert({c,h,p.x,p.y});}
 vector<PatchReader> rr;for(auto z:poses){int c=z[0],h=z[1];P p={z[2],z[3]};int mask=0,req=0,out=0,j=0;for(P q:{q1,q2}){P r=rot(sub(q,p),-h);if(inside(r.x,r.y)){int ix=(r.x+32)*64+r.y+32;int l=M[c].rawlast[ix];if(l>=0){mask|=1<<j;req|=int(M[c].first[ix])<<j;out|=(1-l)<<j;}}j++;}assert(mask);uint16_t ed=0;for(int v=0;v<4;v++)if((v&mask)==req){int w=(v&~mask)|out;ed|=1u<<(4*v+w);}rr.push_back({c,h,p,ed});}
 return PATCHES.emplace(k,move(rr)).first->second;
}
bool reaches(uint16_t edges,int start,int goal){int reach=1<<start;for(int k=0;k<4;k++){int more=reach;for(int v=0;v<4;v++)if(reach&(1<<v))more|=(edges>>(4*v))&15;if(more&(1<<goal))return true;if(more==reach)return false;reach=more;}return false;}
bool patch_excludes(int a,int b,P p,int h,P q1,P q2,int start,int goal){
 if(start==goal)return false;uint16_t edges=0;
 for(auto r:patchreaders(q1,q2)){if(has(a,r.c,r.p,r.h))continue;P rb=rot(sub(p,r.p),-r.h);if(has(r.c,b,rb,(h-r.h+4)%4))continue;edges|=r.edges;if(reaches(edges,start,goal))return false;}
 return true;
}


// The four cells of a physical 2x2 square are a complete dual-vertex star.
struct StarReader{int c,h;P p;array<uint16_t,16> edges;};
map<pair<int,int>,vector<StarReader>> STARS;
const vector<StarReader>& starreaders(P q){
 auto keyq=make_pair(q.x,q.y);auto it=STARS.find(keyq);if(it!=STARS.end())return it->second;
 vector<P>cells={{q.x,q.y},{q.x+1,q.y},{q.x,q.y+1},{q.x+1,q.y+1}};
 set<array<int,4>>poses;for(P z:cells)for(int c=0;c<(int)M.size();c++)for(int h=0;h<4;h++)for(auto a:M[c].raw){P p=sub(z,rot({a.x,a.y},h));if(aligned(p,h))poses.insert({c,h,p.x,p.y});}
 vector<StarReader>rr;for(auto z:poses){int c=z[0],h=z[1];P p={z[2],z[3]};int mask=0,req=0,out=0,j=0;for(P a:cells){P r=rot(sub(a,p),-h);if(inside(r.x,r.y)){int ix=(r.x+32)*64+r.y+32,l=M[c].rawlast[ix];if(l>=0){mask|=1<<j;req|=int(M[c].first[ix])<<j;out|=(1-l)<<j;}}j++;}assert(mask);array<uint16_t,16>edges{};for(int v=0;v<16;v++)if((v&mask)==req)edges[v]|=1u<<((v&~mask)|out);rr.push_back({c,h,p,edges});}
 return STARS.emplace(keyq,move(rr)).first->second;
}
bool starreach(const array<uint16_t,16>&E,int start,int goal){int reach=1<<start;for(int k=0;k<16;k++){int more=reach;for(int v=0;v<16;v++)if(reach&(1<<v))more|=E[v];if(more&(1<<goal))return true;if(more==reach)return false;reach=more;}return false;}
bool starexcludes(int a,int b,P p,int h,P q,int start,int goal){if(start==goal)return false;array<uint16_t,16>E{};for(auto&r:starreaders(q)){if(has(a,r.c,r.p,r.h))continue;P rb=rot(sub(p,r.p),-r.h);if(has(r.c,b,rb,(h-r.h+4)%4))continue;for(int v=0;v<16;v++)E[v]|=r.edges[v];if(starreach(E,start,goal))return false;}return true;}
Proof certify(uint32_t k){auto t=decode(k);int a=t.a,b=t.b,h=t.h;P p=t.p,pa=M[a].end;int ha=M[a].dh;P cb=rot(sub(p,pa),-ha);int cbh=(h-ha+4)%4;bool ok=true;
 vector<tuple<int,P,int,P,int>>ds;
 for(int d:IN[b]){int hd=(h-M[d].dh+4)%4;P pd=sub(p,rot(M[d].end,hd));if(has(a,d,pd,hd))continue;P cd=rot(sub(pd,pa),-ha);ds.push_back({d,pd,hd,cd,(hd-ha+4)%4});}
 for(int c:OUT[a]){if(has(c,b,cb,cbh))continue;for(auto &[d,pd,hd,cd,cdh]:ds)if(!has(c,d,cd,cdh)){ok=false;break;}if(!ok)break;}
 if(ok)return{1,0,0};
 for(auto q:M[a].raw){P z=rot(sub({q.x,q.y},p),-h);if(!inside(z.x,z.y)||M[b].first[(z.x+32)*64+z.y+32]!=q.c)continue;ok=true;
  for(auto r:READERS[{q.x,q.y}]){if(r.color==q.c)continue;if(has(a,r.c,r.p,r.h))continue;P rb=rot(sub(p,r.p),-r.h);if(!has(r.c,b,rb,(h-r.h+4)%4)){ok=false;break;}}
  if(ok)return{2,q.x,q.y};
 }
 vector<array<int,4>>common;for(auto q:M[a].raw){P z=rot(sub({q.x,q.y},p),-h);if(inside(z.x,z.y)){int v=M[b].first[(z.x+32)*64+z.y+32];if(v>=0)common.push_back({q.x,q.y,q.c,v});}}
 for(int i=0;i<(int)common.size();i++)for(int j=i+1;j<(int)common.size();j++){auto q=common[i],r=common[j];int start=(1-q[2])+2*(1-r[2]),goal=q[3]+2*r[3];if(patch_excludes(a,b,p,h,{q[0],q[1]},{r[0],r[1]},start,goal))return{3,q[0],q[1],r[0],r[1]};}

 for(auto q:common){int start=0,goal=0;bool all=true;int j=0;for(P z:vector<P>{{q[0],q[1]},{q[0]+1,q[1]},{q[0],q[1]+1},{q[0]+1,q[1]+1}}){auto it=find_if(common.begin(),common.end(),[&](auto z0){return z0[0]==z.x&&z0[1]==z.y;});if(it==common.end()){all=false;break;}start|=(1-(*it)[2])<<j;goal|=(*it)[3]<<j;j++;}if(all&&starexcludes(a,b,p,h,{q[0],q[1]},start,goal))return{4,q[0],q[1],0,0};}
 return{};
}
int main(int argc,char**argv){if(argc!=3){cerr<<"input output_prefix\n";return 1;}ifstream f(argv[1]);int n;f>>n;assert(n<=128);M.resize(n);OUT.resize(n);IN.resize(n);
 for(int a=0;a<n;a++){int z;f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].first.fill(-1);M[a].rawlast.fill(-1);while(z--){Cell q;f>>q.x>>q.y>>q.c;q.phase=-1;M[a].raw.push_back(q);assert(inside(q.x,q.y));M[a].rawlast[(q.x+32)*64+q.y+32]=q.c;}f>>z;while(z--){Cell q;f>>q.x>>q.y>>q.c>>q.phase;M[a].tar.push_back(q);assert(inside(q.x,q.y));M[a].first[(q.x+32)*64+q.y+32]=q.c;}}
 int z;f>>z;vector<pair<int,int>>pairs;while(z--){int a,b;f>>a>>b;pairs.push_back({a,b});OUT[a].push_back(b);IN[b].push_back(a);}f>>z;vector<array<int,3>>triples;while(z--){array<int,3>q;f>>q[0]>>q[1]>>q[2];triples.push_back(q);}assert(f.good()||f.eof());
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int h=0;h<4;h++)for(auto q:M[a].raw)for(auto z:M[b].tar){P p=sub({q.x,q.y},rot({z.x,z.y},h));if(!aligned(p,h))continue;assert(inside(p.x,p.y));uint32_t k=key(a,b,p.x,p.y,h);if(!bit(CAND,k)){setbit(CAND,k);setbit(S,k);active.push_back(k);}}
 size_t candidates=active.size();
 for(auto [a,b]:pairs){P p=M[a].end;if(inside(p.x,p.y))clearbit(S,key(a,b,p.x,p.y,M[a].dh));}
 for(auto q:triples){int a=q[0],c=q[1],b=q[2];P p=add(M[a].end,rot(M[c].end,M[a].dh));if(inside(p.x,p.y))clearbit(S,key(a,b,p.x,p.y,(M[a].dh+M[c].dh)%4));}
 vector<uint32_t>v;for(auto k:active)if(bit(S,k))v.push_back(k);active.swap(v);sort(active.begin(),active.end());size_t shorts=candidates-active.size();
 set<pair<int,int>>qs;for(auto&m:M)for(auto q:m.raw)qs.insert({q.x,q.y});for(auto [x,y]:qs){auto &rr=READERS[{x,y}];for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){if(M[c].first[(z.x+32)*64+z.y+32]!=z.c)continue;P p=sub({x,y},rot({z.x,z.y},h));if(aligned(p,h))rr.push_back({c,h,z.c,p});}}
 cout<<"INITIAL n="<<n<<" candidates="<<candidates<<" short="<<shorts<<endl;int round=0;vector<Proof>proof;
 while(true){vector<uint32_t>next,removed;proof.clear();for(auto k:active){auto p=certify(k);if(p.kind){next.push_back(k);proof.push_back(p);}else removed.push_back(k);}cout<<"ROUND "<<round<<" kernel="<<next.size()<<" removed="<<removed.size()<<endl;if(removed.empty())break;for(auto k:removed)clearbit(S,k);active.swap(next);round++;}
 string base=argv[2];ofstream cert(base+".tsv");for(size_t i=0;i<active.size();i++){auto t=decode(active[i]);auto p=proof[i];cert<<t.a<<' '<<t.b<<' '<<t.p.x<<' '<<t.p.y<<' '<<t.h<<' '<<p.kind<<' '<<p.x<<' '<<p.y<<' '<<p.x2<<' '<<p.y2<<'\n';}
 ofstream fresh(base+".fresh.tsv");for(int b=0;b<n;b++)for(auto q:M[b].tar)if(q.c==1){bool ok=true;for(int a=0;a<n&&ok;a++)for(int h=0;h<4&&ok;h++)for(auto z:M[a].raw){P p=sub({z.x,z.y},rot({q.x,q.y},h));if(aligned(p,h)&&!has(a,b,p,h)){ok=false;break;}}if(ok){fresh<<b<<' '<<q.x<<' '<<q.y<<' '<<q.phase<<'\n';cout<<"FRESH "<<b<<' '<<q.x<<' '<<q.y<<" phase="<<q.phase<<endl;}}
 ofstream meta(base+".summary.json");meta<<"{\"macros\":"<<n<<",\"candidates\":"<<candidates<<",\"shorts\":"<<shorts<<",\"kernel\":"<<active.size()<<",\"rounds\":"<<round<<"}\n";
}
