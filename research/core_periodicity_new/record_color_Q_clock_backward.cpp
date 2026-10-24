// Backward color cubes x upward historical-Q/latest-clock requirements.
// Register preimages are finitely enumerated then upward-closed: conservative
// even without a monotonicity assumption. Positive paths are concretely replayed.
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
struct E{int f,t,a,qo,ao;U k,v,x,c,r,fk,fv,fx,fc,fr;bool goal;};
struct N{int p,q,a,par,ei,depth;U k,v;bool live;};
int main(int ac,char**av){
 if(ac<9){cerr<<"DAT COLORBITS QSHIFT QBITS QCAP AGESHIFT LABELCAP PREFIX\n";return 2;}
 ifstream f(av[1]);int n,np,ne,nr;f>>n>>np>>ne>>nr;int sp;U sk,sv;f>>sp>>sk>>sv;int cb=stoi(av[2]),qs=stoi(av[3]),qb=stoi(av[4]),qcap=stoi(av[5]),as=stoi(av[6]);size_t cap=stoull(av[7]);string pre=av[8];assert(n==cb+qb+3&&qs==cb&&as==cb+qb&&nr==0&&sk==((1ULL<<n)-1));U cm=(1ULL<<cb)-1,qm=(1ULL<<qb)-1;
 vector<vector<int8_t>>qt,at;map<array<U,5>,int>qi,ai;
 auto table=[&](array<U,5>op,int top,auto&mp,auto&tabs){auto it=mp.find(op);if(it!=mp.end())return it->second;vector<int8_t>v(top+1,-1);for(int x=0;x<=top;x++)if((U(x)&op[0])==op[1]){U y=((U(x)^op[2])&~op[3])|(op[4]&op[3]);assert(y<=U(top));for(int r=0;r<=int(y);r++)if(v[r]<0||x<v[r])v[r]=x;}int id=tabs.size();tabs.push_back(v);mp[op]=id;return id;};
 vector<E>es(ne);vector<vector<int>>inc(np),out(np);vector<int>ge;
 for(int i=0;i<ne;i++){auto&e=es[i];int goal;f>>e.f>>e.t>>e.fk>>e.fv>>e.fx>>e.fc>>e.fr>>goal>>e.a;e.goal=goal;assert(f&&e.f!=np-1);e.k=e.fk&cm;e.v=e.fv&cm;e.x=e.fx&cm;e.c=e.fc&cm;e.r=e.fr&cm;e.qo=table({(e.fk>>qs)&qm,(e.fv>>qs)&qm,(e.fx>>qs)&qm,(e.fc>>qs)&qm,(e.fr>>qs)&qm},qcap,qi,qt);e.ao=table({(e.fk>>as)&7,(e.fv>>as)&7,(e.fx>>as)&7,(e.fc>>as)&7,(e.fr>>as)&7},4,ai,at);out[e.f].push_back(i);if(goal)ge.push_back(i);else inc[e.t].push_back(i);}
 vector<N>ns;vector<vector<int>>B(np);using Item=tuple<long long,int,int>;priority_queue<Item,vector<Item>,greater<Item>>todo;size_t retired=0,comparisons=0;int hit=-1;
 auto dominates=[&](const N&a,const N&b){comparisons++;return a.q<=b.q&&a.a<=b.a&&(a.k&~b.k)==0&&((a.v^b.v)&a.k)==0;};
 auto add=[&](int p,U k,U v,int q,int a,int par,int ei){N z{p,q,a,par,ei,par<0?0:ns[par].depth+1,k,v&k,true};auto&bs=B[p];for(int id:bs)if(ns[id].live&&dominates(ns[id],z))return;for(int id:bs)if(ns[id].live&&dominates(z,ns[id])){ns[id].live=false;retired++;}if(bs.size()>32){vector<int>x;for(int id:bs)if(ns[id].live)x.push_back(id);bs.swap(x);}int id=ns.size();ns.push_back(z);bs.push_back(id);long long score=__builtin_popcountll(k)+4*q+a;todo.emplace(score,z.depth,id);if(p==sp&&(sv&k)==z.v&&int((sv>>qs)&qm)>=q&&int((sv>>as)&7)>=a)hit=id;};
 for(int ei:ge){auto&e=es[ei];if(qt[e.qo][0]>=0&&at[e.ao][0]>=0)add(e.f,e.k,e.v,qt[e.qo][0],at[e.ao][0],-1,ei);}
 size_t pops=0;int maxdepth=0;
 while(!todo.empty()&&hit<0){auto[score,dep,id]=todo.top();todo.pop();if(!ns[id].live)continue;pops++;maxdepth=max(maxdepth,dep);N z=ns[id];if(pops%100000==0)cerr<<"pops "<<pops<<" labels "<<ns.size()<<" live "<<ns.size()-retired<<" queue "<<todo.size()<<" cost "<<score<<" depth "<<dep<<" comparisons "<<comparisons<<"\n";
  for(int ei:inc[z.p]){auto&e=es[ei];int q=qt[e.qo][z.q],a=at[e.ao][z.a];if(q<0||a<0||((z.v^e.r)&z.k&e.c))continue;U k=z.k&~e.c,v=(z.v^e.x)&k;if(((v^e.v)&k&e.k))continue;k|=e.k;v|=e.v;add(e.f,k,v,q,a,id,ei);if(ns.size()>=cap){cout<<"status CAP labels "<<ns.size()<<" live "<<ns.size()-retired<<" pops "<<pops<<" depth "<<maxdepth<<"\n";return 0;}if(hit>=0)break;}
 }
 if(hit<0){cout<<"status CUBE_EXHAUSTED_NO_INITIAL labels "<<ns.size()<<" live "<<ns.size()-retired<<" pops "<<pops<<" depth "<<maxdepth<<"\n";ofstream o(pre+".basis");o<<cb<<" "<<qs<<" "<<qb<<" "<<qcap<<" "<<as<<" "<<np<<" "<<ns.size()-retired<<"\n";for(auto&z:ns)if(z.live)o<<z.p<<" "<<z.k<<" "<<z.v<<" "<<z.q<<" "<<z.a<<"\n";return 0;}
 cout<<"status CUBE_ABSTRACT_HIT labels "<<ns.size()<<" live "<<ns.size()-retired<<" depth "<<ns[hit].depth<<" pops "<<pops<<"\n";U val=sv;int p=sp,u=hit;cout<<"START "<<p<<" "<<val<<"\n";
 auto has=[&](const N&z,U v){return(v&z.k)==z.v&&int((v>>qs)&qm)>=z.q&&int((v>>as)&7)>=z.a;};assert(has(ns[u],val));
 while(ns[u].par>=0){int dest=ns[u].par;int found=-1;U after=0;for(int ei:out[p]){auto&e=es[ei];if(e.goal||e.t!=ns[dest].p||(val&e.fk)!=e.fv)continue;U v=((val^e.fx)&~e.fc)|(e.fr&e.fc);if(has(ns[dest],v)){found=ei;after=v;break;}}if(found<0){cout<<"status CUBE_HIT_NOT_CONCRETELY_LIFTED at "<<p<<" remaining "<<ns[u].depth<<"\n";return 0;}auto&e=es[found];cout<<"EDGE "<<found<<" "<<p<<" "<<e.t<<" "<<e.a<<" "<<val<<" "<<after<<"\n";p=e.t;val=after;u=dest;}
 for(int ei:out[p]){auto&e=es[ei];if(e.goal&&(val&e.fk)==e.fv){cout<<"GOAL "<<ei<<" "<<p<<" "<<e.a<<" "<<val<<"\nstatus CONCRETE_MODEL_WITNESS\n";return 0;}}
 cout<<"status CUBE_HIT_GOAL_NOT_LIFTED\n";
}
