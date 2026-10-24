#include<bits/stdc++.h>
using namespace std;struct Move{int x,y,c;};struct Macro{char n;int dx,dy,dh;vector<Move>a;};map<char,Macro>ms;
uint64_t key(int x,int y){return (uint64_t(uint32_t(x))<<32)|uint32_t(y);}pair<int,int>rot(int x,int y,int h){if(h==0)return{x,y};if(h==1)return{y,-x};if(h==2)return{-x,-y};return{-y,x};}
pair<int,int> check(string w){unordered_map<uint64_t,int>last;int x=0,y=0,h=0,f=0,lf=0;for(char c:w){auto&m=ms.at(c);lf=0;for(auto&a:m.a){auto[dx,dy]=rot(a.x,a.y,h);auto k=key(x+dx,y+dy);auto it=last.find(k);if(it!=last.end()&&it->second==a.c)return{-1,-1};if(it==last.end()&&a.c==1){f++;lf++;}last[k]=a.c;}auto[dx,dy]=rot(m.dx,m.dy,h);x+=dx;y+=dy;h=(h+m.dh)%4;}return{lf,f};}
int main(int argc,char**argv){int n;cin>>n;while(n--){Macro z;int k;cin>>z.n>>z.dx>>z.dy>>z.dh>>k;while(k--){Move a;cin>>a.x>>a.y>>a.c;z.a.push_back(a);}ms[z.n]=z;}string initial=argc>1?argv[1]:"QUVVUVVUVQVVVVVVVVVUVCVUUVUVCVVVVVUVCVUVVQ";int iterations=argc>2?stoi(argv[2]):1000000;mt19937_64 rng(argc>3?stoull(argv[3]):41);string alpha="CVUQB";string w=initial,best=w;auto old=check(w);int bestf=old.first;long long valid=0;cout<<"INITIAL "<<old.first<<" "<<old.second<<" "<<w<<endl;
for(int i=0;i<iterations;i++){
 if(i%20000==0&&i) {w=(rng()%2?best:initial);old=check(w);}
 string v=w;int op=rng()%6;int p=rng()%(v.size()-1);int q;
 if(op==0)v[p]=alpha[rng()%5];
 if(op==1&&v.size()<300)v.insert(p,1,alpha[rng()%5]);
 if(op==2&&v.size()>2)v.erase(p,1);
 if(op==3&&v.size()<300){q=rng()%4+1;string add;while(q--)add+=alpha[rng()%5];v.insert(p,add);}
 if(op==4){q=min((int)v.size()-1-p,(int)(rng()%4+1));v.erase(p,q);}
 if(op==5){q=min((int)v.size()-1-p,(int)(rng()%4+1));while(q--)v[p+q]=alpha[rng()%5];}
 if(v.size()<2)continue;auto now=check(v);if(now.first<0)continue;valid++;
 if(now.first<bestf){bestf=now.first;best=v;cout<<"RECORD "<<i<<" newfuel "<<now.first<<" total "<<now.second<<" length "<<v.size()<<" "<<v<<endl;if(bestf==0)break;}
 double temp=0.3+1.7*(1.0-(i%20000)/20000.0);double delta=now.first-old.first+0.002*(int(v.size())-int(w.size()));
 if(delta<=0||generate_canonical<double,53>(rng)<exp(-delta/temp)){w=v;old=now;}
}cout<<"DONE best "<<bestf<<" valid "<<valid<<" word "<<best<<endl;
}
