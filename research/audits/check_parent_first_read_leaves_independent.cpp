#include <fstream>
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
int main(int argc,char**argv){if(argc!=4)return 2;ifstream plans(argv[1]),leaves(argv[2]);ofstream out(argv[3]);const int W=4096,O=2048;vector<uint32_t>b((size_t)W*W);uint32_t epoch=0;long long count=0,steps=0;int pid,fx,fy,td,cap;
auto ix=[&](int x,int y){if(x< -O||x>=O||y< -O||y>=O){cerr<<"BOUNDS";exit(3);}return(size_t)(y+O)*W+x+O;};
while(plans>>pid>>fx>>fy>>td>>cap){epoch+=4;b[ix(fx,fy)]=epoch+1;int x=0,y=0,h=0;for(int t=0;t<cap;t++){size_t z=ix(x,y);uint32_t old=(b[z]&~3U)==epoch?b[z]:epoch;bool black=old&1,seen=old&2;if(!seen&&t>=td){int p0,t0,f0,g0,a0,b0;if(!(leaves>>p0>>t0>>f0>>g0>>a0>>b0)||p0!=pid||t0!=t||f0!=fx||g0!=fy||a0!=x||b0!=y||black){cerr<<"MISMATCH "<<pid<<" "<<t;return 4;}count++;}b[z]=epoch+2+(black?0:1);h=(h+(black?3:1))%4;if(h==0)y++;if(h==1)x++;if(h==2)y--;if(h==3)x--;steps++;}}
int extra;if(leaves>>extra)return 5;if(count!=4451091||steps!=49090288)return 6;out<<"PASS all="<<count<<" parent_fine_reads="<<steps<<"\n";cerr<<count<<" "<<steps<<endl;}
