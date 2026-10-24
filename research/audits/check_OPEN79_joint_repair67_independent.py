from pathlib import Path
import json,hashlib
S=Path(__file__); R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proof=D/'OPEN79_JOINT_REPAIR67_FINITE_CONTROL.md'; cert=D/'open79_joint_repair67_certificate.json';assert sha(proof)=='ddd6b13af859f3704f93df0e160646c51de8e3b9c4d534ee2ea4d6a14931912d';assert sha(cert)=='1c76fcfd8d710b216ef94fda8459b5e3429a00d8c3f7615393317d79763756e6'
J=json.loads(cert.read_text());B={complex(*q):('initial',tuple(q)) for q in J['complete_initial_black']};seed=set(B);p=complex(*J['initial_position']);h=1j*(-1j)**J['initial_heading'];events=[];owners=[];history={};word=''
for t in range(67):
 c='L'if p in B else'R';word+=c;hh=[1j,1,-1j,-1].index(h);e={'time':t,'position':[int(p.real),int(p.imag)],'normal_level':int(3*p.imag-p.real+11),'incoming_heading':hh,'turn':c};events.append(e);history.setdefault(p,[]).append([t,hh,c]);
 if c=='L':
  born=B.pop(p);owners.append({'L_time':t,'position':e['position'],'owner':'initial BLACK input'if isinstance(born,tuple)else born});h*=1j
 else:B[p]=t;h*=-1j
 p+=h
assert word==J['word']and events==J['events']and owners==J['all_L_lifetime_owners'];assert set(B)=={complex(*q)for q in J['complete_final_black']};assert (p,h)==(-2+0j,-1);assert len(seed)==18 and len(B)==15
for q,k in [(1j,'U_reads'),(-1+1j,'V_reads'),(-1+0j,'C_reads')]:assert history[q]==J[k]
assert history[2+1j]==[[0,2,'R']]and history[1+0j]==[[2,2,'R']];assert all(e['normal_level']>=13 for e in events[7:62]);assert len([x for x in owners if x['owner']=='initial BLACK input'])==18;assert not any(isinstance(v,tuple)for v in B.values())
assert {o['L_time']:o['owner']for o in owners if o['L_time']in(53,62,63,64,65)}=={53:17,62:6,63:3,64:16,65:61}
out={'status':'PASS genuine finite repair67 factor only','proof':sha(proof),'certificate':sha(cert),'script':sha(S),'actual_word':word,'initial_mass':18,'final_mass':15,'final_pose':[-2,0,3],'all_initial_lifetimes_consumed':True,'full_final_R_births':sorted([[int(q.real),int(q.imag),t]for q,t in B.items()]),'scope':'Independent deterministic full-board replay uses only the literal eighteen-cell initial field and pose, not author search. All67 reads, full output, actual L owners, unique U/V restorations, V36/8 first returns, and C four-L consumption square agree. This is a genuine finite factor consuming18 prepared inputs; it does not realize the complete OPEN79 earlier/later chronology or full drift classes, phase schedule, growth-eight inventory, repeated word or regeneration.'};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
