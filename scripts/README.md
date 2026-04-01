# Scripts de automatizacion

Esta carpeta concentra guias y referencias del flujo de Inclusion.

## Referencia principal

- `GUIA_USO_INCLUSION_V2.md`: guia operativa para docentes (Linux/Windows),
  politicas de uso, trabajo con Drive sincronizado y ejemplos de flujo completo.

## Scripts del flujo actual (entorno operativo CEE_26)

- `automatizar_inclusion_v2.py`: crea estructura anual y distribuye docs comunes
  (raiz, `01_documentacion_estudiante`, `02_docentes`, `03_actas_y_seguimiento`)
  y permite envio individual a un docente de un estudiante.
- `crear_historial_estudiantes.py`: vincula material historico con estudiantes y
  lo copia en `historial/<anio>/...` con trazabilidad.
- `cee26_desktop_app.py`: interfaz grafica para operar el flujo sin linea de
  comandos.

## Recomendacion de uso

1. Trabajar en una carpeta local sincronizada con Drive.
2. Ejecutar siempre primero con `--dry-run`.
3. Revisar salida y rutas destino.
4. Ejecutar en modo real recien despues de validar.

## Acceso rapido

- [Abrir guia para docentes](./GUIA_USO_INCLUSION_V2.md)
