#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
// Compass N,E,S,W. Fixed ant geometry; every output record is a first
// repeated-cell equal-turn conflict time, or 65535 for a bounded survivor.
constexpr int H=32768;
struct Slot {uint64_t key=0; uint32_t stamp=0; int time=0; int turn=0;};
array<Slot,H> table;
uint32_t stamp=0;
int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
struct Witness {int time,previous,x,y,turn;};
Witness replay(const array<vector<int>,4>& im,int root,int heading,int cap) {
 ++stamp; int k=im[0].size(),x=0,y=0,h=heading;
 // Choose an even depth: every axis-preserving first-letter map obeying
 // half-turn symmetry fixes each letter after two applications.
 int depth=2; uint64_t len=uint64_t(k)*k;
 while(len<uint64_t(cap)){depth+=2;len*=uint64_t(k)*k;}
 vector<int> powers(depth);powers[0]=1;for(int j=1;j<depth;j++)powers[j]=powers[j-1]*k;
 for(int n=0;n<cap;n++){
  int d=root;
  for(int j=depth-1;j>=0;j--)d=im[d][(n/powers[j])%k];
  int turn=(d-h+4)%4;
  if(turn!=1 && turn!=3){cerr<<"AXIS ERROR\n";exit(2);}
  uint64_t key=(uint64_t(uint32_t(x))<<32)|uint32_t(y);
  uint64_t z=key+0x9e3779b97f4a7c15ULL;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;z^=z>>31;
  int idx=z&(H-1);
  while(table[idx].stamp==stamp && table[idx].key!=key)idx=(idx+1)&(H-1);
  Slot &s=table[idx];
  if(s.stamp==stamp && s.turn==turn)return {n,s.time,x,y,turn};
  s={key,stamp,n,turn};x+=dx[d];y+=dy[d];h=d;
 }
 return {65535,-1,x,y,0};
}
int main(int argc,char**argv){
 if(argc!=6){cerr<<"inventory cap start_pair end_pair outprefix\n";return 2;}
 ifstream in(argv[1]);int k,ne,nn;in>>k>>ne>>nn;
 vector<vector<int>> E(ne),N(nn);string s;
 for(auto*vs:{&E,&N})for(auto &v:*vs){in>>s;for(char c:s)v.push_back(c-'0');if(int(v.size())!=k)return 2;}
 int cap=stoi(argv[2]);if(cap>=65535)return 2;
 uint64_t begin=stoull(argv[3]),end=stoull(argv[4]);if(end==0)end=uint64_t(ne)*nn;
 if(end>uint64_t(ne)*nn || begin>end)return 2;
 string prefix=argv[5];ofstream records(prefix+".u16",ios::binary),surv(prefix+".survivors.jsonl");
 array<vector<int>,4> im;for(auto&v:im)v.resize(k);
 uint64_t cases=0,survivors=0;int latest=-1;uint64_t latestpair=0;int latestroot=0,latestheading=0;Witness latestw{};
 auto start=chrono::steady_clock::now();
 for(uint64_t p=begin;p<end;p++){
  int ie=p/nn,jn=p%nn;im[1]=E[ie];im[0]=N[jn];
  for(int j=0;j<k;j++){im[3][j]=(im[1][j]+2)%4;im[2][j]=(im[0][j]+2)%4;}
  for(int root:{1,0})for(int h:{(root+3)%4,(root+1)%4}){
   Witness w=replay(im,root,h,cap);uint16_t t=w.time;records.write(reinterpret_cast<char*>(&t),2);cases++;
   if(t==65535){survivors++;surv<<"{\"pair\":"<<p<<",\"east\":"<<ie<<",\"north\":"<<jn<<",\"root\":"<<root<<",\"heading\":"<<h<<"}\n";}
   else if(w.time>latest){latest=w.time;latestpair=p;latestroot=root;latestheading=h;latestw=w;}
  }
  if((p+1)%100000==0){double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();cerr<<"pairs "<<p+1<<" cases "<<cases<<" survivors "<<survivors<<" latest "<<latest<<" seconds "<<secs<<"\n";}
 }
 double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 cout<<"{\"k\":"<<k<<",\"east_images\":"<<ne<<",\"north_images\":"<<nn<<",\"start_pair\":"<<begin<<",\"end_pair\":"<<end<<",\"cases\":"<<cases<<",\"survivors\":"<<survivors<<",\"cap\":"<<cap<<",\"latest_conflict\":{\"time\":"<<latest<<",\"pair\":"<<latestpair<<",\"east\":"<<latestpair/nn<<",\"north\":"<<latestpair%nn<<",\"root\":"<<latestroot<<",\"heading\":"<<latestheading<<",\"previous\":"<<latestw.previous<<",\"x\":"<<latestw.x<<",\"y\":"<<latestw.y<<",\"turn\":"<<latestw.turn<<"},\"seconds\":"<<secs<<"}\n";
}
