// Exact port relation from balanced(C-age, transverse-mod4) profiles.
// Unmatched height word is pop^k push^l, k<=entry depth.
#include <bits/stdc++.h>
using namespace std;struct E{int u,v,k,c,t;};struct A{int v,t,w;};
int main(int ac,char**av){
 if(ac<10){cerr<<"UNIT.dat RESIDUE.sparse PREFIX NORIG ND INITCLASS CUTOFF W LIMIT\n";return 2;}
 ifstream f(av[1]);int n,m;f>>n>>m;vector<E>es(m);for(auto&e:es)f>>e.u>>e.v>>e.k>>e.c>>e.t;
 ifstream rf(av[2]);string name;int nn,mod;size_t nr;rf>>name>>nn>>nr>>mod;assert(name=="RESIDUE_BALANCED"&&nn==n&&mod==4);vector<vector<A>>rs(n);vector<vector<pair<int,int>>>r0(n);
 for(size_t k=0;k<nr;k++){int u,v,t,w,p;rf>>u>>v>>t>>w>>p;assert(rf&&t%2==0&&w>=0&&w<=4);rs[u].push_back({v,t,w});}
 for(int u=0;u<n;u++){vector<pair<int,int>>z;for(auto a:rs[u])z.push_back({a.v,a.w});sort(z.begin(),z.end());for(auto[v,w]:z){if(r0[u].empty()||r0[u].back().first!=v)r0[u].push_back({v,w});else r0[u].back().second=max(r0[u].back().second,w);}}
 string pre=av[3];int no=stoi(av[4]),nd=stoi(av[5]),ic=stoi(av[6]),L=stoi(av[7]),W=stoi(av[8]);size_t cap=stoull(av[9]);assert(no==4*nd&&W>0);
 vector<vector<int8_t>>vs;unordered_map<string,int>interns;unordered_map<long long,int>cache;
 auto intern=[&](vector<int8_t>v){string key((char*)v.data(),v.size());auto it=interns.find(key);if(it!=interns.end())return it->second;int id=vs.size();vs.push_back(move(v));interns.emplace(move(key),id);return id;};
 auto makeRow=[&](int u){vector<int8_t>v(n*4,-1);for(auto a:rs[u])v[4*a.v+a.t]=a.w;return v;};
 auto advance=[&](int id,int kind){long long ck=(long long)id*2+(kind==1);auto it=cache.find(ck);if(it!=cache.end())return it->second;auto v=vs[id];vector<int8_t>tmp(n*4,-1),out(n*4,-1);for(auto&e:es)if(e.k==kind)for(int t=0;t<4;t++)if(v[4*e.u+t]>=0){int z=4*e.v+(t+e.t)%4;tmp[z]=max<int>(tmp[z],min(4,v[4*e.u+t]+e.c));}for(int u=0;u<n;u++)for(int t=0;t<4;t++)if(tmp[4*u+t]>=0)for(auto a:rs[u]){int z=4*a.v+(t+a.t)%4;out[z]=max<int>(out[z],min(4,tmp[4*u+t]+a.w));}int ans=intern(move(out));cache[ck]=ans;return ans;};
 vector<tuple<int,int,int>>ports;vector<vector<int>>pid(no,vector<int>(W,-1));for(int u=0;u<no;u++)for(int d=0;d<W;d++)if(((L-d-u/nd)&1)==0){pid[u][d]=ports.size();ports.emplace_back(u/nd,u%nd,d);}
 vector<array<int,4>>ans;
 for(int u=0;u<no;u++){
  vector<vector<int>>tab(W,vector<int>(W));tab[0][0]=intern(makeRow(u));for(int k=1;k<W;k++)tab[k][0]=advance(tab[k-1][0],-1);for(int k=0;k<W;k++)for(int l=1;l<W;l++)tab[k][l]=advance(tab[k][l-1],1);
  for(int d=0;d<W;d++)if(pid[u][d]>=0)for(int v=0;v<no;v++)for(int e=0;e<W;e++)if(pid[v][e]>=0)for(int t=0;t<4;t++){
   if((t-d+e)%2)continue;int w=-1;for(int k=0;k<=d;k++){int l=e-d+k;if(l>=0&&l<W)w=max<int>(w,vs[tab[k][l]][4*v+t]);}if(w>=0)ans.push_back({pid[u][d],pid[v][e],t,w});
  }
  if(vs.size()>=cap){cout<<"status CAP vectors "<<vs.size()<<" controls "<<u<<"\n";return 0;}if(u%100==0)cerr<<"controls "<<u<<" vectors "<<vs.size()<<" edges "<<ans.size()<<"\n";
 }
 // Initial low head height and transverse residue are both arbitrary. Thus
 // only projected reachability is relevant; initially no high token ages exist.
 auto adv0=[&](vector<int8_t>v,int kind){vector<int8_t>tmp(n,-1),out(n,-1);for(auto&e:es)if(e.k==kind&&v[e.u]>=0)tmp[e.v]=max<int>(tmp[e.v],min(4,v[e.u]+e.c));for(int u=0;u<n;u++)if(tmp[u]>=0)for(auto[vv,w]:r0[u])out[vv]=max<int>(out[vv],min(4,tmp[u]+w));return out;};
 vector<int8_t>ini(n,-1);for(int h=0;h<4;h++)for(auto[v,w]:r0[h*nd+ic])ini[v]=max<int>(ini[v],w);size_t iters=0;while(true){auto nxt=adv0(ini,-1);for(int v=0;v<n;v++)nxt[v]=max(nxt[v],ini[v]);iters++;if(nxt==ini)break;ini.swap(nxt);}
 vector<int>initial;auto pref=ini;for(int d=0;d<W;d++){if(d){ini=adv0(ini,1);for(int v=0;v<n;v++)pref[v]=max(pref[v],ini[v]);}for(int u=0;u<no;u++)if(pid[u][d]>=0&&pref[u]>=0)initial.push_back(pid[u][d]);}
 ofstream out(pre+".ports");out<<"RESIDUE_PORTS "<<ports.size()<<" "<<ans.size()<<" "<<initial.size()<<" 4\n";for(int p:initial)out<<p<<" ";out<<"\n";for(auto[h,d,z]:ports)out<<h<<" "<<d<<" "<<z<<"\n";for(auto a:ans)out<<a[0]<<" "<<a[1]<<" "<<a[2]<<" "<<a[3]<<"\n";
 cout<<"status COMPILED ports "<<ports.size()<<" residue_summary_edges "<<ans.size()<<" initial_low_ports "<<initial.size()<<" interned_vectors "<<vs.size()<<" prefix_iterations "<<iters<<"\n";
}
