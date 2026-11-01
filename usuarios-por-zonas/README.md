# usuarios-por-zonas

Turns two raw MySQL dumps (users and delivery zones) plus a CSV of last-order dates into a JSON report: users grouped by zone, most recent buyers first.

## Input

Three files in the working directory:

| File | Content |
|---|---|
| `zonas.sql` | `INSERT INTO zonas (id, nombre) VALUES ...` |
| `usuarios.sql` | `INSERT INTO usuarios (..., nombre, apellido, email, telefono, zona_id) VALUES ...` |
| `u.csv` | `email, last order datetime` (one row per user) |

The [`ejemplo/`](./ejemplo) folder has fake data in exactly this format.

## Run

```bash
cd ejemplo
python ../usuarios_por_zonas.py
```

## Output

| File | Content |
|---|---|
| `zonas_output.json` | Zones indexed by `id` |
| `usuarios_output.json` | Users indexed by `email`, enriched with `fultimopedido` |
| `usuarios por zonas_output.json` | The report: `{ zone name: [users sorted by last order, newest first] }` |

Example (from the sample data):

```json
{
  "Zona no especificada": [
    { "nombre": "Diego", "apellido": "López", "email": "diego.lopez@example.com", "telefono": "01100000004", "fultimopedido": "2024-08-01 14:10:00" }
  ],
  "Zona Norte": [
    { "nombre": "Carla", "apellido": "Ruiz, Hija", "email": "carla.ruiz@example.com", "telefono": "01100000003", "fultimopedido": "2024-10-20 09:45:30" },
    { "nombre": "Ana", "apellido": "Gómez", "email": "ana.gomez@example.com", "telefono": "01100000001", "fultimopedido": "2024-10-02 11:20:00" }
  ]
}
```

## How it works

1. **Parse headers** — reads the column names from the `INSERT INTO (...)` line.
2. **Parse rows** — walks each `(...)` row character by character, tracking whether it is inside a quoted value, so commas inside text don't split fields.
3. **Clean values** — converts numbers to `int`, but keeps strings with a leading zero (phones) as text.
4. **Validate** — asserts that every row has as many values as columns and that no key is repeated.
5. **Join** — attaches the last-order date from the CSV (emails not found are reported), then groups users by zone and sorts each group.

## Next steps

- Read file paths from CLI arguments instead of fixed names.
- Expose it as a FastAPI endpoint that accepts the dumps as uploads.
