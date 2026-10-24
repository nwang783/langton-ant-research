#include <algorithm>
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
const int DX[4]={0,1,0,-1},DY[4]={1,0,-1,0};
const set<pair<int,int>> BLACK={{-3,0},{-3,1},{-2,1},{-1,0},{0,0},{1,1},{2,0},{3,0},{5,1},{6,1},{7,0},{7,1}};
const string H="LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR";
set<string> ALLOWED;
int P,INIT;long long nodes=0,leaves=0,diagonal=0,localbulk=0,accepted=0;
array<int,80> X,Y,TURN;string W;
map<pair<int,int>,int> lastturn;
int mod(int a,int b){int r=a%b;return r<0?r+b:r;}
bool tbit(int t,int a){return BLACK.count({t,mod(a,2)});}
int kcost(const string&w){string q;while(q.size()<w.size()+11)q+=w;int v=0;for(size_t i=0;i<w.size();i++)v+=!ALLOWED.count(q.substr(i,10))&&!ALLOWED.count(q.substr(i+1,10));return v;}
void analyze(int a){
 // Full-drift orbit representatives are selected from actual literal reads.
 vector<bool>done(P,false);vector<tuple<int,int,bool>>guard;
 for(int i=0;i<P;i++)if(!done[i]){
  vector<pair<int,int>>group;
  for(int j=i;j<P;j++)if(!done[j]&&X[j]-X[i]==Y[j]-Y[i]&&(X[j]-X[i])%a==0){
   int k=(X[j]-X[i])/a;group.push_back({j-P*k,j});done[j]=true;
  }
  sort(group.begin(),group.end());
  for(size_t j=1;j<group.size();j++)if(TURN[group[j-1].second]==TURN[group[j].second])return;
  int j=group[0].second;guard.push_back({X[j]-Y[j],X[j],TURN[j]==1});
 }
 localbulk++;
 set<int>translations;bool haveL=false;
 for(auto[t,x,b]:guard)if(b){haveL=true;for(auto z:BLACK)translations.insert(z.first-t);break;}
 if(!haveL)translations.insert(4*P+100); // A possible white-input front.
 for(int t:translations){
  if(mod(t,2))continue; // Same physical sector as the standard writer.
  for(int parity=0;parity<2;parity++){
   bool ok=true;
   for(auto[u,x,b]:guard){
    if(tbit(t+u,parity+x)!=b){ok=false;break;}
    if(mod(a,2)&&tbit(t+u,parity+x+1)!=b){ok=false;break;}
   }
   if(ok){
    accepted++;
    cout<<"ACCEPT P="<<P<<" h="<<INIT<<" drift="<<a<<","<<a<<" t="<<t<<" xparity="<<parity<<" cyclicK="<<kcost(W)<<" word="<<W<<" white="<<!haveL<<endl;
   }
  }
 }
}
void dfs(int t,int x,int y,int h){
 nodes++;
 if(t==P){leaves++;if(h==INIT&&x==y&&x){diagonal++;analyze(x);}return;}
 // Any remaining alternating-axis route must be capable of equal endpoint coordinates.
 // No unproved reachability pruning is used.
 auto key=make_pair(x,y);auto it=lastturn.find(key);int old=it==lastturn.end()?-1:it->second;
 for(int turn=0;turn<2;turn++){
  if(old==turn)continue;
  X[t]=x;Y[t]=y;TURN[t]=turn;W.push_back(turn?'L':'R');lastturn[key]=turn;
  int nh=mod(h+(turn?-1:1),4);
  dfs(t+1,x+DX[nh],y+DY[nh],nh);
  W.pop_back();if(old<0)lastturn.erase(key);else lastturn[key]=old;
 }
}
int main(int argc,char**argv){
 int maxp=argc>1?stoi(argv[1]):28;
 for(int i=0;i<104;i++)ALLOWED.insert((H+H).substr(i,10));
 auto start=chrono::steady_clock::now();
 for(P=2;P<=maxp;P+=2)for(int initial:{1,3}){
  INIT=initial;
  nodes=leaves=diagonal=localbulk=accepted=0;lastturn.clear();W.clear();dfs(0,0,0,INIT);
  double secs=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  cout<<"DONE P="<<P<<" h="<<INIT<<" nodes="<<nodes<<" leaves="<<leaves<<" diagonal="<<diagonal<<" bulk_alternating="<<localbulk<<" accepted="<<accepted<<" seconds="<<secs<<endl;
 }
}
