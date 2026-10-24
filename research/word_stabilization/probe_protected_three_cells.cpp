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

struct PR3{int c,h;P p;uint64_t edges;};map<array<int,6>,vector<PR3>>CACHE3;
const vector<PR3>& readers3(array<P,3>qs){array<int,6>k={qs[0].x,qs[0].y,qs[1].x,qs[1].y,qs[2].x,qs[2].y};auto it=CACHE3.find(k);if(it!=CACHE3.end())return it->second;set<array<int,4>>poses;for(P q:qs)for(int c=0;c<(int)M.size();c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){P p=sub(q,rot(z.p,h));if(aligned(p,h))poses.insert({c,h,p.x,p.y});}vector<PR3>out;
for(auto z:poses){int c=z[0],h=z[1];P p={z[2],z[3]};int mask=0,req=0,val=0;for(int j=0;j<3;j++){P r=rot(sub(qs[j],p),-h);if(inside(r)&&M[c].last[qi(r)]>=0){mask|=1<<j;req|=int(M[c].first[qi(r)])<<j;val|=(1-int(M[c].last[qi(r)]))<<j;}}uint64_t e=0;for(int v=0;v<8;v++)if((v&mask)==req)e|=1ull<<(8*v+((v&~mask)|val));out.push_back({c,h,p,e});}return CACHE3.emplace(k,move(out)).first->second;}
bool reach3(uint64_t e,int s,int t){int r=1<<s;for(int k=0;k<8;k++){int n=r;for(int v=0;v<8;v++)if(r&(1<<v))n|=(e>>(8*v))&255;if(n&(1<<t))return true;if(n==r)return false;r=n;}return false;}
int main(int argc,char**argv){ifstream f(argv[1]);int n,z;f>>n;M.resize(n);for(int a=0;a<n;a++){f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].last.fill(-1);M[a].first.fill(-1);while(z--){Cell c;f>>c.p.x>>c.p.y>>c.c;M[a].raw.push_back(c);M[a].last[qi(c.p)]=c.c;}f>>z;while(z--){Cell c;f>>c.p.x>>c.p.y>>c.c>>c.phase;M[a].tar.push_back(c);M[a].first[qi(c.p)]=c.c;}}
string line;ifstream b(argv[2]);while(getline(b,line)){istringstream ss(line);int a,c,x,y,h;ss>>a>>c>>x>>y>>h;BASE.insert(key(a,c,{x,y},h));}ifstream pk(argv[3]);while(getline(pk,line)){istringstream ss(line);int a,c,x,y,h,qx,qy;ss>>a>>c>>x>>y>>h>>qx>>qy;S.insert((uint64_t(key(a,c,{x,y},h))<<12)|qi({qx,qy}));}
ifstream goals(argv[4]);int a,bx,h;P p,q;int found=0,total=0;while(goals>>a>>bx>>p.x>>p.y>>h>>q.x>>q.y){total++;vector<array<int,4>>common;for(auto x:M[a].raw){if(x.p.x==q.x&&x.p.y==q.y)continue;P z=rot(sub(x.p,p),-h);if(inside(z)&&M[bx].first[qi(z)]>=0)common.push_back({x.p.x,x.p.y,x.c,int(M[bx].first[qi(z)])});}bool ok=false;
for(int i=0;i<(int)common.size()&&!ok;i++)for(int j=i+1;j<(int)common.size()&&!ok;j++)for(int k=j+1;k<(int)common.size()&&!ok;k++){array<P,3>cells;int start=0,goal=0,l=0;for(int t:{i,j,k}){auto x=common[t];cells[l]={x[0],x[1]};start|=(1-x[2])<<l;goal|=x[3]<<l;l++;}if(start==goal)continue;uint64_t edges=0;bool connected=false;int survivors=0;for(auto r:readers3(cells)){if(!avoids(r.c,r.p,r.h,q)||has(a,r.c,r.p,r.h,q))continue;P rb=rot(sub(p,r.p),-r.h),qr=rot(sub(q,r.p),-r.h);if(has(r.c,bx,rb,(h-r.h+4)%4,qr))continue;survivors++;edges|=r.edges;if(reach3(edges,start,goal)){connected=true;break;}}if(!connected){ok=true;found++;cout<<"PROVED "<<a<<' '<<bx<<' '<<p.x<<' '<<p.y<<' '<<h<<' '<<q.x<<' '<<q.y;for(P c:cells)cout<<' '<<c.x<<' '<<c.y;cout<<" states "<<start<<' '<<goal<<" readers "<<survivors<<endl;}}
cout<<"TARGET "<<total<<" common "<<common.size()<<" hit "<<ok<<endl;}cout<<"SUMMARY "<<total<<' '<<found<<endl;}
