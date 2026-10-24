// Plain first-UIP CDCL proof search. No preprocessing or clause minimization.
// Output is untrusted until the separate RUP checker accepts it.
#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
struct Clause {vector<int> a;int w0=0,w1=1;};
int nv;vector<Clause> db;vector<vector<int>> watch;vector<int> val,lev,reason,trail,limits,phase;vector<double>activity;int qhead=0;double increment=1;ofstream proof;long long conflicts=0,decisions=0;
int ix(int l){return 2*abs(l)+(l<0);}int value(int l){return l>0?val[l]:-val[-l];}int dl(){return limits.size();}
bool enqueue(int l,int r){int v=value(l);if(v<0)return false;if(v==0){int x=abs(l);val[x]=l>0?1:-1;lev[x]=dl();reason[x]=r;trail.push_back(l);}return true;}
int add(vector<int>a){int id=db.size();db.push_back({a});if(a.size()>=2){watch[ix(a[0])].push_back(id);watch[ix(a[1])].push_back(id);}return id;}
int propagate(){
 while(qhead<(int)trail.size()){int bad=-trail[qhead++];auto&wl=watch[ix(bad)];size_t i=0;
  while(i<wl.size()){int id=wl[i];auto&c=db[id];int slot=c.a[c.w0]==bad?0:1;assert(c.a[slot?c.w1:c.w0]==bad);int other=slot?c.w0:c.w1;int ol=c.a[other];if(value(ol)>0){++i;continue;}
   int move=-1;for(int j=0;j<(int)c.a.size();++j)if(j!=c.w0&&j!=c.w1&&value(c.a[j])>=0){move=j;break;}
   if(move>=0){if(slot)c.w1=move;else c.w0=move;watch[ix(c.a[move])].push_back(id);wl[i]=wl.back();wl.pop_back();continue;}
   if(!enqueue(ol,id))return id;++i;
  }
 }
 return -1;
}
void cancel(int target){if(dl()<=target)return;int cut=limits[target];for(int i=(int)trail.size()-1;i>=cut;--i){int v=abs(trail[i]);phase[v]=val[v];val[v]=0;lev[v]=0;reason[v]=-1;}trail.resize(cut);limits.resize(target);qhead=trail.size();}
vector<int> analyze(int ci){
 vector<int>out(1,0);vector<char>seen(nv+1,0);int pending=0,p=0,i=trail.size()-1;
 do{
  assert(ci>=0);for(int l:db[ci].a){int v=abs(l);if(v==abs(p)||seen[v]||lev[v]==0)continue;seen[v]=1;activity[v]+=increment;if(lev[v]==dl())++pending;else out.push_back(l);}
  while(i>=0&&!seen[abs(trail[i])])--i;assert(i>=0);p=trail[i--];seen[abs(p)]=0;--pending;ci=reason[abs(p)];
 }while(pending>0);
 out[0]=-p;return out;
}
void emit(const vector<int>&a){for(int l:a)proof<<l<<' ';proof<<"0\n";}
int main(int argc,char**argv){if(argc<3)return 2;long long cap=argc>3?stoll(argv[3]):1000000;ifstream in(argv[1]);proof.open(argv[2]);string line;vector<int>initialunits;bool initialempty=false;
 while(getline(in,line)){if(line.empty()||line[0]=='c')continue;istringstream s(line);if(line[0]=='p'){string p,c;long long nc;s>>p>>c>>nv>>nc;watch.resize(2*nv+2);val.resize(nv+1);lev.resize(nv+1);reason.assign(nv+1,-1);activity.resize(nv+1);phase.assign(nv+1,-1);continue;}
  vector<int>a;int l;while(s>>l&&l){a.push_back(l);activity[abs(l)]+=0.0001;}int id=add(a);if(a.empty())initialempty=true;if(a.size()==1)initialunits.push_back(id);
 }
 if(initialempty){emit({});cout<<"UNSAT 0 0\n";return 0;}
 for(int id:initialunits)if(!enqueue(db[id].a[0],id)){emit({});cout<<"UNSAT 0 0\n";return 0;}
 long long nextrestart=100,restartspan=100;
 while(true){int conflict=propagate();if(conflict>=0){++conflicts;if(dl()==0){emit({});cout<<"UNSAT "<<conflicts<<" "<<decisions<<"\n";return 0;}if(conflicts>=cap){cout<<"UNKNOWN_CAP "<<conflicts<<"\n";return 3;}
   vector<int>a=analyze(conflict);int back=0,second=1;for(int j=1;j<(int)a.size();++j)if(lev[abs(a[j])]>back){back=lev[abs(a[j])];second=j;}if(a.size()>1)swap(a[1],a[second]);emit(a);cancel(back);int id=add(a);assert(enqueue(a[0],id));increment*=1.05;
   if(increment>1e100){for(double&x:activity)x*=1e-100;increment*=1e-100;}
   if(conflicts>=nextrestart){cancel(0);restartspan=restartspan*3/2;nextrestart=conflicts+restartspan;}
  }else{
   int v=0;for(int j=1;j<=nv;++j)if(val[j]==0&&(v==0||activity[j]>activity[v]))v=j;
   if(!v){cout<<"SAT "<<conflicts<<" "<<decisions<<"\n";return 1;}++decisions;limits.push_back(trail.size());assert(enqueue(phase[v]>0?v:-v,-1));
  }
 }
}
