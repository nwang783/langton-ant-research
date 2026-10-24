"""Independent literal-data, coverage and quantitative check. No author code imported.
Analytic scope: full retained observation transport + elementary 53-period lemma;
retained Lean computation/soundness is attributed, not freshly compiled here.
"""
import ast,gzip,hashlib,json,re
from pathlib import Path
from collections import Counter
ROOT=Path('/workspace/shared/langton'); P=ROOT/'global_attraction_bridge_2026-10-24'; R=ROOT/'sources/imfinn-two-black/lean/TwoBlack'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def literal(p):
    s=p.read_text().split(':=',1)[1].lstrip(); stack=[]; close={'[':']','(':')','⟨':'⟩'}
    for i,ch in enumerate(s):
        if ch in close:stack.append(close[ch])
        elif ch in ']⟩)':
            assert stack and stack.pop()==ch,(p,i)
            if not stack:break
    raw=s[:i+1]
    assert re.fullmatch(r'[\s\d\-,.a-z\[\]⟨⟩()]+',raw)
    raw=raw.translate(str.maketrans({'⟨':'[','⟩':']','(':'[',')':']'}))
    raw=re.sub(r'\.(pp|pm|mp|mm)',r'".\1"',raw).replace('true','True').replace('false','False')
    return ast.literal_eval(raw)
V={'.pp':[2,2],'.pm':[2,-2],'.mp':[-2,2],'.mm':[-2,-2]}
manifest=json.loads((P/'GENERIC_P104_FIXED_COHORT_MANIFEST.json').read_text())
for f,h in manifest['files'].items():assert sha(P/f)==h,(f,h)
for f,h in manifest['retained_sources'].items():assert sha(R/f)==h,(f,h)
paths=[R/'Level1Data.lean']+sorted((R/'Parents').glob('Chunk*.lean'))+sorted((R/'Chan').glob('Data*.lean'))+[R/'PerpData.lean',R/'ParData.lean']
jobs=[]; H0periods=[]; child2=[]; two_tables=[]
def record(src,kind,index,cells,ms,s,u):
    assert all(0<=t<=s for t in ms)
    jobs.append({'id':len(jobs),'source':src,'kind':kind,'index':index,'cells':sorted(map(list,set(map(tuple,cells)))),'windows':[{'kind':'switch','time':t}for t in sorted(ms)]+[{'kind':'terminal','time':s}],'terminal_drift':u,'updates':s+104})
def family1(src,kind,index,F,H):
    dg,near,far=F;n,D,C,ms,s,u,A=H
    cells=near+[[z[i]+n*V[dg][i]for i in range(2)]for z in far]
    record(src,kind,index,cells,ms,s,u)
def family2(F,a,b):
    vs,bl=F
    return[[q[i]+sum([a,b][j]*V[vs[j]][i]for j in ids)for i in range(2)]for q,ids in bl]
for p in paths:
    src=str(p.relative_to(R)); data=literal(p)
    if p.name=='Level1Data.lean':
        for i,(F,H)in enumerate(data):family1(src,'level1',i,F,H)
    elif p.parent.name=='Parents':
        for i,(point,tau,H,fs)in enumerate(data):
            s,dg,A,t1,psi,tdiv,periods=H;H0periods.append(periods)
            record(src,'parent_terminal',i,[point],[],s,V[dg])
            for j,(F,h)in enumerate(fs):family1(src,'parent_tail',[i,j],F,h)
    elif p.parent.name=='Chan':
        point,kids,kids2=data;child2+=kids2
        for i,(F,base,H)in enumerate(kids):family1(src,'channel_child',i,F,H)
    else:
        for i,row in enumerate(data):
            if p.name=='PerpData.lean':c,H,s1=row;s2=[];kind='perpendicular'
            else:c,side,H,s1,s2=row;kind='parallel'
            two_tables.append(c);F,base=c;a,b,D1,C1,m1,D2,C2,m2,s,u,A=H
            record(src,kind,i,family2(F,a,b),m1+m2,s,u)
            assert len(s1)==a-base[0]
            if kind=='parallel':assert len(s2)==b-base[1]
            else:assert b<=base[1]
            for j,h in enumerate(s1):record(src,kind+'_slab1',[i,j],family2(F,base[0]+j,h[0]),h[3],h[4],h[5])
            for j,h in enumerate(s2):record(src,kind+'_slab2',[i,j],family2(F,h[0],base[1]+j),h[3],h[4],h[5])
with gzip.open(P/'TWO_BLACK_WORD_JOBS.jsonl.gz','rt')as f:
    for j,line in enumerate(f):assert jobs[j]==json.loads(line),(j,jobs[j],line)
assert j+1==len(jobs)==102488
freeze=lambda x:json.dumps(x,separators=(',',':'))
assert Counter(map(freeze,child2))==Counter(map(freeze,two_tables))
inv=json.loads((P/'TWO_BLACK_WORD_JOB_INVENTORY.json').read_text())
counts=dict(Counter(j['kind']for j in jobs));assert counts==inv['counts']
assert inv['source_hashes']=={str(p.relative_to(R)):sha(p)for p in paths}
assert sum(j['updates']for j in jobs)==inv['total_fixed_updates']==3437614232
one=[j for j in jobs if j['kind']not in ('perpendicular','parallel','parent_terminal')]
two=[j for j in jobs if j['kind']in ('perpendicular','parallel')]
terms=[j for j in jobs if j['kind']=='parent_terminal']
assert len(one)==99550 and len(two)==506
assert max(j['updates']-104 for j in one)==270504
assert max(j['updates']-104 for j in two)==166816
assert max(len(j['windows'])-1 for j in one+two)==5
assert max(H0periods)<=6000
assert max(j['updates']-104 for j in terms)<624000
# Bind the ACTUAL unconditional closure, not the conditional Final theorem alone.
assert 'two_black_final hpart_proved' in (R/'Main.lean').read_text()
assert 'theorem part_checks' in (R/'PartData.lean').read_text()
assert 'checkPart_sound' in (R/'PartData.lean').read_text()
assert 'certB (k.F.cells (k.base + i)) 6000' in (R/'Channels.lean').read_text()
assert 'Kid1.ok' in (R/'PerpKids.lean').read_text() and 'Kid1.ok' in (R/'Check2Par.lean').read_text()
assert '⟨10504, .mm, 49, 10816, 31, 0, 4000⟩' in (R/'OneBlack.lean').read_text()
assert 'certB_sound [] 200' in (R/'OneBlack.lean').read_text()
# Exact analytic bound, using only allowed normals and diagonal full drift.
norms=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
positive=[sum(n[i]*d[i]for i in range(2))for n in norms for d in V.values()if sum(n[i]*d[i]for i in range(2))>0]
assert min(positive)==2
assert -103+52*2>0 and 103//2==51
fringe=104+53*104;family=270504+6*fringe;direct=104*6000+fringe
assert (fringe,family,direct,8*direct)==(5616,304200,629616,5036928)
source_extra=['Main.lean','PartData.lean','Remaining.lean','ParentTable.lean','Pose.lean','Tail.lean','Family.lean','TheoremA.lean','OneBlack.lean','Level1.lean','Highway.lean','Check.lean','Check2.lean','Check2Par.lean','Corridor.lean','Succ.lean','Perp.lean','Par.lean','Parent0.lean','Channels.lean','PerpKids.lean','PartCheck.lean','Final.lean','Parents/All.lean','Chan/All.lean']
report={'status':'PASS: generic GP104 only, conditional on attributed retained Lean soundness/computations; no fresh Lean compilation or canonical direct-leaf annotation claimed','manifest_sha256':sha(P/'GENERIC_P104_FIXED_COHORT_MANIFEST.json'),'script_sha256':sha(Path(__file__)),'counts':counts,'jobs_checked_exactly':len(jobs),'switch_windows':sum(len(j['windows'])-1 for j in jobs),'maximum_parent_direct_period_budget':max(H0periods),'maximum_parent_terminal_start':max(j['updates']-104 for j in terms),'one_family_max_start':270504,'two_family_max_start':166816,'max_switches':5,'fringe':fringe,'family_bound':family,'generic_before_third_fixed_cohort_bound':direct,'direction_marked_bound':8*direct,'source_hashes':{str(p.relative_to(R)):sha(p)for p in paths},'semantic_source_hashes':{f:sha(R/f)for f in source_extra if (R/f).exists()},'analytic_checks':['53-copy parity stabilization: all old initial bits absent on future rays by k52; preceding equal-phase-copy lag at most51','Full observation, not just position, corridor transfer; insertion windows wholly within the other relation interval','No new arbitrary prefix on coverage branches; Main plus PartData discharges the 22-channel partition','Original-cut fixed cohort coupling through but excluding the third old-L update, with actual full-field pristine lemma at each interior cut','Terminal truncated-piece fringe charged; generic PermanentP104 is not canonical word or guard predicate'],'unclaimed':['canonical624375 universal bound','global attraction','a cumulative fixed-cohort fuel bound after resetting','new independent Lean native_decide replay']}
out=ROOT/'audits/generic_P104_fixed_cohort_independent.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if not k.endswith('hashes')},indent=2));print('REPORT_SHA256',sha(out))
