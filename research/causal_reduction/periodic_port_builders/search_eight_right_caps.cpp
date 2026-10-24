// Exact bounded inverse-read search for one four-cap right-end prefix.
// Outside-cut bulk guards omitted conservatively. No renewal inference.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct P{int x,y,h;};struct U{int i,c,s;};
const int cut=-4,ylo=-10,yhi=11,H=22,XMAX=30;int width=4,maxlen=24;long long nodes=0,capnodes=3000000;bool capped=false;
vector<int> color((XMAX-cut+1)*H),seed;vector<U> undo;vector<string> words(4);string A="LRLLRRRRLLRL",B="RRRLLLLRLLLLRLLLLRRRRLRRRRLR",S="RLLR",W="LLRLRRRRLRRRRLLLLRLL";
int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
int ix(int x,int y){return (x-cut)*H+y-ylo;}bool same(P a,P b){return a.x==b.x&&a.y==b.y&&a.h==b.h;}
void rollback(size_t z){while(undo.size()>z){auto u=undo.back();undo.pop_back();color[u.i]=u.c;seed[u.i]=u.s;}}
bool read(P&p,int c){if(p.x>=cut){if(p.x>XMAX||p.y<ylo||p.y>yhi)return false;int i=ix(p.x,p.y);if(color[i]>=0&&color[i]!=c)return false;undo.push_back({i,color[i],seed[i]});if(color[i]<0)seed[i]=c;color[i]=1-c;}p.h=(p.h+(c?3:1))%4;p.x+=dx[p.h];p.y+=dy[p.h];return true;}
bool literal(string w,int n,P p){for(int k=0;k<n;k++)for(char c:w)if(!read(p,c=='L'))return false;return true;}
P starts[4]={{0,0,1},{0,2,1},{0,0,1},{0,2,1}};P targets[4]={{0,8,3},{0,8,1},{0,10,3},{-1,9,3}};
long long reached[5]={0};bool dfs(int k,P p,int t,string &word);
bool nextstage(int k){size_t z=undo.size();bool ok=true;
 if(k==0)ok=literal(S,3,targets[k])&&literal(B,2,{cut,2,1});
 if(k==1)ok=literal(W,3,targets[k])&&literal(A,2,{cut,0,1});
 if(k==2)ok=literal(S,3,targets[k])&&literal(B,2,{cut,2,1});
 if(k==3)ok=literal(S,2,targets[k]);
 if(ok){reached[k+1]++;if(k==3)return true;string w;if(dfs(k+1,starts[k+1],0,w))return true;}
 rollback(z);return false;}
bool dfs(int k,P p,int t,string &word){if(++nodes>capnodes){capped=true;return false;}if(p.x<cut||p.x>width+5||p.y<ylo||p.y>yhi)return false;
 int dist=abs(p.x-targets[k].x)+abs(p.y-targets[k].y);if(dist>maxlen-t)return false;
 if(t>0&&same(p,targets[k])){words[k]=word;return nextstage(k);}if(t==maxlen)return false;
 int c0=color[ix(p.x,p.y)];array<int,2> options={0,1};if(c0<0){auto cost=[&](int c){int h=(p.h+(c?3:1))%4;return abs(p.x+dx[h]-targets[k].x)+abs(p.y+dy[h]-targets[k].y);};if(cost(1)<cost(0))swap(options[0],options[1]);}
 for(int c:options){if(c0>=0&&c!=c0)continue;size_t z=undo.size();P q=p;if(read(q,c)){word+=c?'L':'R';if(dfs(k,q,t+1,word))return true;word.pop_back();}rollback(z);if(capped)return false;}return false;}
int main(int argc,char**argv){if(argc>1)maxlen=stoi(argv[1]);if(argc>2)width=stoi(argv[2]);if(argc>3)capnodes=stoll(argv[3]);for(int x=cut;x<=XMAX;x++)for(int y=ylo;y<=yhi;y++)color[ix(x,y)]=x<width?-1:0;seed=color;bool initial=literal(A,2,{cut,0,1});string w;bool ok=initial&&dfs(0,starts[0],0,w);cout<<"{\"status\":\""<<(ok?"PREFIX_FOUND":capped?"UNKNOWN_CAP":"EXHAUSTED")<<"\",\"nodes\":"<<nodes<<",\"maxlen\":"<<maxlen<<",\"width\":"<<width<<",\"reached\":[";for(int i=0;i<5;i++)cout<<(i?",":"")<<reached[i];cout<<"],\"words\":[";for(int i=0;i<4;i++)cout<<(i?",":"")<<'"'<<words[i]<<'"';cout<<"],\"seed\":[";bool first=true;if(ok)for(int x=cut;x<width;x++)for(int y=ylo;y<=yhi;y++)if(seed[ix(x,y)]==1){cout<<(first?"":",")<<'['<<x<<','<<y<<']';first=false;}cout<<"]}\n";}
