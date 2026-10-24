"""Exact single-period packet parse of the source-bound standard word."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
source=P.parent/'recovered_bundle/ant_global/root/standard.json'
W=json.loads(source.read_text())['word']
assert len(W)==104
stack=[]
for i,a in enumerate(W):
 if stack and stack[-1][0]==a:
  stack[-1][1].append(i)
  if len(stack[-1][1])==4:stack.pop()
 else:stack.append([a,[i]])
survivors=sorted(i for a,indices in stack for i in indices)
q=''.join(W[i] for i in survivors)
assert q=='LRRLLRLLRLRRLRLLRLLRLLRRLRLLRLLR'
def G(a,n):return a*4 if n==0 else a*2+G('L' if a=='R' else'R',n-1)+a*2
def B(a,n,m=None):
 b='L' if a=='R' else'R'
 return a+G(b,n)+(a*3 if m is None else a+G(b,m)+a*2)
expected={(0,21):('B','R',1,1),(26,31):('G','R',0,None),(31,40):('B','R',0,None),
 (43,52):('B','L',0,None),(53,66):('B','L',0,0),(69,74):('G','R',0,None),
 (74,91):('B','R',2,None)}
gaps=[]
assert survivors[0]==0 and survivors[-1]==103
for i,j in zip(survivors,survivors[1:]):
 if j==i+1:continue
 kind,a,n,m=expected.pop((i,j));gap=W[i+1:j]
 assert gap==(G(a,n) if kind=='G' else B(a,n,m))
 gaps.append({'between_core_positions':[i,j],'word':gap,'kind':kind,'sign':a,
 'first_depth':n,'second_depth':m,'mass_change':gap.count('R')-gap.count('L')})
assert not expected
core_positions=[{'sign':a,'exponent':len(indices),'positions':indices} for a,indices in stack]
assert ''.join(str(z['exponent']) for z in core_positions)=='1221211211212122112121'
assert W.count('R')-W.count('L')==12
assert q.count('R')-q.count('L')==-4
assert sum(g['mass_change'] for g in gaps)==16
out={'status':'PASS','source':str(source),'word':W,'reduced_core':q,'core_syllables':core_positions,
 'deleted_packets':gaps,'mass_change':12,'core_mass_change':-4,'packet_mass_change':16,
 'scope':'Literal single-period parse. All-epoch core stability uses the separate standard lift certificate.'}
(P/'standard_packet_decomposition.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
