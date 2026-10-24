// Complete literal-word check of ONE fixed 32-step/full-drift8 target.
// No interface-window bound. This is not an all-length exclusion.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
const int N=32,D=8,H=5,DX[4]={0,1,0,-1},DY[4]={1,0,-1,0},want[4]={8,12,8,4};
uint64_t nodes=0,leaves=0,survivors=0;int lastread[32][H],ct[4],xx[N],yy[N],bb[N],yroot,xroot;string word;
bool inp(int a,int y){return a%2==1&&y==1;}
bool outp(int a,int y){return y==0||y==2||(a%2==1&&y==3);}
bool profile(){
 vector<pair<int,int>> v[8][5];
 for(int t=0;t<N;t++){int a=(xx[t]%8+8)%8;v[a][yy[t]].push_back({8*t-32*xx[t],bb[t]});}
 for(int a=0;a<8;a++)for(int y=0;y<5;y++){
  auto &z=v[a][y];sort(z.begin(),z.end());int c=inp(a,y);
  for(auto e:z){if(e.second!=c)return false;c^=1;}
  if(c!=outp(a,y))return false;
 }
 return true;
}
void dfs(int t,int x,int y,int h,int L){
 nodes++;if(L>8||L+N-t<8)return;
 if(t==N){if(x!=xroot+8||y!=yroot||h!=1||L!=8)return;leaves++;if(profile()){survivors++;cout<<"SURVIVOR "<<xroot<<" "<<yroot<<" "<<word<<"\n";}return;}
 int prior=lastread[x+8][y];
 for(int b=0;b<2;b++){
  if(b==prior)continue;
  int hh=(h+(b?3:1))%4;
  if(ct[hh]>=want[hh])continue;
  int nx=x+DX[hh],ny=y+DY[hh];
  if(ny<0||ny>=H)continue;
  if(nx< xroot-4||nx>xroot+12)continue;
  int rem=N-t-1;
  if(abs(nx-(xroot+8))+abs(ny-yroot)>rem)continue;
  lastread[x+8][y]=b;ct[hh]++;xx[t]=x;yy[t]=y;bb[t]=b;word.push_back(b?'L':'R');
  dfs(t+1,nx,ny,hh,L+b);
  word.pop_back();ct[hh]--;lastread[x+8][y]=prior;
 }
}
int main(){
 for(xroot=0;xroot<=1;xroot++)for(yroot=0;yroot<H;yroot++){
  for(auto &r:lastread)for(int &x:r)x=-1;
  dfs(0,xroot,yroot,1,0);
 }
 cout<<"{\"status\":\"COMPLETE_ONE_FIXED_TARGET\",\"length\":32,\"drift\":[8,0],\"read_height\":5,\"roots\":10,\"nodes\":"<<nodes<<",\"literal_endpoint_leaves\":"<<leaves<<",\"survivors\":"<<survivors<<"}\n";
}
