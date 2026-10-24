from pathlib import Path
import json,hashlib
P=Path(__file__);R=P.parent.parent;S=R/'U_q_shadow_reserve_budget_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=S/'manifest.json';assert sha(mf)=='e19a8e32efefab3970ad9f2d2394b3cbc849b8378605c3c2fecd9124ef323c37';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(S/f)==h
ref=json.loads((S/'q_shadow_budget.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
base=P.with_name('check_preforeign_shadow_ports_independent.py');ns={'__file__':str(base)};exec(base.read_text().split('entry=-1+5j')[0],ns)
W,M,K,walk,xy,center=[ns[k]for k in('W','M','K','walk','xy','center')]
raw=lambda s:''.join(W[c]for c in s)
def packet(s):
 z=walk(raw(s));a=walk(raw(s)+M);assert z['feasible']and a['feasible'];par=set();last={}
 for i,(p,h,c)in enumerate(z['reads']):
  if p in par:par.remove(p)
  else:par.add(p)
  last[p]=(i,c)
 ek={z['p']+q*(-1j)**z['h']for q in K};final={p for p,b in a['req'].items()if bool(b)^(p in par)}
 assert len(K)==len(ek)==5 and K<=set(p for p,b in a['req'].items()if b) and ek<=final
 return z,a,last,ek,final-ek,set(p for p,b in a['req'].items()if b)-K
births=[]
for s in('U','UC','UCC'):
 z,a,last,ek,O,I=packet(s);tags={0j:4,1j:19,1:9,1+1j:18,-1+2j:21}
 assert all(q in O and last[q]==(i,'R')for q,i in tags.items());births.append({'source':s,'tags':[[*xy(q),i]for q,i in tags.items()]})
clean=[]
for s in('V','VC'):
 z,a,last,ek,O,I=packet(s);assert last[0j]==(4,'R') and last[1j]==(11,'R') and{0j,1j}<=O
 qr=[(i,c)for i,(q,h,c)in enumerate(a['reads'])if q==3j];assert qr[0]==(19,'L')
 if s=='V':assert 3j in ek and not any(q==3j for q,h,c in z['reads'])
 else:assert any(i==19 and q==3j and c=='L'for i,(q,h,c)in enumerate(z['reads']))
 assert -1+5j-3j==-1+2j and -1+5j-1j==-1+4j
 clean.append({'source':s,'q_first_read_tick':19,'physical_owner':'next full word tick1/read2'if s=='V'else'own C tail tick1/read2','r_A_current_at_RAW_exit':True})
# Original-source and only cleanup-shadow retirement chord reconstructed literally.
u=walk(W['U']);v=walk(W['V']);sourceexit=center(u['p'],u['h']);hp=-1+1j;helperend=center(hp+v['p'],v['h']);assert sourceexit==helperend==-1+7j and center(hp,0)==-3+1j
mass=[]
for s in('D','DC','V','VC','VCC','U','UC','UCC'):
 z,a,last,ek,O,I=packet(s);delta=raw(s).count('R')-raw(s).count('L');expected=3*s.count('C')+4*(s[0]in'VU');assert delta==expected==len(O)-len(I)
 mass.append({'packet':s,'mass_delta':delta,'input_count':len(I),'output_count':len(O),'core_size':5})
for x,y in zip(mass,ref['full_packet_mass_table']):assert x['packet']==y['packet']and x['mass_delta']==y['BLACK_and_CURRENT_delta']and x['input_count']==y['input_count']and x['output_count']==y['output_count']
# Arithmetic reserve and its local switch bookkeeping, without asserting any such tuple is attained.
for u in range(10):
 for v in range(10):
  for s in range(min(u,v)+1):assert 4*u+(u-s)+2*s==5*u+s
out={'status':'PASS all-age q-or-shadow reserve and finite-entry causal budget within uninterrupted U-entry complete8 only','manifest_sha256':sha(mf),'dependencies':ref['dependencies'],'fresh_source_births':births,'cleanup_ownership':clean,'forbidden_shadow_consumer_old_U_exit':list(xy(sourceexit)),'mass_table':mass,'analytic_review':[
'The retained all-age1954/2027 law permits the first loss of a genuine U-family q only at full V/VC(-1,5,S), original full-entry C age2, through the unique UPPER input(0,3). Older prose calling this lower is not used. Own U-family tails preserve q. The new conclusion is conditional on an uninterrupted actual U-entry complete-eight factor, whose whole proxy is already signed simple.',
'The cleanup producer creates genuinely fresh r at its R4 and A at R11, preserved by its possible C tail. Applying signed2043 to its SAME A gives only V/VC at relative(0,4,S), exact source age2, hence original Uclock4. The physical global pose(-1,1,N) and base chord(-3,1)->(-1,7) return to the creating U EXIT, not an adjacent source-start convention. Simplicity prohibits this actual consumer. Because2043 is an all-age first-consumer law, no later-age fallback exists, so SAME A stays CURRENT until the factor ends. Signed r-lock while A current then protects SAME r without circularly assuming whole-cohort permanence.',
'CURRENT is same physical birth and BLACK outside actual K. In plain V the original q is absorbed into exit CORE at RAW cut18, before physical next-word tick1/read2 death; both new reserve identities already exist outside K. VC owns that L in its C tail. Thus assignment switches at the completed producer cut without a gap, and switch count is not merely physical-death count.',
'Every original star/q tag is a distinct U-base fine R event. Every cleanup r/A is a distinct V-base fine R event; actual full packet base intervals do not overlap. One V/VC can clean at most one tracked q because ALL such first losses require its unique upper slot, never selected(1,2). Hence all5u+s labels are distinct and simultaneously CURRENT; distinct current births cannot occupy one cell. The four-star permanence1918 is a retained signed dependency.',
'At every full cut both entry and exit canonical K have five BLACK cells. Literal total mass increments and full residual I/O give r=r0+3c+4v+4u for arbitrary retained unread exterior as well as minimal boards. Reserve subset inequality yields u+s<=r0+3c+4v and exactly r0+3c+4v-u-s unreserved residual cells. Counts u/v refer completed full producers and c actual tails, not an internal atomic cut.',
'No bound on u without c/v, no initial-only fuel, no historical beta/stock component budget, and no persistence across a foreign or departure from this exact language. Unreserved cells are not all freely spendable.'
]};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
