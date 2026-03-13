# Guia de uso - Inclusion v2.0

## Script

- `scripts/automatizar_inclusion_v2.py`

## Objetivo

Crear estructura de carpetas por estudiante en base a CSV, respetando chips de `localidad`, `nivel` e `institucion`.

Ruta generada:

- `inclusion/<anio>/<localidad>/<nivel>/<institucion>/<estudiante>/`

## Requisitos minimos del CSV

Columnas obligatorias:

- `apellido`
- `nombre`
- `localidad`
- `institucion`
- `nivel`

Columna opcional:

- `docentes` (separados por `;` por defecto)

## Comando base

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv
```

## Modo prueba (sin crear nada)

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv --dry-run
```

## Opciones utiles

- `--separador-lista ","` cambia separador de docentes.
- `--docs-replicar-todos <carpeta>` replica archivos comunes a todos los estudiantes.
- `--crear-admin` crea `_administracion/<anio>`.
- `--crear-plantilla-modelo` crea `_plantilla_carpeta_estudiante/...`.

## Reglas clave de normalizacion

- `Pendiente Definir` se transforma a `pendiente_definir`.
- Localidades no validas (ej. `visita domiciliaria`, `sede`) pasan a `pendiente_definir`.
- El `nivel` se toma del CSV y no se infiere por institucion.

## Ayuda

```bash
python3 scripts/automatizar_inclusion_v2.py --help
```
