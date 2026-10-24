from pathlib import Path
import json, hashlib
SELF=Path(__file__).resolve(); ROOT=SELF.parents[1]; D=ROOT/'K1_pipeline_detours_2026-10-23'
notes={'top_output_rail_capacity_and_deep_band_root_partition.md':'eb620d9f7806a6d1a6c9dc69d8fe4131f1b42401e2487996762751eafa48b1c8','half_turn_typed_rail_no_hidden_even_next_parent.md':'83e9c7f500df2a439cebd25aa5dc3972935e0685b3295379134ea4c76b0dac2f'}
for p,h in notes.items(): assert hashlib.sha256((D/p).read_bytes()).hexdigest()==h
# Recompute all odd cap-four local height possibilities directly, normalizing M=0.
levels={}
for label,rs,ls in [('singleton',(1,0),0),('opposite_R',(1,1),1),('same_R',(2,0),1)]:
 out=[]
 for rE,rW in (rs,rs[::-1]):
  a=-max(rE,rW)
  for lE in range(ls+1):
   lW=ls-lE
   C=(rW+a,rE+a);L=(1-lE+a-1,1-lW+a-1)
   assert max(C)==0
   out.append(sorted(L))
 expected={'singleton':[-1,-1],'opposite_R':[-2,-1],'same_R':[-3,-2]}[label]
 assert all(x==expected for x in out);levels[label]=expected
# Bind the earlier independently fresh all-110 reconstruction, not the author's table.
prev=SELF.parent/'check_half_turn_typed_nonpositive_capacity_independent.json'
j=json.loads(prev.read_text());assert len(j['all110_next_parent_challenge_five_profiles'])==5
# Reconstruct the five physical next-parent completions with uninspected odd corners.
ns={'__file__':str(SELF.parent/'check_zero_output_Q2_and_same_curve_ear_independent.py')}
exec(Path(ns['__file__']).read_text().split('def close(')[0],ns)
rows=[]
for row in ns['base']:
 for t in range(4):
  hh,ht,en,bd=ns['locate'](row,-2,t)
  children={-2+.5+.5j+(ns['cp'][v]-(.5+.5j))*1j**t for v in row[2]}
  if hh[-1]=='NNSN' and hh[-1+1j]=='EEWE' and -1+1j in children:
   assert en==-1
   rows.append(tuple(hh[p] for p in (-1,-2,-2+1j,-1+1j)))
assert set(rows)=={('NNSN','WWW','NSN','EEWE'),('NNSN','WWWE','NNNS','EEWE'),('NNSN','WWWE','NSNN','EEWE'),('NNSN','WWEW','NSSS','EEWE'),('NNSN','EWWW','SSNS','EEWE')}
assert len(rows)==5
out={'status':'PASS top-output/deep-band partition and no-hidden-evenness clarification','note_sha256':notes,'normalized_incident_L_heights':levels,'all110_physical_next_parent_profiles_SE_SW_NW_NE':rows,'dependencies':{prev.name:hashlib.sha256(prev.read_bytes()).hexdigest()},'analytic':[
'The five typed-rail stopping witnesses are actual corners of the global maximum U_n or R_n, not merely arbitrary odd classes. The previously signed residual negative-unit output union consists of canonical maximum-face entries, maximum-I same-R helpers and maximum-I singletons; its optional disjoint ancestor singletons also touch M. Thus its entire payment lies in Q, the top non-positive-flat odd classes: |U|+nSanc<=Q and H<=6Q+|U|<=7Q-nSanc.',
'The independently recomputed incident-height cases exhaust odd WHITE cap4 multiplicities one and three. Their minimum is M-3, so none of these top classes can meet an L minimum at M-4 or below. Rotation changes labels, not these height differences.',
'Every reservation in the signed early six-mode union touches an explicitly actual maximum: P0/J/Q2/F/Q1. Therefore Ntop>=E. The two positive-flat x/e outputs per interface3 source are distinct, yielding T>=2n3; disjoint Q and T then give Ntop>=2n3+ceil((H+nSanc)/7). Combine these possibly overlapping lower bounds only by maximum.',
'For ACTUALLY DISTINCT ordered inter-curve spatial bands with minima<=M-j, j>=4, odd roots must lie outside Ntop, and different bands have distinct physical root classes. At least max(0,k_j-Nodd+Ntop) bands are unrooted. In the already signed disjoint physical edge partition each supplies two counterflows of magnitude at least j, hence4jD beyond baseline6D. This is a single partition, not addition of overlapping clocks. No number of deep bands is inferred from branch counts or repeated minima.',
'The clarification is also independently reconstructed from all110 profiles in all rotations. All five possible next parents, including WWW/NSN odd uninspected corners, have actual canonical entry a. The retained actual parent identities close a physical four-face birth cycle, so this alternative is impossible before inverse-I saturation. No hidden evenness of the next parent is needed.'
],'scope':'Complete WHITE cap-four translating front and exact rail interfaces. K1 only for early/ordered-band applications. H<=7Q-nSanc; Ntop>=max(E,2n3+ceil((H+nSanc)/7)); P>=6D+4jD max(0,k_j-Nodd+Ntop) for actual distinct deep bands. OUTPUT/current bounds, not initial fuel, manufactured bands, K1 exclusion or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
