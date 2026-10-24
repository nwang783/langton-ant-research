from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
  return(ss,tt)if 0<=ss<=1 and 0<=tt<=1 else None
 if det(zz,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])));lo,hi=max(Q(0),lo),min(Q(1),hi)
 if lo>hi:return None
 pt=(c[0]+lo*v[0],c[1]+lo*v[1]);j=0 if u[0]else 1;ss=Q(pt[j]-a[j],u[j]);return(ss,lo,hi)

Ssets={'Q':{(-3,-3),(-2,-3),(-1,-3),(-1,-2)},'B':{(-2,-4),(-1,-4),(0,-4),(0,-3)}}
allcases=[]
windows=json.load(open(R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json'))['all44_exact_source_target_C_window_rows']
for A,S in Ssets.items():
 geom=l.literal_geometry(W[A]);ep=tuple(geom['endpoint']);norm=lambda q:l.rot(sub(q,ep[:2]),2);poses=[(0,0,0),after(W['F']),ep];pp=[(*norm(p[:2]),(p[2]+2)%4)for p in poses];verts=list(map(z,pp));segs=list(zip(verts,verts[1:]));out=[];seen=set();total=0;cols=Counter()
 for atom in'DCVU':
  g=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for h in range(4):
   c,d=z((0,0,h)),z(after(W[atom],(0,0,h)))
   for a,b in segs:
    u,v=sub(b,a),sub(d,c)
    corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)]
    bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
    for x in range(bounds[0][0],bounds[0][1]+1):
     for y in range(bounds[1][0],bounds[1][1]+1):
      if(x+y+h)%2:continue
      key=(atom,x,y,h)
      if key in seen:continue
      cc,dd=add(c,(2*x,2*y)),add(d,(2*x,2*y));hits=[(j,hh)for j,(aa,bb)in enumerate(segs)if(hh:=hit(aa,bb,cc,dd))is not None]
      if not hits:continue
      if any(hh[1]==0 and not(hh[0]==1 and j==len(segs)-1 and (x,y,h)==(0,0,0)and(len(hh)==2 or hh[2]==0))for j,hh in hits):continue
      hits=[(j,hh)for j,hh in hits if hh[1]>0]
      if not hits:continue
      seen.add(key);total+=1;head=(x,y)
      core=[q for q in S if l.rot(sub(q,head),-h)in l.K]
      white=[q for q in S if(vv:=l.rot(sub(q,head),-h))in tr['first']and tr['first'][vv][0]=='R']
      if core:cols['CORE']+=1
      elif white:cols['WHITE']+=1
      else:
       lost=[q for q in S if list(l.rot(sub(q,head),-h))in g['inputs']]
       firstt=min(hh[1]for j,hh in hits);at=[(j,hh)for j,hh in hits if hh[1]==firstt]
       owners={j+1 if hh[0]==1 else j for j,hh in at};assert len(owners)==1;owner=next(iter(owners))
       label='Fprefix'if owner==0 else(A+'tail'if owner==1 else'outgoing_first_postFOREIGN_atom_b1')
       r=dict(foreign=A,atom=atom,head=head,h=h,hook_inputs=sorted(lost),first_foreign_contact_new_t=str(firstt),actual_outgoing_owner=label,contacts=[(j,tuple(str(q)for q in hh))for j,hh in hits])
       if not lost:
        assert all(l.rot(sub(q,head),-h)not in tr['first']and l.rot(sub(q,head),-h)not in l.K for q in S)
        r['all4_hook_complete_RAW_plus_actual_M11_context_MISS']=True
       else:r['all4_hook_complete_RAW_plus_actual_M11_context_MISS']=False
       if owner==2:
        assert not lost
        r['route']='FOREIGN_EXIT_contact_owned_by_b1_not_discarded'
       else:
        w=next(r for r in windows if r['source_class']==label and r['contact_atom']==atom)
        counts=[k for k in w['allowed_C_counts_before_contact_ENTRY']if(-k)%4==h]
        r['signed_piece_C_window']=w['allowed_C_counts_before_contact_ENTRY'];r['heading_compatible_C_counts']=counts
        if lost:
         counts=[k for k in counts if k>=4];r['after_signed_hook_min4']=counts
         if not counts:r['route']='excluded_by_piece_window_and_hook_min4'
         elif h==0:
          assert atom=='U'and counts==[4]and head in([(-1,-5),(0,-4)]if A=='Q'else[(0,-6),(1,-5)])
          r['route']='excluded_by_signed_R39_R54_N4_guard'
         else:
          assert atom=='U'and h==3 and counts==[5]and head==((0,-1)if A=='Q'else(1,-2))
          r['route']='excluded_by_signed_B_W5_hole'if A=='B'else'OPEN_Q_W5_hook_loss_funding'
        else:
         assert h==3 and counts==[5];r['route']='OPEN_W5_hook_MISS_tail_contact'
       out.append(r);cols['compatible']+=1

 print(A,'total',total,'counts',cols,'remaining',len(out),'MISS',sum(not r['hook_inputs']for r in out))
 allcases.append(dict(foreign=A,exact_geometry_head_count=total,held_hook_context_classification=dict(cols),all_colour_compatible_earliest_contact_owners_and_clock_routes=out))
flat=[r for a in allcases for r in a['all_colour_compatible_earliest_contact_owners_and_clock_routes']]
assert len(flat)==41
assert Counter(r['route']for r in flat)=={'FOREIGN_EXIT_contact_owned_by_b1_not_discarded':20,'excluded_by_piece_window_and_hook_min4':10,'excluded_by_signed_R39_R54_N4_guard':4,'excluded_by_signed_B_W5_hole':1,'OPEN_Q_W5_hook_loss_funding':1,'OPEN_W5_hook_MISS_tail_contact':5}
miss=[r for r in flat if r['route']=='OPEN_W5_hook_MISS_tail_contact']
assert {(r['foreign'],r['atom'],tuple(r['head']),r['h'])for r in miss}=={('Q','V',(0,-1),3),('B','V',(0,-1),3),('B','V',(1,-2),3),('B','U',(0,-1),3),('B','U',(2,-1),3)}
result=dict(status='AUTHOR_OUTGOING_FOREIGN_OWNER_HOOK_SPLIT_PENDING_REVIEW',scope='GLOBAL first positive ordinary proxy contact on the original Q/B pieces, under simple executed prefix and actual terminalM11. Currenthook split plus signed actual-piece windows. FOREexit terminal contacts are routed to outgoingb1, not incorrectly retained as FOREsources or excluded globally.',foreign_cases=allcases,exact_disjoint_routes=dict(Counter(r['route']for r in flat)),all5_genuine_FOREIGN_owned_W5_hook_MISS_tail_gates=miss,no_b1_terminal_or_other_ordinary_source_closure=True,no_Q_W5_hookloss_closure_until_funding_guard_audited=True,no_arbitrary_tail_or_secondFOREIGN_or_capture=True)
Path('/workspace/shared/langton/Q_B_foreign_first_contact_hook_split_2026-10-24/hook_split.json').write_text(json.dumps(result,indent=2)+'\n')
print('Proper outgoingFORE compatible cases21:15 signedexcluded,6 live;20 otherterminal contacts explicitly owned byb1. HookMISS properFORE tailgates exactly5,allW5.')
