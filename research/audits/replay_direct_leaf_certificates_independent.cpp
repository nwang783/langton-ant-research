#include <fstream>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>
#include <cstdint>
#include <string>
using namespace std;
const int W=8192,O=4096;const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
size_t ix(int x,int y){if(x< -O||x>=O||y< -O||y>=O){cerr<<"BOUNDS "<<x<<","<<y<<endl;exit(11);}return(size_t)(y+O)*W+x+O;}
int xx(int z){return z%W-O;}int yy(int z){return z/W-O;}
uint64_t mix(uint64_t z){z+=0x9e3779b97f4a7c15ULL;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
void require(bool c,const char*msg){if(!c){cerr<<msg<<endl;exit(12);}}
int main(int argc,char**argv){
 if(argc!=4)return 2;ifstream input(argv[1]),obs(argv[2]);ofstream report(argv[3]);
 vector<uint32_t>field((size_t)W*W,0);uint32_t epoch=0;vector<int>touch;
 unordered_set<int>pb,pseen;int pid=-1,px=0,py=0,ph=0,pt=0,pfx=0,pfy=0;
 auto pstep=[&](){int z=ix(px,py);bool b=pb.count(z);pseen.insert(z);if(b)pb.erase(z);else pb.insert(z);ph=(ph+(b?3:1))%4;px+=dx[ph];py+=dy[ph];pt++;};
 string H="10110000110110000110000110100001011110000100100001111010000100001111010000101100111100110000110010110110";
 long long id,oi,before,s,T,A,mass;uint64_t hash;int kind,ux,uy,sx,sy,sh,phase;long long count=0,steps=0,firstid=-1,lastid=-1;
 while(input>>id>>kind){if(firstid<0)firstid=id;lastid=id;
  require(bool(obs>>oi>>before>>s>>T>>ux>>uy>>A>>sx>>sy>>sh>>phase>>mass>>hash),"MISSING OBS");require(oi==id&&s>=before&&T-s==104&&T<=624000,"INDEX/TIMING");require(abs(ux)==2&&abs(uy)==2&&phase>=0&&phase<104,"DRIFT/PHASE");
  epoch+=2;touch.clear();auto put=[&](int z,bool black){if((field[z]&~1U)!=epoch)touch.push_back(z);field[z]=epoch+(black?1:0);};
  int x=0,y=0,h=0;
  if(kind==0){int p,at,fx,fy,ax,ay;input>>p>>at>>fx>>fy>>ax>>ay;
   if(p!=pid){pid=p;pfx=fx;pfy=fy;px=py=ph=pt=0;pb.clear();pseen.clear();pb.insert(ix(fx,fy));}
   require(pfx==fx&&pfy==fy&&pt<=at&&at==before,"PARENT SOURCE");while(pt<at)pstep();int z=ix(px,py);
   require(px==ax&&py==ay&&!pb.count(z)&&!pseen.count(z),"NOT VIRGIN SECOND CELL");
   for(int q:pb)put(q,true);put(z,true);x=px;y=py;h=ph;
  }else{require(kind==1&&before==0,"KIND");int n;input>>n;for(int j=0,a,b;j<n;j++){input>>a>>b;put(ix(a,b),true);}}
  vector<int>last;last.reserve(104);int startx=0,starty=0,starth=0;long long minphi=INT64_MAX;
  for(long long t=before;t<T;t++){
   if(t==s){startx=x;starty=y;starth=h;require(x==sx&&y==sy&&h==sh,"CLAIMED START POSE");}
   int z=ix(x,y);bool b=field[z]==epoch+1;
   if(t>=s){require((b?'1':'0')==H[(phase+t-s)%104],"NONCANONICAL ACTUAL READ");last.push_back(z);minphi=min(minphi,(long long)ux*x+(long long)uy*y);}
   put(z,!b);h=(h+(b?3:1))%4;x+=dx[h];y+=dy[h];steps++;
  }
  require(x==startx+ux&&y==starty+uy&&h==starth&&minphi>A,"END POSE/HALFPLANE");
  sort(last.begin(),last.end());vector<int>odd;for(int j=0;j<(int)last.size();){int k=j+1;while(k<(int)last.size()&&last[k]==last[j])k++;if((k-j)%2)odd.push_back(last[j]);j=k;}
  auto colT=[&](int a,int b){if(a< -O||a>=O||b< -O||b>=O)return false;return field[(size_t)(b+O)*W+a+O]==epoch+1;};
  auto colS=[&](int a,int b){bool c=colT(a,b);if(a< -O||a>=O||b< -O||b>=O)return c;return bool(c^binary_search(odd.begin(),odd.end(),(int)ix(a,b)));};
  long long m2=0;uint64_t h2=0;
  for(int q:touch){int a=xx(q),b=yy(q);bool ct=colT(a,b),cs=colS(a,b);
   if(ct){m2++;uint64_t key=(uint64_t(uint32_t(a))<<32)|uint32_t(b);h2^=mix(key);}
   if((long long)ux*a+(long long)uy*b>A&&cs)require(colT(a+ux,b+uy),"FULLFIELD FORWARD DISAGREE");
   if((long long)ux*(a-ux)+(long long)uy*(b-uy)>A&&ct)require(colS(a-ux,b-uy),"FULLFIELD BACKWARD DISAGREE");
  }
  require(m2==mass&&h2==hash,"FULL FINAL FIELD DIAGNOSTIC");if(kind==0)pstep();count++;
 }
 require(!(obs>>oi),"EXTRA OBS");report<<"PASS first="<<firstid<<" last="<<lastid<<" count="<<count<<" independent_fine_reads="<<steps<<"\n";cerr<<"PASS "<<count<<" reads="<<steps<<endl;
}
