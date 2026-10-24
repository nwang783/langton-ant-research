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
int main(int argc,char**argv){if(argc!=3)return 2;ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;Runner R;ll id,cap,total=0;int n,jobs=0;auto start=chrono::steady_clock::now();
while(in>>id>>n){vector<pair<int,int>>cells(n);for(auto&q:cells){in>>q.first>>q.second;if(!Board::inb(q.first,q.second)){cerr<<"INITIAL BOUNDS "<<id;return 3;}}in>>cap;
 Cert c=R.certify(cells,0,cap);if(c.oob||!c.ok||!fullcheck(R,c)){cerr<<"UNKNOWN leaf "<<id<<" steps="<<c.steps<<" oob="<<c.oob<<" ok="<<c.ok;return 4;}
 out<<id<<" "<<c.s<<" "<<c.T<<" "<<c.ux<<" "<<c.uy<<" "<<c.A<<" "<<R.X[c.s]<<" "<<R.Y[c.s]<<" "<<int(R.H[c.s])<<" ";for(char b:c.word)out<<(b=='1'?'L':'R');out<<"\n";
 total+=c.steps;jobs++;}
 cerr<<"jobs="<<jobs<<" actual_reads="<<total<<" elapsed_ms="<<chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-start).count()<<"\n";
}
