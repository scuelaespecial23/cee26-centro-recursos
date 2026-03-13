# Scripts de automatizacion

Esta carpeta concentra scripts utiles para tareas operativas.

Estructura recomendada por script:

- Script principal (`*.py`, `*.sh`, etc.).
- Guia de uso con ejemplos reales.
- CSV o plantillas de prueba en una carpeta separada.

Scripts iniciales para migrar aqui:

- `automatizar_inclusion_v2.py`
- `GUIA_USO_INCLUSION_V2.md`

Uso recomendado de Inclusion v2.0:

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv
```
