// Exact witness search on cap-three prefixes; random failures are not exclusion.
#include <bits/stdc++.h>
using namespace std;
struct Cell {int n=0; int c[3],h[3]; int e[4]={0,0,0,0}; bool seed=false;};
using Pt=pair<int,int>; const int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
int main(int argc,char**argv){long long trials=argc>1?atoll(argv[1]):1000000; mt19937_64 rng(5315923); long long nodes=0;int longest=0; 
 for(long long trial=0;trial<trials;trial++){
  map<Pt,Cell> a;vector<Pt> seed;string word;Pt p={0,0};int h=0; int massmax=5+rng()%50, prob=3+rng()%28;
  for(int step=0;step<2000;step++){
   Cell &v=a[p]; if(v.n==3)break; int c=v.n?-v.c[v.n-1]:(seed.size()<massmax && rng()%100<prob?-1:1); if(v.n==0&&c==-1){v.seed=true;seed.push_back(p);} v.c[v.n]=c;v.h[v.n]=h;v.n++;word.push_back(c==1?'R':'L'); h=(h+c+4)%4;v.e[h]++;Pt q={p.first+dx[h],p.second+dy[h]};nodes++;
   // Check newly completed doubled edge and its immediate predecessor/successor.
   if(v.e[h]==2 || v.n==3){
    vector<Pt> candidates={p};for(int k=0;k<4;k++)candidates.push_back({p.first+dx[k],p.second+dy[k]});
    for(Pt u:candidates){auto ui=a.find(u);if(ui==a.end())continue;Cell&z=ui->second;
     if(z.n!=3||z.seed||u==Pt{0,0}||u==q||z.h[0]!=z.h[1]||z.h[0]==z.h[2])continue;
     int incoming=z.h[0],out=(incoming+3)%4;
     Pt pr={u.first-dx[incoming],u.second-dy[incoming]},en={u.first+dx[out],u.second+dy[out]};
     auto pi=a.find(pr),ei=a.find(en);if(pi==a.end()||ei==a.end())continue;Cell&b=pi->second;Cell&e=ei->second;
     if(b.n!=2||e.n!=2||b.seed||e.seed||b.h[0]==b.h[1]||e.h[0]!=e.h[1]||b.e[incoming]!=2||z.e[out]!=2||pr==Pt{0,0}||en==Pt{0,0}||pr==q||en==q)continue;
     cout<<"{\"status\":\"FINITE_PREFIX_WITNESS\",\"trial\":"<<trial<<",\"nodes\":"<<nodes<<",\"word\":\""<<word<<"\",\"seed\":[";bool first=true;for(auto s:seed){if(!first)cout<<",";first=false;cout<<"["<<s.first<<","<<s.second<<"]";}cout<<"],\"path\":[["<<pr.first<<","<<pr.second<<"],["<<u.first<<","<<u.second<<"],["<<en.first<<","<<en.second<<"]]}\n";return 0;
    }
   }
   p=q;
  }
  longest=max(longest,(int)word.size());
 }
 cout<<"{\"status\":\"RANDOM_NO_WITNESS\",\"trials\":"<<trials<<",\"nodes\":"<<nodes<<",\"longest\":"<<longest<<"}\n";
}
