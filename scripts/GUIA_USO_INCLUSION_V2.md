# Guia docente - Inclusion (flujo operativo actualizado)

Ultima actualizacion: 2026-04-01

Esta guia explica el flujo real que hoy se usa para organizar Inclusion:

1. crear estructura anual de estudiantes,
2. subir documentos comunes de forma masiva,
3. subir documentos de forma puntual a un docente de un estudiante,
4. vincular historial de anos anteriores.

Se puede trabajar en Linux o Windows.

## 1) En que entorno se recomienda trabajar

El flujo esta pensado para usarse con Drive sincronizado a una carpeta local de
la PC (no desde navegador web).

- Linux: por ejemplo, una carpeta montada/sincronizada en `/home/.../CEE_26`.
- Windows: por ejemplo, una carpeta sincronizada en `C:\...\CEE_26`.

Beneficio: todo se hace localmente (mas rapido y mas controlado) y Drive luego
sincroniza los cambios.

## 2) Politicas de uso recomendadas (docentes)

- Ejecutar siempre primero con `--dry-run` antes de copiar en real.
- Trabajar sobre una carpeta local sincronizada; no sobre pendrive directo.
- Mantener nombres de archivos simples y activar normalizacion cuando aplique.
- No borrar manualmente estructura interna (`01`, `02`, `03`, `historial`) salvo
  decision de equipo.
- Si hay dudas de destino, detener ejecucion y revisar el CSV antes de copiar.
- Registrar cambios grandes (fecha, que se corrio, quien lo corrio).

## 3) Scripts del flujo actualizado

- `automatizar_inclusion_v2.py`
  - crea estructura desde CSV,
  - copia docs masivos a zonas concretas,
  - copia docs puntuales a `02_docentes/<docente>` para 1 estudiante.
- `crear_historial_estudiantes.py`
  - vincula carpetas historicas y las integra dentro de cada estudiante.
- `cee26_desktop_app.py`
  - opcion grafica para operar el flujo sin linea de comandos.

## 4) Requisitos minimos

### Linux

```bash
python3 --version
```

### Windows (PowerShell)

```powershell
py --version
```

Si no responde, instalar Python 3.

## 5) Flujo sugerido de trabajo

1. Validar CSV de estudiantes.
2. Crear estructura (`--dry-run` y luego real).
3. Subir docs comunes (si corresponde).
4. Subir docs puntuales por estudiante+docente (si corresponde).
5. Vincular historial (`--dry-run` + reporte CSV, luego real).

## 6) Comandos clave (linea de comandos)

## 6.1 Crear estructura anual desde CSV

Linux:

```bash
python3 scripts/automatizar_inclusion_v2.py --students-csv ./scripts/estudiantes_2026.csv --anio 2026 --dry-run
```

Windows:

```powershell
py scripts/automatizar_inclusion_v2.py --students-csv .\scripts\estudiantes_2026.csv --anio 2026 --dry-run
```

## 6.2 Subir docs comunes de forma masiva

Raiz del estudiante:

```bash
python3 scripts/automatizar_inclusion_v2.py --docs-enviar-raiz-estudiante ./archivos_nuevos --anio 2026 --normalizar-nombres-archivos --dry-run
```

`01_documentacion_estudiante`:

```bash
python3 scripts/automatizar_inclusion_v2.py --docs-enviar-01-doc-estudiante ./archivos_nuevos --anio 2026 --normalizar-nombres-archivos --dry-run
```

`02_docentes`:

```bash
python3 scripts/automatizar_inclusion_v2.py --docs-enviar-02-docentes ./archivos_nuevos --anio 2026 --normalizar-nombres-archivos --dry-run
```

`03_actas_y_seguimiento`:

```bash
python3 scripts/automatizar_inclusion_v2.py --docs-enviar-03-actas ./archivos_nuevos --anio 2026 --normalizar-nombres-archivos --dry-run
```

## 6.3 Subir docs a un unico docente de un unico estudiante

```bash
python3 scripts/automatizar_inclusion_v2.py --docs-enviar-docente-estudiante-dir ./archivos_nuevos --target-apellido Huenchual --target-nombre Candy --target-docente "Karina Loncon" --target-localidad "Ingeniero Jacobacci" --target-institucion "Escuela N 356" --target-nivel "Nivel Primario" --anio 2026 --normalizar-nombres-archivos --dry-run
```

Notas:

- un docente puede estar en muchos estudiantes,
- un estudiante puede tener 1 o N docentes,
- el destino es `.../02_docentes/<docente_slug>/` dentro del estudiante elegido.

## 6.4 Vincular historial de anos anteriores

Simulacion + reporte:

```bash
python3 scripts/crear_historial_estudiantes.py --inclusion-anio-dir ./inclusion/2026 --historial-root ./historial_años_anteriores --students-csv ./scripts/estudiantes_2026.csv --dry-run --reporte-csv ./scripts/reporte_historial_2026.csv
```

Copia real:

```bash
python3 scripts/crear_historial_estudiantes.py --inclusion-anio-dir ./inclusion/2026 --historial-root ./historial_años_anteriores --students-csv ./scripts/estudiantes_2026.csv --max-component-len 80 --max-dest-rel-len 220 --reporte-csv ./scripts/reporte_historial_2026.csv
```

## 7) Ejemplo de estructura resultante (recorte)

```text
inclusion/
└── 2026/
    └── ingeniero_jacobacci/
        └── nivel_primario/
            └── escuela_n_356/
                └── huenchual_candy/
                    ├── 01_documentacion_estudiante/
                    │   └── consentimiento_informado.pdf
                    ├── 02_docentes/
                    │   └── karina_loncon/
                    │       └── plan_apoyo_abril.docx
                    ├── 03_actas_y_seguimiento/
                    │   └── acta_reunion_familia_2026_04_10.pdf
                    └── historial/
                        └── 2025/
                            └── turno_manana_huenchual_candy/
                                └── informe_trimestral.pdf
```

## 8) Uso desde app de escritorio

En la app:

- Pestaña 1: crear estructura.
- Pestaña 2: docs comunes o envio individual (selector estudiante + docente).
- Pestaña 3: anadir historial.

Recomendacion: en cualquier pestaña, usar primero `Simular`.

## 9) Errores comunes y solucion

- `no existe ...`: revisar ruta y carpeta base de trabajo.
- CSV invalido: revisar encabezados (`apellido`, `nombre`, etc.).
- match ambiguo en historial: completar mejor nombres o apoyar con CSV.
- cortes por rutas largas en Windows/Drive: usar limites de longitud en historial.

## 10) Recordatorio operativo

Este flujo fue pensado para reducir trabajo manual repetitivo y errores humanos:

- estructura consistente,
- carga masiva controlada,
- envio puntual a docente especifico,
- historial trazable por estudiante y anio.
