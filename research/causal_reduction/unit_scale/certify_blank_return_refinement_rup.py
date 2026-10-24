from pathlib import Path
import json
import certify_short_refinement_rup as C
P=Path(__file__).resolve().parent
z=json.loads((P/'blank_return_refinement.json').read_text());C.dom=z['images'];C.run('white_blank_return',C.H,(0,0),set())
