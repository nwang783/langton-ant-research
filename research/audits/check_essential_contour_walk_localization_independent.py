from pathlib import Path
from itertools import product
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
def sign(x):return 1 if x>0 else-1
checks=[]
for j,k,u,v in product(range(-5,6),range(-5,6),[-1,1],[-1,1]):
 # At a boundary's own halflevel, take its OPEN band collar.
 equal=True
 for q in range(min(j,k)-1,max(j,k)+2):
  left=sign(j-q)if j!=q else u;right=sign(k-q)if k!=q else-v
  if left!=right:equal=False
 allowed=k-j==(u if u==v else 0);assert equal==allowed
 if equal:checks.append((j,k,u,v))
ends=[]
for c,j,w in product(range(-5,6),range(-6,7),[-1,1]):
 leftok=rightok=True
 for q in range(min(c,j)-2,max(c,j)+3):
  exterior=1 if c>=q else-1
  left=sign(j-q)if j!=q else-w;right=sign(j-q)if j!=q else w
  leftok&=exterior==left;rightok&=exterior==right
 assert leftok==(j==c+(w==1))
 assert rightok==(j==c+(w==-1))
 if leftok or rightok:ends.append((c,j,w,leftok,rightok))
# Finite algebra controls of the stated ceiling grammar, not a proof by bounded length.
grammar=[]
for n in range(1,13):
 for signs in product([-1,1],repeat=n):
  heights=[-1]
  for w in signs:heights.append(heights[-1]+w)
  if heights[-1]!=0 or max(heights)>0:continue
  if any(signs[i-1]==1 and signs[i]==-1 and heights[i]!=0 for i in range(1,n)):continue
  first=next(i for i,h in enumerate(heights)if h==0);a=sum(w==-1 for w in signs[:first]);assert signs[:first]==(-1,)*a+(1,)*(a+1)
  i=first;valleys=[]
  while i<n:
   b=0
   while i+b<n and signs[i+b]==-1:b+=1
   assert b>=1 and signs[i+b:i+2*b]==(1,)*b;i+=2*b;valleys.append(b)
  grammar.append((signs,a,valleys))
files=['essential_contour_walk_and_K1_high_band_localization.md','canonical_simultaneous_scalar_interpolation.md','zero_output_contractible_canonical_nodes_are_elementary_faces.md','canonical_sheet_two_level_contact_barriers.md','prepared_plateau_black_corner_alternative_and_reverse_output.md','chronological_stream_sheet_exchange.md','positive_output_scope_addendum_stages15_through20.md'];hs={f:hashlib.sha256((D/f).read_bytes()).hexdigest()for f in files}
out={'status':'PASS all-output ordered essential level walk, band height bound and K1 ceiling localization','sources':hs,'exact_collar_sign_controls':checks,'exterior_controls':ends,'ceiling_grammar_controls':len(grammar),'analytic':['The finite full-quotient scalar triangulation has finitely many regular halflevel circles; signed total stream forces at least one essential component. Their simultaneous disjoint embedding orders them across the cylinder. Between consecutive essential curves a regular halflevel with opposite boundary-collar signs separates annulus ends; at least one of its finitely many circles must be essential. Contractible circles cannot separate the two annular ends. The same argument works at an endpoint boundary own level using its open collar.','For labelsj,k and signsu,v, band-collar signs at halflevelq are sign(j-q),sign(k-q), except respectivelyu and-v at equality. Requiring equality for every integerq forces k-j=u whenu=v and0 otherwise, as the boundary and strictly intermediate cases show. Comparing the first/last collars with constant integer exteriors similarly gives the exact endpoint rules. Thus labels/signs are precisely an integer nearest-neighbor walk fromc_left toc_right, with edge labelmax(previous,next). This is contour order, not actual cursor chronology.','Every exchange connector lies on one shared dual edge between consecutive halflevels. Its open segment meets no contour at all; hence a contractible-node graph component after deleting essential nodes cannot leave its spatial essential band, and a direct essential exchange joins consecutive boundaries. Other contractible contours within the band do not invalidate this barrier.','For a base-a band, both boundary collars are belowa+1/2; exterior constants in outer regions also equal a. A high component inside cannot wrap essentially, since its separating boundary would contain an additional essential circle. A bounded lift therefore has a clockwise outer level-(a+1) circle. Unconditional clockwise classification makes this the high star of one C vertex of heighta+1. It cannot enclose a Cface>=a+2. Hence every Cface in that whole band is<=a+1. This does not give a dual lower-L bound with positive output.','In a +,- band of labelj, a LEFT corner of its positive essential boundary exists because its total signed turning over a translated period iszero. The local RIGHT Csector has height>=j+1 and lies in the high band; the band bound makes it exactlyj+1. C>=j+1 contact confinement prevents its plateau crossing either sheet-j boundary, and no larger C exists inside. It is therefore a globally locally-maximal WHITE plateau, finite in the actual full quotient. The signed prepared-plateau theorem forces j+1>c_right, so j>=c_right.','UnderK1, M=c_right+1, the top sheetM consists only of clockwise elementary Cface loops, with no higher active sheet. Essential labels are<=c_right and every peak is consequently exactlyc_right. Startingc_left=c_right-1 and endingc_right gives D^a U^(a+1) followed by balanced D^b U^b valleys. This algebra permits unbounded valley depths and numbers, and is not the ant turn grammar.','A global maximum Cface M can lie only in a basec_right band, namely a ceiling +,- band or final right outer region. The high-C contact barrier keeps each complete max plateau, its canonical parent edges and its max-C suppliers in that same band. Cross-Gamma or same-component transfer within the band stays open.'],'scope':'Positive output explicitly retained. No new speed/fuel bound, no bound on number of bands or graph size, no realized front construction or global capture/exclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
