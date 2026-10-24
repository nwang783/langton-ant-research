// Independent monotone-RUP checker: occurrence counts, not watched literals.
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>
using namespace std;
struct Checker {
 int n; long long round=0; vector<vector<int>> clauses,occ; vector<long long> vs,cs,sat;vector<int> val,fc,units;
 Checker(int N):n(N),occ(2*N+2),vs(N+1),val(N+1){}
 int ix(int l){return l>0?2*l:2*(-l)+1;}
 void add(vector<int> c){sort(c.begin(),c.end());c.erase(unique(c.begin(),c.end()),c.end());int id=clauses.size();clauses.push_back(c);cs.push_back(0);sat.push_back(0);fc.push_back(0);for(int l:c)occ[ix(l)].push_back(id);if(c.size()==1)units.push_back(c[0]);}
 bool rup(const vector<int>& c){
  ++round;vector<int> pending=units;for(int l:c)pending.push_back(-l);
  for(auto &d:clauses)if(d.empty())return true;
  for(size_t head=0;head<pending.size();head++){
   int l=pending[head],v=abs(l),sg=l>0?1:-1;
   if(vs[v]==round){if(val[v]!=sg)return true;continue;}
   vs[v]=round;val[v]=sg;
   for(int id:occ[ix(l)])sat[id]=round;
   for(int id:occ[ix(-l)]){
    if(cs[id]!=round){cs[id]=round;fc[id]=0;}
    ++fc[id];if(sat[id]==round)continue;
    int left=(int)clauses[id].size()-fc[id];if(left==0)return true;
    if(left==1){int unit=0;bool satisfied=false;for(int q:clauses[id]){if(vs[abs(q)]!=round)unit=q;else if(val[abs(q)]==(q>0?1:-1)){satisfied=true;break;}}if(!satisfied){if(unit==0)throw runtime_error("count inconsistency");pending.push_back(unit);}}
   }
  }
  return false;
 }
};
int main(int argc,char**argv){try{
 if(argc!=3)throw runtime_error("usage CNF RUP");ifstream f(argv[1]);string line;int n=-1,m=-1;vector<vector<int>> input;vector<int> buf;
 while(getline(f,line)){if(line.empty()||line[0]=='c')continue;istringstream s(line);if(line[0]=='p'){string p,fmt;s>>p>>fmt>>n>>m;if(fmt!="cnf"||n<0||m<0)throw runtime_error("header");continue;}int l;while(s>>l){if(l==0){input.push_back(buf);buf.clear();}else {if(abs(l)>n)throw runtime_error("input literal");buf.push_back(l);}}}
 if(!buf.empty()||input.size()!=size_t(m))throw runtime_error("input count");Checker c(n);for(auto d:input)c.add(d);
 ifstream g(argv[2]);int adds=0;bool lastempty=false;
 while(getline(g,line)){if(line.empty())continue;istringstream s(line);vector<int>d;int l;bool end=false;while(s>>l){if(end)throw runtime_error("tokens after zero");if(l==0)end=true;else{if(abs(l)>n)throw runtime_error("proof literal");d.push_back(l);}}if(!s.eof()||!end)throw runtime_error("bad proof line");sort(d.begin(),d.end());d.erase(unique(d.begin(),d.end()),d.end());if(!c.rup(d)){cerr<<"INVALID at addition "<<adds<<"\n";return 1;}c.add(d);++adds;lastempty=d.empty();}
 if(!lastempty)throw runtime_error("no final empty clause");cout<<"{\"valid\":true,\"variables\":"<<n<<",\"original_clauses\":"<<m<<",\"rup_additions\":"<<adds<<"}\n";return 0;
 }catch(exception&e){cerr<<e.what()<<"\n";return 2;}}
