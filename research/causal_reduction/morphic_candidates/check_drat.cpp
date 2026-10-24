// Independent finite DRAT checker. Inputs are DIMACS clauses and text DRAT.
// Every addition is checked by RUP or the defining RAT resolvent condition.
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
using namespace std;
struct Cl {vector<int> a;int w0=0,w1=1;bool active=true;};
int nv=0;vector<Cl> db;vector<vector<int>> watches,occ;vector<int> units;
unordered_map<string,vector<int>> bykey;unordered_set<string> originals;
long long rups=0,rats=0,calls=0,inputs=0,deletes=0,adds=0;bool finalempty=false;
int ix(int l){return 2*abs(l)+(l<0);}
string key(vector<int> a){sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());string s;for(int l:a)s+=to_string(l)+",";return s;}
vector<int> canon(vector<int>a){sort(a.begin(),a.end());a.erase(unique(a.begin(),a.end()),a.end());return a;}
bool taut(const vector<int>&a){for(int l:a)if(binary_search(a.begin(),a.end(),-l))return true;return false;}
void add(vector<int>a){a=canon(a);int id=db.size();db.push_back({a});bykey[key(a)].push_back(id);if(a.size()<2)units.push_back(id);else{watches[ix(a[0])].push_back(id);watches[ix(a[1])].push_back(id);}for(int l:a)occ[ix(l)].push_back(id);}
void del(const vector<int>&a){auto it=bykey.find(key(a));if(it==bykey.end())return;auto&v=it->second;while(!v.empty()&&!db[v.back()].active)v.pop_back();if(!v.empty()){db[v.back()].active=false;v.pop_back();}}
bool rup(const vector<int>&a){
 ++calls;vector<signed char> val(nv+1,0);vector<int> trail;
 auto value=[&](int l){return l>0?int(val[l]):-int(val[-l]);};
 auto enqueue=[&](int l){int z=value(l);if(z<0)return false;if(z==0){val[abs(l)]=l>0?1:-1;trail.push_back(l);}return true;};
 for(int id:units)if(db[id].active){auto&b=db[id].a;if(b.empty())return true;if(!enqueue(b[0]))return true;}
 for(int l:a)if(!enqueue(-l))return true;
 for(size_t t=0;t<trail.size();++t){int bad=-trail[t];auto&wl=watches[ix(bad)];size_t k=0;
  while(k<wl.size()){int id=wl[k];auto&c=db[id];if(!c.active){wl[k]=wl.back();wl.pop_back();continue;}
   int slot;if(c.a[c.w0]==bad)slot=0;else if(c.a[c.w1]==bad)slot=1;else{cerr<<"Invalid watch\n";exit(2);}
   int other=slot?c.w0:c.w1;int ol=c.a[other];if(value(ol)>0){++k;continue;}
   int newpos=-1;for(int q=0;q<(int)c.a.size();++q)if(q!=c.w0&&q!=c.w1&&value(c.a[q])>=0){newpos=q;break;}
   if(newpos>=0){if(slot)c.w1=newpos;else c.w0=newpos;watches[ix(c.a[newpos])].push_back(id);wl[k]=wl.back();wl.pop_back();continue;}
   if(!enqueue(ol))return true;++k;
  }
 }
 return false;
}
bool verify(const vector<int>&raw){
 vector<int>a=canon(raw);if(rup(a)){++rups;return true;}if(raw.empty())return false;int pivot=raw[0];
 for(int id:occ[ix(-pivot)])if(db[id].active){vector<int>r;for(int x:a)if(x!=pivot)r.push_back(x);for(int x:db[id].a)if(x!=-pivot)r.push_back(x);r=canon(r);if(!taut(r)&&!rup(r))return false;}
 ++rats;return true;
}
int main(int argc,char**argv){if(argc!=3){cerr<<"usage: checker input.cnf proof.drat\n";return 2;}ifstream in(argv[1]);string line;long long declared=0;
 while(getline(in,line)){if(line.empty()||line[0]=='c')continue;istringstream s(line);if(line[0]=='p'){string p,cnf;s>>p>>cnf>>nv>>declared;watches.resize(2*nv+2);occ.resize(2*nv+2);continue;}vector<int>a;int l;while(s>>l&&l){if(abs(l)>nv)return 2;a.push_back(l);}originals.insert(key(a));add(a);++inputs;}
 if(inputs!=declared){cerr<<"Header mismatch\n";return 2;}
 ifstream proof(argv[2]);long long lineno=0;while(getline(proof,line)){++lineno;if(line.empty()||line[0]=='c')continue;istringstream s(line);char kind='a';if(line[0]=='i'||line[0]=='d')s>>kind;vector<int>a;int l;bool zero=false;while(s>>l){if(!l){zero=true;break;}if(abs(l)>nv){cerr<<"Extension variable at "<<lineno<<"\n";return 2;}a.push_back(l);}if(!zero){cerr<<"Missing zero\n";return 2;}
  if(kind=='i'){auto it=bykey.find(key(a));bool present=false;if(it!=bykey.end())for(int id:it->second)if(db[id].active){present=true;break;}if(present)continue;/* Simplified input clauses must be proved too. */}
  if(kind=='d'){del(a);++deletes;continue;}
  if(!verify(a)){cerr<<"Invalid addition at "<<lineno<<"\n";return 1;}++adds;if(a.empty())finalempty=true;add(a);
 }
 cout<<"{\"valid\":"<<(finalempty?"true":"false")<<",\"input_clauses\":"<<inputs<<",\"additions\":"<<adds<<",\"deletions\":"<<deletes<<",\"RUP\":"<<rups<<",\"RAT\":"<<rats<<",\"propagation_checks\":"<<calls<<"}\n";return finalempty?0:1;
}
