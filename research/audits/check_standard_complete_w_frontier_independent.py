from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_serial_bridge_archive_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('# Fixed local masks')[0],ns)
ends,graph,component,step,wvertex=[ns[k]for k in('ends','graph','component','step','wvertex')]
D=ROOT/'standard_unread_cap_2026-10-23';a=json.loads((D/'standard_w_frontier_certificate.json').read_text());J=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text());H=J['word'];I={complex(*q)for q in J['seed']};dr=-2-2j;lat=2
shift=lambda B,n:{q+n*dr for q in B};vertices=lambda B:set(graph(B,lat));xy=lambda z:[int(z.real),int(z.imag)]
B=set(I);pos=0j;h=3;tr=[]
for t,ch in enumerate(H*2):
 assert ('L'if pos in B else'R')==ch
 if t<104:tr.append((pos,h,ch))
 pos,h,c=step(B,pos,h);assert c==ch
assert(pos,h)==(2*dr,3)
A=set()
for q in shift(I,2):A|=component(B,lat,ends(q,lat)[0])[1]
K=shift(A,-2);G=B-A;assert len(K)==28 and len(G)==9
assert K=={complex(*q)for q in a['frontier_K']}and G=={complex(*q)for q in a['startup_archive_G']}
def occurrences(q):
 result=[]
 for i,(z,h,c)in enumerate(tr):
  dd=q-z
  if dd.real==dd.imag and int(dd.real)%2==0:
   k=int(dd.real)//-2;result.append((104*k+i,k,i,c))
 return sorted(result)
assert all(not any(k>=2 for t,k,i,c in occurrences(q))for q in G)
def offsets(X,Y):
 out=set()
 for x in X:
  for y in Y:
   delta=x-y
   if delta.real==delta.imag and int(delta.real)%4==0:out.add(int(delta.real)//-4)
 return out
B=set(K);pos=0j;h=3;ph=[];maxmass=maxage=0;Y=set();checked_births=0
for i,ch in enumerate(H):
 assert('L'if pos in B else'R')==ch;w=wvertex(pos,h);assert w==complex(*a['phases'][i]['w_cursor']);ages={}
 for q in B:
  hist=[row for row in occurrences(q)if row[0]<i];assert hist;last=hist[-1];assert last[3]=='R'and last[1]>=-2;ages[q]=i-last[0];checked_births+=1
  assert ages[q]<=240
 maxage=max(maxage,*ages.values());maxmass=max(maxmass,len(B));Y|=vertices(B)|{w}
 assert B=={complex(*q)for q in a['phases'][i]['black_frontier']};ph.append((set(B),w,ages));pos,h,c=step(B,pos,h)
assert(pos,h)==(dr,3);assert shift(K,1)<=B;T=B-shift(K,1);assert len(T)==12 and T=={complex(*q)for q in a['emitted_w_tree_T']}
assert component(T,lat,next(iter(vertices(T))))[1]==T and len(vertices(T))==13
assert offsets(vertices(T),vertices(T))=={0}
assert all(not any(k>=1 for t,k,i,c in occurrences(q))for q in T)
phase_offsets=[]
for i,(B,w,ages)in enumerate(ph):
 os=offsets(vertices(B)|{w},vertices(T));assert not any(m<0 for m in os);assert os==set(a['phases'][i]['all_possible_T_vertex_contact_offsets']);phase_offsets.append(sorted(os))
assert maxage==240 and maxmass==42 and max(z.real+z.imag for z in Y)==6
# Complete-board controls use actual unread finite fields, without deleting old outputs.
cap={-2+1j,-1+1j,1j,1+1j,1,1-1j,2-2j,2-3j,1-4j,1-5j,1-6j}
extras=[set(),cap,{50+50j,51+50j,-50+40j,-40+50j}]
controls=[]
for extra in extras:
 assert not extra&I and all(not any(k>=0 for t,k,i,c in occurrences(q))for q in extra)
 E=G|extra;mi=min(z.real+z.imag for z in vertices(E));n0=max(2,int((6-mi)//8)+1);full=I|extra;pos=0j;h=3;num=0
 for t in range((n0+3)*104):
  n,i=divmod(t,104)
  assert('L'if pos in full else'R')==H[i]
  if n>=n0:
   B,w,age=ph[i];actual=component(full,lat,wvertex(pos,h))[1];expected=shift(component(B,lat,w)[1],n);assert actual==expected;num+=1
  pos,h,c=step(full,pos,h)
 controls.append({'extra_mass':len(extra),'archive_min_vertex_sum':mi,'clearance_period':n0,'complete_component_comparisons':num})
assert controls[1]['clearance_period']==3
note=D/'W_FRONTIER.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='fa3608e58b22fe9911282893dc79f92b9f8f09af18b711be8ecbf7ff915aca52'
out={'status':'PASS eventual complete active w-component mass42 and lifetime age240 for any actual finite-board standard104 tail','note_sha256':sha,'author_checker_sha256':hashlib.sha256((D/'check_standard_w_frontier.py').read_bytes()).hexdigest(),'author_certificate_sha256':hashlib.sha256((D/'standard_w_frontier_certificate.json').read_bytes()).hexdigest(),'K_mass':28,'startup_G_mass':9,'emitted_T_mass':12,'entire_phase_maxmass':42,'entire_phase_maxage':240,'literal_phase_birth_checks':checked_births,'all104_phase_offset_sets':phase_offsets,'controls':controls,'analytic':['The canonical13-cell seed is the actual entire infinite-stream first-L set, by the signed104 full-field induction. Any other finite realization of the same stream is I disjoint union an initial finite F missing every future geometric read. The initial extra field is not dropped or modeled as white.','Two actual periods partition the full canonical board into K+2d and G. K is reconstructed as the complete union of three w-components meeting I+2d, not an arbitrary cropped frontier. Every G cell has no read at actual copy>=2. One period from K gives exactly K+d disjoint union T12, and every T cell has no copy>=1 read. These identities inductively retain the entire output stack and arbitrary F.','The exact doubled-vertex difference equation x-y=2md exhausts every integer translate intersection. T copies meet only at m0. At all104 phases, entire K_i plus the isolated active cursor has no vertex contact with T+md for any negative integer m. No past emitted tree can relay an external attachment to the active frontier, even temporarily within a period.','All phase frontier vertices have coordinate sum<=6. After n periods the maximum is6-8n. Once this is below every vertex sum of finite E=G union F, no E edge can meet the frontier. Together with all-offset T separation, the complete active component equals its certified finite phase component, while every archive remains on the board.','Every K_i black edge has a uniquely last earlier geometric R, copy offset>=-2 and age<=240. For n>=2 that R actually occurred in the standard future. No older initial unread lifetime can substitute at that site. Thus all edges of the full active w-component, not just the next consumed token or a chosen cycle, satisfy the uniform age bound.'],'scope':'Conditional on an already actual infinite standard104 tail on a complete finite board, in the oriented w graph only. Clearance is geometry-dependent. No assertion of capture, universal prestandard component bound, z support forgetting, or converse characterization.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(controls)
