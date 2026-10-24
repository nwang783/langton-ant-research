from pathlib import Path
import ast,hashlib,json,re
P=Path(__file__).resolve();ROOT=P.parent.parent;S=ROOT/'sources/kehao95-core/one_black/lean/OneBlack'
def lean_list(file,name):
 s=(S/file).read_text();start=s.index('[',s.index(':=',s.index('def '+name+' ')));depth=0
 for i in range(start,len(s)):
  depth+=(s[i]=='[')-(s[i]==']')
  if depth==0:return ast.literal_eval(s[start:i+1])
 raise AssertionError('unclosed supplied finite list')
tables={}
for file,name,size,maximum in [('PrefixData.lean','prefixTimes',1376,106258),('EntryData.lean','actualActiveTimes',27,15209),('EntryData.lean','actualLaneTimes',179,62345),('EntryData.lean','pristineLaneTimes',152,64978)]:
 a=lean_list(file,name);flat=[x for row in a for x in row]if isinstance(a[0],list)else a
 assert len(flat)==size and max(flat)==maximum
 tables[name]=dict(count=len(flat),maximum=max(flat))
 if name=='pristineLaneTimes':assert len(a)==22 and all(a);tables[name]['stable_last_entries']=[r[-1]for r in a]
assert re.search(r'def postHitTime\s*:\s*Nat\s*:=\s*7994',(S/'PhaseChecks.lean').read_text())
budgets=dict(prefix=106258+10,inert=9977+10,active=9977+15209+10,shallow=9977+62345+10,ordinary_deep=9977+64978+20,exceptional_deep=9977+64978+7994+30)
assert max(budgets.values())==106268
out=dict(status='PASS independent finite-table extraction and reviewed decomposition count consequence',tables=tables,budgets=budgets,uniform_mass_at_most_one_K_bound=106268,sources={n:hashlib.sha256((S/n).read_bytes()).hexdigest()for n in('PrefixData.lean','EntryData.lean','PristineChecks.lean','PhaseChecks.lean')},scope='Uses retained all-position one-black capture/same-read/exceptional archive theorem, not a new replay or theorem build. Count arbitrary pieces by length plus ten per genuine standard piece, including all true-history joins. Distance-uniform defect count only, not capture-time, optimality or higher-mass induction.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
