#!/usr/bin/env python3
"""Extract finite supplied maxima; no ant simulation or theorem import."""
import hashlib,json,re
from pathlib import Path
ROOT=Path('/workspace/shared/langton/sources/kehao95-core/one_black/lean/OneBlack')
EXPECT={'prefixTimes':(1376,106258),'actualActiveTimes':(27,15209),
        'actualLaneTimes':(179,62345),'pristineLaneTimes':(152,64978)}
result={'status':'PASS','scope':'Finite table extraction and arithmetic, not re-audit of retained capture theorem.','sources':{},'tables':{}}
for file in ['PrefixData.lean','EntryData.lean']:
    raw=(ROOT/file).read_bytes(); txt=raw.decode()
    result['sources'][file]=hashlib.sha256(raw).hexdigest()
    for m in re.finditer(r'def (\w+).*?:=.*?\[([\s\S]*?)\]\s*(?=def|end|$)',txt):
        if m[1] not in EXPECT: continue
        nums=list(map(int,re.findall(r'\d+',m[2])))
        assert (len(nums),max(nums))==EXPECT[m[1]]
        result['tables'][m[1]]={'count':len(nums),'maximum':max(nums)}
assert set(result['tables'])==set(EXPECT)
phase=(ROOT/'PhaseChecks.lean').read_bytes()
assert re.search(r'def postHitTime : Nat := 7994',phase.decode())
result['sources']['PhaseChecks.lean']=hashlib.sha256(phase).hexdigest()
result['budgets']={
 'prefix':106258+10,
 'inert':9977+10,
 'active':9977+15209+10,
 'shallow':9977+62345+10,
 'ordinary_deep':9977+64978+20,
 'exceptional_deep':9977+64978+7994+30}
result['uniform_mass_one_budget']=max(result['budgets'].values())
assert result['uniform_mass_one_budget']==106268
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
