from check_biexterior_return import *
B=set();p=(0,0);h=0;states=[];turns=[]
for t in range(199):
    states.append((set(B),p,h,exterior(B,p,h)))
    turns.append('L' if p in B else 'R')
    p,h=step(B,p,h)
claims=[]
for name,s,t in [('nontrivial_return_mass_increase',7,10),('normalizer_mass_increase',174,198),('section_pose_repeats',0,16)]:
    a,pp,hh,ee=states[s];b,qq,kk,ff=states[t]
    assert all(ff)
    if name=='section_pose_repeats':
        assert all(ee) and (pp,hh)==(qq,kk) and b!=a
    elif name=='normalizer_mass_increase':
        assert not all(ee) and all(not all(st[3]) for st in states[s:t]) and len(b)>len(a)
    else:
        assert all(ee) and all(not all(st[3]) for st in states[s+1:t]) and len(b)>len(a)
    claims.append({'claim':name,'start':s,'end':t,'word':''.join(turns[s:t]),'entry_B':sorted(a),'entry_mass':len(a),'return_mass':len(b),'entry_pose':(pp,hh),'return_pose':(qq,kk),'flags':[st[3] for st in states[s:t+1]]})
(OUT/'scope_countercontrols.json').write_text(json.dumps({'status':'literal blank-orbit controls passed','claims':claims},indent=2))
print([(c['claim'],c['start'],c['end'],c['entry_mass'],c['return_mass']) for c in claims])
