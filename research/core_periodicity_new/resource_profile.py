"""Read immutable literal resource-profile dependencies with hash checks."""
from pathlib import Path
import hashlib,json

def load_profile(path):
 path=Path(path).resolve();profile=json.loads(path.read_text());data={}
 for name,record in profile['files'].items():
  file=Path(record['path']);raw=file.read_bytes();assert hashlib.sha256(raw).hexdigest()==record['sha256'],(name,'hash mismatch')
  data[name]=json.loads(raw)if file.suffix=='.json'else {tuple(map(int,l.split()[:5 if name=='ordinary'else 7]))for l in raw.decode().splitlines()if l.strip()}
 return profile,data,{'resource_profile_file':str(path),'resource_profile_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
