// Independent exhaustive finite-word check. Each first-read color branches.
// Later reads use the exact toggled cell, so all explored words are physical.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
const int OFF=128,W=256;
array<signed char,W*W> board;
struct Counts {long long M=0,H=0,EB=0,Q=0,KC=0,J0=0,Jplus=0,roof=0;array<long long,4>N{},delta{};};
uint64_t nodes=0,checks=0,old_bridge_checks=0;long long minZ=999999,minD=999999;
string word;int depth_cap;
void dfs(int x,int y,int h,int depth,Counts c){
 ++nodes;
 if(x+y<=-4&&c.M){
  ++checks;old_bridge_checks+=c.H>0;
  long long D=c.EB-c.M+2*c.H,Z=c.KC+2*D+c.H-c.Q;
  minD=min(minD,D);minZ=min(minZ,Z);
  long long D0=c.EB-c.J0,rho=c.H-c.Jplus;
  bool good=D>=0&&Z>=0&&D0>=0&&rho>=0&&D==D0+rho&&c.roof==0
   &&c.KC+2*D0>=c.Q&&Z>=c.H+2*rho&&c.M==c.J0+c.Jplus+c.H
   &&c.Q==2*c.M-c.delta[1]-3*c.H
   &&c.N[1]==4*c.M-c.delta[1]-4*c.H
   &&c.N[2]==8*c.M-4*c.delta[1]+c.delta[2]-8*c.H-4*D
   &&c.N[3]==12*c.M-8*c.delta[1]+4*c.delta[2]-c.delta[3]-8*D-4*Z;
  if(!good){cerr<<"COUNTEREXAMPLE "<<word<<" M="<<c.M<<" H="<<c.H<<" D="<<D<<" Z="<<Z<<'\n';exit(1);}
 }
 if(depth==depth_cap)return;
 int at=(y+OFF)*W+x+OFF;int old=board[at];
 for(int black=0;black<2;black++){
  if(old>=0&&old!=black)continue;
  int nh=(h+(black?3:1))&3,nx=x+dx[nh],ny=y+dy[nh];
  if(nx+ny>0)continue;
  Counts d=c;int level=x+y;
  if(level>=-3){int j=-level;d.N[j]++;d.delta[j]+=black?-1:1;
   if(j==0){d.M++;d.roof++;}
   if(j==1&&!black&&h==2&&nh==3){assert(d.roof>0);if(d.roof==1)d.J0++;else d.Jplus++;d.roof=0;}
   if(j==1&&black){if(h==2&&nh==1)d.H++;if(h==0&&nh==3)d.Q++;}
   if(j==2&&!black&&h==3&&nh==0)d.EB++;
   if(j==3&&black&&h==2&&nh==1)d.KC++;
  }
  board[at]=!black;word+=black?'L':'R';dfs(nx,ny,nh,depth+1,d);word.pop_back();board[at]=old;
 }
}
int main(int argc,char**argv){depth_cap=argc>1?atoi(argv[1]):24;int heading=argc>2?atoi(argv[2]):3;int gap=argc>3?atoi(argv[3]):4;assert(depth_cap<100&&gap<20&&(heading==1||heading==3)&&gap%2==0);board.fill(-1);dfs(0,-gap,heading,0,{});cout<<"{\"max_length\":"<<depth_cap<<",\"heading\":"<<heading<<",\"start_level\":"<<-gap<<",\"nodes\":"<<nodes<<",\"completed_prefixes\":"<<checks<<",\"bridge_prefixes\":"<<old_bridge_checks<<",\"min_D\":"<<minD<<",\"min_Z\":"<<minZ<<"}\n";}
