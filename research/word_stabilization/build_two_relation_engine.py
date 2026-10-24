from pathlib import Path
s=Path('generic_spatial_kernel.cpp').read_text();s=s[:s.index('int main(')];s=s.replace('vector<uint64_t>CAND(SZ/64),S(SZ/64);','vector<uint64_t>CAND(SZ/64),S(SZ/64),G(SZ/64),DIRECT(SZ/64);');s=s.replace('struct Type{','bool hasG(int a,int b,P p,int h){return inside(p.x,p.y)&&bit(G,key(a,b,p.x,p.y,h));}\nstruct Type{');s=s.replace('Proof certify(uint32_t k){','Proof certify(uint32_t k,bool goal=false){if(!goal&&bit(DIRECT,k))return{3,0,0};');s=s.replace('if(has(c,b,cb,cbh))continue;','if(goal?hasG(c,b,cb,cbh):has(c,b,cb,cbh))continue;');s=s.replace('if(!has(r.c,b,rb,(h-r.h+4)%4))','if(!(goal?hasG(r.c,b,rb,(h-r.h+4)%4):has(r.c,b,rb,(h-r.h+4)%4)))')
s+=r'''
vector<vector<P>>MARKS;
uint64_t pointkey(P p){return(uint64_t(uint32_t(p.x))<<32)|uint32_t(p.y);}
bool fvalid(vector<int>w,bool ignorelast){unordered_set<uint64_t>seen;P p{0,0};int h=0;for(size_t i=0;i<w.size();i++){int a=w[i];if(!(ignorelast&&i+1==w.size()))for(auto q:MARKS[a])if(seen.count(pointkey(add(p,rot(q,h)))))return false;for(auto q:M[a].raw)seen.insert(pointkey(add(p,rot({q.x,q.y},h))));p=add(p,rot(M[a].end,h));h=(h+M[a].dh)%4;}return true;}
int main(int argc,char**argv){if(argc!=4){cerr<<"input marks output_prefix\n";return 1;}ifstream f(argv[1]);int n;f>>n;assert(n<=128);M.resize(n);MARKS.resize(n);OUT.resize(n);IN.resize(n);
 for(int a=0;a<n;a++){int z;f>>M[a].end.x>>M[a].end.y>>M[a].dh>>z;M[a].first.fill(-1);while(z--){Cell q;f>>q.x>>q.y>>q.c;q.phase=-1;M[a].raw.push_back(q);}f>>z;while(z--){Cell q;f>>q.x>>q.y>>q.c>>q.phase;M[a].tar.push_back(q);assert(inside(q.x,q.y));M[a].first[(q.x+32)*64+q.y+32]=q.c;}}
 int z;f>>z;vector<pair<int,int>>pairs;while(z--){int a,b;f>>a>>b;pairs.push_back({a,b});OUT[a].push_back(b);IN[b].push_back(a);}f>>z;vector<array<int,3>>triples;while(z--){array<int,3>q;f>>q[0]>>q[1]>>q[2];triples.push_back(q);}assert(f.good()||f.eof());
 ifstream marks(argv[2]);int a,x,y;while(marks>>a>>x>>y){assert(a>=0&&a<n&&inside(x,y)&&M[a].first[(x+32)*64+y+32]==1);MARKS[a].push_back({x,y});}
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)for(int h=0;h<4;h++)for(auto q:M[a].raw)for(auto z:M[b].tar){P p=sub({q.x,q.y},rot({z.x,z.y},h));if(!aligned(p,h))continue;assert(inside(p.x,p.y));uint32_t k=key(a,b,p.x,p.y,h);if(!bit(CAND,k)){setbit(CAND,k);active.push_back(k);}}
 sort(active.begin(),active.end());set<pair<int,int>>qs;for(auto&m:M)for(auto q:m.raw)qs.insert({q.x,q.y});for(auto [x,y]:qs){auto &rr=READERS[{x,y}];for(int c=0;c<n;c++)for(int h=0;h<4;h++)for(auto z:M[c].raw){P p=sub({x,y},rot({z.x,z.y},h));if(aligned(p,h))rr.push_back({c,h,p});}}
 string base=argv[3];int outer=0;
 while(true){size_t mcount=0;for(auto&v:MARKS)mcount+=v.size();cout<<"OUTER "<<outer<<" marks="<<mcount<<" candidates="<<active.size()<<endl;if(!mcount){ofstream o(base+".status.json");o<<"{\"status\":\"empty candidate freshness family\",\"outer_rounds\":"<<outer<<"}\n";break;}
  S=CAND;G=CAND;fill(DIRECT.begin(),DIRECT.end(),0);
  for(int b=0;b<n;b++)for(auto mark:MARKS[b])for(int a=0;a<n;a++)for(int h=0;h<4;h++)for(auto q:M[a].raw){P p=sub({q.x,q.y},rot(mark,h));if(aligned(p,h)){assert(inside(p.x,p.y));setbit(DIRECT,key(a,b,p.x,p.y,h));}}
  for(auto [a,b]:pairs){P p=M[a].end;if(!inside(p.x,p.y))continue;auto k=key(a,b,p.x,p.y,M[a].dh);if(fvalid({a,b},false))clearbit(S,k);if(fvalid({a,b},true))clearbit(G,k);}
  for(auto q:triples){int a=q[0],c=q[1],b=q[2];P p=add(M[a].end,rot(M[c].end,M[a].dh));if(!inside(p.x,p.y))continue;auto k=key(a,b,p.x,p.y,(M[a].dh+M[c].dh)%4);if(fvalid({a,c,b},false))clearbit(S,k);if(fvalid({a,c,b},true))clearbit(G,k);}
  vector<uint32_t>normal,goal;for(auto k:active){assert(!bit(DIRECT,k)||bit(S,k));if(bit(S,k))normal.push_back(k);if(bit(G,k))goal.push_back(k);}vector<Proof>np,gp;
  for(int pass=0;pass<2;pass++){auto &cur=pass?goal:normal;auto &bits=pass?G:S;auto &proof=pass?gp:np;int round=0;while(true){vector<uint32_t>next,removed;proof.clear();for(auto k:cur){auto p=certify(k,pass);if(p.kind){next.push_back(k);proof.push_back(p);}else removed.push_back(k);}cout<<(pass?"GOAL ":"NORMAL ")<<round<<" kernel="<<next.size()<<" removed="<<removed.size()<<endl;if(removed.empty())break;for(auto k:removed)clearbit(bits,k);cur.swap(next);round++;}}
  vector<vector<P>>next(n);size_t kept=0;for(int b=0;b<n;b++)for(auto q:MARKS[b]){bool ok=true;for(int a=0;a<n&&ok;a++)for(int h=0;h<4&&ok;h++)for(auto z:M[a].raw){P p=sub({z.x,z.y},rot(q,h));if(aligned(p,h)&&!hasG(a,b,p,h)){ok=false;break;}}if(ok){next[b].push_back(q);kept++;}}
  cout<<"CLOSED marks="<<kept<<" removed="<<mcount-kept<<endl;
  ofstream markout(base+".round"+to_string(outer)+".marks.tsv");for(int b=0;b<n;b++)for(auto q:next[b])markout<<b<<' '<<q.x<<' '<<q.y<<'\n';
  if(kept==mcount){for(int pass=0;pass<2;pass++){auto &cur=pass?goal:normal;auto &proof=pass?gp:np;ofstream o(base+(pass?".goal.tsv":".normal.tsv"));for(size_t i=0;i<cur.size();i++){auto t=decode(cur[i]);auto p=proof[i];o<<t.a<<' '<<t.b<<' '<<t.p.x<<' '<<t.p.y<<' '<<t.h<<' '<<p.kind<<' '<<p.x<<' '<<p.y<<'\n';}}ofstream o(base+".status.json");o<<"{\"status\":\"stable nonempty candidate\",\"marks\":"<<kept<<",\"normal_pairs\":"<<normal.size()<<",\"goal_pairs\":"<<goal.size()<<",\"outer_rounds\":"<<outer<<"}\n";break;}
  MARKS.swap(next);outer++;
 }
}
'''
Path('two_relation_spatial_kernel.cpp').write_text(s)
