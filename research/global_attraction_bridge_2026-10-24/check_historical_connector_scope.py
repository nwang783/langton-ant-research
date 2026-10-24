from pathlib import Path
import hashlib,json
P=Path(__file__).parent
R=json.loads((P/'RECURSIVE_PHASE13_PACKET_CHECKED.json').read_text());A=json.loads((P/'SOUTHWEST_ARCHIVE_IMPORT_CHECKED.json').read_text());J=json.loads((P/'CHRONOLOGICAL_SPINE_ORIENTATION_CHECKED.json').read_text());D=((0,1),(1,0),(0,-1),(-1,0));W=R['W'];v=(157,164);w=(158,164)
def geo(p,h,word):
 Q=[]
 for c in word:Q.append(p);h=(h+(1 if c=='R'else -1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return Q,p,h
pre=W*100+W[:13]+R['modes']['M']['recovery_word'];PQ,pe,ph=geo((0,0),1,pre)
assert len(pre)==21125 and(pe,ph)==((228,229),0)
assert[(i,pre[i])for i,q in enumerate(PQ)if q==v]==[(8183,'R')]and PQ[8184]==w
assert[(i,pre[i])for i,q in enumerate(PQ)if q==w]==[(8184,'R'),(8292,'L'),(8304,'R'),(8308,'L')]
FQ,_,_=geo(pe,ph,W[41:]+W[:41]);assert min(x for x,y in FQ)==225
TQ,te,th=geo((0,0),0,A['T_recovery']);assert min(x for x,y in TQ)==-38 and(te,th)==((-36,-10),0)
VQ,_,_=geo((0,0),th,A['T_tail_word']);assert min(x for x,y in VQ)==-4 and min(x for x,y in VQ[:100])==-4
assert 210+min(x for x,y in VQ)==206 and 208+min(x for x,y in VQ[:100])==204
post=A['postcollision_word'];Q,qe,qh=geo((207,229),1,post);assert v not in Q and[(i,post[i])for i,q in enumerate(Q)if q==w]==[(47390,'R')]
assert(qe,qh)==((155,215),1)
NW=A['controls'][0]['complete_future_certificate']['tail_word'];NQ,ne,nh=geo(qe,qh,NW);assert min(y for x,y in NQ)==213 and(ne[0]-qe[0],ne[1]-qe[1])==(-2,2)
controls=[]
for c in J['MT_controls']:
 q=(0,0);h=1;last={};parent={}
 for k,ch in enumerate(c['complete_prefix_word']):
  old=q;h=(h+(1 if ch=='R'else -1))%4;q=(q[0]+D[h][0],q[1]+D[h][1]);last[old]=k;parent[old]=q
 assert parent[v]==w and last[v]==8183 and last[w]==79196+208*c['n']
 B={tuple(q):i for q,i in c['full_end_field']};assert B[v]==8183 and B[w]==last[w]
 assert v not in {tuple(q)for q,p in c['full_interval_tree']}
 controls.append(dict(n=c['n'],edge=[v,w],last_departure=last[v],parent_last_read=last[w],jump=last[w]-last[v],whole_end_identities=[[v,B[v]],[w,B[w]]],old_vertex_absent_from_reset_tree=True))
fs=['CHRONOLOGICAL_SPINE_ORIENTATION_MANIFEST.json','../audits/check_chronological_spine_independent.json','PRIMITIVE_SPINE_CLOCK_MANIFEST.json','SOUTHWEST_ARCHIVE_IMPORT_MANIFEST.json','../audits/check_southwest_archive_import_independent.json']
for f in fs:assert(P/f).exists(),f
out=dict(status='AUTHOR exact all-n historical connector; independent audit pending',parameter='integer n>=100',edge=[v,w],last_departure=8183,parent_last_read='79196+208n',jump='71013+208n',both_actual_R_outputs_permanent=True,
 exclusions=dict(NE_min_x=225,T_min_x='2n+192',SW_full_min_x=206,SW_partial_min_x=204,collision=[206,229],post_last_parent_offset=47390,NW_all_future_min_y=213),controls=controls,
 dependencies={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in fs},scope='A full historical edge omitted by interval resetting. Not a universal connector theorem, whole-history maximum formula, or one-orbit unbounded-age example.')
(P/'HISTORICAL_CONNECTOR_SCOPE_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n');print('AUTHOR exact all-n edge and3 full historical controls checked')
