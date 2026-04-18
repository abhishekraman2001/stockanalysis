import argparse
import zipfile
from pathlib import Path

BLACKLIST_DIRS = {"__pycache__"}
BLACKLIST_SUFFIXES = {".pyc", ".ipynb"}
MAXSIZE_MB = 40


def bundle(homework_dir: str, utid: str):
    """
    Usage:
        python3 bundle.py <homework_dir> <utid>

    Examples:
        python3 bundle.py . abhi234
        python3 bundle.py earnings_bot abhi234
    """
    homework_path = Path(homework_dir).expanduser().resolve()

    if not homework_path.exists():
        raise FileNotFoundError(f"Directory not found: {homework_path}")

    if not homework_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {homework_path}")

    output_path = Path(__file__).resolve().parent / f"{utid}.zip"

    files = []
    for f in homework_path.rglob("*"):
        if not f.is_file():
            continue

        if any(part in BLACKLIST_DIRS for part in f.parts):
            continue

        if f.suffix in BLACKLIST_SUFFIXES:
            continue

        if f.resolve() == output_path:
            continue

        files.append(f)

    if not files:
        print("No files found to include in the zip.")
        return

    print("Files included in zip:")
    for f in files:
        print(f.relative_to(homework_path))

    with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            arcname = homework_path.name / f.relative_to(homework_path)
            zf.write(f, arcname)

    output_size_mb = output_path.stat().st_size / 1024 / 1024

    if output_size_mb > MAXSIZE_MB:
        print(f"Warning: The created zip file is larger than expected ({output_size_mb:.2f} MB)!")

    print(f"Submission created: {output_path} ({output_size_mb:.2f} MB)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bundle a homework directory into a zip file.")
    parser.add_argument("homework", help="Path to the homework directory, e.g. '.' or 'earnings_bot'")
    parser.add_argument("utid", help="UTID used to name the output zip file")

    args = parser.parse_args()
    bundle(args.homework, args.utid)