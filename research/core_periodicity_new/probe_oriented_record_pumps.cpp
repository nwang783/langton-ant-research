#include <bits/stdc++.h>
using namespace std;struct M{int a,x,y,h;};int A[4]={0,22,20,10};
pair<int,int>rot(int x,int y,int h){if(h==0)return{x,y};if(h==1)return{y,-x};if(h==2)return{-x,-y};return{-y,x};}
bool allowed(int a,int h){return(a==1&&h==3)||(a==4&&h==1)||(a==6&&h==0)||(a==7&&h==1)||(a==9&&h==0);}
int val(int x,int y,int h,int r){auto z=rot(x,y,r);return 2*(z.first+z.second)+A[(h+r)%4];}
int main(int argc,char**argv){vector<M>m;ifstream f(argv[1]);M z;while(f>>z.a>>z.x>>z.y>>z.h)m.push_back(z);mt19937_64 rng(387284);long lim=argc>2?stol(argv[2]):3000000;for(long trial=0;trial<lim;trial++){int len=4+rng()%77;vector<int>w(len);for(int&i:w)i=rng()%8;int x=0,y=0,h=0;vector<array<int,4>>vals(1);vector<int>heads{0};for(int r=0;r<4;r++)vals[0][r]=A[r];for(int i:w){auto q=rot(m[i].x,m[i].y,h);x+=q.first;y+=q.second;h=(h+m[i].h)%4;heads.push_back(h);array<int,4>v;for(int r=0;r<4;r++)v[r]=val(x,y,h,r);vals.push_back(v);}if(h||(!x&&!y))continue;bool ok=true;array<int,4>start;for(int r=0;r<4&&ok;r++){int d=vals.back()[r]-A[r],mx=A[r];for(auto v:vals)mx=max(mx,v[r]);if(d<=0){start[r]=mx;continue;}int cur=mx-d;start[r]=cur;for(int j=0;j<len;j++){if(vals[j+1][r]>cur&&!allowed(m[w[j]].a,(heads[j]+r)%4)){ok=false;break;}cur=max(cur,vals[j+1][r]);}}
if(ok){cout<<"PUMP trial "<<trial<<" drift "<<x<<' '<<y<<" startH ";for(int q:start)cout<<q<<' ';cout<<" word ";for(int i:w)cout<<m[i].a<<' ';cout<<'\n';return 0;}}
cout<<"NO_PUMP_RANDOM_CONTROL "<<lim<<'\n';}
