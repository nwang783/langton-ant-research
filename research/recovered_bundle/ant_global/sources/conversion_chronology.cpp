// Periodic converter gluing on an arbitrary periodic input substrate.
// Every rejection is a necessary exact integer condition.
// Ordered crossings between a fixed pair of physical cells are matched in order.
// The input specifies every row's total visit count; no period timeout is implicit.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
struct Node {int s,r,k,h,c,a,b,next=-1,prev=-1,lift=0;};
struct Link {int node,lift;};
using Row=array<vector<int>,2>;
vector<Node> nodes;
int lo,hi,P,uid,phase[4]{},heads[4]{},outs[4]{},U[64][2]{},V[64][2]{},rowN[64]{};
uint64_t trials=0,order_rejects=0,cycle_rejects=0,direction_rejects=0,solutions=0;
bool stop_first=false,found=false,timed=false;
double limit_seconds=0;
chrono::steady_clock::time_point started;
int at(int s){return s-lo;}
int parity(int z){return (z%2+2)%2;}
void attach(int i,int j,int lift){
 if(nodes[i].next>=0||nodes[j].prev>=0)throw runtime_error("occupied edge");
 nodes[i].next=j;nodes[i].lift=lift;nodes[j].prev=i;
}
void append(int s,int r,int k,int a,const Link* in,const Link* out){
 int c=U[at(s)][r]^(k&1);
 int h=parity(s)?(a?0:2):(a?3:1);
 int oh=(h+(c?3:1))&3;
 int b=(dx[oh]-dy[oh])==1;
 int n=nodes.size();nodes.push_back({s,r,k,h,c,a,b});
 phase[2*r+parity(s)]++;heads[h]++;outs[oh]++;
 if(a){if(!in)throw runtime_error("missing incoming");attach(in->node,n,in->lift);}
 if(b){if(!out)throw runtime_error("missing outgoing");attach(n,out->node,out->lift);}
}
void pop(){
 int n=nodes.size()-1;auto nd=nodes.back();
 if(nd.prev>=0){nodes[nd.prev].next=-1;nodes[nd.prev].lift=0;}
 if(nd.next>=0)nodes[nd.next].prev=-1;
 phase[2*nd.r+parity(nd.s)]--;heads[nd.h]--;outs[(nd.h+(nd.c?3:1))&3]--;
 nodes.pop_back();
}
bool feasible(){
 ++trials;
 if(limit_seconds>0 && (trials&16383)==0 && chrono::duration<double>(chrono::steady_clock::now()-started).count()>limit_seconds){timed=true;return false;}
 for(int h=0;h<4;h++){
  int bound=P/4+((h<2)?1:-1);
  if(heads[h]>bound||outs[h]>bound||phase[h]>P/4){direction_rejects++;return false;}
 }
 int n=nodes.size(),chains=0,seen=0;
 vector<int> chain(n,-1),off(n),dist;
 for(int root=0;root<n;root++)if(nodes[root].prev<0){
  int j=root,pos=0,lift=0;
  while(j>=0){
   if(chain[j]>=0)throw runtime_error("merged paths");
   chain[j]=chains;off[j]=pos-lift*P;seen++;pos++;
   lift+=nodes[j].lift;j=nodes[j].next;
  }
  chains++;
 }
 if(seen<n){cycle_rejects++;return false;}
 struct Edge{int a,b,w;};vector<Edge> constraints;
 for(int i=0;i<n;i++)if(nodes[i].k){
  if(i==0||nodes[i-1].s!=nodes[i].s||nodes[i-1].r!=nodes[i].r||nodes[i-1].k!=nodes[i].k-1)throw runtime_error("bad rank");
  int a=chain[i-1],b=chain[i],w=4+off[i-1]-off[i];
  if(a==b){if(w>0){order_rejects++;return false;}}
  else constraints.push_back({a,b,w});
 }
 dist.assign(chains,0);
 for(int it=0;it<chains;it++){
  bool change=false;
  for(auto e:constraints)if(dist[e.b]<dist[e.a]+e.w){dist[e.b]=dist[e.a]+e.w;change=true;}
  if(!change)return true;
 }
 order_rejects++;return false;
}
void finish(){
 if(int(nodes.size())!=P)throw runtime_error("wrong full size");
 vector<int> seen(P),off(P);int i=0,lift=0,pos=0;string word;
 while(i>=0&&!seen[i]){
  seen[i]=1;off[i]=pos-lift*P;pos++;word+=nodes[i].c?'L':'R';
  lift+=nodes[i].lift;i=nodes[i].next;
 }
 if(i!=0||pos!=P||lift!=1){cycle_rejects++;return;}
 for(int j=0;j<P;j++)if(nodes[j].k&&off[j]<=off[j-1]){order_rejects++;return;}
 solutions++;found=true;
 cout<<"SOLUTION "<<uid<<' '<<nodes[0].r<<' '<<nodes[0].r-nodes[0].s<<' '<<nodes[0].h<<' '<<word<<'\n'<<flush;
}
void row(int s,const Row&upper){
 if(timed||(stop_first&&found))return;
 if(s<lo){finish();return;}
 array<vector<Link>,2> incoming,outgoing;
 if(s<hi){
  for(int r=0;r<2;r++)for(int id:upper[r]){
   auto nd=nodes[id];int oh=(nd.h+(nd.c?3:1))&3;
   if(!nd.b){
    int x=nd.r+dx[oh],r2=parity(x);
    incoming[r2].push_back({id,(x-r2)/2});
   }
   if(!nd.a){
    int x=nd.r-dx[nd.h],r2=parity(x);
    // predecessor physical point is current representative plus 2*k.
    // Translate its edge back to the representative current point.
    outgoing[r2].push_back({id,-(x-r2)/2});
   }
  }
 }
 Row now;
 function<void(int,int,int,int,int,int,int)> fill;
 // lane, total lane length, rank, used incoming/outgoing, remaining a at q0/q1
 fill=[&](int r,int n,int k,int ni,int no,int left0,int left1){
  if(timed||(stop_first&&found))return;
  if(k==n){
   if(ni!=int(incoming[r].size())||no!=int(outgoing[r].size())||left0||left1)throw runtime_error("bad lane endpoint");
   if(r==0){
    int m=rowN[at(s)]-n;
    int q1=0;for(int j=0;j<m;j++)q1+=U[at(s)][1]^(j&1)^(!parity(s));
    int aa=int(incoming[1].size())+q1-int(outgoing[1].size());
    if(aa%2)return;
    int a1=aa/2,a0=int(incoming[1].size())-a1;
    if(min(a0,a1)<0||a1>q1||a0>m-q1)return;
    fill(1,m,0,0,0,a0,a1);
   }else row(s-1,now);
   return;
  }
  int q=U[at(s)][r]^(k&1)^(!parity(s));
  for(int a=0;a<2;a++){
   int b=a^q;
   if(ni+a>int(incoming[r].size())||no+b>int(outgoing[r].size()))continue;
   int l0=left0-(!q&&a),l1=left1-(q&&a);
   if(min(l0,l1)<0)continue;
   int rem1=0;for(int j=k+1;j<n;j++)rem1+=U[at(s)][r]^(j&1)^(!parity(s));
   if(l1>rem1||l0>n-k-1-rem1)continue;
   int id=nodes.size();append(s,r,k,a,a?&incoming[r][ni]:nullptr,b?&outgoing[r][no]:nullptr);
   now[r].push_back(id);
   if(int(nodes.size())==P||feasible())fill(r,n,k+1,ni+a,no+b,l0,l1);
   now[r].pop_back();pop();
  }
 };
 int nrow=rowN[at(s)];
 for(int n=0;n<=nrow;n++){
  int m=nrow-n;
  if((n&1)!=(U[at(s)][0]^V[at(s)][0])||(m&1)!=(U[at(s)][1]^V[at(s)][1]))continue;
  int q1=0;for(int k=0;k<n;k++)q1+=U[at(s)][0]^(k&1)^(!parity(s));
  int aa=int(incoming[0].size())+q1-int(outgoing[0].size());
  if(aa%2)continue;
  int a1=aa/2,a0=int(incoming[0].size())-a1;
  if(min(a0,a1)<0||a1>q1||a0>n-q1)continue;
  fill(0,n,0,0,0,a0,a1);
 }
}
int main(int argc,char**argv){
 if(argc<2){cerr<<"usage conversion_chronology INPUT [seconds_per_profile] [stop_first]\n";return 2;}
 if(argc>2)limit_seconds=stod(argv[2]);if(argc>3)stop_first=stoi(argv[3]);
 ifstream in(argv[1]);
 while(in>>uid>>lo>>hi>>P){
  if(hi-lo>=64||P%4)throw runtime_error("unsupported input");
  for(int s=lo;s<=hi;s++)in>>U[at(s)][0]>>U[at(s)][1]>>V[at(s)][0]>>V[at(s)][1]>>rowN[at(s)];
  nodes.clear();fill(begin(phase),end(phase),0);fill(begin(heads),end(heads),0);fill(begin(outs),end(outs),0);
  trials=order_rejects=cycle_rejects=direction_rejects=solutions=0;found=timed=false;
  started=chrono::steady_clock::now();Row empty;row(hi,empty);
  double elapsed=chrono::duration<double>(chrono::steady_clock::now()-started).count();
  cout<<"RESULT "<<uid<<' '<<(timed?"timeout":(stop_first&&found?"positive_stop":"complete"))<<' '<<P<<' '<<trials<<' '<<order_rejects<<' '<<cycle_rejects<<' '<<direction_rejects<<' '<<solutions<<' '<<elapsed<<'\n'<<flush;
 }
}
