from pathlib import Path

for path in sorted(Path(".").glob("*.json")):

    with path.open("r", encoding="utf-8", newline="") as f:
        lines = f.readlines()

    with path.open("w", encoding="utf-8", newline="\n") as f:
        for i, line in enumerate(lines):
            f.write(line.rstrip("\r\n"))
            if i < len(lines) - 1:
                f.write("\n\n")
            else:
                f.write("\n")
