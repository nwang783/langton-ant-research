"""Uniform all-k contact bound for six actual standard output-tree families.
The whole-family execution/774 recovery is a retained dependency.
No sampling supplies this all-parameter geometric bound.
"""
from check_active_itineraries import *
from fractions import Fraction
OUT=Path(__file__).parent
Z=json.loads((ROOT/'standard_unread_cap_2026-10-23/standard_w_frontier_certificate.json').read_text());T={tuple(q)for q in Z['emitted_w_tree_T']}
def rot(q,r):
 x,y=q
 for _ in range(r%4):x,y=y,-x
 return x,y

def vecadd(a,b):return(a[0]+b[0],a[1]+b[1])
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def afsub(a,b):return[a[0]-b[0],a[1]-b[1]]
def afval(a,k):return a[0]*k+a[1]
def enc(a):return [[v.numerator,v.denominator]for v in a]
FAM=[]
for name,pa,pb,h,hi in [('stage0',(0,0),(0,0),1,[1,-5]),('stage1',(2,2),(-1,0),0,[2,-6]),('stage2',(-2,6),(0,-4),3,[4,-7]),('stage3',(-10,-2),(5,0),2,[2,-8]),('stage4',(-6,-6),(0,8),1,[3,-5]),('final_tail',(0,0),(5,-4),2,None)]:
 origin=pb if name=='final_tail'else vecadd(pb,rot((5,1),h-1))
 cells={vecadd(origin,rot(q,h-3))for q in T};V=vertices(cells,0);D=rot((-4,-4),h-3)
 assert len(V)==13
 offsets=set()
 for u in V:
  for v in V:
   d=(u[0]-v[0],u[1]-v[1])
   if cross(d,D)==0 and d[0]%D[0]==0:offsets.add(d[0]//D[0])
 assert offsets=={0}
 FAM.append({'name':name,'alpha':(2*pa[0],2*pa[1]),'base_vertices':V,'drift':D,'lo':[0,2],'hi':hi,'base_cells':cells})

def main():
 pairs=[];P=0
 for i,A in enumerate(FAM):
  for j in range(i+1,len(FAM)):
   B=FAM[j];Da=A['drift'];Db=B['drift'];delta=(A['alpha'][0]-B['alpha'][0],A['alpha'][1]-B['alpha'][1]);bound=0;details=[]
   if cross(Da,Db)!=0:
    bound=len(A['base_vertices'])*len(B['base_vertices']);kind='nonparallel: each vertex pair determines at most one copy pair at each k'
   else:
    kind='parallel: exact perpendicular domains or uniformly bounded longitudinal overlap';sgn=1 if Da==Db else-1;assert Db==tuple(sgn*x for x in Da)
    for u in sorted(A['base_vertices']):
     for v in sorted(B['base_vertices']):
      z=(u[0]-v[0],u[1]-v[1]);aa=cross(delta,Da);bb=cross(z,Da)
      if aa:
       k=Fraction(-bb,aa)
       if k.denominator!=1 or k<10:continue
       counts=[afval(f['hi'],int(k))-1 for f in(A,B)if f['hi']is not None];assert counts
       n=max(0,min(counts));bound+=n;details.append({'vertices':[u,v],'only_parameter_k':int(k),'copy_pair_upper_bound':n})
      elif bb:continue
      else:
       # y=sgn*x+F(k), exact real coordinate equality. Counting integer solutions
       # is bounded by the width of every valid real x interval.
       ff=[Fraction(sgn*delta[0],Da[0]),Fraction(sgn*z[0],Da[0])]
       lows=[[Fraction(0),Fraction(2)]];highs=[]
       if A['hi']is not None:highs.append(list(map(Fraction,A['hi'])))
       if sgn==1:
        lows.append(afsub([Fraction(0),Fraction(2)],ff))
        if B['hi']is not None:highs.append(afsub(list(map(Fraction,B['hi'])),ff))
       else:
        highs.append(afsub(ff,[Fraction(0),Fraction(2)]))
        if B['hi']is not None:lows.append(afsub(ff,list(map(Fraction,B['hi']))))
       widths=[afsub(hi,lo)for hi in highs for lo in lows];finite=[a for a in widths if a[0]<=0];assert finite,(A['name'],B['name'],u,v,ff,widths)
       mx=min(afval(a,10)for a in finite);n=max(0,mx.numerator//mx.denominator+1);bound+=n
       details.append({'vertices':[u,v],'all_k_perpendicular_identity':True,'copy_relation_sgn':sgn,'copy_relation_offset':enc(ff),'nonincreasing_width_bounds':[enc(a)for a in finite],'copy_pair_upper_bound':n})
   P+=bound;pairs.append({'families':[A['name'],B['name']],'kind':kind,'uniform_contacting_copy_pair_upper_bound':bound,'parallel_certificates':details})
 S=5*(4+390+42)+983+42
 M=S+12*(12*S+2*P)
 out={'status':'PASS exact all-k>=10 bounded cross-family output-tree contacts','parameter':'n=2k, all integers k>=10','tree_edges':12,'tree_vertices':13,'family_count':6,'finite_caps_edge_bound':S,'cross_family_contact_pair_bound':P,'uniform_all_black_w_component_bound':M,'families':[{**a,'base_vertices':sorted(a['base_vertices']),'base_cells':sorted(a['base_cells'])}for a in FAM],'pair_bounds':pairs,'counting_argument':'Each cap vertex touches at most one tree per family, <=12S trees total. Every non-isolated remaining tree touches another family, <=2P trees total. Every component has at most S+12(12S+2P) edges.','scope':'Geometric contact certificate. All-parameter five-stage legality, fixed774 recovery and final phase0 H at(5,-4),S are retained execution dependencies; proof note separately establishes complete envelope.'}
 (OUT/'twenty_cell_tree_contact_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('families','pair_bounds')},indent=2));print([(x['families'],x['uniform_contacting_copy_pair_upper_bound'])for x in pairs])
if __name__=='__main__':main()
