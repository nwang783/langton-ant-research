"""Complex-coordinate literal controls for ordered residual transactions."""
import json,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent;J=json.loads((ROOT/'literal_residual_geometry.json').read_text());G={g['name']:g for g in J['geometry']};K={complex(*p)for p in J['core']};W={a:G[a]['word']for a in 'DVU'};W['C']='LLLLRLRRRRLRRRR';MARK='LLLLRLRRRRL';DIR=(1j,1,-1j,-1)
def first_requirements(word):
 p=0j;h=0;initial={};parity=set()
 for c in word:
  needed=(c=='L')^(p in parity)
  if p in initial and initial[p]!=needed:return None
  initial[p]=needed;parity.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=DIR[h]
 return {p for p,b in initial.items()if b}
def packetize(word):
 packets=[]
 for c in word:
  if c=='C':packets[-1]+=c
  else:packets.append(c)
 return packets
def replay(word,seed):
 # Far unread cells test arbitrary-background equality, not just minimal support.
 seed=set(seed)|{1001+1002j,-1002+1003j};board=set(seed);residual={p:None for p in seed-K};p=0j;h=0;consumed_initial=0;recycled_count=0
 for number,name in enumerate(packetize(word)):
  g=G[name];turns=g['word'];pose=p;heading=h;world=lambda c:pose+complex(*c)*(-1j)**heading;ins=[world(q)for q in g['inputs']];outs=[world(q)for q in g['outputs']]
  assert K and {pose+k*(-1j)**heading for k in K}<=board
  for q in ins:consumed_initial+=residual.pop(q) is None
  assert all(q not in residual for q in outs)
  for slot,q in enumerate(outs):residual[q]=(number,name,slot)
  recycled_count+=len(g['recycled'])
  for c in turns:
   assert (p in board)==(c=='L');board.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=DIR[h]
  assert p==world(g['endpoint'][:2]) and h==(heading+g['endpoint'][2])%4
  assert board-{p+k*(-1j)**h for k in K}==set(residual)
 assert len(seed)==5+consumed_initial+sum(v is None for v in residual.values())
 return recycled_count
limit=int(sys.argv[1])if len(sys.argv)>1 else 8;counts=[0]*(limit+1);recycled=0;digest=hashlib.sha256();examples=[]
def dfs(s):
 global recycled
 raw=''.join(W[c]for c in s);seed=first_requirements(raw+MARK)
 if seed is None:return
 counts[len(s)]+=1;recycled+=replay(s,seed);digest.update((s+'\n').encode())
 if 'U'in s and len(examples)<6:examples.append({'word':s,'seed':sorted([[int(p.real),int(p.imag)]for p in seed]),'mass':len(seed)})
 if len(s)<limit:
  for c in 'DCVU':dfs(s+c)
for c in 'DVU':dfs(c)
result={'status':'PASS_LITERAL_FINITE_CONTROLS_NOT_TRANSFER_EXCLUSION','depth':limit,'counts_by_macro_length':counts,'total':sum(counts),'recycled_input_output_transactions':recycled,'word_digest':digest.hexdigest(),'examples':examples,'ledger_sha256':hashlib.sha256((ROOT/'literal_residual_geometry.json').read_bytes()).hexdigest()};(ROOT/f'finite_controls_depth{limit}.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items()if k!='examples'}))
