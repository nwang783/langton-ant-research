// Exact finite-support simulation. The step cap is NOT a proof of capture.
// A positive tail result uses the full finite-ray discrepancy criterion.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
using Point=pair<int,int>;
using Key=uint64_t;
static const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
Key key(int x,int y){return (Key(uint32_t(x))<<32)|uint32_t(y);}
Point point(Key k){return {int32_t(k>>32),int32_t(k)};}
struct Hash {size_t operator()(Key k)const{k+=0x9e3779b97f4a7c15ULL;k=(k^(k>>30))*0xbf58476d1ce4e5b9ULL;k=(k^(k>>27))*0x94d049bb133111ebULL;return k^(k>>31);}};
using Field=unordered_set<Key,Hash>;
void flip(Field&b,Key k){auto i=b.find(k);if(i==b.end())b.insert(k);else b.erase(i);}
int fdiv(int a,int b){int q=a/b,r=a%b;if(r&&((r<0)!=(b<0)))--q;return q;}
pair<Point,int> orbit(int x,int y,int vx,int vy){return {{vx*y-vy*x,((x%abs(vx))+abs(vx))%abs(vx)},fdiv(x,vx)};}
struct Data {int h;string word;vector<Point> seed;bool allowed[1024]{};set<string> rotations;};
Data load(const char*path){ifstream in(path);Data d;int n;in>>d.h>>d.word>>n;while(n--){int x,y;in>>x>>y;d.seed.push_back({x,y});}for(int i=0;i<104;i++){string w=d.word.substr(i)+d.word.substr(0,i);d.rotations.insert(w);int z=0;for(int j=0;j<10;j++)z=(z<<1)|(w[j]=='R');d.allowed[z]=true;}return d;}
bool tail(const Field&b,int x,int y,int h,const Data&data){
 int xx=x,yy=y,hh=h;vector<Point> p;Field mask;string word;
 for(int i=0;i<104;i++){p.push_back({xx,yy});Key k=key(xx,yy);bool black=bool(b.count(k))^bool(mask.count(k));flip(mask,k);word+=black?'L':'R';hh=(hh+(black?3:1))%4;xx+=dx[hh];yy+=dy[hh];}
 int vx=xx-x,vy=yy-y;if(hh!=h||abs(vx)!=2||abs(vy)!=2||!data.rotations.count(word))return false;
 map<Point,int> lower;
 for(auto [px,py]:p){auto [c,n]=orbit(px,py,vx,vy);auto it=lower.find(c);if(it==lower.end()||it->second>n+1)lower[c]=n+1;}
 auto bad=[&](int px,int py)->bool{auto [c,n]=orbit(px,py,vx,vy);auto it=lower.find(c);if(it==lower.end()||n<it->second)return false;return bool(b.count(key(px,py)))^bool(mask.count(key(px,py)))^bool(b.count(key(px-vx,py-vy)));};
 for(auto k:b){auto [px,py]=point(k);if(bad(px,py)||bad(px+vx,py+vy))return false;}
 for(auto k:mask){auto [px,py]=point(k);if(bad(px,py))return false;}
 return true;
}
void run(const Data&data,int id,int n,const vector<Point>&gate,int cap){
 Field b;b.reserve(32768);for(auto [x,y]:data.seed)b.insert(key(x,y));for(auto [x,y]:gate)b.insert(key(x-2*n,y-2*n));
 int mass0=b.size(),x=0,y=0,h=data.h,bits=0,t=0,last=-1;long long defects=0;array<char,208> recent{};bool certified=false;
 for(;t<cap;t++){
  Key q=key(x,y);bool black=b.count(q);flip(b,q);char c=black?'L':'R';recent[t%208]=c;bits=((bits<<1)|!black)&1023;if(t>=9&&!data.allowed[bits]){++defects;last=t;}
  h=(h+(black?3:1))&3;x+=dx[h];y+=dy[h];
  if(t>=207&&(t+1)%256==0&&t-last>=208){string w;for(int j=t-103;j<=t;j++)w+=recent[j%208];if(data.rotations.count(w)&&tail(b,x,y,h,data)){certified=true;++t;break;}}
 }
 cout<<id<<' '<<n<<' '<<mass0<<' '<<t<<' '<<defects<<' '<<last<<' '<<certified<<' '<<b.size()<<' '<<x<<' '<<y<<' '<<h<<'\n';
}
int main(int argc,char**argv){if(argc!=4){cerr<<"usage gate_scan standard.txt cases.txt max_steps\n";return 2;}Data d=load(argv[1]);ifstream in(argv[2]);int id,n,k,cap=stoi(argv[3]);while(in>>id>>n>>k){vector<Point>g;while(k--){int x,y;in>>x>>y;g.push_back({x,y});}run(d,id,n,g,cap);cout.flush();}}
