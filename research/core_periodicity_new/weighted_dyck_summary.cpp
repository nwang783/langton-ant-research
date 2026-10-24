// Exact finite weighted Dyck1 balanced-path closure. Discovery prototype;
// exported summaries carry finite derivation DAGs, not extrapolated stack caps.
#include <bits/stdc++.h>
using namespace std;
struct E{int u,v,k,c;};struct Proof{int u,v,w,kind,a,b,c;};
int main(int ac,char**av){ifstream f(av[1]);int n,m;f>>n>>m;vector<E>es(m);vector<vector<int>>pushin(n),popout(n);for(int i=0;i<m;i++){auto&e=es[i];f>>e.u>>e.v>>e.k>>e.c;assert(f&&abs(e.k)<=1&&0<=e.c&&e.c<=4);if(e.k==1)pushin[e.v].push_back(i);if(e.k==-1)popout[e.u].push_back(i);}string pre=ac>2?av[2]:"dyck";size_t limit=ac>3?stoull(av[3]):5000000;vector<int8_t>R(size_t(n)*n,-1);vector<int>P(size_t(n)*n,-1);vector<Proof>proof;vector<vector<int>>pred(n),succ(n);deque<pair<int,int>>q;auto add=[&](int u,int v,int w,int kind,int a,int b,int c){size_t z=size_t(u)*n+v;w=min(4,w);if(w<=R[z])return;if(R[z]<0){pred[v].push_back(u);succ[u].push_back(v);}R[z]=w;P[z]=proof.size();proof.push_back({u,v,w,kind,a,b,c});q.push_back({u,v});};for(int u=0;u<n;u++)add(u,u,0,0,-1,-1,-1);for(int i=0;i<m;i++)if(es[i].k==0)add(es[i].u,es[i].v,es[i].c,1,i,-1,-1);size_t pops=0;
while(!q.empty()){auto[u,v]=q.front();q.pop_front();pops++;size_t uv=size_t(u)*n+v;int w=R[uv],pv=P[uv];int nl=pred[u].size();for(int i=0;i<nl;i++){int a=pred[u][i];size_t au=size_t(a)*n+u;add(a,v,R[au]+w,2,P[au],pv,-1);}int nr=succ[v].size();for(int i=0;i<nr;i++){int b=succ[v][i];size_t vb=size_t(v)*n+b;add(u,b,w+R[vb],2,pv,P[vb],-1);}for(int a:pushin[u])for(int b:popout[v])add(es[a].u,es[b].v,es[a].c+w+es[b].c,3,a,pv,b);if(proof.size()>=limit){cout<<"status CAP proofs "<<proof.size()<<" pops "<<pops<<"\n";return 0;}if(pops%100000==0)cerr<<"pops "<<pops<<" proofs "<<proof.size()<<" queue "<<q.size()<<"\n";}
size_t pairs=0;for(int u=0;u<n;u++)pairs+=succ[u].size();bool sparse=ac>4&&string(av[4])=="sparse";
if(sparse){ofstream r(pre+".sparse");r<<"SPARSE "<<n<<" "<<pairs<<"\n";for(int u=0;u<n;u++)for(int v:succ[u]){size_t z=size_t(u)*n+v;r<<u<<" "<<v<<" "<<int(R[z])<<" "<<P[z]<<"\n";}}
else{ofstream r(pre+".summary");r<<n<<"\n";for(int u=0;u<n;u++){for(int v=0;v<n;v++)r<<int(R[size_t(u)*n+v])<<" ";r<<"\n";}ofstream fin(pre+".roots");for(int u=0;u<n;u++){for(int v=0;v<n;v++)fin<<P[size_t(u)*n+v]<<" ";fin<<"\n";}}
ofstream p(pre+".proof");p<<n<<" "<<proof.size()<<"\n";for(auto&v:proof)p<<v.u<<" "<<v.v<<" "<<v.w<<" "<<v.kind<<" "<<v.a<<" "<<v.b<<" "<<v.c<<"\n";
cout<<"status CLOSED nodes "<<n<<" balanced_pairs "<<pairs<<" proof_nodes "<<proof.size()<<" processed "<<pops<<"\n";
}
