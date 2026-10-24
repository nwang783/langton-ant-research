// Explicit-state hash-set closure, independent of the ROBDD search/verifier.
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <stdexcept>
struct E{uint32_t to;uint64_t mask,value,flip;bool goal;};
int main(int argc,char**argv){if(argc!=2)return 2;std::ifstream f(argv[1]);uint32_t n,np,nt,nr,sp;uint64_t sk,sv;f>>n>>np>>nt>>nr>>sp>>sk>>sv;if(n>=40)throw std::runtime_error("width");uint64_t colors=1ULL<<n;std::vector<std::vector<E>>edges(np);for(uint32_t i=0;i<nt;i++){uint32_t p,to,g,a;uint64_t k,v,x;f>>p>>to>>k>>v>>x>>g>>a;edges[p].push_back({to,k,v,x,bool(g)});}std::vector<uint32_t>re(nr);for(auto&p:re)f>>p;if(!f)throw std::runtime_error("input");
 std::unordered_set<uint64_t>seen;seen.reserve(500000);std::vector<uint64_t>q;q.reserve(500000);auto add=[&](uint32_t p,uint64_t c){if(p>=np||c>=colors)throw std::runtime_error("state");uint64_t id=(uint64_t(p)<<n)|c;if(seen.insert(id).second)q.push_back(id);};
 if(sk==colors-1)add(sp,sv);else for(uint64_t c=0;c<colors;c++)if((c&sk)==sv)add(sp,c);
 uint64_t checks=0,rechecks=0;
 for(size_t i=0;i<q.size();i++){uint32_t p=q[i]>>n;uint64_t c=q[i]&(colors-1);if(p==np-1){for(auto d:re){add(d,c);rechecks++;}}else for(auto&e:edges[p]){checks++;if((c&e.mask)!=e.value)continue;if(e.goal){std::cout<<"{\"status\":\"ABSTRACT_GOAL\",\"explored\":"<<i<<"}\n";return 1;}add(e.to,c^e.flip);}}
 uint64_t checksum=0;for(uint64_t id:seen){id=(id^(id>>30))*0xbf58476d1ce4e5b9ULL;id=(id^(id>>27))*0x94d049bb133111ebULL;checksum^=id^(id>>31);}
 std::cout<<"{\"status\":\"PASS explicit independent sparse no-goal closure\",\"reachable_states\":"<<seen.size()<<",\"packet_edge_checks\":"<<checks<<",\"out_reentry_checks\":"<<rechecks<<",\"visited_checksum\":"<<checksum<<"}\n";
}
