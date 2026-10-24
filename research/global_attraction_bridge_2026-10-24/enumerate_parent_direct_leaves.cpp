#include "/workspace/shared/langton/sources/imfinn-two-black/code/core.hpp"
int main(int argc,char**argv){if(argc!=3)return 2;ifstream in(argv[1]);ofstream out(argv[2]);if(!in||!out)return 2;Board B;int id,fx,fy,td,cap;long long count=0,steps=0;
while(in>>id>>fx>>fy>>td>>cap){B.clear();if(!Board::inb(fx,fy))return 3;int z=Board::idx(fx,fy);B.touch(z,0);B.c[z]|=1;int x=0,y=0,h=0;
for(int t=0;t<cap;t++){if(!Board::inb(x,y))return 4;int i=Board::idx(x,y);B.touch(i,t);bool first=!(B.c[i]&4);B.c[i]|=4;if(first&&t>=td){out<<id<<" "<<t<<" "<<fx<<" "<<fy<<" "<<x<<" "<<y<<"\n";count++;}int b=B.c[i]&1;B.c[i]^=1;h=(h+(b?3:1))&3;x+=DX[h];y+=DY[h];}steps+=cap;}
cerr<<"parent_fixed_reads="<<steps<<" direct_leaf_obligations="<<count<<"\n";}
