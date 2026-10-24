#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static uint64_t cell(int x,int y){return(uint64_t(uint32_t(x))<<32)|uint32_t(y);}
struct Node{int parent,dist;unsigned char letter,count;};
vector<Node> ns{{-1,0,2,0}};unordered_map<uint64_t,int> intern;
int mult(int s,int letter){int par=s,n=1;if(ns[s].letter==letter){par=ns[s].parent;n=ns[s].count+1;}if(n==4)return par;uint64_t key=uint64_t(par)*8+letter*4+n;auto q=intern.find(key);if(q!=intern.end())return q->second;int z=ns.size();intern[key]=z;ns.push_back({par,ns[par].dist+4-n,(unsigned char)letter,(unsigned char)n});return z;}
unordered_map<uint64_t,int>known;long long countnodes=0,cap;string prefix="RRLRRLRRLRRL",suffix;int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0},limit;
bool inH(int s){ if(!s)return true; int b=ns[s].letter;if(ns[s].count!=3)return false;while(s){if(ns[s].letter!=b||ns[s].count!=3)return false;s=ns[s].parent;if(!s||ns[s].letter==b||ns[s].count!=1)return false;s=ns[s].parent;}return true;}
bool dfs(int depth,int x,int y,int h,int s){
 if(++countnodes>cap)return false;
 if(depth>0&&inH(s)){cout<<"FOUND "<<depth<<" "<<suffix<<endl;ofstream o("/workspace/shared/langton/first_principles_new/interleaving_found.txt");o<<prefix+suffix<<endl;return true;}
 if(depth+abs(x)+abs(y)>limit||depth>=limit)return false;
 uint64_t p=cell(x,y);auto it=known.find(p);bool fresh=it==known.end();int choices[2]={0,1};int n=2;
 if(!fresh){choices[0]=it->second;n=1;}
 else if(ns[mult(s,1)].dist<ns[mult(s,0)].dist)swap(choices[0],choices[1]);
 for(int j=0;j<n;j++){int bit=choices[j];known[p]=1-bit;int hh=(h+(bit?3:1))%4;int ss=mult(s,bit);suffix.push_back(bit?'L':'R');
  if(dfs(depth+1,x+dx[hh],y+dy[hh],hh,ss))return true;
  suffix.pop_back();if(countnodes>cap)break;
 }
 if(fresh)known.erase(p);else known[p]=choices[0];return false;
}
int main(int argc,char**argv){limit=argc>1?stoi(argv[1]):100;cap=argc>2?stoll(argv[2]):10000000;
 int x=0,y=0,h=0,s=0;for(char c:prefix){int b=c=='L';auto p=cell(x,y);auto it=known.find(p);if(it!=known.end()&&it->second!=b){cerr<<"badprefix\n";return 1;}known[p]=1-b;h=(h+(b?3:1))%4;x+=dx[h];y+=dy[h];s=mult(s,b);}cout<<"START "<<x<<" "<<y<<" "<<h<<" "<<s<<" known "<<known.size()<<endl;
 bool found=dfs(0,x,y,h,s);cout<<"END found "<<found<<" nodes "<<countnodes<<" cap "<<(countnodes>cap)<<" depth "<<limit<<" groupnodes "<<ns.size()<<endl;
}
