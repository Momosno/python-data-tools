# Python Data Tools

Small, focused Python utilities I built for real client needs while strengthening my backend skills. Each tool lives in its own folder and is the base for a larger backend service (FastAPI).

| Tool | What it does | Status |
|---|---|---|
| [`usuarios-por-zonas`](./usuarios-por-zonas) | Parses raw MySQL dumps, joins users with delivery zones and their last order date, and outputs a JSON report grouped by zone | Working |
| [`transcriptor`](./transcriptor) | Transcribes interview audio with the OpenAI transcription API | Work in progress |

## Why these exist

**usuarios-por-zonas** — A client needed to know which customers belonged to each delivery zone, ordered by how recently they had bought. The only source was a SQL export, with no database access. Instead of importing it into a database, I wrote a parser that reads the dump directly and produces a report the client can use.

**transcriptor** — A tool to transcribe recorded interviews, meant to be simple for non-technical users and later integrated into a backend.

## Highlights

- Hand-written parser for SQL `INSERT` dumps — no external dependencies, handles commas inside quoted values and keeps numeric strings with leading zeros (phone numbers, IDs) as text.
- Defensive checks with `assert`: column count must match every row, and duplicate keys stop the run instead of silently overwriting records.
- Users that don't match a known zone are not lost: they go to an explicit `Zona no especificada` group.
- Real data never touches the repo: `.gitignore` blocks `.sql`, `.csv`, `.json` and audio files; the parser ships with fake sample data instead.

## Tech

Python 3 · standard library (`csv`, `json`) · OpenAI Python SDK · python-dotenv

## Quick start

```bash
git clone https://github.com/Momosno/python-data-tools.git
cd python-data-tools/usuarios-por-zonas/ejemplo
python ../usuarios_por_zonas.py
```

See each tool's README for details.
