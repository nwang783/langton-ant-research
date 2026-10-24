#include <bits/stdc++.h>
using namespace std;using U=uint64_t;struct T{int from,to;U k,v,f,c,r;int goal,a;};
int main(int argc,char**argv){try{if(argc<2)return 1;ifstream in(argv[1]);int n,np,nt,nr;in>>n>>np>>nt>>nr;if(n>30)throw runtime_error("n too large");int sp;U sk,sv;in>>sp>>sk>>sv;vector<vector<T>>out(np),inc(np);for(int i=0;i<nt;i++){T t;in>>t.from>>t.to>>t.k>>t.v>>t.f>>t.c>>t.r>>t.goal>>t.a;out[t.from].push_back(t);inc[t.to].push_back(t);}vector<int>re(nr);for(int&i:re)in>>i;U cols=1ull<<n,total=cols*np,lim=argc>2?stoull(argv[2]):300000000;if(total>lim||total>UINT32_MAX)throw runtime_error("dense state universe cap");vector<uint16_t>d(total,65535);vector<uint32_t>fr,nx;U count=0;for(U c=0;c<cols;c++)if((c&sk)==sv){U s=U(sp)*cols+c;d[s]=0;fr.push_back(s);count++;}bool hit=false;U gs=0;int ga=-1,depth=0;
for(;!fr.empty()&&!hit&&depth<65534;depth++){
 for(U s:fr){int p=s/cols;U c=s%cols;auto add=[&](int q,U cc){U ss=U(q)*cols+cc;if(d[ss]==65535){d[ss]=depth+1;nx.push_back(ss);count++;}};
 if(p==np-1){for(int q:re)add(q,c);}else for(T t:out[p])if(((c^t.v)&t.k)==0){if(t.goal){hit=true;gs=s;ga=t.a;break;}add(t.to,((c^t.f)&~t.c)|(t.r&t.c));}if(hit)break;
 }cerr<<"depth "<<depth<<" states "<<count<<" frontier "<<fr.size()<<" next "<<nx.size()<<" hit "<<hit<<'\n';if(!hit){fr.swap(nx);nx.clear();}}
cout<<"status "<<(hit?"ABSTRACT_WITNESS":fr.empty()?"EXHAUSTED_NO_HIT":"CAP")<<" states "<<count<<" depth "<<depth<<"\n";
if(hit){vector<array<U,3>>path;U s=gs;path.push_back({s/cols,s%cols,U(ga)});while(d[s]){int dd=d[s],p=s/cols;U c=s%cols;bool found=false;auto take=[&](int q,U cc,int a){U ss=U(q)*cols+cc;if(d[ss]!=65535&&d[ss]+1==dd){path.push_back({U(q),cc,U(a)});s=ss;found=true;}};
if(p!=np-1&&find(re.begin(),re.end(),p)!=re.end())take(np-1,c,99);
if(!found)for(T t:inc[p]){if(t.goal||(c&t.c)!=(t.r&t.c))continue;U keep=(cols-1)&~t.c,wanted=(c^t.f)&keep;if(((wanted^t.v)&t.k&keep)!=0)continue;U base=wanted|(t.v&t.c),free=t.c&~t.k;U sub=free;while(true){take(t.from,base|sub,t.a);if(found||!sub)break;sub=(sub-1)&free;}if(found)break;}
if(!found)throw runtime_error("no predecessor");}reverse(path.begin(),path.end());for(auto r:path)cout<<"WITNESS "<<r[0]<<' '<<r[1]<<' '<<r[2]<<'\n';}
}catch(exception&e){cout<<"status CAP_OR_ERROR reason "<<e.what()<<'\n';return 2;}}
