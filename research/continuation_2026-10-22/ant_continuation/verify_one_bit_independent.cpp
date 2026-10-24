#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
using Point=std::pair<int,int>;
using Field=std::set<Point>;
const std::string word="LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR";
const std::array<Point,4> unit={Point{0,1},Point{1,0},Point{0,-1},Point{-1,0}};
const Field seed={{0,-2},{0,-1},{0,0},{1,-1},{2,-1},{2,1},{3,-2},{3,1},{4,-2},{4,0},{5,-1},{5,0},{6,0}};
const Field deposit={{0,-3},{0,0},{1,-4},{1,-3},{1,-2},{2,-1},{2,0},{3,0},{6,-1},{7,-1},{7,0},{8,-1}};
struct State{Field B;Point p;int h;};
char update(State &s){
  bool black=s.B.count(s.p);
  if(black)s.B.erase(s.p);else s.B.insert(s.p);
  s.h=(s.h+(black?3:1))%4;
  s.p.first+=unit[s.h].first;s.p.second+=unit[s.h].second;
  return black?'L':'R';
}
char reverse(State &s){
  s.p.first-=unit[s.h].first;s.p.second-=unit[s.h].second;
  bool oldWhite=s.B.count(s.p);
  if(oldWhite)s.B.erase(s.p);else s.B.insert(s.p);
  s.h=(s.h+(oldWhite?3:1))%4;
  return oldWhite?'R':'L';
}
int radius(Point a,Point b){return std::max(abs(a.first-b.first),abs(a.second-b.second));}
int determinant(Point a,Point b){return a.first*b.second-a.second*b.first;}
Point diff(Point a,Point b){return {a.first-b.first,a.second-b.second};}
bool hits_tail_point(Point p,int n){
  for(auto b:deposit){
    auto d=diff(b,p);
    if(d.first%2==0 && d.second==-d.first && d.first/2>n)return true;
  }return false;
}
bool hits_tail_ray(Point p,Point drift,int n){
  const Point backwards={-2,2};
  for(auto b:deposit){
    auto d=diff(b,p);int det=determinant(drift,backwards);
    if(det){
      int j=determinant(d,backwards),k=determinant(d,drift);
      if(j%det==0 && k%det==0 && j/det>=0 && k/det>n)return true;
    }else{
      if(d.first%2 || d.second!=-d.first)continue;
      if(drift==backwards)return true;
      assert(drift==Point(2,-2));
      if(d.first/2>n)return true;
    }
  }return false;
}
int main(int argc,char**argv){
  if(argc!=2){std::cerr<<"usage: verify_one_bit_independent records.tsv\n";return 2;}
  std::ifstream file(argv[1]);assert(file.good());
  std::set<std::string> legal;
  for(int i=0;i<104;i++)legal.insert((word+word).substr(i,10));
  const int thresholds[]={8,7,9,2,1,5,1,3,5,15,7,2,2,1,2,6,1,2,5,2,3,11,21,3,4,3,2,1,13,17,1,17,3,7,1,3,18,10,7,0,14,8,3,5,9,9,4,4,9,4,5,25,9,13,2,12,7,2,0,16,9,14,12,14,0,3,2,4,14,3,4,8,11,6,12,5,12,4,4,15,14,0,0,15,1,15,0,8,0,1,0,3,1,4,2,5,8,1,3,0,3,2,1,1};
  std::set<Point> seen;
  int n,r,L,x,y,h,phase,mass,defects,last,rmax,base;
  long long replay=0,tail_steps=0;int guarded=0;
  while(file>>n>>r>>L>>x>>y>>h>>phase>>mass>>defects>>last>>rmax>>base){
    assert(r>=0&&r<104&&n>=0&&n<=thresholds[r]);assert(seen.insert({n,r}).second);
    assert(base==(n==thresholds[r]));
    // Build by literal unperturbed time, independently of the affine field formula.
    State s={seed,{0,0},2};
    for(int i=0;i<104*n+r;i++)assert(update(s)==word[i%104]);
    Field normalized;for(auto b:s.B)normalized.insert({b.first-2*n,b.second+2*n});
    s.B=normalized;s.p.first-=2*n;s.p.second+=2*n;
    Point impact=s.p;
    if(s.B.count(s.p))s.B.erase(s.p);else s.B.insert(s.p);
    State backwards=s;std::string history;
    for(int i=0;i<9;i++){
      history+=reverse(backwards);
      if(base)assert(!hits_tail_point(backwards.p,n));
    }
    std::reverse(history.begin(),history.end());
    int nd=0,ld=-1,mr=0;
    for(int i=0;i<L;i++){
      if(base)assert(!hits_tail_point(s.p,n));
      mr=std::max(mr,radius(s.p,impact));
      history+=update(s);if(history.size()>10)history.erase(history.begin());
      if(!legal.count(history)){nd++;ld=i;}
    }
    replay+=L;
    assert(s.p==Point(x,y)&&s.h==h&&int(s.B.size())==mass&&nd==defects&&ld==last&&mr==rmax);
    std::string w=word.substr(phase)+word.substr(0,phase);
    State geometry=s;std::vector<Point> positions;int rq=0,rb=0;
    // Derive the proposed geometry with an independent literal direction calculation.
    for(char c:w){
      positions.push_back(geometry.p);rq=std::max(rq,radius(geometry.p,s.p));
      geometry.h=(geometry.h+(c=='R'?1:3))%4;
      geometry.p.first+=unit[geometry.h].first;geometry.p.second+=unit[geometry.h].second;
    }
    auto drift=diff(geometry.p,s.p);assert(geometry.h==s.h&&abs(drift.first)==2&&abs(drift.second)==2);
    for(auto b:s.B)rb=std::max(rb,radius(b,s.p));
    if(base){for(auto p:positions)assert(!hits_tail_ray(p,drift,n));guarded++;}
    // For epochs k > 2(rb+rq+1), no original black cell can lie on a phase ray,
    // and every self-write offset has already occurred. Each phase color is
    // then independent of k. Literal checks through that threshold prove infinity.
    int epochs=2*(rb+rq+1)+3;
    for(int k=0;k<epochs;k++)for(char c:w)assert(update(s)==c);
    tail_steps+=104LL*epochs;
  }
  assert(seen.size()==739&&guarded==104);
  for(int r=0;r<104;r++)for(int n=0;n<=thresholds[r];n++)assert(seen.count({n,r}));
  std::cout<<"{\"cases\":"<<seen.size()<<",\"literal_recovery_steps\":"<<replay
           <<",\"independent_tail_steps\":"<<tail_steps<<",\"all_epoch_guards\":"<<guarded<<"}\n";
}
