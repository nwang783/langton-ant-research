#include <bits/stdc++.h>
using namespace std;
int N;long long ct;int best;vector<pair<int,int>>path,win;bool vis[70][70];
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};
void dfs(int n,int x,int y,int d,int s){if(s>best){best=s;win=path;} if(n==N)return; for(int k=-1;k<=1;k++){int nd=(d+k+4)%4,xx=x+dx[nd],yy=y+dy[nd];if(!vis[xx][yy]){vis[xx][yy]=1;path.push_back({xx,yy});dfs(n+1,xx,yy,nd,s+k);path.pop_back();vis[xx][yy]=0;}}}
int main(int ac,char**av){N=atoi(av[1]);best=0;vis[30][30]=vis[31][30]=true;path={{30,30},{31,30}};dfs(1,31,30,0,0);cout<<N<<" "<<best<<"\n";for(auto[x,y]:win)cout<<x-30<<","<<y-30<<" ";cout<<"\n";}
