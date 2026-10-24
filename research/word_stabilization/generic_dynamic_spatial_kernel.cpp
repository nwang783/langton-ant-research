#include <bits/stdc++.h>
using namespace std;
struct P{int x,y;};
P rot(P p,int h){h=(h%4+4)%4;if(h==0)return p;if(h==1)return{p.y,-p.x};if(h==2)return{-p.x,-p.y};return{-p.y,p.x};}
P add(P a,P b){return{a.x+b.x,a.y+b.y};} P sub(P a,P b){return{a.x-b.x,a.y-b.y};}
struct Cell{int x,y,c,phase;};struct Macro{P end;int dh;vector<Cell>raw,tar;array<signed char,4096>first;};
int N=0;vector<uint64_t>CAND,S;vector<uint32_t>active;
uint32_t key(int a,int b,int x,int y,int h){return (((((uint32_t)a*N+b)*4+h)*64+(x+32))*64+(y+32));}
bool inside(int x,int y){return x>=-32&&x<32&&y>=-32&&y<32;}
bool bit(const vector<uint64_t>&v,uint32_t k){return(v[k>>6]>>(k&63))&1;}
void setbit(vector<uint64_t>&v,uint32_t k){v[k>>6]|=1ull<<(k&63);}void clearbit(vector<uint64_t>&v,uint32_t k){v[k>>6]&=~(1ull<<(k&63));}
bool has(int a,int b,P p,int h){return inside(p.x,p.y)&&bit(S,key(a,b,p.x,p.y,h));}
bool aligned(P p,int h){return((p.x+p.y-h)&1)==0;}
struct Type{int a,b,h;P p;};Type decode(uint32_t k){Type t;t.p.y=int(k%64)-32;k/=64;t.p.x=int(k%64)-32;k/=64;t.h=k%4;k/=4;t.b=k%N;t.a=k/N;return t;}
struct Reader{int c,h;P p;};vector<Macro>M;vector<vector<int>>OUT,IN;map<pair<int,int>,vector<Reader>>READERS;
struct Proof{int kind=0,x=0,y=0;};
Proof certify(uint32_t k){auto t=decode(k);int a=t.a,b=t.b,h=t.h;P p=t.p,pa=M[a].end;int ha=M[a].dh;P cb=rot(sub(p,pa),-ha);int cbh=(h-ha+4)%4;bool ok=true;
 vector<tuple<int,P,int,P,int>>ds;
 for(int d:IN[b]){int hd=(h-M[d].dh+4)%4;P pd=sub(p,rot(M[d].end,hd));if(has(a,d,pd,hd))continue;P cd=rot(sub(pd,pa),-ha);ds.push_back({d,pd,hd,cd,(hd-ha+4)%4});}
 for(int c:OUT[a]){if(has(c,b,cb,cbh))continue;for(auto &[d,pd,hd,cd,cdh]:ds)if(!has(c,d,cd,cdh)){ok=false;break;}if(!ok)break;}
 if(ok)return{1,0,0};
 for(auto q:M[a].raw){P z=rot(sub({q.x,q.y},p),-h);if(!inside(z.x,z.y)||M[b].first[(z.x+32)*64+z.y+32]!=q.c)continue;ok=true;
  for(auto r:READERS[{q.x,q.y}]){if(has(a,r.c,r.p,r.h))continue;P rb=rot(sub(p,r.p),-r.h);if(!has(r.c,b,rb,(h-r.h+4)%4)){ok=false;break;}}
  if(ok)return{2,q.x,q.y};
 }
 return{};
}
int main(int argc,char**argv){if(argc!=3){cerr<<"input output_prefix\n";return 1;}ifstream f(argv[1]);int n;f>>n;assert(n<=512);N=n;uint64_t SZ=(uint64_t)n*n*4*64*64;CAND.resize((SZ+63)/64);S.resize((SZ+63)/64);M.resize(n);OUT.resize(n);IN.resize(n);
 for(int a=0;a<n;a++){int z;f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].first.fill(-1);while(z--){Cell q;f>>q.x>>q.y>>q.c;q.phase=-1;M[a].raw.push_back(q);}f>>z;while(z--){Cell q;f>>q.x>>q.y>>q.c>>q.phase;M[a].tar.push_back(q);assert(inside(q.x,q.y));M[a].first[(q.x+32)*64+q.y+32]=q.c;}}
 int z;f>>z;vector<pair<int,int>>pairs;while(z--){int a,b;f>>a>>b;pairs.push_back({a,b});OUT[a].push_back(b);IN[b].push_back(a);}f>>z;vector<array<int,3>>triples;while(z--){array<int,3>q;f>>q[0]>>q[1]>>q[2];triples.push_back(q);}assert(f.good()||f.eof());
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int h=0;h<4;h++)for(auto q:M[a].raw)for(auto z:M[b].tar){P p=sub({q.x,q.y},rot({z.x,z.y},h));if(!aligned(p,h))continue;assert(inside(p.x,p.y));uint32_t k=key(a,b,p.x,p.y,h);if(!bit(CAND,k)){setbit(CAND,k);setbit(S,k);active.push_back(k);}}
 size_t candidates=active.size();
 for(auto [a,b]:pairs){P p=M[a].end;if(inside(p.x,p.y))clearbit(S,key(a,b,p.x,p.y,M[a].dh));}
 for(auto q:triples){int a=q[0],c=q[1],b=q[2];P p=add(M[a].end,rot(M[c].end,M[a].dh));if(inside(p.x,p.y))clearbit(S,key(a,b,p.x,p.y,(M[a].dh+M[c].dh)%4));}
 vector<uint32_t>v;for(auto k:active)if(bit(S,k))v.push_back(k);active.swap(v);sort(active.begin(),active.end());size_t shorts=candidates-active.size();
 set<pair<int,int>>qs;for(auto&m:M)for(auto q:m.raw)qs.insert({q.x,q.y});for(auto [x,y]:qs){auto &rr=READERS[{x,y}];for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){P p=sub({x,y},rot({z.x,z.y},h));if(aligned(p,h))rr.push_back({c,h,p});}}
 cout<<"INITIAL n="<<n<<" candidates="<<candidates<<" short="<<shorts<<endl;int round=0;vector<Proof>proof;
 while(true){vector<uint32_t>next,removed;proof.clear();for(auto k:active){auto p=certify(k);if(p.kind){next.push_back(k);proof.push_back(p);}else removed.push_back(k);}cout<<"ROUND "<<round<<" kernel="<<next.size()<<" removed="<<removed.size()<<endl;if(removed.empty())break;for(auto k:removed)clearbit(S,k);active.swap(next);round++;}
 string base=argv[2];ofstream cert(base+".tsv");for(size_t i=0;i<active.size();i++){auto t=decode(active[i]);auto p=proof[i];cert<<t.a<<' '<<t.b<<' '<<t.p.x<<' '<<t.p.y<<' '<<t.h<<' '<<p.kind<<' '<<p.x<<' '<<p.y<<'\n';}
 ofstream fresh(base+".fresh.tsv");for(int b=0;b<n;b++)for(auto q:M[b].tar)if(q.c==1){bool ok=true;for(int a=0;a<n&&ok;a++)for(int h=0;h<4&&ok;h++)for(auto z:M[a].raw){P p=sub({z.x,z.y},rot({q.x,q.y},h));if(aligned(p,h)&&!has(a,b,p,h)){ok=false;break;}}if(ok){fresh<<b<<' '<<q.x<<' '<<q.y<<' '<<q.phase<<'\n';cout<<"FRESH "<<b<<' '<<q.x<<' '<<q.y<<" phase="<<q.phase<<endl;}}
 ofstream meta(base+".summary.json");meta<<"{\"macros\":"<<n<<",\"candidates\":"<<candidates<<",\"shorts\":"<<shorts<<",\"kernel\":"<<active.size()<<",\"rounds\":"<<round<<"}\n";
}
