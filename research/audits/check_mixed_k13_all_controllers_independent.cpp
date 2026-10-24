// Complete Cartesian-product replay, no lazy assignment or author imports.
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;
struct W{array<int,13>d;int H;};
vector<W> words[4];const int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
static int stamp[1001][1001],color[1001][1001];int epoch=0;
int main(int argc,char**argv){ifstream f(argv[1]);for(int s=0;s<4;s++){int n;f>>n;while(n--){string w;W a;f>>w>>a.H;for(int j=0;j<13;j++)a.d[j]=w[j]-'0';words[s].push_back(a);}}
 long long total=0,gn=0,cases=0,late=0;array<long long,501> hist{};
 for(auto &N:words[0])for(auto &E:words[1])for(auto &S:words[2])for(auto &W:words[3]){
  total++;array<const struct W*,4> im={&N,&E,&S,&W};
  if(E.d[0]!=W.d[0]&&E.H!=W.H){gn++;continue;}
  int root=E.d[0]==1?1:(W.d[0]==3?3:1);
  assert(im[im[root]->d[0]]->d[0]==root);
  for(int initial:{0,2}){
   ++epoch;int x=500,y=500,h=initial;bool failed=false;
   for(int t=0;t<500;t++){
    int z=root,a=t;array<int,4>ds{};for(int j=3;j>=0;j--){ds[j]=a%13;a/=13;}
    for(int d:ds)z=im[z]->d[d];int turn=(z-h+4)%4;assert(turn==1||turn==3);
    assert(x>=0&&x<=1000&&y>=0&&y<=1000);
    if(stamp[x][y]==epoch&&color[x][y]!=(turn==3)){
     hist[t]++;late=max(late,(long long)t);failed=true;break;
    }
    stamp[x][y]=epoch;color[x][y]=!(turn==3);x+=dx[z];y+=dy[z];h=z;
   }
   if(!failed){cerr<<"UNRESOLVED controller at finite bound\n";return 2;}cases++;
  }
 }
 assert(total==1863225&&gn==581175&&cases==2564100&&late==221);
 cout<<"{\"status\":\"PASS complete independent Cartesian product\",\"controllers\":"<<total<<",\"vertex_theorem_cases\":"<<gn<<",\"residual_root_heading_replays\":"<<cases<<",\"latest_conflict\":"<<late<<",\"histogram\":{";
 bool first=true;for(int i=0;i<=500;i++)if(hist[i]){if(!first)cout<<',';first=false;cout<<'\"'<<i<<"\":"<<hist[i];}cout<<"}}\n";
}
