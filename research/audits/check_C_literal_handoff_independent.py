from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'C_LITERAL_HANDOFF_UNCAPPED_DOMAINS.md';JF=D/'C_literal_handoff_domains_certificate.json'
assert sha(P)=='60e586548aa3a84e98f8fba62aa625850383d3bc6c5c09a1e29d6dce84ac6435'and sha(JF)=='9bd295f4d88e651eaa0c6284c4e37ad295014820542fc02d7858e24b00c3cd13'and sha(D/'certify_C_literal_handoff_domains.py')=='d1e8f1277cc5bd6abce40551bfebb572b6cbe94fc3c3731b6ec038e63ccc025a';J=json.loads(JF.read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_active_C_entry_exit_independent.py'))};src=Path(ns['__file__']).read_text().split('base={};summary={}')[0].replace(' return sig',' return dict(E=E,d=d,n=n,ev=ev,rep=rep,face=face,H=H,F=F,starts=starts,ends=ends,graphs=graphs,cycles=cycs)');exec(src,ns);analyze=ns['analyze'];base=ns['J']['base_controls'];xy=ns['xy']
def handoffs(w,h=0):
 z=analyze(w,h);n=len(w);A=z['starts'];B=z['ends'];G=z['graphs'];sets=[set().union(*(cc for cc,nu,g in cs))if cs else set()for cs in z['cycles']];ans=[]
 for u,f in G[1].items():
  v=complex(*f['target']);nu=f['voltage']
  if A[v]+nu*n!=B[u]+1:continue
  first=G[0][v];assert complex(*first['target'])==u and first['voltage']==-nu and first['L_phase']==f['L_phase'];t=B[u];p,hi,c,i=z['ev'](t);assert c=='L';rc,k=z['rep'](p);ls=z['H'][rc];heads=[e['hi']for tt,e in ls];turns=''.join(e['c']for tt,e in ls);white=ls[0][1]['c']=='R';assert turns in(['RL','RLR']if white else['L','LR'])and heads[:2 if white else 1]==[hi]*(2 if white else 1)
  if turns[-1]=='R':assert heads[-1]==(hi+2)%4
  su=B[u]-A[u];sv=B[v]-A[v];assert first['clock_gap']==su+1 and f['clock_gap']==sv+1
  if v in sets[0]:assert su<n
  if u in sets[2]:assert sv<n
  rows=[dict(canonical_time=tt,**{**e,'p':xy(e['p'])})for tt,e in ls]
  ans.append(dict(source=xy(u),target=xy(v),voltage=nu,L_phase=i,complete_read_class=xy(rc),complete_history=rows,first_is_WHITE=white,permanent_output=turns[-1]=='R',source_span=su,target_span=sv,first_edge_gap=first['clock_gap'],last_edge_gap=f['clock_gap'],on_full_first_cycle=v in sets[0],on_WHITE_first_cycle=v in sets[1],on_last_cycle=u in sets[2]))
 return ans
canon=lambda ls:sorted(json.dumps(z,sort_keys=True)for z in ls);summary={}
for name,rows in J['base_controls'].items():
 own=handoffs(base[name]['word']);assert canon(own)==canon(rows);summary[name]=dict(count=len(own),modes=sorted(set(''.join(e['c']for e in r['complete_history'])for r in own)))
for row in J['representation_controls']:
 own=handoffs(base[row['name']]['word']*row['power'],row['heading']);assert len(own)==row['count']==summary[row['name']]['count']*row['power']
assert len(J['representation_controls'])==48 and summary['S104']['count']==1 and summary['M10']['count']==0 and summary['F80']['count']==2
O=dict(status='PASS conditional cap-free literal C handoff domains and cycle-span identities only',proof=sha(P),certificate=sha(JF),script=sha(S),controls=summary,representation_controls=48,analytic_review=[
'Literal last-L to first-active-next-face makes the same L both firstL and lastL of its physical cell. Complete-WHITE history is RL or RLR with same first two headings and opposite finalR; BLACK-first is L or LR. These are full histories, so finalR is an actual permanent output. BLACK LR keeps distinct initial and output roots.',
'No later same-heading read can reactivate retired sourceC; a later opposite-heading L also returns to it. Alternation therefore forbids more reads, without a supplied cap. This local bound is not a bound at adjacentC faces or elsewhere.',
'The same physicalL supplies both first and last selected edges with exact full-drift voltages. Their gaps equal source-span+1 and target-span+1. On the corresponding respective embedded cycle the full gaps sumP, yielding the appropriate endpoint span<P. No existence or membership of a handoff is inferred.',
'Independently rebuilt all193 handoffs across five complete controls and48 rotations/powers. StandardL26 has completeNNS RLR, source/targetspans13/101. Prepared80 retains bothRL andRLR without a WHITEfirstcycle. Supplied1564/4352 retain allBLACK/WHITE possibilities, so cycleintersection alone cannot discardRL.',
'No handoff existence, canonical12/4 ages, finite modulealphabet, WHITE lifetimeS1, controller classification or universal entry follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
