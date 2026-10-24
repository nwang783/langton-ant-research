"""Build the continuation archive without downloaded packages or binaries.

Run from any directory. The output is placed at the workspace root.
"""
from hashlib import sha256
import json
from pathlib import Path
import zipfile


WORKSPACE = Path(__file__).resolve().parents[2]
RESEARCH = WORKSPACE / "ant_rethink"
OUTPUT = WORKSPACE / "Langton_Ant_First_Principles_2026-10-21.zip"
SUFFIXES = {".md", ".py", ".cpp", ".json", ".jsonl", ".txt",
            ".stdout", ".log", ".csv", ".tsv"}
EXCLUDED_PARTS = {"deps", "__pycache__", ".git"}


def main():
    paths = [p for p in RESEARCH.rglob("*")
             if p.is_file() and p.suffix in SUFFIXES
             and not (EXCLUDED_PARTS & set(p.relative_to(RESEARCH).parts))]
    paths.append(WORKSPACE / "ant_global/root/standard.json")
    paths.sort(key=lambda p: p.relative_to(WORKSPACE).as_posix())
    payload = {p.relative_to(WORKSPACE).as_posix(): p.read_bytes()
               for p in paths}
    manifest = "".join(f"{sha256(data).hexdigest()}  {name}\n"
                       for name, data in payload.items())
    readme = (
        "Langton's ant research continuation, 21 October 2026\n\n"
        "Start with ant_rethink/README.md.\n"
        "The full conjecture is not proved or disproved by this work.\n"
        "No undecidability or independence claim is made.\n\n"
        "SHA256SUMS.txt records every retained source and research file.\n"
        "Downloaded dependencies and compiled binaries are excluded.\n"
        "The retained standard seed preserves the scripts' relative paths.\n"
    )
    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as archive:
        archive.writestr("START_HERE.txt", readme)
        archive.writestr("SHA256SUMS.txt", manifest)
        for name, data in payload.items():
            archive.writestr(name, data)
    with zipfile.ZipFile(OUTPUT) as archive:
        assert archive.testzip() is None
        for name, data in payload.items():
            assert archive.read(name) == data
        assert not any(EXCLUDED_PARTS & set(Path(name).parts)
                       for name in archive.namelist())
    print(json.dumps({"archive": str(OUTPUT), "research_files": len(payload),
                      "archive_entries": len(payload) + 2,
                      "uncompressed_payload_bytes": sum(map(len, payload.values())),
                      "archive_bytes": OUTPUT.stat().st_size,
                      "sha256": sha256(OUTPUT.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
