# Guia de uso - Inclusion v2.0

Ultima actualizacion: 2026-03-30

## Script

- `scripts/automatizar_inclusion_v2.py`

## Para que sirve

Este script ayuda a crear y ordenar la estructura de carpetas de inclusion por estudiante a partir de un archivo CSV.

Tambien permite copiar documentos comunes a todas las carpetas creadas.

## Estructura que genera

Ruta base:

`inclusion/<anio>/<localidad>/<nivel>/<institucion>/<estudiante>/`

Dentro de cada estudiante crea, segun corresponda:

- `01_documentacion_estudiante`
- `02_docentes`
- `03_actas_y_seguimiento`

## Que hay que tener instalado

### Linux

- `python3`

Comando para verificar:

```bash
python3 --version
```

### Windows

- Python 3 instalado

Comandos posibles para verificar:

```powershell
py --version
```

o

```powershell
python --version
```

Si ninguno responde, primero hay que instalar Python.

## Desde donde hay que ejecutarlo

Siempre desde la raiz del repositorio `cee26-centro-recursos`.

Ejemplo en Linux:

```bash
cd /ruta/a/cee26-centro-recursos
```

Ejemplo en Windows PowerShell:

```powershell
cd C:\ruta\a\cee26-centro-recursos
```

## Requisitos del CSV

Columnas obligatorias:

- `apellido`
- `nombre`
- `localidad`
- `institucion`
- `nivel`

Columna opcional:

- `docentes`

Separador por defecto para `docentes`:

- `;`

## Flujo recomendado

1. Preparar o revisar el CSV.
2. Ejecutar primero en modo `--dry-run`.
3. Revisar que las rutas generadas sean correctas.
4. Ejecutar en modo real.
5. Si hace falta, usar el mismo script para copiar documentos comunes.

## Comandos basicos

### 1. Crear estructura desde CSV en Linux

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv
```

### 2. Crear estructura desde CSV en Windows

```powershell
py scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv
```

Si `py` no funciona, probar:

```powershell
python scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv
```

### 3. Modo prueba sin crear nada

Linux:

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv --dry-run
```

Windows:

```powershell
py scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --students-csv scripts/estudiantes_2026.csv --dry-run
```

## Copiar documentos comunes

### A la raiz de cada estudiante

Linux:

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --docs-enviar-raiz-estudiante ./archivos_nuevos --normalizar-nombres-archivos
```

Windows:

```powershell
py scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --docs-enviar-raiz-estudiante .\archivos_nuevos --normalizar-nombres-archivos
```

### A `01_documentacion_estudiante`

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --docs-enviar-01-doc-estudiante ./archivos_nuevos --normalizar-nombres-archivos
```

### A `02_docentes`

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --docs-enviar-02-docentes ./archivos_nuevos --normalizar-nombres-archivos
```

### A `03_actas_y_seguimiento`

```bash
python3 scripts/automatizar_inclusion_v2.py --base-dir . --anio 2026 --docs-enviar-03-actas ./archivos_nuevos --normalizar-nombres-archivos
```

## Opciones utiles

- `--dry-run`: simula sin crear ni copiar nada.
- `--normalizar-nombres-archivos`: deja nombres mas compatibles con Drive y Windows.
- `--separador-lista ","`: cambia el separador de docentes.
- `--crear-admin`: crea `_administracion/<anio>`.
- `--crear-plantilla-modelo`: crea una estructura modelo de estudiante.

## Reglas de normalizacion importantes

- Los nombres se convierten a formato seguro tipo `snake_case`.
- Se eliminan tildes y caracteres conflictivos en rutas.
- Algunas localidades no validas pasan a `pendiente_definir`.
- El nivel se toma del CSV y no se infiere automaticamente.

## Problemas comunes

### Python no existe

- Instalar Python 3.
- En Windows, durante la instalacion, activar la opcion para agregar Python al sistema si aparece.

### El CSV da error

- Revisar que tenga los encabezados obligatorios.
- Verificar que el archivo este guardado en formato CSV.

### Las rutas generadas no son las esperadas

- Ejecutar primero con `--dry-run`.
- Revisar valores de `localidad`, `institucion` y `nivel` dentro del CSV.

## Ayuda del script

Linux:

```bash
python3 scripts/automatizar_inclusion_v2.py --help
```

Windows:

```powershell
py scripts/automatizar_inclusion_v2.py --help
```
