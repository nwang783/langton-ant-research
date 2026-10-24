from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'even_one_use_staircase_has_a_closed_small_first_R_basin.md';JF=D/'check_four_read_one_use_basin_closure.json';assert sha(P)=='28cb8901ba2ee3792b48e0194a9bc15c04c8ec86c859dc5d03e15e7e54614b5d'and sha(JF).startswith('702fc9c4')and sha(D/'check_four_read_one_use_basin_closure.py').startswith('9c251143');J=json.loads(JF.read_text());H='NESW';V=[1j,1,-1j,-1];xy=lambda p:[int(p.real),int(p.imag)];W={'A':'WWEW','R':'N','D':'SSSN','E':'EWW'};pos={'A':lambda i:complex(i+1,i),'R':lambda i:complex(i+1,i+1),'D':lambda i:complex(i+2,i),'E':lambda i:complex(i+2,i-1)}
def identify(p):
 x,y=int(p.real),int(p.imag);f={0:'R',1:'A',2:'D',3:'E'}.get(x-y)
 if f is None:return None
 i=y-1 if f=='R'else y+1 if f=='E'else y;assert pos[f](i)==p;return f,i
def dest(f,i):return pos[f](i)+V[(H.index(W[f][0])+1)%4]
ports=[];pred={}
for f in'ARD':
 q=pos[f](0);pp=[]
 for h,d in zip(H,V):
  ranks=[r for r,c in enumerate(W[f])if c==h];p=q-d;ident=identify(p);hit=bool(ranks)and ident is not None and dest(*ident)==q
  row=dict(target_family=f,input_direction=h,complete_arrival_ranks=ranks,physical_source=xy(p),source_family_index=list(ident)if ident else None,first_destination=xy(dest(*ident))if ident else None,is_first_R_predecessor=hit);ports.append(row)
  if ranks:
   au=next(v for v in J['physical_predecessor_rows']if v['target_family']==f and v['input_direction']==h);assert row==au
  if hit:pp.append(ident)
 pred[f]=sorted(pp)
assert pred=={'A':[('D',0),('R',-1)],'R':[('A',0)],'D':[]}
for f in'ARD':assert identify(dest(f,0))[0]in'AR'
assert identify(dest('E',0))is None and int(pos['E'](0).real-pos['E'](0).imag)==3
for n in range(1,9):
 d=complex(-n,-n);classes={(f,i)for f in W for i in range(n)};assert len(classes)==4*n
 for f in W:
  assert pos[f](n)-pos[f](0)==-d
  for i in range(n):assert identify(pos[f](i))==(f,i)
# Bind the exact signed scope dependencies, including EVERY-cycle positive
# first-track clock, not merely the selected one-use cycle level.
deps={
'audits/check_four_read_one_use_terrace_independent.json':'206a102fdaa1e6a1755b97d7d780395f1fe212395465b7ef3b0c90bcdcb7d8cd',
'audits/four_read_terrace_even_scope_binding.json':'ca37b0343ec17af4f3c8eacbe5d48580e60bd0b405591fd557679e795adf4d2e',
'audits/check_one_use_L3_transport_independent.json':'ad205d481891b627c1fa783be2f185a112ae784eca5768149867cf68f004069e',
'audits/check_three_read_one_use_staircase_independent.json':'8fd1d92b752e25f17151bac74664fd748543a16f606160f5cf0acefa73385c8d',
'audits/check_mixed_first_track_pipeline_independent.json':'8ff4e2b77138f10372b4074fe93d9e0a7d28b4af32d29137f16cf4df8add9bab'}
for p,h in deps.items():assert sha(R/p)==h
bl=R/'audits/boundary_local_first_track_independent.json';b=json.loads(bl.read_text());assert b['proof_sha256']=='3eee26b9785a7af4b759bca2e0c3c96c5018d65a4d0b1c1aff8b60613194b789'
for p,h in b['dependencies'].items():assert sha(R/p)==h
deps[str(bl.relative_to(R))]=sha(bl)
O=dict(status='PASS exact even staircase first-R basin closure and critical complete-cap4 RIGHT-extremal consequence',proof=sha(P),certificate=sha(JF),script=sha(S),signed_dependencies=deps,all12_physical_direction_ports=ports,first_R_predecessors=pred,analytic_review=[
'The graph is actual physical first-R departure b, not C-discovery or last-exit and not a repaired rank map. CompleteWHITE ensures every visited vertex has a genuinefirstR. The explicit all-index evenreaderD_i=SSSN premise is retained, with E_i=EWW/EWWW; five-read sharedreader alternatives are not covered.',
'All four inputdirections at every A/R/D are exhausted, includingzeroports. Only R_(i-1),D_i firstdepartintoA_i; onlyA_i firstdepartsintoR_i; neitherA_(i+1) norE_i firstdepartsintoD_i although later actualreads supply itsS/N ports. Thus predDempty,predGamma=GammaunionD, and bimageGammaunionD=Gamma. Backwardclosure proves its ENTIRE basin has no deepernodes.',
'Familytransverseoffsets0/1/2/3 are distinct under FULL d=(-n,-n), includingn1 andnonminimalquotients. Physicalneighbor exhaustiveness survivesalllifts. Every E_i isoutside thebasin andvisited. Finitecompletefront quotient therefore forces its bforwardorbit to a DIFFERENT cycle; no infinite spatialdescent argument isused.',
'The b staircase travelsN/E with offsets1/0, whileE hasoffset3 on geometricRIGHT. Cardinalgridpaths cannotcross theembeddedessentialGamma withouta sharedvertex; backwardclosure forbids that. Hence theentire newcycle isonRIGHT. This doesnot mean a newCplateau, first-entrybasin, BLACKroot orfreshfuel, andmultipleE maymerge.',
'Only under COMPLETEWHITEcap4 andGLOBALM=c_right+1 do allnewcyclevertices inherit signedlocalfirstRmaximum/monotoneheight. Finitecycles thenhaveconstantselectedc. The signed mixed first-track proof applies toeverycycle, withALL edgecopies, and eachnonemptyRIGHT repairedcircuit haspositiveintegerwinding; thus c>=c_right+1. Globalc<=M forces EVERY bcycleheightM. No unrestrictedallcapmaximum rule is imported.',
'Finitelymanydisjointembeddedessentialbcycles areordered across thefullcylinder, so aRIGHT-extremal Mcycleexists. The newRIGHT Mcycle contradicts thatselection iftheextremalcyclehasthewholeevenstaircase. Ifitisonlyassumedwhollyoneuse/purealternating, signedcyclicno-fall makesLEFTbitsconstant; bit0fails thephysicalthreeLEFTstaircase eveninshortlifts, bit1forcesallDSSSNundercompletecap4 andusesthebasinargument.',
'Conclusion only: aRIGHT-extremal criticalmaxcap4 bcircle cannotbe bothwhollyoneuse andpurealternating. It mayhave multiplyusededges orRR/LL bends. No strongeroneusetheorem, mixedfront exclusion, odd/fuelbound, allcapnewcycleheight or universalcapture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
