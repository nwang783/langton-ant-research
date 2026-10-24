// Packed exact color-only forward closure. No parent tree or state-count bound.
// Useful as a separately checkable invariant for hybrid resource pruning.
#include <bits/stdc++.h>
using namespace std;using U=uint64_t;struct E{int to;U k,v,f,c,r;};
int main(int ac,char**av){ifstream in(av[1]);int n,np,ne,nr;in>>n>>np>>ne>>nr;assert(in&&n<=22);int sp;U sk,sv;in>>sp>>sk>>sv;vector<vector<E>>adj(np);for(int j=0;j<ne;j++){int f,t,goal,a;E e;in>>f>>t>>e.k>>e.v>>e.f>>e.c>>e.r>>goal>>a;e.to=t;e.v&=e.k;e.r&=e.c;adj[f].push_back(e);}vector<int>re(nr);for(int&p:re)in>>p;U cols=1ULL<<n,words=(cols+63)/64,total=U(np)*words;assert(U(np)*cols<=UINT32_MAX);vector<U>bits(total);deque<uint32_t>q;U count=0,pops=0;auto add=[&](int p,U c){U z=U(p)*words+c/64,b=1ULL<<(c%64);if(!(bits[z]&b)){bits[z]|=b;q.push_back(uint32_t(U(p)*cols+c));count++;}};for(U c=0;c<cols;c++)if((c&sk)==sv)add(sp,c);
while(!q.empty()){uint32_t z=q.front();q.pop_front();int p=z/cols;U c=z%cols;pops++;for(auto&e:adj[p])if((c&e.k)==e.v)add(e.to,((c^e.f)&~e.c)|e.r);if(p==np-1)for(int t:re)add(t,c);if(pops%10000000==0)cerr<<"processed "<<pops<<" reached "<<count<<" queued "<<q.size()<<"\n";}
ofstream out(av[2],ios::binary);const char magic[8]={'C','O','L','R','C','H','1',0};out.write(magic,8);uint32_t head[3]={uint32_t(n),uint32_t(np),uint32_t(words)};out.write((char*)head,sizeof(head));out.write((char*)bits.data(),bits.size()*sizeof(U));cout<<"status CLOSED_EXACT_COLOR_REACH bits "<<n<<" controls "<<np<<" reached "<<count<<" processed "<<pops<<" binary_bytes "<<bits.size()*8+20<<"\n";
}
