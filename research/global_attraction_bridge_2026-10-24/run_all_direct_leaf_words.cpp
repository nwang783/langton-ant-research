#include "/workspace/shared/langton/sources/imfinn-two-black/code/core.hpp"
#include <chrono>
static bool fullcheck(Runner&ru,const Cert&c){
 if(!c.ok||abs(c.ux)!=2||abs(c.uy)!=2||c.T-c.s!=104)return false;
 unordered_set<int>odd;for(ll t=c.s;t<c.T;t++){int z=Board::idx(ru.X[t],ru.Y[t]);if(!odd.erase(z))odd.insert(z);}
 auto colT=[&](int x,int y){if(!Board::inb(x,y))return false;return bool(ru.B.c[Board::idx(x,y)]&1);};
 auto colS=[&](int x,int y){if(!Board::inb(x,y))return false;int i=Board::idx(x,y);return bool((ru.B.c[i]&1)^odd.count(i));};
 for(int i:ru.B.touched){int x=cx(i),y=cy(i);if(colS(x,y)&&(ll)c.ux*x+(ll)c.uy*y>c.A&&!colT(x+c.ux,y+c.uy))return false;
 if(colT(x,y)&&(ll)c.ux*(x-c.ux)+(ll)c.uy*(y-c.uy)>c.A&&!colS(x-c.ux,y-c.uy))return false;}
 for(ll t=c.s;t<c.T;t++)if((ll)c.ux*ru.X[t]+(ll)c.uy*ru.Y[t]<=c.A)return false;
 int ht=(ru.H[c.T-1]+(ru.R[c.T-1]?3:1))&3;
 return ht==ru.H[c.s]&&c.fx==ru.X[c.s]+c.ux&&c.fy==ru.Y[c.s]+c.uy;
}

static uint64_t mix64(uint64_t z){z+=0x9e3779b97f4a7c15ULL;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
int main(int argc,char**argv){
 if(argc!=5)return 2;ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;
 ll expected=stoll(argv[3]),number=stoll(argv[4]),nextid=expected;Runner R;Board P;
 string ref="10110000110110000110000110100001011110000100100001111010000100001111010000101100111100110000110010110110";unordered_map<string,int>phases;for(int i=0;i<104;i++)phases[ref.substr(i)+ref.substr(0,i)]=i;
 ll childsteps=0,parentsteps=0,copied=0;int current=-1,fx=0,fy=0,x=0,y=0,h=0,t=0;
 auto start=chrono::steady_clock::now();
 auto stepParent=[&](){if(!Board::inb(x,y)){cerr<<"PARENT BOUNDS";exit(4);}int i=Board::idx(x,y);P.touch(i,t);P.c[i]|=4;int b=P.c[i]&1;P.c[i]^=1;h=(h+(b?3:1))&3;x+=DX[h];y+=DY[h];t++;parentsteps++;};
 auto child=[&](ll id,vector<pair<int,int>>&cells,int hin,int before,int ox,int oy){
  for(auto&q:cells)if(!Board::inb(q.first,q.second)){cerr<<"INITIAL BOUNDS "<<id;exit(3);}
  Cert c=R.certify(cells,hin,624000-before);
  if(c.oob||!c.ok||!fullcheck(R,c)){cerr<<"UNKNOWN CERTIFICATE "<<id<<" before="<<before<<" steps="<<c.steps;exit(5);}
  auto it=phases.find(c.word);if(it==phases.end()){cerr<<"NONCANONICAL "<<id<<" word="<<c.word;exit(6);}
  ll mass=0;uint64_t hash=0;for(int q:R.B.touched)if(R.B.c[q]&1){mass++;uint64_t key=(uint64_t(uint32_t(cx(q)+ox))<<32)|uint32_t(cy(q)+oy);hash^=mix64(key);}
  out<<id<<" "<<before<<" "<<before+c.s<<" "<<before+c.T<<" "<<c.ux<<" "<<c.uy<<" "<<c.A+(ll)c.ux*ox+(ll)c.uy*oy<<" "<<R.X[c.s]+ox<<" "<<R.Y[c.s]+oy<<" "<<int(R.H[c.s])<<" "<<it->second<<" "<<mass<<" "<<hash<<"\n";
  childsteps+=c.steps;
 };
 ll id;int kind;
 while(in>>id>>kind){if(id!=nextid++){cerr<<"COVERAGE ID "<<id;return 7;}
  if(kind==0){int pid,at,af,ag,ax,ay;in>>pid>>at>>af>>ag>>ax>>ay;
   if(pid!=current){if(current>=0&&pid!=current+1){cerr<<"PARENT ORDER";return 8;}current=pid;fx=af;fy=ag;x=y=h=t=0;P.clear();if(!Board::inb(fx,fy))return 3;int q=Board::idx(fx,fy);P.touch(q,0);P.c[q]|=1;}
   if(fx!=af||fy!=ag||at<t){cerr<<"SOURCE ORDER "<<id;return 9;}
   while(t<at)stepParent();if(!Board::inb(x,y))return 4;int q=Board::idx(x,y);P.touch(q,t);
   if(x!=ax||y!=ay||(P.c[q]&4)||(P.c[q]&1)){cerr<<"FIRST READ FIELD MISMATCH "<<id;return 10;}
   vector<pair<int,int>>cells;for(int a:P.touched)if(P.c[a]&1)cells.push_back({cx(a)-x,cy(a)-y});cells.push_back({0,0});copied+=cells.size();child(id,cells,h,t,x,y);stepParent();
  }else if(kind==1){int n;in>>n;vector<pair<int,int>>cells(n);for(auto&q:cells)in>>q.first>>q.second;child(id,cells,0,0,0,0);}else return 11;
  if(!in){cerr<<"TRUNCATED INPUT";return 12;}
 }
 if(nextid!=expected+number){cerr<<"COVERAGE COUNT";return 13;}
 cerr<<"COMPLETE first="<<expected<<" count="<<number<<" child_reads="<<childsteps<<" parent_reads="<<parentsteps<<" copied_black="<<copied<<" elapsed_ms="<<chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count()<<"\n";
}
