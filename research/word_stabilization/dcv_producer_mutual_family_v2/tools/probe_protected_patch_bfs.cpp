#include <bits/stdc++.h>
using namespace std;
struct T{int from,to;uint64_t k,v,f;int goal,a;};
int main(int argc,char**argv){if(argc<2)return 1;ifstream in(argv[1]);int n,np,nt,nr;in>>n>>np>>nt>>nr;int sp;uint64_t sk,sv;in>>sp>>sk>>sv;vector<vector<T>>out(np),inc(np);vector<T>all;for(int i=0;i<nt;i++){T t;in>>t.from>>t.to>>t.k>>t.v>>t.f>>t.goal>>t.a;out[t.from].push_back(t);inc[t.to].push_back(t);all.push_back(t);}vector<int>re(nr);for(int&i:re)in>>i;uint64_t cols=1ull<<n,total=cols*np;if(total>1000000000ull){cout<<"too_large "<<total<<endl;return 2;}vector<uint16_t>dist(total,65535);vector<uint64_t>front,next;uint64_t count=0;for(uint64_t c=0;c<cols;c++)if((c&sk)==sv){uint64_t s=sp*cols+c;dist[s]=0;front.push_back(s);count++;}int goalA=-1;uint64_t goalState=0;int depth=0;bool hit=false;uint64_t cap=argc>2?stoull(argv[2]):100000000;
for(;!front.empty()&&depth<65534&&!hit;depth++){
 for(uint64_t state:front){int p=state/cols;uint64_t c=state%cols;
  auto add=[&](int q,uint64_t cc){uint64_t ss=q*cols+cc;if(dist[ss]==65535){dist[ss]=depth+1;next.push_back(ss);count++;}};
  if(p==np-1){for(int q:re)add(q,c);}
  else for(T t:out[p])if(((c^t.v)&t.k)==0){if(t.goal){hit=true;goalState=state;goalA=t.a;break;}add(t.to,c^t.f);}
  if(hit||count>cap)break;
 }
 cerr<<"depth "<<depth<<" states "<<count<<" frontier "<<front.size()<<" next "<<next.size()<<" hit "<<hit<<endl;
 if(count>cap)break;front.swap(next);next.clear();
}
cout<<"status "<<(hit?"ABSTRACT_WITNESS":front.empty()?"EXHAUSTED_NO_HIT":"CAP")<<" states "<<count<<" depth "<<depth<<"\n";
if(hit){vector<array<uint64_t,3>>path;uint64_t s=goalState;path.push_back({s/cols,s%cols,uint64_t(goalA)});while(dist[s]){int dd=dist[s],p=s/cols;uint64_t c=s%cols;bool found=false;
 auto take=[&](int q,uint64_t cc,int a){uint64_t ss=q*cols+cc;if(dist[ss]+1==dd){path.push_back({uint64_t(q),cc,uint64_t(a)});s=ss;found=true;}};
 if(p!=np-1&&find(re.begin(),re.end(),p)!=re.end())take(np-1,c,99);
 if(!found)for(T t:inc[p]){if(t.goal)continue;uint64_t cc=c^t.f;if(((cc^t.v)&t.k)==0){take(t.from,cc,t.a);if(found)break;}}
 if(!found){cerr<<"No predecessor!"<<endl;return 3;}}
 reverse(path.begin(),path.end());for(auto a:path)cout<<a[0]<<' '<<a[1]<<' '<<a[2]<<'\n';}
}
