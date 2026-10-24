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

struct Target{ll id;int t,fx,fy,x,y,cap;};
int main(int argc,char**argv){if(argc!=3)return 2;ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;Runner R;Board P;map<int,vector<Target>>parents;vector<pair<ll,vector<pair<int,int>>>>raised;ll id,total=0,parentsteps=0,copycells=0;int kind,jobs=0;
while(in>>id>>kind){if(!kind){int pid;Target z;z.id=id;in>>pid>>z.t>>z.fx>>z.fy>>z.x>>z.y>>z.cap;parents[pid].push_back(z);}else{int n,cap;in>>n;vector<pair<int,int>>cells(n);for(auto&q:cells)in>>q.first>>q.second;in>>cap;if(cap!=624000)return 3;raised.push_back({id,cells});}}
auto start=chrono::steady_clock::now();
auto child=[&](ll id,vector<pair<int,int>>&cells,int h,int before,int ox,int oy){for(auto&q:cells)if(!Board::inb(q.first,q.second)){cerr<<"initial bounds "<<id;exit(3);}Cert c=R.certify(cells,h,624000-before);if(c.oob||!c.ok||!fullcheck(R,c)){cerr<<"UNKNOWN "<<id;exit(4);}out<<id<<" "<<before+c.s<<" "<<before+c.T<<" "<<c.ux<<" "<<c.uy<<" "<<c.A+(ll)c.ux*ox+(ll)c.uy*oy<<" "<<R.X[c.s]+ox<<" "<<R.Y[c.s]+oy<<" "<<int(R.H[c.s])<<" ";for(char b:c.word)out<<(b=='1'?'L':'R');out<<"\n";total+=c.steps;jobs++;};
for(auto&group:parents){auto&ts=group.second;sort(ts.begin(),ts.end(),[](auto&a,auto&b){return a.t<b.t;});P.clear();int fx=ts[0].fx,fy=ts[0].fy;if(!Board::inb(fx,fy))return 3;int q=Board::idx(fx,fy);P.touch(q,0);P.c[q]|=1;int x=0,y=0,h=0;size_t next=0;
for(int t=0;t<=ts.back().t;t++){if(!Board::inb(x,y))return 4;int i=Board::idx(x,y);P.touch(i,t);bool first=!(P.c[i]&4);while(next<ts.size()&&ts[next].t==t){auto&z=ts[next++];if(z.fx!=fx||z.fy!=fy||z.x!=x||z.y!=y||!first||(P.c[i]&1)){cerr<<"SOURCE MISMATCH "<<z.id;return 5;}vector<pair<int,int>>cells;for(int a:P.touched)if(P.c[a]&1)cells.push_back({cx(a)-x,cy(a)-y});cells.push_back({0,0});copycells+=cells.size();child(z.id,cells,h,t,x,y);}P.c[i]|=4;int b=P.c[i]&1;P.c[i]^=1;h=(h+(b?3:1))&3;x+=DX[h];y+=DY[h];parentsteps++;}}
for(auto&z:raised)child(z.first,z.second,0,0,0,0);
cerr<<"jobs="<<jobs<<" child_reads="<<total<<" parent_reads="<<parentsteps<<" copied_black_cells="<<copycells<<" elapsed_ms="<<chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count()<<"\n";
}
