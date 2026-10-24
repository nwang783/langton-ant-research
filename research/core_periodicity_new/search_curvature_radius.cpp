#include <bits/stdc++.h>
using namespace std;
struct Cell {int x,y;bool operator==(const Cell&o)const{return x==o.x&&y==o.y;}};
struct H{size_t operator()(const Cell&p)const{return(uint64_t(uint32_t(p.x))*0x9e3779b185ebca87ULL)^uint32_t(p.y);}};
unordered_map<Cell,int,H> color;
vector<pair<int,int>> st;
string w,bestw;long long nodes=0,limit;int dep,maxmass,maxgap=-99; bool found=false;
int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
void dfs(int x,int y,int h,int n,int m,int c){
 if(++nodes>limit||found)return;
 if(c+2*max(abs(x),abs(y))-2*m>maxgap){maxgap=c+2*max(abs(x),abs(y))-2*m;bestw=w;cerr<<"BEST "<<maxgap<<" depth "<<w.size()<<" nodes "<<nodes<<" word "<<w<<"\n";}
 if(c+2*max(abs(x),abs(y))-2*m>7){found=true;cout<<"VIOLATION "<<w<<" m="<<m<<" c="<<c<<"\n";return;}
 if(n==0)return;
 Cell p{x,y};auto it=color.find(p);bool fresh=it==color.end();int old=fresh?-1:it->second;
 for(int b=0;b<=1;++b){if(!fresh&&b!=old)continue;if(fresh&&b&&m>=maxmass)continue;int a=b?-1:1;int cc=c+a;auto save=st.size()?st.back():pair<int,int>{0,0};bool pop=false;
 if(!st.empty()&&st.back().first==a){if(++st.back().second==4){st.pop_back();cc-=4*a;pop=true;}}
 else st.push_back({a,1});
 color[p]=1-b;w.push_back(b?'L':'R');int hh=(h+a+4)%4;dfs(x+dx[hh],y+dy[hh],hh,n-1,m+(fresh&&b),cc);w.pop_back();
 if(pop)st.push_back(save);else if(st.back().second==1)st.pop_back();else st.back()=save;
 if(fresh)color.erase(p);else color[p]=old;
 if(found||nodes>limit)break;
 }
}
int main(int argc,char**argv){dep=argc>1?atoi(argv[1]):30;limit=argc>2?atoll(argv[2]):100000000;maxmass=argc>3?atoi(argv[3]):3;dfs(0,0,0,dep,0,0);cout<<"DONE depth="<<dep<<" nodes="<<nodes<<" maxgap="<<maxgap<<" complete="<<(nodes<=limit)<<" found="<<found<<" bestword="<<bestw<<"\n";}
