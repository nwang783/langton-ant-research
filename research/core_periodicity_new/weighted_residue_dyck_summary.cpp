// Exact C-age weighted balanced closure with transverse residue modulo4.
// Balanced profiles are only0/2, by unit-edge parity. Sparse relation records
// retain proof roots; dense byte weights permit cheap failed updates.
#include <bits/stdc++.h>
using namespace std;
struct E{int u,v,k,c,t;};
struct Rel{int u,v,p,w,proof;};
struct Proof{int u,v,p,w,kind,a,b,c;};
int main(int ac,char**av){
 ifstream f(av[1]);int n,m;f>>n>>m;vector<E>es(m);vector<vector<int>>pushin(n),popout(n);
 for(int i=0;i<m;i++){auto&e=es[i];f>>e.u>>e.v>>e.k>>e.c>>e.t;assert(f&&abs(e.k)<=1&&e.c>=0&&e.c<=4&&e.t>=0&&e.t<4&&(e.t-e.k)%2==0);if(e.k==1)pushin[e.v].push_back(i);if(e.k==-1)popout[e.u].push_back(i);}
 string pre=ac>2?av[2]:"residue_dyck";size_t limit=ac>3?stoull(av[3]):5000000;
 vector<int8_t>R(size_t(n)*n*2,-1);vector<Rel>rs;vector<Proof>proof;vector<vector<int>>pred(n),succ(n);unordered_map<uint64_t,int>ids;deque<int>q;
 auto add=[&](int u,int v,int p,int w,int kind,int a,int b,int c){
  assert(p==0||p==1);uint64_t z=(uint64_t(u)*n+v)*2+p;w=min(4,w);if(w<=R[z])return;
  int rid;if(R[z]<0){rid=rs.size();ids.emplace(z,rid);rs.push_back({u,v,p,w,-1});pred[v].push_back(rid);succ[u].push_back(rid);}else{rid=ids.at(z);}
  R[z]=w;rs[rid].w=w;rs[rid].proof=proof.size();proof.push_back({u,v,p,w,kind,a,b,c});q.push_back(rid);
 };
 for(int u=0;u<n;u++)add(u,u,0,0,0,-1,-1,-1);
 for(int i=0;i<m;i++)if(es[i].k==0)add(es[i].u,es[i].v,es[i].t/2,es[i].c,1,i,-1,-1);
 size_t pops=0;
 while(!q.empty()){
  int rid=q.front();q.pop_front();Rel r=rs[rid];pops++;
  int nl=pred[r.u].size();for(int i=0;i<nl;i++){Rel a=rs[pred[r.u][i]];add(a.u,r.v,(a.p+r.p)%2,a.w+r.w,2,a.proof,r.proof,-1);}
  int nr=succ[r.v].size();for(int i=0;i<nr;i++){Rel b=rs[succ[r.v][i]];add(r.u,b.v,(r.p+b.p)%2,r.w+b.w,2,r.proof,b.proof,-1);}
  for(int ai:pushin[r.u])for(int bi:popout[r.v]){E a=es[ai],b=es[bi];int dt=(a.t+2*r.p+b.t)%4;assert(dt%2==0);add(a.u,b.v,dt/2,a.c+r.w+b.c,3,ai,r.proof,bi);}
  if(proof.size()>=limit){cout<<"status CAP proofs "<<proof.size()<<" relations "<<rs.size()<<" pops "<<pops<<"\n";return 0;}
  if(pops%100000==0)cerr<<"pops "<<pops<<" relations "<<rs.size()<<" proofs "<<proof.size()<<" queue "<<q.size()<<"\n";
 }
 ofstream out(pre+".sparse");out<<"RESIDUE_BALANCED "<<n<<" "<<rs.size()<<" 4\n";for(auto&r:rs)out<<r.u<<" "<<r.v<<" "<<2*r.p<<" "<<r.w<<" "<<r.proof<<"\n";
 ofstream pr(pre+".proof");pr<<n<<" "<<proof.size()<<" 4\n";for(auto&p:proof)pr<<p.u<<" "<<p.v<<" "<<2*p.p<<" "<<p.w<<" "<<p.kind<<" "<<p.a<<" "<<p.b<<" "<<p.c<<"\n";
 cout<<"status CLOSED nodes "<<n<<" balanced_residue_pairs "<<rs.size()<<" proof_nodes "<<proof.size()<<" processed "<<pops<<"\n";
}
