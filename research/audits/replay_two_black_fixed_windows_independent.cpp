#include <iostream>
#include <fstream>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;
// Independent epoch-tag complete finite field; no retained simulator headers.
int main(int argc,char**argv){
 if(argc!=3)return 2; ifstream in(argv[1]);ofstream out(argv[2]);
 const int W=4096,O=W/2; vector<uint32_t> b((size_t)W*W,0);
 auto at=[&](int x,int y)->size_t{if(x< -O||x>=O||y< -O||y>=O){cerr<<"OUT OF GRID "<<x<<","<<y<<endl;exit(3);}return(size_t)(y+O)*W+x+O;};
 int id,n;uint32_t epoch=0;long long reads=0;int jobs=0;
 while(in>>id>>n){epoch+=2;for(int i=0,x,y;i<n;i++){in>>x>>y;b[at(x,y)]=epoch+1;}
  int nw;in>>nw;vector<int> ts(nw);for(int &t:ts)in>>t;int stop=*max_element(ts.begin(),ts.end())+104;
  vector<int> xs(stop+1),ys(stop+1),hs(stop+1);string turns(stop,'?');int x=0,y=0,h=0;
  for(int t=0;t<stop;t++){
   xs[t]=x;ys[t]=y;hs[t]=h;size_t j=at(x,y);bool black=b[j]==epoch+1;b[j]=black?epoch:epoch+1;turns[t]=black?'L':'R';
   if(black)h=(h+3)%4;else h=(h+1)%4;
   switch(h){case 0:y++;break;case 1:x++;break;case 2:y--;break;case 3:x--;break;}
  }
  xs[stop]=x;ys[stop]=y;hs[stop]=h;out<<id;
  for(int t:ts)out<<' '<<t<<':'<<xs[t]<<','<<ys[t]<<','<<hs[t]<<':'<<xs[t+104]-xs[t]<<','<<ys[t+104]-ys[t]<<','<<(hs[t+104]-hs[t]+4)%4<<':'<<turns.substr(t,104);
  out<<'\n';reads+=stop;jobs++;
 }
 cerr<<"jobs="<<jobs<<" reads="<<reads<<'\n';return jobs==102488&&reads==3437614232LL?0:4;
}
