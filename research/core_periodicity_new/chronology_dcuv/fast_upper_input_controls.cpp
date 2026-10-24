#include <algorithm>
#include <array>
#include <cassert>
#include <chrono>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
#include <set>
using namespace std;
struct P{int x,y;};struct Geo{string word;vector<P> in,out,ctx;};
#include "fast_control_geometry.hpp"
using Key=uint64_t;
Key key(P p){return (Key)(uint32_t)p.x<<32 | (uint32_t)p.y;}
P rot(P p,int h){switch((h%4+4)%4){case 0:return p;case 1:return{p.y,-p.x};case 2:return{-p.x,-p.y};default:return{-p.y,p.x};}}
P pos;int heading=0;P world(P q){auto t=rot(q,heading);return{pos.x+t.x,pos.y+t.y};}
unordered_map<Key,char> colors;vector<pair<Key,char>> colorundo;
bool trace(string const&w){P dirs[]={{0,1},{1,0},{0,-1},{-1,0}};for(char c:w){Key q=key(pos);auto it=colors.find(q);char old=it==colors.end()?0:it->second;if(old==c)return false;colorundo.push_back({q,old});colors[q]=c;heading=(heading+(c=='R'?1:3))%4;pos.x+=dirs[heading].x;pos.y+=dirs[heading].y;}return true;}
void undo(size_t n){while(colorundo.size()>n){auto [q,c]=colorundo.back();colorundo.pop_back();if(c)colors[q]=c;else colors.erase(q);}}
struct Label{int t,a,k;};unordered_map<Key,Label> labels;vector<pair<Key,Label>> labelundo;
void setlabel(Key q,Label l){auto it=labels.find(q);labelundo.push_back({q,it==labels.end()?Label{-1,0,0}:it->second});if(l.t<0)labels.erase(q);else labels[q]=l;}
void undolabel(size_t n){while(labelundo.size()>n){auto [q,l]=labelundo.back();labelundo.pop_back();if(l.t<0)labels.erase(q);else labels[q]=l;}}
struct Event{array<int,7> row;int source,target,slot;bool upper;};
vector<int> path;vector<pair<P,int>> poses;long long candidates=0;vector<long long> counts;int limit;bool stopupper;bool skipDCCC=false;set<array<int,7>> seen;int minroots[10];
void printpath(){cout<<'[';for(size_t k=0;k<path.size();k++)cout<<(k?",":"")<<path[k];cout<<']';}
void record(vector<Event>const&events,int prevroots){if(path.size()>1){int a=path[path.size()-2];minroots[a]=min(minroots[a],prevroots);}
 for(auto&e:events){if(seen.insert(e.row).second){cout<<"EVENT {\"tuple\":[";for(int k=0;k<7;k++)cout<<(k?",":"")<<e.row[k];cout<<"],\"packet_ids\":";printpath();cout<<",\"source_index\":"<<e.source<<",\"target_index\":"<<e.target<<",\"target_input_slot\":"<<e.slot<<",\"upper_U\":"<<(e.upper?"true":"false")<<"}\n";cout.flush();}if(e.upper&&stopupper){cerr<<"FOUND_UPPER\n";exit(0);}}
}
void dfs(vector<Event>const&pending,int prevroots){
 if((int)path.size()==limit)return;
 for(int a=0;a<10;a++){
  if(skipDCCC && a==3)continue;
  candidates++;auto cp=colorundo.size();P pp=pos;int hh=heading;
  if(!trace(geometry[a].word)){undo(cp);pos=pp;heading=hh;continue;}
  auto cm=colorundo.size();P pe=pos;int he=heading;bool good=trace("LLLLRLRRRRL");undo(cm);pos=pe;heading=he;
  if(!good){undo(cp);pos=pp;heading=hh;continue;}
  int t=path.size();path.push_back(a);poses.push_back({pp,hh});counts[path.size()]++;record(pending,prevroots);
  pos=pp;heading=hh;vector<Event> next;int roots=0;
  for(int j=0;j<(int)geometry[a].in.size();j++){
   P z=geometry[a].in[j];auto it=labels.find(key(world(z)));if(it==labels.end()){roots++;continue;}auto l=it->second;auto [sp,sh]=poses[l.t];auto delta=rot({pp.x-sp.x,pp.y-sp.y},-sh);P q=geometry[l.a].out[l.k];bool upper=a>=7&&(z.x==0||z.y==4);next.push_back({{l.a,a,delta.x,delta.y,(hh-sh+4)%4,q.x,q.y},l.t,t,j,upper});
  }
  auto lp=labelundo.size();for(P z:geometry[a].ctx){Key q=key(world(z));if(labels.count(q))setlabel(q,{-1,0,0});}
  for(int k=0;k<(int)geometry[a].out.size();k++)setlabel(key(world(geometry[a].out[k])),{t,a,k});
  pos=pe;heading=he;dfs(next,roots);undolabel(lp);path.pop_back();poses.pop_back();undo(cp);pos=pp;heading=hh;
 }
}
int main(int argc,char**argv){limit=argc>1?atoi(argv[1]):8;stopupper=argc>2&&atoi(argv[2]);skipDCCC=argc>3&&atoi(argv[3]);counts.assign(limit+1,0);counts[0]=1;fill(minroots,minroots+10,100);auto t=chrono::steady_clock::now();dfs({},0);cout<<"SUMMARY {\"depth\":"<<limit<<",\"candidates\":"<<candidates+1<<",\"counts\":[";for(int k=0;k<=limit;k++)cout<<(k?",":"")<<counts[k];cout<<"],\"transfers\":"<<seen.size()<<",\"minimum_U_initial_tokens\":["<<minroots[7]<<','<<minroots[8]<<','<<minroots[9]<<"],\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<"}\n";}
