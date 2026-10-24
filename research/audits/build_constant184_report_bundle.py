from pathlib import Path
import json,hashlib
ROOT=Path('/workspace/shared/langton');AU=ROOT/'audits';U=ROOT/'causal_reduction/unit_scale';DEST=ROOT/'deliverables/constant_184_capturing_family';DEST.mkdir(parents=True,exist_ok=True)
M=json.loads((U/'prepared1564_uniform_support_manifest.json').read_text());A=json.loads((U/'prepared1564_source_endpoint_family.json').read_text());H=json.loads((ROOT/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
family={k:M[k]for k in ['seed_families','initial_pose','stages']}
endpoint={k:A[k]for k in ['after_checkpoint_word','capture_word']}
exceptions={str(n):json.loads((U/f'prepared1564_endpoint_N{n}.json').read_text())for n in range(1,5)}
for j in exceptions.values():
 for k in ['scope','status','seconds']:j.pop(k,None)
reverse=json.loads((U/'prepared1564_reverse_source.json').read_text());reverse.pop('scope',None)
data=dict(format_version=1,parameter_domain='integer N>=1',standard_word=H,family=family,uniform_endpoint=endpoint,small_endpoints=exceptions,reverse=reverse)
(DEST/'family_data.json').write_text(json.dumps(data,indent=2)+'\n')
# Standalone already-reviewed ray checker.
s=(AU/'check_prepared1564_connected_capture_independent.py').read_text();fn=s[s.index('def periodic('):s.index('reports=[]')]
(DEST/'common.py').write_text('"""Exact finite-board translating-word tail checker. Standard library only."""\nfrom collections import defaultdict\nV=((0,1),(1,0),(0,-1),(-1,0))\n'+fn)
# Full all-N prefix proof with data rather than any source-tree dependency.
s=(AU/'check_1564_constant_mass_family_independent.py').read_text()
functions=s[s.index('def scalar('):s.index('# Exact affine target router positions')].replace("for j,z in enumerate(sorted(Hseed,key=xy)):addseed(pA,pB+z,('initial',j))\n",'')
arrangement=s[s.index('# Each read template'):s.index('# Exact defect count')]
header='''"""Verify EVERY N>=1 by an exact affine-interval arrangement, not sampling."""
from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();DATA=json.loads(SELF.with_name('family_data.json').read_text());M=DATA['family'];H=DATA['standard_word'];W=M['stages'][-1]['word'];D=(1j,1,-1j,-1)
def xy(z):return(int(z.real),int(z.imag))
def lit(w,p=0j,h=3):
 out=[]
 for i,c in enumerate(w):out.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return out,p,h
G=defaultdict(list);seeds=[];blocks=[];block=0;pA=14+14j;pB=33+70j;h=3
'''
setup='''
for j,(x,y) in enumerate(M['seed_families']):addseed(complex(x[0],y[0]),complex(x[1],y[1]),j)
timeA=timeB=0
for st in M['stages']:
 assert [int(pA.real),int(pB.real)]==st['start_x_N_constant']
 assert [int(pA.imag),int(pB.imag)]==st['start_y_N_constant'] and h==st['heading']
 assert [timeA,timeB]==st['start_time_N_constant']
 ca,cb=st['count_N_constant'];addblock(st['word'],(ca,cb),st['kind'])
 timeA+=len(st['word'])*ca;timeB+=len(st['word'])*cb
assert len(seeds)==184 and len(blocks)==16 and (timeA,timeB)==(25588,91747)
assert (pA,pB,h)==(14+14j,-6-6j,0)
'''
finish='''
# The exact inverse ten turns follow from the co-moving source and no remote collision.
cofixed={complex(*b)-(33+70j)for a,b,tag in seeds if complex(*a)==14+14j};assert len(cofixed)==13
back=set(cofixed);p=0j;hh=3;rev=[];backreads=[]
for _ in range(10):
 p-=D[hh];backreads.append(p);post=p in back;rev.append('R'if post else'L');hh=(hh+(-1 if post else 1))%4;back.symmetric_difference_update({p})
history=''.join(rev[::-1]);assert history=='LRLRRRRLLL'
for aa,bb,tag in seeds:
 A=complex(*aa)-(14+14j);B=complex(*bb)-(33+70j)
 if A==0:continue
 for q in backreads:
  n=Fraction(int((q-B).real),int(A.real));assert not(n.denominator==1 and n>=1 and int(A.imag)*n==int((q-B).imag))
allowed={(H*2)[i:i+10]for i in range(104)};assert len(allowed)==84
compressed=''.join(st['word']for st in M['stages'][:-1])
def cost(w):
 s=history+w;return sum(s[i:i+10]not in allowed and s[i+1:i+11]not in allowed for i in range(len(w)))
assert [cost(compressed+W*n)for n in(1,2,3)]==[706,1320,1934]
assert W[-10:]==(W*2)[-10:]
assert sum((W*2)[i:i+10]not in allowed and(W*2)[i+1:i+11]not in allowed for i in range(len(W)))==614
out=dict(status='PASS all integer N>=1',initial_mass=184,physical_classes=len(G),parameter_regions=total_regions,spatial_slabs=total_slabs,read_obligations=total_obligations,parameter_partition=sorted(globalcuts),exact_first_L_count=[0,184],true_inverse_ten=history,prefix_K=[614,92],prefix_time=[25588,91747],obligation_digest=digest.hexdigest())
assert (len(G),total_regions,total_slabs,total_obligations)==(1460,1508,4581,17470)
SELF.with_name('prefix_result.json').write_text(json.dumps(out,indent=2)+'\\n');print(out)
'''
(DEST/'verify_prefix.py').write_text(header+functions+setup+arrangement+finish)
# Endpoint proof: keep the exact code but replace source-tree inputs by the public data file.
s=(AU/'check_1564_family_endpoint_capture_independent.py').read_text()
start=s.index('def trace(')
s='''"""Verify all-N endpoint stabilization, all small exceptions and complete standard tails."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
from common import periodic
SELF=Path(__file__).resolve();DATA=json.loads(SELF.with_name('family_data.json').read_text());M=DATA['family'];A=DATA['uniform_endpoint'];H=DATA['standard_word'];W=M['stages'][-1]['word'];word=A['after_checkpoint_word'];V=((0,1),(1,0),(0,-1),(-1,0))
assert len(word)==56504 and len(W)==1564
'''+s[start:]
s=s.replace("J=json.loads((U/f'prepared1564_endpoint_N{n}.json').read_text())","J=DATA['small_endpoints'][str(n)]")
s=s.replace("note_sha256=sha(U/'prepared1564_source_endpoint_capture.md'),source_certificate_sha256=sha(U/'prepared1564_source_endpoint_family.json'),manifest_sha256=sha(U/'prepared1564_uniform_support_manifest.json'),","data_sha256=hashlib.sha256(SELF.with_name('family_data.json').read_bytes()).hexdigest(),")
s=s.replace("SELF.with_suffix('.json').write_text","SELF.with_name('capture_result.json').write_text")
(DEST/'verify_capture.py').write_text(s)
# Reverse proof similarly keeps the reviewed determinant checks.
s=(AU/'check_1564_original_bistandard_independent.py').read_text();start=s.index('canonical=set();')
s='''"""Verify the entire backward trajectory for every original family member."""
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import json,hashlib
from common import periodic
SELF=Path(__file__).resolve();DATA=json.loads(SELF.with_name('family_data.json').read_text());M=DATA['family'];J=DATA['reverse'];H=DATA['standard_word'];V=((0,1),(1,0),(0,-1),(-1,0))
'''+s[start:]
line="source=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(source[source.index('def periodic('):source.index('reports=[]')],str(SELF),'exec'))\n"
s=s.replace(line,'')
s=s.replace("note_sha256=hashlib.sha256((U/'prepared1564_original_bistandard_family.md').read_bytes()).hexdigest(),canonical_source_sha256=hashlib.sha256((U/'prepared1564_reverse_source.json').read_bytes()).hexdigest(),","data_sha256=hashlib.sha256(SELF.with_name('family_data.json').read_bytes()).hexdigest(),")
s=s.replace("SELF.with_suffix('.json').write_text","SELF.with_name('reverse_result.json').write_text")
(DEST/'verify_reverse.py').write_text(s)
(DEST/'verify_all.py').write_text('''"""Run the three independent exact checks. Requires Python 3, standard library only."""
from pathlib import Path
import subprocess,sys
root=Path(__file__).resolve().parent
for name in ['verify_prefix.py','verify_capture.py','verify_reverse.py']:
 subprocess.run([sys.executable,str(root/name)],cwd=root,check=True)
print('PASS: every supplied184-cell family member is bi-standard; its forward defect count is unbounded.')
''')
print(DEST)
