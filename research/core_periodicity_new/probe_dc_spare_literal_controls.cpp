#include <bits/stdc++.h>
using namespace std;
struct Q{int x,y,v;};struct P{int id,c,x,y,h;vector<Q>req;vector<pair<int,int>>odd;};vector<P> ps;unordered_map<uint32_t,bool>col;vector<int>path;vector<array<int,3>> poses;long long nodes,cap;int maxdepth,goalid,gx,gy;bool found=false;ofstream out;
pair<int,int>rot(int x,int y,int h){switch(h&3){case 0:return{x,y};case 1:return{y,-x};case 2:return{-x,-y};default:return{-y,x};}}
uint32_t key(int x,int y){return(uint32_t(x+32768)<<16)|uint32_t(y+32768);}
vector<pair<uint32_t,int>> changes;
bool apply(const P&p,int x,int y,int h,bool strict){
 static const set<pair<int,int>>watch={{2,0},{2,3},{3,1},{3,2}};
 for(auto q:p.req){auto [u,v]=rot(q.x,q.y,h);u+=x;v+=y;if(strict&&watch.count({u,v}))return false;auto it=col.find(key(u,v));if(it!=col.end()&&it->second!=q.v)return false;}
 for(auto q:p.req){auto [u,v]=rot(q.x,q.y,h);auto k=key(u+x,v+y);if(!col.count(k)){changes.push_back({k,-1});col[k]=q.v;}}
 for(auto q:p.odd){auto[u,v]=rot(q.first,q.second,h);auto k=key(u+x,v+y);changes.push_back({k,int(col.at(k))});col[k]=!col[k];}
 return true;
}
void undo(size_t n){while(changes.size()>n){auto[k,v]=changes.back();changes.pop_back();if(v<0)col.erase(k);else col[k]=v;}}
bool zeroPossible(int x,int y,int h){auto[a,b]=rot(gx-x,gy-y,(-h)&3);if(a<0||b<a||(b-a)%2)return false;int t=(b-a)/2;for(int z=0;z<=a;++z)if(z<=t&&(t-z)%2==0)return true;return false;}
bool dfs(int x,int y,int h,int c,int d){
 if(++nodes>cap)return false;
 if(c==5&&x==gx&&y==gy&&h==2){auto n=changes.size();if(apply(ps[goalid],x,y,h,false)){out<<"{\"status\":\"FOUND_BOUNDED_LITERAL_CONTROL\",\"nodes\":"<<nodes<<",\"path\":[1";for(int a:path)out<<","<<ps[a].id;out<<","<<ps[goalid].id<<"],\"strict_poses\":[";for(int i=0;i<(int)poses.size();++i){if(i)out<<",";auto p=poses[i];out<<"["<<p[0]<<","<<p[1]<<","<<p[2]<<"]";}out<<"],\"source_included_C_age\":6}\n";undo(n);return true;}undo(n);}
 if(d==maxdepth||nodes>=cap)return false;if(c==5&&!zeroPossible(x,y,h))return false;
 struct Z{int i,x,y,h,c,score;};vector<Z>cand;
 for(int i=0;i<(int)ps.size();++i){auto&p=ps[i];if(c+p.c>5)continue;auto[u,v]=rot(p.x,p.y,h);int nx=x+u,ny=y+v,nh=(h+p.h)&3,nc=c+p.c;if(nc==5&&!zeroPossible(nx,ny,nh))continue;int score=abs(nx-gx)+abs(ny-gy)+2*(5-nc);cand.push_back({i,nx,ny,nh,nc,score});}
 sort(cand.begin(),cand.end(),[](Z a,Z b){return a.score<b.score;});
 for(auto z:cand){auto n=changes.size();if(apply(ps[z.i],x,y,h,true)){path.push_back(z.i);poses.push_back({x,y,h});if(dfs(z.x,z.y,z.h,z.c,d+1)){undo(n);return true;}poses.pop_back();path.pop_back();}undo(n);if(nodes>=cap)break;}return false;
}
int main(int argc,char**argv){ifstream f(argv[1]);int N;f>>N;for(int i=0;i<N;++i){P p;int nr,no;f>>p.id>>p.c>>p.x>>p.y>>p.h>>nr>>no;for(int j=0;j<nr;++j){Q q;f>>q.x>>q.y>>q.v;p.req.push_back(q);}for(int j=0;j<no;++j){int x,y;f>>x>>y;p.odd.push_back({x,y});}ps.push_back(p);}goalid=stoi(argv[2]);gx=stoi(argv[3]);gy=stoi(argv[4]);maxdepth=stoi(argv[5]);cap=stoll(argv[6]);out.open(argv[7]);int source=1;assert(ps[source].id==1);assert(apply(ps[source],0,0,0,false));found=dfs(1,2,3,0,0);if(!found)out<<"{\"status\":\"BOUNDED_NO_CONTROL_UNKNOWN\",\"nodes\":"<<nodes<<",\"max_strict_packets\":"<<maxdepth<<",\"node_cap\":"<<cap<<",\"source_included_C_age\":6}\n";cout<<"found="<<found<<" nodes="<<nodes<<" depth="<<maxdepth<<"\n";}
