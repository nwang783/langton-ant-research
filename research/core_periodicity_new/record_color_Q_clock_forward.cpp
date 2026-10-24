// Forward exact-color / upward-Q-and-age coverability antichain pilot.
// Specialized to the assembled historical-Q/latest-output-clock semantics,
// not an arbitrary guarded-reset model. Monotonicity requires model review.
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
struct E{int f,t;U k,v,x,c,r;int goal,a;};
struct N{int p;U val;int par,ei,depth;};
int main(int ac,char**av){
 if(ac<9){cerr<<"DAT COLORBITS QSHIFT QBITS QCAP AGESHIFT LABELCAP OUTPUT_PREFIX\n";return 2;}
 ifstream in(av[1]);int n,np,ne,nr;in>>n>>np>>ne>>nr;int sp;U sk,sv;in>>sp>>sk>>sv;int cb=stoi(av[2]),qs=stoi(av[3]),qb=stoi(av[4]),qcap=stoi(av[5]),as=stoi(av[6]);size_t limit=stoull(av[7]);string pre=av[8];assert(n==cb+qb+3&&qs==cb&&as==cb+qb&&nr==0&&sk==((1ULL<<n)-1));
 vector<E>es(ne);vector<vector<int>>adj(np),rev(np);vector<int>goals;for(int i=0;i<ne;i++){auto&e=es[i];in>>e.f>>e.t>>e.k>>e.v>>e.x>>e.c>>e.r>>e.goal>>e.a;assert(in&&e.f!=np-1);adj[e.f].push_back(i);if(e.goal)goals.push_back(i);else rev[e.t].push_back(e.f);}
 U colors=(1ULL<<cb)-1,qmask=(1ULL<<qb)-1;auto Q=[&](U x){return int((x>>qs)&qmask);};auto A=[&](U x){return int((x>>as)&7);};
 vector<int>dist(np,1000000000);queue<int>qq;for(int ei:goals)if(dist[es[ei].f]){dist[es[ei].f]=0;qq.push(es[ei].f);}while(!qq.empty()){int p=qq.front();qq.pop();for(int r:rev[p])if(dist[r]>dist[p]+1){dist[r]=dist[p]+1;qq.push(r);}}
 U goalmask=0,goalval=0;if(!goals.empty()){goalmask=es[goals[0]].k&colors;goalval=es[goals[0]].v&colors;for(int ei:goals)assert((es[ei].k&colors)==goalmask&&(es[ei].v&colors)==goalval);}
 unordered_map<U,array<int8_t,5>>best;best.reserve(limit*1.2);vector<N>ns;using Item=tuple<long long,int,int>;priority_queue<Item,vector<Item>,greater<Item>>todo;size_t retired=0;int hit=-1,ge=-1;
 auto key=[&](int p,U v){return(U(p)<<cb)|(v&colors);};
 auto add=[&](int p,U val,int par,int ei){int q=Q(val),a=A(val);assert(q>=0&&q<=qcap&&a>=0&&a<=4);if(dist[p]>=1000000000)return;U k=key(p,val);auto[it,fresh]=best.try_emplace(k);if(fresh)it->second.fill(-1);auto&b=it->second;if(b[a]>=q)return;for(int j=0;j<=a;j++)b[j]=max<int>(b[j],q);int depth=par<0?0:ns[par].depth+1;int id=ns.size();ns.push_back({p,val,par,ei,depth});int mismatch=__builtin_popcountll((val^goalval)&goalmask);long long h=4LL*dist[p]+mismatch+max(0,15-q)+(4-a);todo.emplace(h*1000+depth,depth,id);};
 add(sp,sv,-1,-1);size_t pops=0;
 while(!todo.empty()&&hit<0){auto[score,dep,id]=todo.top();todo.pop();auto z=ns[id];auto&b=best.at(key(z.p,z.val));int q=Q(z.val),a=A(z.val);if(b[a]>q||(a<4&&b[a+1]>=q)){retired++;continue;}pops++;if(pops%100000==0)cerr<<"pops "<<pops<<" labels "<<ns.size()<<" color_keys "<<best.size()<<" queue "<<todo.size()<<" depth "<<dep<<" score "<<score<<"\n";
  for(int ei:adj[z.p]){auto&e=es[ei];if((z.val&e.k)!=e.v)continue;if(e.goal){hit=id;ge=ei;break;}U v=((z.val^e.x)&~e.c)|(e.r&e.c);add(e.t,v,id,ei);if(ns.size()>=limit){cout<<"status CAP labels "<<ns.size()<<" color_keys "<<best.size()<<" pops "<<pops<<"\n";return 0;}}
 }
 if(hit<0){cout<<"status PARETO_EXHAUSTED_NO_GOAL labels "<<ns.size()<<" color_keys "<<best.size()<<" pops "<<pops<<"\n";ofstream f(pre+".front");f<<cb<<" "<<qs<<" "<<qb<<" "<<qcap<<" "<<as<<" "<<best.size()<<"\n";for(auto&[k,b]:best){f<<(k>>cb)<<" "<<(k&colors);for(int x:b)f<<" "<<x;f<<"\n";}return 0;}
 vector<int>path;for(int u=hit;u>=0;u=ns[u].par)path.push_back(u);reverse(path.begin(),path.end());cout<<"status ABSTRACT_PARETO_WITNESS labels "<<ns.size()<<" color_keys "<<best.size()<<" length "<<path.size()<<" pops "<<pops<<"\n";for(int u:path){auto&z=ns[u];if(z.par<0)cout<<"START "<<z.p<<" "<<z.val<<"\n";else{auto&e=es[z.ei];cout<<"EDGE "<<z.ei<<" "<<e.f<<" "<<e.t<<" "<<e.a<<" "<<ns[z.par].val<<" "<<z.val<<"\n";}}cout<<"GOAL "<<ge<<" "<<es[ge].f<<" "<<es[ge].a<<" "<<ns[hit].val<<"\n";
}
