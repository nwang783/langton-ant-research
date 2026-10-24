// Independent exhaustive reconstruction using first-color macro constraints and XOR parity, not last-turn walks.
#include <bits/stdc++.h>
using namespace std;const int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
struct Need{int x,y,color,flip;};struct Sig{bool valid=false;vector<Need> cells;};struct Word{string s;array<Sig,4> sig;};
vector<Word>dom[4];int chosen[4],origin[17],coarse[17];int8_t colors[256*256];uint64_t attempts=0,leaves=0;ofstream out;
Sig signature(const string&w,int heading){int x=0,y=0,h=heading;map<pair<int,int>,pair<int,int>>cells;Sig sig;for(char ch:w){int d=ch-'0',t=(d-h+4)%4;if(t!=1&&t!=3)return sig;int b=t==3;auto key=make_pair(x,y);auto it=cells.find(key);if(it==cells.end())cells[key]={b,1};else{if((it->second.first^(it->second.second&1))!=b)return sig;it->second.second++;}x+=dx[d];y+=dy[d];h=d;}sig.valid=true;for(auto [p,v]:cells)sig.cells.push_back({p.first,p.second,v.first,v.second&1});return sig;}
void dfs(int t,int heading,int h0){if(t==17){for(int d=0;d<4;d++)assert(chosen[d]>=0);out<<h0;for(int d=0;d<4;d++)out<<' '<<dom[d][chosen[d]].s;out<<'\n';leaves++;return;}
 int d=coarse[t],lo=chosen[d],hi=lo+1;bool fresh=lo<0;if(fresh){lo=0;hi=dom[d].size();}
 for(int i=lo;i<hi;i++){
  if(d==3&&dom[1][chosen[1]].s[0]=='3'&&dom[3][i].s[0]!='1')continue;
  attempts++;const Word&w=dom[d][i];const Sig&s=w.sig[heading];if(!s.valid)continue;int adr[17],old[17],m=0;bool legal=true;
  for(auto v:s.cells){int j=origin[t]+v.x*256+v.y;assert(j>=0&&j<256*256);if(colors[j]>=0&&colors[j]!=v.color){legal=false;break;}adr[m]=j;old[m]=colors[j];m++;colors[j]=v.color^v.flip;}
  if(legal){if(fresh)chosen[d]=i;dfs(t+1,w.s.back()-'0',h0);if(fresh)chosen[d]=-1;}
  for(int j=0;j<m;j++)colors[adr[j]]=old[j];
 }
}
int main(int argc,char**argv){assert(argc==4);ifstream f(argv[1]);int k,a,b;f>>k>>a>>b;assert(k==17&&a==3&&b==5);for(int d=0;d<4;d++){int n;f>>n;set<string>supplied;for(int i=0;i<n;i++){string w;f>>w;assert(supplied.insert(w).second);}set<string>found;
 for(int mask=0;mask<(1<<17);mask++){string w;int x=0,y=0;for(int j=0;j<17;j++){int z=((d&1)^(j&1))+2*((mask>>j)&1);w+=char('0'+z);x+=dx[z];y+=dy[z];}if(x!=3*dx[d]||y!=5*dy[d])continue;Word z;z.s=w;bool ok=false;for(int h=0;h<4;h++){z.sig[h]=signature(w,h);ok|=z.sig[h].valid;}if(ok){found.insert(w);dom[d].push_back(move(z));}}
 assert(found==supplied);sort(dom[d].begin(),dom[d].end(),[](auto&a,auto&b){return a.s<b.s;});cerr<<"INVENTORY "<<d<<' '<<dom[d].size()<<'\n';}
 string extra;assert(!(f>>extra));out.open(argv[2]);fill(begin(colors),end(colors),-1);
 for(int i=0;i<(int)dom[1].size();i++)for(int h:{0,2}){fill(begin(chosen),end(chosen),-1);chosen[1]=i;int x=0,y=0;for(int j=0;j<17;j++){coarse[j]=dom[1][i].s[j]-'0';origin[j]=(3*x+128)*256+5*y+128;x+=dx[coarse[j]];y+=dy[coarse[j]];}dfs(0,h,h);}
 ofstream meta(argv[3]);meta<<"{\"status\":\"PASS independent complete macro-color enumeration\",\"attempts\":"<<attempts<<",\"leaves\":"<<leaves<<",\"root_headings\":"<<dom[1].size()*2<<"}\n";cerr<<"DONE "<<attempts<<" attempts "<<leaves<<" leaves\n";
}
