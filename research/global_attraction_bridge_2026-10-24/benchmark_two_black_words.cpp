// Fixed source-hint windows only; no search, no terminal detector, no extrapolation.
#include "/workspace/shared/langton/sources/imfinn-two-black/code/core.hpp"
#include <chrono>
int main(int argc,char**argv){
 if(argc!=3)return 2;ifstream in(argv[1]);ofstream out(argv[2]);string line;Board B;
 long long total=0;int jobs=0;auto start=chrono::steady_clock::now();
 while(getline(in,line)){
  istringstream ss(line);int id,n,x,y;ss>>id>>n;B.clear();
  for(int j=0;j<n;j++){ss>>x>>y;if(!Board::inb(x,y)){cerr<<"INITIAL OUT OF BOUNDS "<<id<<"\n";return 3;}int ix=Board::idx(x,y);B.touch(ix,0);B.c[ix]|=1;}
  int nw;ss>>nw;vector<int>times(nw);int cap=0;for(int&i:times){ss>>i;cap=max(cap,i+104);}
  vector<uint8_t>rd(cap);vector<int>px(cap+1),py(cap+1),hd(cap+1);x=y=0;int h=0;
  for(int t=0;t<cap;t++){
   if(!Board::inb(x,y)){cerr<<"HEAD OUT OF BOUNDS "<<id<<" at "<<t<<"\n";return 4;}
   px[t]=x;py[t]=y;hd[t]=h;int ix=Board::idx(x,y);B.touch(ix,t);int b=B.c[ix]&1;rd[t]=b;B.c[ix]^=1;h=(h+(b?3:1))&3;x+=DX[h];y+=DY[h];
  }
  px[cap]=x;py[cap]=y;hd[cap]=h;
  out<<id;
  for(int t:times){out<<" "<<t<<":"<<px[t]<<","<<py[t]<<","<<hd[t]<<":"<<px[t+104]-px[t]<<","<<py[t+104]-py[t]<<","<<(hd[t+104]-hd[t]+4)%4<<":";for(int j=0;j<104;j++)out<<(rd[t+j]?'L':'R');}
  out<<"\n";total+=cap;jobs++;
 }
 auto ms=chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count();cerr<<"jobs="<<jobs<<" fixed_reads="<<total<<" elapsed_ms="<<ms<<"\n";
}
