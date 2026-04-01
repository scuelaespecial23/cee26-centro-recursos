# Scripts de automatizacion

Esta carpeta concentra automatizaciones y sus guias de uso.

## Disponible hoy

- `automatizar_inclusion_v2.py`: crea estructura de carpetas y permite distribuir documentacion comun. Se puede usar tanto en Linux como en Windows con Python 3.
- `GUIA_USO_INCLUSION_V2.md`: guia detallada de uso en Linux y Windows.

## Recomendacion de uso

Antes de ejecutar cualquier script:

1. leer la guia,
2. probar primero con `--dry-run`,
3. validar rutas y archivos de entrada,
4. recien despues ejecutar en modo real.

## Acceso rapido

- [Abrir guia detallada](./GUIA_USO_INCLUSION_V2.md)
- [Abrir script principal](./automatizar_inclusion_v2.py)

## Ejemplo minimo

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv --dry-run
```
