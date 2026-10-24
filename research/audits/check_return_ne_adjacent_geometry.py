"""Independent literal/affine geometry for seven previously replayed color proofs."""
import json,pathlib,hashlib
P=pathlib.Path('/workspace/shared/langton');S=P/'scattering/return_ne_frontier/adjacent';R=P/'audits/return_ne_adjacent_replay'
W='LRLLRRRRLLRLLRRRRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLR'
D=((0,1),(1,0),(0,-1),(-1,0));PH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,k):return tuple(x*k for x in a)
def sub(a,b):return add(a,scale(b,-1))
def form(a,b,c):return (a,b,c+100*(a+b))
def constant(c):return (0,0,c)
def ptadd(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def walk(w,h):
 x=y=0;qs=[]
 for c in w:
  qs.append((x,y));h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
 return qs,(x,y),h
qne=walk(W,1)[0]
def translate(q,p):return add(p[0],constant(q[0])),add(p[1],constant(q[1]))
def le(a,b):return all(v<=0 for v in sub(a,b))
def scalar(q,key):return sub(*q) if key[0]=='u' else add(*q)
def equalpoints(a,b):assert tuple(map(tuple,a))==tuple(map(tuple,b))
manifest=json.loads((R/'replay_manifest.json').read_text());assert manifest['status']=='all seven matched'
for row in manifest['results']:
 assert hashlib.sha256((S/('certify_cycle72.py' if row['file']=='certificate_cycle72.json' else 'certify.py')).read_bytes()).hexdigest()==row['source_sha256']
 assert hashlib.sha256((S/row['file']).read_bytes()).hexdigest()==row['certificate_sha256']
 assert (S/row['file']).read_bytes()==(R/row['file']).read_bytes()
parent=json.loads((P/'scattering/return_ne_frontier/mass5_interfaces.json').read_text())
expected={15:(104,520,168039,(-2,-2,-68),(-2,-2,3),3,0),29:(104,416,132511,(-2,0,0),(-2,0,47),1,99),45:(104,520,165799,(-2,-2,-68),(-2,-2,3),3,0),56:(104,416,127355,(-2,0,0),(-2,0,47),1,99),62:(104,416,126907,(-2,0,-6),(-2,0,41),1,99),72:(104,416,174812,(-2,0,-30),(-2,0,-102),2,0),'cycle72':(104,624,217977,(-2,0,39),(-2,0,-36),1,100)}
forced_epochs={15:-12,45:-20,72:-16,29:-29,56:-31,62:-33};offs={15:1,45:-11,72:-33,29:-12,56:-12,62:-24};rows=[]
for r in [15,29,45,56,62,72,'cycle72']:
 stem='r'+str(r) if isinstance(r,int) else r;c=json.loads((S/f'certificate_{stem}.json').read_text());tfile=S/f'template_{stem}.json';t=json.loads(tfile.read_text());assert c['template_sha256']==hashlib.sha256(tfile.read_bytes()).hexdigest()
 rr=72 if r=='cycle72' else r
 q=(form(-2,-2,-33),form(-2,-2,-14));s=(form(-2,0,6+qne[rr][0]),form(-2,0,-43+qne[rr][1]));hit=(q[0],form(-2,2,offs[rr])) if rr in (15,45,72) else (form(-2,2,offs[rr]),q[1]);points=[s,q,hit]
 if r=='cycle72':points += [(form(-2,2,-112),q[1]),(form(-2,2,-112),hit[1])]
 assert c['initial_points']==[[list(a),list(b)] for a,b in points]
 pose=(constant(0),constant(0));h=0;clock=constant(0);bound={k:tuple(v) for k,v in c['finite_prefix_bounds'].items()};checks=0
 for idx,seg in enumerate(t['segments']):
  w=seg['word'];qs,delta,hh=walk(w,h)
  if seg['type']=='finite':count=constant(1)
  else:
   assert seg['type']=='periods' and len(w)==104 and w in [W[j:]+W[:j] for j in range(104)] and hh==h
   count=form(*seg['count_m_k_constant']);assert le(constant(1),count)
  for v in qs:
   a=translate(v,pose);b=ptadd(a,(scale(sub(count,constant(1)),delta[0]),scale(sub(count,constant(1)),delta[1])))
   for point in [a,b]:
    for key,lim in bound.items():
     value=scalar(point,key);assert le(value,lim) if key.endswith('max') else le(lim,value),(r,idx,key)
    checks+=1
  pose=ptadd(pose,(scale(count,delta[0]),scale(count,delta[1])));h=hh;clock=add(clock,scale(count,len(w)))
  assert c['records'][idx]['time']==list(clock);equalpoints(c['records'][idx]['pose'][0],pose);assert c['records'][idx]['pose'][1]==h
 ex=expected[r];assert c['capture_time']==list(clock);equalpoints(c['capture_pose'][0],pose);assert c['capture_pose'][1]==h;assert clock==form(*ex[:3]);equalpoints(pose,(form(*ex[3]),form(*ex[4])));assert (h,c['tail_phase'])==ex[5:]
 tw=t['infinite_tail_word'];assert tw==W[c['tail_phase']:]+W[:c['tail_phase']];qs,delta,hh=walk(tw,h);assert hh==h and list(delta)==c['tail']['drift'];tail=[translate(v,pose) for v in qs];assert c['tail_read_points']==[[list(a),list(b)] for a,b in dict.fromkeys(tail)]
 # Include every entry bit, not only the last packet, in finite archive bounds.
 for point in (points[:-1] if r=='cycle72' else points):
  for key,lim in bound.items():
   val=scalar(point,key);assert le(val,lim) if key.endswith('max') else le(lim,val),(r,key,'initial')
 if r in (15,45):
  for point in tail:
   assert le(scalar(point,'u_max'),bound['u_max']) and le(scalar(point,'z_max'),constant(35))
  assert delta[0]-delta[1]==0 and sum(delta)<0
 if r in (29,56,62):
  zoff=(43,53) if r in (29,56) else (31,41)
  assert all(scalar(point,'z_min')[:2]==(-4,0) for point in tail)
  assert min(scalar(point,'z_min')[2]+400 for point in tail)==zoff[0] and max(scalar(point,'z_min')[2]+400 for point in tail)==zoff[1]
  assert bound['u_min']==constant(-82)
  assert all(le(scalar(point,'z_max'),constant(35)) for point in tail) and sum(delta)==0
  # First phase-72 read in this cyclic tail is even/even, unlike A odd/odd.
  p72=tail[(72-c['tail_phase'])%104];assert tuple(a[2]%2 for a in p72)==(0,0)
 if r==72:
  assert all(scalar(point,'z_min')[:2]==(-4,0) for point in tail)
  assert (min(scalar(point,'z_min')[2]+400 for point in tail),max(scalar(point,'z_min')[2]+400 for point in tail))==(-135,-125)
  assert bound['u_max']==constant(106)
  p72=translate(walk(W,h)[0][72],pose);age=form(0,1,-45)
  forced=ptadd(p72,(scale(age,delta[0]),scale(age,delta[1])));equalpoints(forced,(form(-2,2,-112),q[1]))
  assert add(clock,add(scale(age,104),constant(72)))==form(104,520,170204)
 if isinstance(r,int):
  expected_s={15:61942,29:61956,45:61972,56:61983,62:61989,72:61999}[r]
  expected_hit={15:74914,29:72328,45:73298,56:67172,62:67036,72:112022}[r]
  assert c['first_contacts']==[list(form(104,208,expected_s)),list(form(104,104,10881)),list(form(104,312,expected_hit))]
  old=next(a for a in parent['rows'] if a['phase']==r);pp,ph=old['phase_zero_pose_constant'];p72=translate(walk(W,ph)[0][72],(form(-2,0,pp[0]),form(-2,0,pp[1])));age=form(0,1,forced_epochs[r]);assert le(constant(0),age)
  forced=ptadd(p72,(scale(age,old['drift'][0]),scale(age,old['drift'][1])));equalpoints(forced,hit)
 if r=='cycle72':assert c['first_contacts'][4] is None and c['first_contacts'][3]==list(form(104,520,170204))
 
 if r in (29,56,62,72):
  ph0=walk(W,0 if r in (29,56,62) else 2)[0];dr=walk(W,0 if r in (29,56,62) else 2)[1]
  def before(v,q,i,j):
   dx,dy=v[0]-q[0],v[1]-q[1]
   return dx*dr[1]==dy*dr[0] and dx%dr[0]==0 and (dx//dr[0]>0 or (dx==0 and i<j))
  fresh=[j for j,q0 in enumerate(ph0) if not any(before(v,q0,i,j) for i,v in enumerate(ph0))];assert fresh==PH
  assert [j for j in fresh if j%2==0]==[14,28,32,38,46,56,60,62,70,72]
 rows.append({'phase':r,'read_endpoint_checks':checks,'drift':delta,'capture_time_m_k':ex[:3],'capture_heading':h,'tail_phase':c['tail_phase'],'complete_prefix_bounds':bound})
out={'status':'PASS','color_replay_binding':hashlib.sha256((R/'replay_manifest.json').read_bytes()).hexdigest(),'rows':rows,'scope':'Seven complete color certificates bound; six retained-core recurrence couplings are proved separately in the accompanying analytic note.'}
(P/'audits/return_ne_adjacent_geometry.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
