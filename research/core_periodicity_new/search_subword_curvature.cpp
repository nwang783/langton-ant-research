#include <bits/stdc++.h>
using namespace std;
using P=pair<int,int>;
struct H{size_t operator()(P p)const{return ((uint64_t)(uint32_t)p.first<<32)^((uint32_t)p.second*0x9e3779b9u);}};
int main(int argc,char**argv){
 int T=argc>1?atoi(argv[1]):20000, seed=argc>2?atoi(argv[2]):0;
 unordered_set<P,H>B;
 mt19937 gen(seed);
 if(seed)for(int i=0;i<20;i++)B.insert({int(gen()%11)-5,int(gen()%11)-5});
 vector<P>pos;vector<int>heads,ids,a;unordered_map<P,int,H>index;
 int x=0,y=0,h=0;int dx[]={0,1,0,-1},dy[]={1,0,-1,0};
 for(int t=0;t<T;t++){
  P p{x,y};pos.push_back(p);heads.push_back(h);
  if(!index.count(p)){int z=index.size();index[p]=z;}ids.push_back(index[p]);
  int z=B.count(p)?-1:1;a.push_back(z);if(z<0)B.erase(p);else B.insert(p);
  h=(h+z+4)%4;x+=dx[h];y+=dy[h];
 }
 vector<int>seen(index.size(),-1);vector<pair<int,int>>st;st.reserve(T);
 int best=-100;long long count=0;
 for(int i=0;i<T;i++){
  st.clear();int c=0,m=0;
  for(int j=i;j<T;j++){
   int z=a[j];if(seen[ids[j]]!=i){seen[ids[j]]=i;if(z<0)m++;}
   c+=z;
   if(!st.empty()&&st.back().first==z){if(++st.back().second==4){st.pop_back();c-=4*z;}}
   else st.push_back({z,1});
   count++;int gap=c-2*m;
   if(gap>best){best=gap;cerr<<"best "<<best<<" start "<<i<<" end "<<j+1<<" m "<<m<<" c "<<c<<"\n";}
   if(gap>3){
    cout<<"VIOLATION seed="<<seed<<" start="<<i<<" end="<<j+1<<" m="<<m<<" c="<<c<<"\n";
    for(int k=i;k<=j;k++)cout<<(a[k]>0?'R':'L');cout<<"\ninitial blacks:";
    unordered_set<P,H>S;
    for(int k=i;k<=j;k++)if(S.insert(pos[k]).second&&a[k]<0)cout<<" ("<<pos[k].first<<","<<pos[k].second<<")";
    cout<<" pose="<<pos[i].first<<","<<pos[i].second<<","<<heads[i]<<"\n";return 1;
   }
  }
 }
 cout<<"COMPLETE T="<<T<<" seed="<<seed<<" intervals="<<count<<" best="<<best<<"\n";
}
