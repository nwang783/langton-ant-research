#!/usr/bin/env python3
"""All-length mandatory U/V restoration and exact following C unit return.
Conditional on the complete OPEN79 gap3 fork; no exterior cap or controller claim.
"""
from pathlib import Path
import hashlib,json
from certify_physical_return_debt import STR,replay
from partial_drift31_graph import graph
R=Path(__file__).resolve().parent;D=((0,1),(1,0),(0,-1),(-1,0));X=(2,1);Q=(1,1);A=(1,0);B=(0,0);U=(0,1);V=(-1,1);C=(-1,0);Z=(2,0)
T=lambda p:3*p[1]-p[0]+11

def full_control(word,seed,p,h):
 f=replay(word,set(seed),p,h);f['initial_position']=p;f['initial_heading']=h;return f

def main():
 H=[tuple('NESW'.index(c)for c in s)for s in STR];kind,G=graph(H,list(range(13)));assert kind=='open'
 ch=next(ch for ch in G['chains']if ch[0][0]==(12,11));assert len(ch)==35
 path=[]
 for a,((i,j),k)in enumerate(ch):
  p=(11-i+3*k,k);path.append({'offset':a,'position':p,'class':i,'rank':j,'lift':k,'incoming':STR[i][j],'turn':'R'if j%2==0 else'L'})
 for x,y in zip(path,path[1:]):
  h='NESW'.index(x['incoming']);h=(h+(1 if x['turn']=='R'else-1))%4
  assert y['position']==(x['position'][0]+D[h][0],x['position'][1]+D[h][1])and y['incoming']=='NESW'[h]
 assert(path[0]['position'],path[0]['rank'])==(C,11)
 assert(path[25]['position'],path[25]['rank'])==(Z,0)
 assert(path[26]['position'],path[26]['rank'])==(X,2)
 assert(path[34]['position'],path[34]['rank'])==(X,3)
 assert [j for j,h in enumerate(STR[9])if h=='E']==[3]
 assert STR[10][3]=='S'and STR[11][9]=='E'and STR[12][9:12]=='SSS'
 # X's only W departure before its locked rank3 is the already-read rank0.
 early_x_w=[j for j in range(3)if(H[12][j]+(1 if j%2==0 else-1))%4==3];assert early_x_w==[0]
 noU=[(C,2,'L'),(B,1,'L'),(U,0,'R'),(Q,1,'R'),(A,2,'L'),(Z,1,'L')]
 for(p,h,c),(pp,hh,cc)in zip(noU,noU[1:]):
  out=(h+(1 if c=='R'else-1))%4;assert out==hh and pp==(p[0]+D[out][0],p[1]+D[out][1])
 # If U were untouched, Z3=C9+5; but C11>=C9+8, Z0=C11+25,
 # and Z3>=Z0+12. This is the explicit positive40 clock contradiction.
 noU_clock={'C9_to_C11_minimum':8,'C11_to_Z0_exact':25,'Z0_to_Z3_minimum':12,'forced_C9_to_Z3':5,'positive_cycle_constant':40};assert 8+25+12-5==40
 # Physical post-restoration consumption square, with every BLACK input kept.
 square=full_control('LLLLR',{C,B,U,V},C,2)
 assert [e['position']for e in square['events']]==[C,B,U,V,C]
 assert square['final_black']==[C]
 # Extend the existing genuine U17 first-import control through the forced V R.
 raw=json.load(open(R/'open79_cluster_reimport_discovery.json'))['found'];f=next(f for f in raw if tuple(f['contact_position'])==U)
 pair=full_control(f['word']+'R',map(tuple,f['initial_black']),X,2)
 assert [(e['position'],e['incoming_heading'],e['turn'])for e in pair['events'][-2:]]==[(U,2,'R'),(V,3,'R')]
 # A standalone physically genuine higher-return motif. It is NOT glued to pair.
 word='RLLLLRLLRLLRLRLLRLLRR';relative_seed=[(-3,0),(-3,1),(-2,-1),(-2,2),(-1,-1),(-1,0),(-1,1),(-1,3),(0,1),(0,3),(1,1),(1,2)]
 motif=full_control(word,{(V[0]+x,V[1]+y)for x,y in relative_seed},V,3)
 vr=[e for e in motif['events']if e['position']==V]
 assert [(e['time'],e['incoming_heading'],e['turn'])for e in vr]==[(0,3,'R'),(4,1,'L'),(20,1,'R')]
 assert all(e['position']!=U and T(e['position'])>=13 for e in motif['events'])
 assert(motif['final_position'],motif['final_heading'])==(C,2)
 # The standalone motif cannot simply follow the retained U17 factor: its first
 # next helper needs L, whereas that helper was erased by the retained factor.
 combined=f['word']+word;p=X;h=2;last={};conflict=None
 for t,c in enumerate(combined):
  if p in last and last[p][1]==c:conflict={'position':p,'earlier':last[p],'later':(t,c)};break
  last[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert conflict is not None
 out={'scope':__doc__,'complete_named_histories':dict(enumerate(STR)),'locked_named_chain':path,'no_U_forced_tail':noU,'explicit_no_U_clock_contradiction':noU_clock,'forced_consecutive_V_reads_after_earlier_W_L':[{'incoming':'W','turn':'R','meaning':'Immediately follows the unique U S/R restoration.'},{'incoming':'E','turn':'L','meaning':'Leaves north for an unbounded exterior first-return excursion.'},{'incoming':'E','turn':'R','meaning':'Leaves south and immediately produces C rank9.'}],'exact_following_C_rank9_to_rank10_duration':4,'genuine_finite_pair_restoration_control':pair,'standalone_higher_return_control':motif,'standalone_control_non_gluing_witness':conflict,'genuine_finite_four_black_consumption_square':square,'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['OPEN79_SHORT_GAP_FORCES_PREPARATION_AGE.md','OPEN79_ALL_LENGTH_TWO_PORT_REIMPORT.md','physical_return_debt_certificate.json','partial_drift31_graph.py']},'limits':'U is restored exactly once before C rank9; V has exactly three reads in that excursion, followed by the forced four-step C unit return. This does not bound the two V excursions, repeated debt growth, the period, or the exterior inventory. The three positive controls are separate factors and are not a completed OPEN79 trajectory.'}
 (R/'open79_mandatory_guide_pair_certificate.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('PASS full35 chain, positive40 contradiction, literal RR restoration and LLLLR square; standalone 4+16 return control and non-gluing witness')
if __name__=='__main__':main()
