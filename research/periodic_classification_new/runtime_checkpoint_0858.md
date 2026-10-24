# Classification checkpoint, 23 October 2026 08:58 UTC

Current SIGNED classification:
- cap3 every nonzero white front excluded allP/width/drift.
- allcap unitaxis±2,0 and unitdiag±1,±1 excluded.
- full2,2 excludedcap6, needs>=7reads.
- fullaxis4 excludedcap5(KR), needs>=6reads.
- cap4 exclusions both3±1,diag3,3(KH),both4±2(KI),both5±1(KS),diag4,4(KW),
  BOTH5±3(LD). Combinedcap4 norm²>=36,Manhattan>=6. Axis6candidatepending.
- KT heavyflowstructure signed: cap4m flow>=3m nofinitephysicalcycle;
  cap4m+1 flow>=3m+1 hasonlyclockwiseunitfacearcs<=3edges, noessentialcycle.
Generalcap4/allcapaxis4/fullfiniteblackseed104conjectureOPEN.

NEW signed structural all-cap period mechanism LC/addendum:
all_cap_period_bounds.md is lateststatusindex with frozenproofhashes.
AnywhitefrontwithD=||d||inf>=3 andclassmultiplicityn>=4 hasP>=4n+2D.
HenceEVERYnonzero completewhitefrontP>=26 (no104minimality/noveltyclaim).
Prooflayers:
1. arbitraryquarterturnwalk D>=2: cyclicclassgaps ki*d,sumki1 give
 P>=4(n-1)+2D. quotient_visit_drift_packing.md and synchronizedphase-note,
 SHAaecd51bd92e318274606a72e6caf734eaeb96f37a56d831bb849e3a6dfc10bdf.
2. ANYcolor actualant cannotmakeFOURconsecutive4-stepphysicalreturns.
 All32 cases explicit same-turnconsecutivecellcontradictions,
 four_unit_returns.certificate.json SHAe38b61d81d5e8c11a4018643aff3099487fc68040e837f7e7fd7505915d391bb.
 Exactly4 THREE-loop preparedpositives retained; doNOTassert3loopno-go.
3. n>=5,D>=3: packing equalitywouldhave>=4unitloops, soP>=4n+2D bymod4.
 frozenfour_unit_return_factor_obstruction.md SHA01ebdb9dd44b00699e0d48cbfd08a6cc8a38468f2c2641faadc7021024640dfb.
4. WHITE n4,D>=3: onlyR-initialthree-loopwordsA=RRRRLRRRRLLL and
 B=RRRRLLLLRLLL needSE/NWblack. Earlierloopcopiesmissnearv(D>=3),
 extremal2D-stepincomingpassageismonotone. BneedsunvisitedNW; Aexcept
 westneedsunvisitedSE; westcanprepareSEonlybyfirst-readLatE(1,0).
 frozenwhite_four_visit_packing_equality.md SHA760259f33049e36baa81087b15d19b39d81f901dc1fb940a3bdf76171bd74900.
UniversalP26 usescap3+n4whitebound,D2diagcap6,D3/D4cap4cases.
Allcapaxis4P>=32,full5±1/5±3P>=30,diag4,4P>=28,diag2,2P>=28.
Earlierweakerperiodnumbers24/28and22/26aresupersededfinalconsequences.

Also signeduniformdensity: cheapzero4-stepgapruns<=3 imply
D>=4:P>=4n+4ceil(n/4)+2D−8;D3:P>=4n+2ceil(n/4),roundedP2mod4.
unit_return_density_refinement.md SHA59df7db33db413b9a8bd64811bcc6129d220fc52b9963e7d3700a92db9895f77.

CompleteAUTHORcandidatependingaudit:
general_flux_d6_0_first_return_w3_real_cap4_N20_M40_mod2.certificate.json
fullaxis6cap4,51,047states/67,920edges/18,545,018extensions,
95,521zero-fluxrows/parity. Auditorrunningindependentreplay.
Ifpassesnorm²>=40,Manhattan>=8; DO NOTclaimuntilpassed.
Noadditionaldriftradiusfamilyplanned/launchedafterthis.

ACTIVE handles, POLL before restart:
6803: genericfullaxis4cap6,zero-flux3rowfirstreturnFIXED N24/M48/q2,max120k.
 Last10,370states/11,080edges,2,738queue,27.7mattempts1560s. Incomplete.
24540: samecap6axis4FIXED N32/M64/q2, justificationnowSIGNEDLC+KR.
 Last6,008states/6,052edges755s,2,284queue,13.5mattempts. Incomplete.
59585: NEW adaptivecap6axis4,Nmin32,fixedscale128/M256/q2,window3,
 saturateddistinctreadcount128. Producerprobe_general_first_return_adaptive_depth.py.
 Last2,816states/2,816edges243s,1,573queue,4.2mattempts. Incomplete.
No cap6axis4 graphcomplete; no new exclusion inferred.

Stoppedolder81719axis4cap6w3N16 at11,466states/12,072edges1456sUNKNOWN,
 dominatedbystrongerperiodbounds. Earlier2275w2N16stopped20,891states.
Completed69648 isaxis6candidateabove. Completed44852both5±3nowsignedLD.
No activeoldfull5±1or4,4casesremain.

Puremathnextpriority structuralmechanism,NOTautomaticradiusorperiodscan.
Allcapaxis4two-rowclocksadmitSATrelaxationslargercaps,notfronts.
Unusedheavy_cycle_frontier.pyweightedUFfiltersemanticsreviewedbutnoproof
 dependsit;stopped56kstate4,4runwasdominatedby3rowKWcertificate.
