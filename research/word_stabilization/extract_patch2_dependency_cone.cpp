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
 return{};
}

struct Row{uint32_t k;Proof p;};vector<Row>ROWS;
Proof getproof(uint32_t k){auto it=lower_bound(ROWS.begin(),ROWS.end(),k,[](const Row&r,uint32_t k){return r.k<k;});assert(it!=ROWS.end()&&it->k==k);return it->p;}
vector<uint32_t>todo;
void need(uint32_t k){assert(bit(S,k));if(!bit(CAND,k)){setbit(CAND,k);todo.push_back(k);}}
uint32_t normalized(int a,int b,P p,int h){assert(inside(p.x,p.y));return key(a,b,p.x,p.y,h);}
void choose(vector<uint32_t>v){assert(!v.empty());for(auto k:v)if(bit(CAND,k)){need(k);return;}uint32_t best=v[0];int score=INT_MAX;for(auto k:v){auto p=getproof(k);auto t=decode(k);int z=p.kind==1?int(OUT[t.a].size()*IN[t.b].size()):p.kind==2?100000:200000;if(z<score){score=z;best=k;}}need(best);}
void addif(vector<uint32_t>&v,int a,int b,P p,int h){if(has(a,b,p,h))v.push_back(normalized(a,b,p,h));}
int main(int argc,char**argv){assert(argc==5);ifstream f(argv[1]);int n;f>>n;M.resize(n);OUT.resize(n);IN.resize(n);
for(int a=0;a<n;a++){int z;f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].first.fill(-1);M[a].rawlast.fill(-1);while(z--){Cell q;f>>q.x>>q.y>>q.c;q.phase=-1;M[a].raw.push_back(q);M[a].rawlast[(q.x+32)*64+q.y+32]=q.c;}f>>z;while(z--){Cell q;f>>q.x>>q.y>>q.c>>q.phase;M[a].tar.push_back(q);M[a].first[(q.x+32)*64+q.y+32]=q.c;}}
int z;f>>z;while(z--){int a,b;f>>a>>b;OUT[a].push_back(b);IN[b].push_back(a);}f>>z;while(z--){int a,b,c;f>>a>>b>>c;}
set<pair<int,int>>qs;for(auto&m:M)for(auto q:m.raw)qs.insert({q.x,q.y});for(auto[x,y]:qs){auto&rr=READERS[{x,y}];for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){if(M[c].first[(z.x+32)*64+z.y+32]!=z.c)continue;P p=sub({x,y},rot({z.x,z.y},h));if(aligned(p,h))rr.push_back({c,h,z.c,p});}}
ifstream cert(argv[2]);int a,b,x,y,h,kind,x1,y1,x2,y2;while(cert>>a>>b>>x>>y>>h>>kind>>x1>>y1>>x2>>y2){auto k=key(a,b,x,y,h);setbit(S,k);ROWS.push_back({k,{kind,x1,y1,x2,y2}});}assert(is_sorted(ROWS.begin(),ROWS.end(),[](auto a,auto b){return a.k<b.k;}));
ifstream marks(argv[3]);while(marks>>b>>x>>y){for(int a=0;a<n;a++)for(int h=0;h<4;h++)for(auto q:M[a].raw){P p=sub({q.x,q.y},rot({x,y},h));if(aligned(p,h))need(normalized(a,b,p,h));}}
cout<<"FULL "<<ROWS.size()<<" INITIAL "<<todo.size()<<endl;
for(size_t at=0;at<todo.size();at++){uint32_t k=todo[at];auto t=decode(k);int a=t.a,b=t.b,h=t.h;P p=t.p;auto pf=getproof(k);
 if(pf.kind==1){P pa=M[a].end;int ha=M[a].dh;P cb=rot(sub(p,pa),-ha);int cbh=(h-ha+4)%4;for(int c:OUT[a])for(int d:IN[b]){int hd=(h-M[d].dh+4)%4;P pd=sub(p,rot(M[d].end,hd));P cd=rot(sub(pd,pa),-ha);vector<uint32_t>ch;addif(ch,a,d,pd,hd);addif(ch,c,b,cb,cbh);addif(ch,c,d,cd,(hd-ha+4)%4);choose(ch);}}
 else if(pf.kind==2){int color=M[a].rawlast[(pf.x+32)*64+pf.y+32];assert(color>=0);for(auto r:READERS[{pf.x,pf.y}]){if(r.color==color)continue;P rb=rot(sub(p,r.p),-r.h);vector<uint32_t>ch;addif(ch,a,r.c,r.p,r.h);addif(ch,r.c,b,rb,(h-r.h+4)%4);choose(ch);}}
 else if(pf.kind==3){P q1={pf.x,pf.y},q2={pf.x2,pf.y2};int st=0,go=0,j=0;for(P q:{q1,q2}){int c=M[a].rawlast[(q.x+32)*64+q.y+32];P z=rot(sub(q,p),-h);int v=M[b].first[(z.x+32)*64+z.y+32];assert(c>=0&&v>=0);st|=(1-c)<<j;go|=v<<j;j++;}auto&rr=patchreaders(q1,q2);uint16_t edges=0;for(auto r:rr){P rb=rot(sub(p,r.p),-r.h);if(!has(a,r.c,r.p,r.h)&&!has(r.c,b,rb,(h-r.h+4)%4))edges|=r.edges;}int reach=1<<st;for(int i=0;i<4;i++){int next=reach;for(int v=0;v<4;v++)if(reach&(1<<v))next|=(edges>>(4*v))&15;reach=next;}assert(!(reach&(1<<go)));for(auto r:rr){bool cross=false;for(int v=0;v<4;v++)if(reach&(1<<v))if(((r.edges>>(4*v))&15)&~reach)cross=true;if(!cross)continue;P rb=rot(sub(p,r.p),-r.h);vector<uint32_t>ch;addif(ch,a,r.c,r.p,r.h);addif(ch,r.c,b,rb,(h-r.h+4)%4);choose(ch);}}
 else assert(false);
 if(at%100000==0)cout<<"CONE "<<at<<" QUEUED "<<todo.size()<<endl;
}
sort(todo.begin(),todo.end());ofstream o(argv[4]);for(auto k:todo){auto t=decode(k);auto p=getproof(k);o<<t.a<<' '<<t.b<<' '<<t.p.x<<' '<<t.p.y<<' '<<t.h<<' '<<p.kind<<' '<<p.x<<' '<<p.y<<' '<<p.x2<<' '<<p.y2<<'\n';}cout<<"FINAL "<<todo.size()<<endl;
}
