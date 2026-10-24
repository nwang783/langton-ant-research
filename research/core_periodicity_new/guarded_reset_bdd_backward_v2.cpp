// Symbolic exact reachability for the finite guarded-XOR patch abstraction.
// No-hit is meaningful only after the frontier becomes empty, never at a cap.
// v2: collect between predecessor-position expansions, retaining seen/fr/next.
#include <bits/stdc++.h>
using namespace std; using U=uint64_t;
struct N{int v,lo,hi;};
struct NK{int v,lo,hi;bool operator==(NK const&o)const{return v==o.v&&lo==o.lo&&hi==o.hi;}};
struct NH{size_t operator()(NK const&x)const{return (U(x.lo)*11995408973635179863ull)^(U(x.hi)*10150724397891781847ull)^x.v;}};
struct XKey{int f;U k,v,x,c,r;bool operator==(XKey const&o)const{return f==o.f&&k==o.k&&v==o.v&&x==o.x&&c==o.c&&r==o.r;}};
struct XH{size_t operator()(XKey const&a)const{return U(a.f)*11995408973635179863ull ^a.k*10150724397891781847ull ^a.v*14406626329776981559ull ^a.x*1099511628211ull ^a.c*14695981039346656037ull ^a.r*7809847782465536327ull;}};
struct BDD{
 int n;size_t cap;vector<N>a;unordered_map<NK,int,NH>uniq;unordered_map<U,int>oc,dc;unordered_map<XKey,int,XH>xc; unordered_map<U,int>ec;
 BDD(int nn,size_t cc):n(nn),cap(cc){a.push_back({n,0,0});a.push_back({n,1,1});}
 int mk(int v,int l,int h){if(l==h)return l;NK k{v,l,h};auto it=uniq.find(k);if(it!=uniq.end())return it->second;if(a.size()>=cap)throw runtime_error("node cap");int z=a.size();a.push_back({v,l,h});uniq.emplace(k,z);return z;}
 int OR(int f,int g){if(!f)return g;if(!g||f==g)return f;if(f==1||g==1)return 1;if(f>g)swap(f,g);U k=(U(f)<<32)|unsigned(g);auto it=oc.find(k);if(it!=oc.end())return it->second;int v=min(a[f].v,a[g].v);int l=OR(a[f].v==v?a[f].lo:f,a[g].v==v?a[g].lo:g);int h=OR(a[f].v==v?a[f].hi:f,a[g].v==v?a[g].hi:g);int z=mk(v,l,h);oc[k]=z;return z;}
 int DIFF(int f,int g){if(!f||g==1||f==g)return 0;if(!g)return f;U k=(U(f)<<32)|unsigned(g);auto it=dc.find(k);if(it!=dc.end())return it->second;int v=min(a[f].v,a[g].v);int l=DIFF(a[f].v==v?a[f].lo:f,a[g].v==v?a[g].lo:g);int h=DIFF(a[f].v==v?a[f].hi:f,a[g].v==v?a[g].hi:g);int z=mk(v,l,h);dc[k]=z;return z;}
 int image(int f,U k,U v,U flip,U clear=0,U reset=0){if(!f)return 0;v&=k;reset&=clear;flip&=~clear;if(f==1&&!k&&!clear)return 1;if(!k&&!flip&&!clear)return f;
  // Flip bits below the first relevant variable do not affect a cylinder set.
  int top=min({a[f].v,k?__builtin_ctzll(k):n,clear?__builtin_ctzll(clear):n});if(top==n)return f;U mask=~((1ull<<top)-1);flip&=mask;k&=mask;v&=k;
  XKey key{f,k,v,flip,clear,reset};auto it=xc.find(key);if(it!=xc.end())return it->second;
  U bit=1ull<<top;int l=a[f].v==top?a[f].lo:f,h=a[f].v==top?a[f].hi:f;U kk=k&~bit,vv=v&~bit,ff=flip&~bit,cc=clear&~bit,rr=reset&~bit;
  if(k&bit){if(v&bit)l=0;else h=0;}l=image(l,kk,vv,ff,cc,rr);h=image(h,kk,vv,ff,cc,rr);int z;if(clear&bit)z=(reset&bit)?mk(top,0,OR(l,h)):mk(top,OR(l,h),0);else{if(flip&bit)swap(l,h);z=mk(top,l,h);}xc.emplace(key,z);return z;
 }
 int exists_uncached(int f,U clear){if(f<2||!clear)return f;N z=a[f];clear&=~((1ull<<z.v)-1);if(!clear)return f;XKey key{f,clear,0,0,0,0};auto it=excache.find(key);if(it!=excache.end())return it->second;int l=exists_uncached(z.lo,clear),h=exists_uncached(z.hi,clear);int y=(clear&(1ull<<z.v))?OR(l,h):mk(z.v,l,h);excache.emplace(key,y);return y;}
 unordered_map<XKey,int,XH>excache;
 int preimage(int f,U k,U v,U flip,U clear,U reset){int z=image(f,clear,reset&clear,flip&~clear);z=exists_uncached(z,clear);return image(z,k,v,0);}
 int cube(U k,U v){return image(1,k,v,0);}
 U count(int f){unordered_map<int,U>memo;function<U(int)>go=[&](int z)->U{if(z<2)return z;auto it=memo.find(z);if(it!=memo.end())return it->second;N b=a[z];U l=go(b.lo)<<(a[b.lo].v-b.v-1);U h=go(b.hi)<<(a[b.hi].v-b.v-1);return memo[z]=l+h;};return go(f)<<a[f].v;}
};
struct T{int from,to;U k,v,f,clear,reset;int goal,a;};

int main(int argc,char**argv){try{if(argc<2)return 1;ifstream in(argv[1]);int n,np,nt,nr;in>>n>>np>>nt>>nr;if(n>50)throw runtime_error("too many variables");int sp;U sk,sv;in>>sp>>sk>>sv;vector<vector<T>>incoming(np);vector<T>goals;for(int i=0;i<nt;i++){T t;in>>t.from>>t.to>>t.k>>t.v>>t.f>>t.clear>>t.reset>>t.goal>>t.a;if(t.from==np-1)continue;if(t.goal)goals.push_back(t);else incoming[t.to].push_back(t);}vector<int>re(nr);for(int&i:re)in>>i;vector<bool>is_re(np);for(int p:re)is_re[p]=true;size_t cap=argc>2?stoull(argv[2]):2000000;BDD b(n,cap);vector<int>seen(np),fr(np),next(np);for(T t:goals)seen[t.from]=b.OR(seen[t.from],b.cube(t.k,t.v));fr=seen;bool hit=false,nonempty=true;int depth=0;
 size_t gc_min=argc>4?stoull(argv[4]):200000,gc_slack=argc>5?stoull(argv[5]):10000;size_t last_live=b.a.size(); auto gc=[&](){BDD fresh(n,cap);vector<int>ren(b.a.size(),-1);ren[0]=0;ren[1]=1;function<int(int)>copy=[&](int f)->int{if(ren[f]>=0)return ren[f];N z=b.a[f];return ren[f]=fresh.mk(z.v,copy(z.lo),copy(z.hi));};for(int&f:seen)f=copy(f);for(int&f:fr)f=copy(f);for(int&f:next)f=copy(f);cerr<<"midgc "<<b.a.size()<<" -> "<<fresh.a.size()<<endl;b=move(fresh);last_live=b.a.size();};
 for(;nonempty&&depth<100000&&!hit;depth++){
  if(b.image(seen[sp],sk,sv,0)){hit=true;break;}nonempty=false;
  auto add=[&](int p,int img){int z=b.DIFF(img,seen[p]);if(z){next[p]=b.OR(next[p],z);seen[p]=b.OR(seen[p],z);nonempty=true;}};
  for(int p=0;p<np;p++){if(fr[p]){if(is_re[p])add(np-1,fr[p]);for(T t:incoming[p])add(t.from,b.preimage(fr[p],t.k,t.v,t.f,t.clear,t.reset));} if(b.a.size()>max(gc_min,min(cap*7/10,last_live*8/5+gc_slack)))gc();}
  cerr<<"depth "<<depth<<" nodes "<<b.a.size()<<" nonempty "<<nonempty<<endl;fr.swap(next);fill(next.begin(),next.end(),0);
  if(b.a.size()>200000){BDD fresh(n,cap);vector<int>ren(b.a.size(),-1);ren[0]=0;ren[1]=1;function<int(int)>copy=[&](int f)->int{if(ren[f]>=0)return ren[f];N z=b.a[f];return ren[f]=fresh.mk(z.v,copy(z.lo),copy(z.hi));};for(int&f:seen)f=copy(f);for(int&f:fr)f=copy(f);cerr<<"gc "<<b.a.size()<<" -> "<<fresh.a.size()<<endl;b=move(fresh);last_live=b.a.size();}
 }
 if(!hit&&b.image(seen[sp],sk,sv,0))hit=true;U states=0;for(int f:seen)states+=b.count(f);cout<<"status "<<(hit?"ABSTRACT_WITNESS":nonempty?"CAP":"EXHAUSTED_NO_HIT")<<" bad_states "<<states<<" depth "<<depth<<" nodes "<<b.a.size()<<"\n";
 if(argc>3&&!hit&&!nonempty){BDD fresh(n,cap);vector<int>ren(b.a.size(),-1);ren[0]=1;ren[1]=0;function<int(int)>neg=[&](int f)->int{if(ren[f]>=0)return ren[f];N z=b.a[f];return ren[f]=fresh.mk(z.v,neg(z.lo),neg(z.hi));};vector<int>roots;for(int f:seen)roots.push_back(neg(f));ofstream f(argv[3]);f<<n<<' '<<np<<' '<<fresh.a.size()<<'\n';for(auto x:fresh.a)f<<x.v<<' '<<x.lo<<' '<<x.hi<<'\n';for(int r:roots)f<<r<<' ';f<<'\n';}
 }catch(exception&e){cout<<"status CAP_OR_ERROR reason "<<e.what()<<"\n";return 2;}}
