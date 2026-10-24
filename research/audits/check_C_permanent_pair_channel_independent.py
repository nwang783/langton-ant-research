from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'C_PERMANENT_PAIR_TERMINAL_CHANNEL_AND_MIDDLE_SHORT_MOTIF.md';JF=D/'C_permanent_pair_terminal_channel_certificate.json';assert sha(P).startswith('10b4b262')and sha(JF).startswith('38c79af8')and sha(D/'certify_C_permanent_pair_terminal_channel.py').startswith('0e29ad14');J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_active_C_entry_exit_independent.py'))};code=Path(ns['__file__']).read_text().split('base={};summary={}')[0].replace(' return sig',' return dict(E=E,d=d,n=n,ev=ev,rep=rep,face=face,H=H,F=F,starts=starts,ends=ends,graphs=graphs,cycles=cycs)');exec(code,ns);analyze,V,off,xy=[ns[k]for k in('analyze','V','off','xy')];base={n:r['word']for n,r in ns['J']['base_controls'].items()}
def paircheck(w,h=0,author=None):
 z=analyze(w,h);n=len(w);ev,face,rep,H,FF=[z[k]for k in('ev','face','rep','H','F')];O={ls[-1][1]['t']for ls in H.values()if ls[-1][1]['c']=='R'}
 def owner(t):
  p,hh,c,i=ev(t);assert c=='L';q,k=rep(p);ls=H[q];j=next(j for j,(tt,e)in enumerate(ls)if tt+k*n==t)
  if j==0:return dict(BLACK_input=True,L_time=t,L_position=xy(p))
  rt=ls[j-1][0]+k*n;rp,rh,rc,ri=ev(rt);assert rp==p and rc=='R';return dict(BLACK_input=False,R_time=rt,L_time=t,position=xy(p),R_heading=rh,L_heading=hh,R_C_face=xy(face(rt)))
 result=[]
 for i in sorted(O):
  if(i+1)%n not in O:continue
  p0,h0,_,_=ev(i);p1,h1,_,_=ev(i+1);f=face(i);assert face(i+1)==f
  p2,h2,_,_=ev(i+2);p3=p2+V[(h2+1)%4];assert len({p0,p1,p2,p3})==4
  q,k=rep(f);after=[t+k*n for t,_ in FF[q]if t+k*n>i+1];mode=ev(after[0])[2];initial=1 if mode=='L'else 2;assert after[:initial]==list(range(i+2,i+2+initial));assert ''.join(ev(t)[2]for t in after[:initial])in['L','RL'];ex=after[initial-1];trans=[];external=0
  for t in after[initial:]:
   assert ev(t)[0]==p3 and ev(t)[2]=='L'and ev(t-1)[0]==p2 and ev(t-1)[2]=='L'and face(t-1)!=f;ow=[owner(t-1),owner(t)];external+=sum(not o['BLACK_input']and o['R_time']>ex and complex(*o['R_C_face'])!=f for o in ow);trans.append(dict(entry=t-1,exit=t,owners=ow))
  assert external>=max(0,2*len(trans)-1)
  if mode=='R'and trans:assert trans[0]['owners'][0]['R_time']==i+2
  row=dict(first_R=i,face=xy(f),permanent=[xy(p0),xy(p1)],initial_exit=after[:initial],later=trans,external=external)
  if author is not None:
   au=next(a for a in author if a['first_R_time']==i);assert au['C_face']==xy(f)and au['permanent_output_cells']==row['permanent'];assert [e['t']for e in au['complete_remaining_C_history']]==after;assert [e['t']for e in au['initial_exit']]==after[:initial];assert au['external_R_owners_after_initial_exit']==external
   assert len(au['all_later_two_L_transits'])==len(trans)
   for a,b in zip(au['all_later_two_L_transits'],trans):assert a['entry']['t']==b['entry']and a['exit']['t']==b['exit']and a['owners']==b['owners']
  result.append(row)
 return result
pairs={n:paircheck(base[n],author=rows)for n,rows in J['base_permanent_pair_controls'].items()};assert {n:len(v)for n,v in pairs.items()}==dict(S104=3,P1564=118,Q4352=216,M10=0,F80=4)
reps=[]
for r in J['representation_controls']:
 v=paircheck(base[r['name']]*r['power'],r['heading']);assert len(v)==r['permanent_pairs'];reps.append(dict(r))
standard=next(v for v in pairs['S104']if v['first_R']==29);assert [o['R_time']for r in standard['later']for o in r['owners']]==[39,28,123,120]and standard['external']==3
# Independent literal full-drift ordinal matching of all named complete cells.
words=['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW'];HH=[list(map('NESW'.index,w))for w in words];nodes={(t,r)for t,w in enumerate(HH)for r in range(len(w))};su={};inc={}
for t,w in enumerate(HH):
 p=-t+0j
 for h in range(4):
  src=[r for r,hh in enumerate(w)if(hh+(1 if r%2==0 else-1))%4==h];q=p+V[h];tt=int(3*q.imag-q.real);kk=int(q.imag)
  if not 0<=tt<8:continue
  dst=[r for r,hh in enumerate(HH[tt])if hh==h];assert len(src)==len(dst)
  for r,s in zip(src,dst):su[t,r]=((tt,s),kk);assert(tt,s)not in inc;inc[tt,s]=((t,r),kk)
chains=[];seen=set()
for start in sorted(nodes-set(inc)):
 u=start;k=0;chain=[]
 while True:
  assert u not in seen;seen.add(u);chain.append((u,k))
  if u not in su:break
  u,dk=su[u];k+=dk
 chains.append(chain)
assert seen==nodes and len(nodes)==25
norm=lambda cs:sorted(tuple((tuple(u),k)for u,k in c)for c in cs);assert norm(chains)==norm(J['middle_short_necessary_C_interface']['all25_named_successor_chains']);chain=max(chains,key=len);assert len(chain)==17
ph={};events=[]
for j,((t,r),k)in enumerate(chain):
 p=-t+k*(3+1j);h=HH[t][r];c='R'if r%2==0 else'L';f=p+off[h];ph[t,r]=(j,k);events.append(dict(time_relative=j,level=t,rank=r,lift=k,position=xy(p),heading=h,turn=c,C_face=xy(f)))
assert events==J['middle_short_necessary_C_interface']['forced17_events'];w17=''.join(v['turn']for v in events);assert w17=='RLRRRRLRRRRLLLLRL';w15=w17[2:]
# First-entry candidate ports of all four relevant physical faces.
F1=-7-2j;F3=-6-1j;F5=-8-1j;F7=-7+0j;ports={};allface=defaultdict(list)
for t,w in enumerate(HH):
 for r,h in enumerate(w):
  f=-t+off[h];k=int(f.imag);rep=f-k*(3+1j);allface[rep].append((t,r,k))
for f in[F1,F3,F5,F7]:
 rows=[]
 for xx in range(int(f.real),int(f.real)+2):
  for yy in range(int(f.imag),int(f.imag)+2):
   p=complex(xx,yy);t=3*yy-xx
   for h in range(4):
    ho=(h-1)%4
    if p+V[ho]+off[ho]!=f:continue
    ranks=[r for r,hh in enumerate(HH[t])if r%2 and hh==h]if 0<=t<8 else None
    rows.append(dict(cell=xy(p),level=t,heading='NESW'[h],parent=xy(p+off[h]),L_ranks=ranks))
 ports[str(xy(f))]=rows
assert [r['level']for r in ports[str(xy(F1))]if r['L_ranks']]==[4]
assert [r['level']for r in ports[str(xy(F3))]if r['L_ranks']]==[3,6]
# Signed WHITE first-entry uses firstL rank1 with SAME R0, removing higher Ls.
assert HH[4][0]==HH[4][1]and HH[3][0]==HH[3][1]
assert ph[4,1]==(1,-1)and ph[3,0]==(2,-1)and ph[3,1]==(6,-1)and ph[6,0]==(7,0)
# C5: T7.L3 is preceded on this SAME face by T7.R2; T5/T8 use only rank1.
assert events[0]['C_face']==xy(F5)and events[0]['level']==7 and events[0]['rank']==2
# C7: T7.L1 is before T7.L3, and T6.L1 feeds that later T7.L3 immediately.
assert su[6,1]==((7,3),0)and HH[7][1]==1 and HH[7][0]==1
# A T9 W/L entering C7 next reads physical T6 incomingS, whose first S isr3.
assert next(r for r,h in enumerate(HH[6])if h==2)==3
assert ph[6,2][0]==15>ph[7,3][0]==12
# T8/T10 entry S/L must have firstR S, hence exact SS prefix.
for f,t in[(F5,8),(F7,10)]:assert next(r for r in ports[str(xy(f))]if r['level']==t)['heading']=='S'
# If C5 usesT5.L1, first activations are C5 at17-P,C1 at2,C3 at7,C5+d at17.
assert ph[5,1]==(16,0);cycle_gaps=['P-15',5,10]
# Permanent-pair physical channel and owner headings at the unknown cells.
assert su[6,4]==((7,4),0)
p0=-6+0j;p1=-7+0j;p2=-7+1j;p3=-6+1j
assert p0+off[HH[6][4]]==p1+off[HH[7][4]]==F7
assert p2+off[0]==F7 and p3+off[1]==F7 and p2+off[2]==-8+1j and p3+off[3]==-6+1j
# Independently replay the complete EMPTY orbit and certify full-field tail.
fs={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(fs['__file__']).read_text().split('# Canonical source')[0],fs);sim,future,phases=fs['sim'],fs['future'],fs['phases'];blank=J['blank_early_retirement_countercontrol'];cuts={int(t)for t in blank['full_field_snapshots']};z=sim(set(),10449,h=0,cuts=cuts)
for t,row in blank['full_field_snapshots'].items():
 bb,p,h=z['snap'][int(t)];assert sorted(map(xy,bb))==row['complete_BLACK']and xy(p)==row['head']and h==row['heading']
bb,p,h=z['snap'][9977];tw,dd,fate,tests=future(bb,p,h);assert tw==base['S104']and tw in phases and dd==-2-2j
PH=defaultdict(list);CH=defaultdict(list)
for t,(p,h,c)in enumerate(zip(z['pts'],z['heads'],z['word'])):
 row=dict(time=t,position=xy(p),heading=h,turn=c,C_face=xy(p+off[h]));PH[p].append(row);CH[p+off[h]].append(row)
for name,rows in blank['full_eight_physical_histories'].items():assert PH[complex(*rows[0]['position'])]==rows
for rows in blank['complete_two_C_histories']:assert CH[complex(*rows[0]['C_face'])]==rows
clear=[]
for typ,qs in [('cell',[complex(*v[0]['position'])for v in blank['full_eight_physical_histories'].values()]),('face',[complex(*v[0]['C_face'])for v in blank['complete_two_C_histories']])]:
 for q in qs:
  hits=[]
  for i in range(104):
   r=z['pts'][9977+i]+(off[z['heads'][9977+i]]if typ=='face'else 0);a=q-r
   if a.real==a.imag and int(a.real)%2==0:
    k=int(a.real)//-2
    if k>=0:hits.append(9977+i+104*k)
  assert not any(t>=10449 for t in hits);clear.append((typ,xy(q),sorted(hits)))
assert z['word'][7895:7910]==w15 and base['S104'][55:70]==w15
zz=analyze(base['S104']);sf=zz['face'](55);q,k=zz['rep'](sf);assert len(zz['F'][q])==15 and zz['ends'][q]+k*104==309
# Standard actual full-field pair and all four SAME owner identities.
for L,rr in[(115,39),(116,28),(127,123),(128,120)]:assert z['events'][9977+L]==9977+rr
O=dict(status='PASS permanent-pair all-length terminal channel, exact middle-short alternatives and scoped full-field controls',proof=sha(P),certificate=sha(JF),script=sha(S),base_pairs=pairs,representation_controls=reps,all25_named_chains=chains,all_four_first_entry_port_domains=ports,conditional_lower_cycle_gaps=cycle_gaps,full_blank_future=dict(cut=9977,word=tw,drift=xy(dd),parity_tests=tests,selected_cells_and_faces_ray_hits=clear,actual_all_original_fields_checked=sorted(cuts)),analytic_review=[
'Two genuinely forever unread adjacent R outputs block two corners of one physical active C face. Cursor geometry forces initial exit L or RL and every subsequent entry/exit to be the actual consecutive two-L channel across the other corners. No quotient alias or bounded exterior is used.',
'For q later visits, the 2q consumed physical lifetimes are distinct. In initial RL mode only its fresh p2 R can supply the first reentry internally; in initial L mode only the first p3 consumption can use a pre-exit lifetime. Every other R must occur after the previous L on the other active C face. Thus at least2q-1 external post-exit R owners, not initial fuel and not automatically additive across faces.',
'The standard pair29/30 attains q2 with actual R owners39,28,123,120, precisely three external post-exit writes and one older internalR28. All341 pair controls and48 rotated/powered representations reconstruct with full-lift owners and prepared BLACK inputs retained.',
'Full lower(3,1) ordinal matching gives all25 named events and the17-read chain, plus exact permanentT6.R4->T7.R4. The resulting unknown T10/T9 channel, external owner headings and last-successor locations use only these complete lower histories. No upper read or period cap is assumed.',
'All four physical C-face incoming L corner domains are rebuilt. C1 can first enter only viaT4.L1, C3 viaT3.L1. C5 cannot first enter throughT7.L3 because its earlier samephysicalR2 already activates it; it retainsT5.L1 orT8.L1 withSSprefix. C7 T6.L1 follows alreadyearlierT7.L1, and T9 entry would nextreadT6.S firstatRANK3 afterT7.L3, so retainsT7.L1 orT10.L1 withSSprefix. These are necessary alternatives, not SS-sufficiency.',
'If C5 takes its lowerparent, actual firstactivation positions give P-15,5,10 gaps around the full-drift three-face cycle. This is a real conditional first-entry cycle; the upperparent case remains open. Last-exit clocks are never replaced by discovery clocks.',
'The two fullyknown local C histories are genuine complete RRRRLL and RRRRLRLL from all four incident complete histories. The bare15-word occurs in standard but its corresponding face has15reads ending309, so the bare word is not an early-retirement certificate.',
'The complete EMPTY trajectory realizes those two early-retired faces at7895 with all eight full physical histories S,W,S,EEWE,SSNS,EEWE,NNNS,EEEW. Full boards at every supplied cut and full9977 infinite104 parity are independently checked; all104 future cell/face rays show no omitted laterread. The finaltwo histories differ from the proposedmiddle NNNSS/EEEWW, so this is not its realization.',
'No four middle-short type is excluded or completed. No WHITE S1, basin split, first/last union connectivity, finite macro alphabet, fuel bound or universal capture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print({n:len(v)for n,v in pairs.items()});print(sha(S.with_suffix('.json')))
