#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using U=unsigned __int128;
struct UH{size_t operator()(U z)const{return uint64_t(z)^(uint64_t(z>>64)*0x9e3779b97f4a7c15ULL);}};
uint64_t cell(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}
int main(int argc,char**argv){
 std::string w;int count;std::cin>>w>>count;
 if(w.size()!=104)return 2;
 std::unordered_set<U,UH> phases;
 for(int j=0;j<104;j++){U v=0;for(int i=0;i<104;i++)v=(v<<1)|(w[(i+j)%104]=='L');phases.insert(v);}
 U mask=(U(1)<<104)-1;long long budget=argc>1?std::stoll(argv[1]):5000000;
 const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
 std::cout<<"seed_x,seed_y,first_end,black_at_first_end,max_radius\n";
 long long total=0,worst=0;int wx=0,wy=0;
 for(int j=0;j<count;j++){
  int bx,by;std::cin>>bx>>by;std::unordered_set<uint64_t>B;B.reserve(65536);B.insert(cell(bx,by));
  int x=0,y=0,h=0,radius=0;U code=0;long long t=0;bool found=false;
  while(t<budget){auto q=cell(x,y);auto it=B.find(q);bool black=it!=B.end();if(black)B.erase(it);else B.insert(q);
   code=((code<<1)|black)&mask;h=(h+(black?3:1))&3;x+=dx[h];y+=dy[h];t++;
   radius=std::max(radius,std::max(std::abs(x),std::abs(y)));
   if(t>=104&&phases.count(code)){found=true;break;}
  }
  std::cout<<bx<<","<<by<<","<<(found?t:-1)<<","<<B.size()<<","<<radius<<"\n";
  total+=t;if(t>worst){worst=t;wx=bx;wy=by;}
  if(j%100==99)std::cerr<<j+1<<"/"<<count<<" max="<<worst<<" total="<<total<<"\n";
 }
 std::cerr<<"FINAL total="<<total<<" max="<<worst<<" seed="<<wx<<","<<wy<<"\n";
}
