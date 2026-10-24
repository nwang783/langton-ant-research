// Independent queue closure with packed visited bits, not layered distances.
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdexcept>
struct Edge { uint32_t destination,mask,value,flip; bool terminal; };
int main(int argc,char**argv){
 if(argc!=2)return 2;
 std::ifstream in(argv[1]);uint32_t n,poses,nt,nr,sp,sk,sv;in>>n>>poses>>nt>>nr>>sp>>sk>>sv;
 if(n>=24)throw std::runtime_error("unsupported audit bit width");
 uint32_t colors=1U<<n;uint64_t total=uint64_t(colors)*poses;
 std::vector<std::vector<Edge>> edges(poses);
 for(uint32_t i=0;i<nt;i++){uint32_t from,to,k,v,f,goal,a;in>>from>>to>>k>>v>>f>>goal>>a;edges[from].push_back({to,k,v,f,bool(goal)});}
 std::vector<uint32_t> reentry(nr);for(auto &p:reentry)in>>p;
 if(!in)throw std::runtime_error("bad input");
 std::vector<uint64_t> visited((total+63)/64,0);
 std::vector<uint32_t> queue;queue.reserve(12000000);
 auto push=[&](uint32_t p,uint32_t c){uint64_t id=uint64_t(p)*colors+c;if(id>=total)throw std::runtime_error("bad state");uint64_t mask=1ULL<<(id%64);if(!(visited[id/64]&mask)){visited[id/64]|=mask;queue.push_back(uint32_t(id));}};
 for(uint32_t c=0;c<colors;c++)if((c&sk)==sv)push(sp,c);
 uint64_t edge_checks=0,out_checks=0,goal_checks=0;
 for(size_t i=0;i<queue.size();i++){
  uint32_t id=queue[i],p=id/colors,c=id%colors;
  if(p==poses-1){for(auto next:reentry){push(next,c);out_checks++;}}
  else for(const auto&e:edges[p]){
   edge_checks++;if((c&e.mask)!=e.value)continue;
   if(e.terminal){std::cout<<"FAIL goal at state "<<id<<" after "<<i<<" pops\n";return 1;}
   push(e.destination,c^e.flip);
  }
 }
 uint64_t checksum=1469598103934665603ULL;
 for(uint64_t word:visited){checksum^=word;checksum*=1099511628211ULL;}
 std::cout<<"{\"status\":\"PASS exhaustive independent no-goal closure\",\"reachable_states\":"<<queue.size()<<",\"abstract_space\":"<<total<<",\"packet_edge_checks\":"<<edge_checks<<",\"out_reentry_checks\":"<<out_checks<<",\"visited_checksum\":"<<checksum<<"}\n";
}
