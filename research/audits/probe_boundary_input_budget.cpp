#include <bits/stdc++.h>
using namespace std; using ll=long long;
struct E{int x,y,h,c;}; struct Edge{int v,k;};
vector<E> es;string word;map<pair<int,int>,int>board;long long nodes=0,checked=0,legal=0;int maxN=32;bool found=false,stopped=false;auto started=chrono::steady_clock::now();
int dxs[]={0,1,0,-1},dys[]={1,0,-1,0};
int floor_div(int x,int y){int q=x/y,r=x%y;return q-(r<0);}
void test(int dx,int dy){int P=es.size(); checked++;vector<int>ks(P);map<pair<int,int>,vector<pair<int,int>>>g;
 for(int i=0;i<P;i++){int k=floor_div(es[i].x,abs(dx))*(dx>0?1:-1);ks[i]=k;g[{es[i].x-k*dx,es[i].y-k*dy}].push_back({i-k*P,i});}
 vector<Edge>A(P,{-1,0}),B(P,{-1,0});vector<int>roots(P,0);int I=0,O=0;
 for(auto &[q,v]:g){sort(v.begin(),v.end());for(int j=1;j<(int)v.size();j++)if(es[v[j-1].second].c==es[v[j].second].c)return;
 int a=v.front().second,b=v.back().second;if(es[a].c==0){I++;roots[a]=1;}if(es[b].c==1){O++;roots[b]=1;}
 for(int j=0;j+1<(int)v.size();j++){a=v[j].second;b=v[j+1].second;if(es[a].c){A[a]={b,ks[a]-ks[b]};A[b]={a,ks[b]-ks[a]};}}
 }
 legal++;for(int i=0;i<P;i++)if(A[i].v>=0){int j=A[i].v;B[(i+1)%P]={(j+1)%P,A[i].k+(j==P-1)-(i==P-1)};}
 vector<vector<Edge>>adj(P);vector<int>seen(P,0),lift(P,0);
 for(int i=0;i<P;i++)if(!seen[i]){vector<int>st={i};seen[i]=1;vector<pair<int,int>>ends;
  while(st.size()){int a=st.back();st.pop_back();if(A[a].v<0)ends.push_back({a,lift[a]});if(B[a].v<0)ends.push_back({(a+P-1)%P,lift[a]-(a==0)});
   for(auto e:{A[a],B[a]})if(e.v>=0){if(seen[e.v]){if(lift[e.v]!=lift[a]+e.k){cerr<<"bad fiber\n";exit(2);}}else{seen[e.v]=1;lift[e.v]=lift[a]+e.k;st.push_back(e.v);}}
  }
  if(ends.size()){if(ends.size()!=2){cerr<<"bad endpoint\n";exit(3);}int a=ends[0].first,b=ends[1].first,k=ends[1].second-ends[0].second;adj[a].push_back({b,k});adj[b].push_back({a,-k});}
 }
 int S=0;fill(seen.begin(),seen.end(),0);for(int a=0;a<P;a++)if(roots[a]&&!seen[a]){int b=a,prev=-1,prevK=0,vol=0;
  do{seen[b]=1;if(adj[b].size()!=2){cerr<<"bad degree\n";exit(4);}auto e=adj[b][0];if(e.v==prev&&e.k==-prevK)e=adj[b][1];prev=b;prevK=e.k;b=e.v;vol+=e.k;}while(b!=a);S+=abs(vol);
 }
 int m=gcd(abs(dx),abs(dy));if(m*(S-1)>2*min(I,O)){cout<<"COUNTER "<<word<<" d "<<dx<<" "<<dy<<" I "<<I<<" O "<<O<<" S "<<S<<" m "<<m<<"\n";found=true;}
}
void dfs(int x,int y,int h){if(found||stopped)return;nodes++;if((nodes&4095)==0 &&chrono::duration<double>(chrono::steady_clock::now()-started).count()>15){stopped=true;return;}
 int n=es.size();if(n>=20&&h==0&&x&&y)test(x,y);if(n==maxN||found)return;
 auto q=make_pair(x,y);auto it=board.find(q);bool fresh=it==board.end();int old=fresh?-1:it->second;
 for(int c=0;c<2;c++){if(!fresh && c!=(old?0:1))continue;board[q]=c;es.push_back({x,y,h,c});word+=c?'R':'L';int nh=(h+(c?1:3))%4;dfs(x+dxs[nh],y+dys[nh],nh);word.pop_back();es.pop_back();if(found||stopped)break;}
 if(fresh)board.erase(q);else board[q]=old;
}
int main(){dfs(0,0,0);cout<<"nodes "<<nodes<<" tested "<<checked<<" stable_legal "<<legal<<" stopped "<<stopped<<" found "<<found<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-started).count()<<"\n";}
