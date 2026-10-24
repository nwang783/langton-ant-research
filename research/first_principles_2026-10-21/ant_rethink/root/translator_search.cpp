// Exact search for a restricted family of possible nonstandard translators.
// Word family: T C T_j D, where C,D are variable even-length connectors.
// C reverses heading, D restores it, and full displacement is (2,0).
// Finite-support acceptance uses full translation-class visit chronology.
// A completed negative search excludes only this explicitly bounded family.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
using Pt=pair<int,int>;
const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
const string T="RRRRLLRLLRRRRLLRRRRLLRLL";
struct KeyHash {size_t operator()(Pt p) const{return (uint64_t(uint32_t(p.first))*0x9e3779b97f4a7c15ULL)^uint32_t(p.second);}};
using Board=unordered_map<Pt,int,KeyHash>;
struct Step{Pt p;int old;bool fresh;};
Board state;
vector<Step> stackv;
vector<Pt> positions;
string word;
int x=0,y=0,h=0;
uint64_t nodes=0,closed_count=0,valid=0;
int gcdint(int a,int b){while(b){int c=a%b;a=b;b=c;}return abs(a);}
int floordiv(int a,int b){int q=a/b,r=a%b;if(r&&((r<0)!=(b<0)))--q;return q;}
bool push(char c){Pt p={x,y};auto it=state.find(p);int v=(c=='L');
 if(it!=state.end()&&it->second!=v)return false;
 stackv.push_back({p,v,it==state.end()});state[p]=1-v;positions.push_back(p);word+=c;
 h=(h+(v?3:1))%4;x+=dx[h];y+=dy[h];return true;}
void pop(){x-=dx[h];y-=dy[h];char c=word.back();h=(h+(c=='L'?1:3))%4;word.pop_back();positions.pop_back();auto s=stackv.back();stackv.pop_back();if(s.fresh)state.erase(s.p);else state[s.p]=s.old;}
bool fixed(const string&w){int n=0;for(char c:w){if(!push(c)){while(n--)pop();return false;}++n;}return true;}
bool infinite_tail(){
 if(h!=0||(x==0&&y==0))return false;
 map<Pt,vector<tuple<int,int,char>>> cl;
 for(int i=0;i<(int)word.size();i++){
  auto [px,py]=positions[i];int a=x?floordiv(px,x):floordiv(py,y);
  Pt b={px-a*x,py-a*y};cl[b].push_back({-a,i,word[i]});
 }
 for(auto&[b,v]:cl){sort(v.begin(),v.end());if(get<2>(v.front())!='R')return false;
  for(int i=1;i<(int)v.size();i++)if(get<2>(v[i])==get<2>(v[i-1]))return false;
 }
 return true;
}
void after_second(int left){++nodes;
 if(abs(x-2)+abs(y)>left)return;
 if(left==0){if(x==2&&y==0&&h==0){++closed_count;if(infinite_tail()){++valid;cout<<"FOUND "<<word<<'\n';cout.flush();}}return;}
 for(char c:{'R','L'})if(push(c)){after_second(left-1);pop();}
}
void connector(int left,int last,const string&second){++nodes;
 if(left==0){if(h!=2)return;if(fixed(second)){after_second(last);for(int i=0;i<24;i++)pop();}return;}
 for(char c:{'R','L'})if(push(c)){connector(left-1,last,second);pop();}
}
int main(int argc,char**argv){int total=argc>1?stoi(argv[1]):20;
 // Positive control: known P104 must pass exact infinite chronology.
 string W="RRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRR";
 if(W.size()!=104||!fixed(W)||!infinite_tail()){cerr<<"positive control failed\n";return 2;}while(!word.empty())pop();
 for(int a=2;a<=total-2;a+=2){int b=total-a;
  for(int phase=0;phase<24;phase++){
   if(!fixed(T)){cerr<<"T infeasible\n";return 3;}
   string second=T.substr(phase)+T.substr(0,phase);
   connector(a,b,second);while(!word.empty())pop();
  }
  cerr<<"connector_lengths "<<a<<' '<<b<<" nodes "<<nodes<<" ends "<<closed_count<<" accepted "<<valid<<'\n';
 }
 cout<<"SUMMARY total_connector_length="<<total<<" nodes="<<nodes<<" closed_candidates="<<closed_count<<" accepted="<<valid<<'\n';
}
