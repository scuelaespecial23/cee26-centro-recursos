# Guia docente - CEE26 Inclusion (programa de escritorio)

<div style="position: sticky; top: 12px; z-index: 1000;">
  <a href="../README.md" style="display:inline-block; padding:8px 12px; background:#f5f5f5; border:1px solid #ccc; border-radius:8px; text-decoration:none;">
    ← Volver a Normativa
  </a>
</div>

---

Ultima actualizacion: 2026-04-20

Esta guia corresponde al programa de escritorio CEE26 Inclusion,
disponible para Windows y Linux (base Debian).

Con esta aplicacion el docente puede:

1. crear la estructura anual de estudiantes,
2. subir documentos comunes de forma masiva,
3. enviar documentos puntuales por docente/estudiante,
4. vincular historial de anos anteriores.

## 1) Instalacion

### Windows

- Ejecutar `CEE26_Inclusion_windows.exe`.
- Alternativa: descomprimir `CEE26_Inclusion_0.2.0_windows.zip` y abrir el ejecutable.
- Importante: no se requiere Python instalado en Windows para usar este programa.

### Linux Debian/Ubuntu

- Instalar con:

```bash
sudo dpkg -i cee26-inclusion_0.2.0_amd64.deb
```

- Si faltan dependencias:

```bash
sudo apt-get -f install
```

Tambien se incluye paquete portable:

- `cee26_inclusion_0.2.0_linux_amd64.tar.gz`
- binario `cee26_inclusion_linux`

Nota: para estas versiones empaquetadas tampoco hace falta instalar Python por separado.

## 2) Entorno recomendado

Trabajar siempre sobre una carpeta local sincronizada con Drive
(no directamente desde navegador).

- Linux: por ejemplo `/home/.../CEE_26`
- Windows: por ejemplo `C:\...\CEE_26`

Beneficio: mayor velocidad, control local y sincronizacion posterior.

## 3) Uso basico del programa

En la ventana principal se ven 5 pestanas:

1. `1) Crear estructura`
2. `2) Subir docs comunes`
3. `3) Envio individual por docente`
4. `4) Envio individual por alumno`
5. `5) Anadir historial`

Recomendacion general: activar primero `Simular (no crea archivos)` y ejecutar.
Si el resultado es correcto, repetir sin simulacion.

## 4) Flujo sugerido

1. Seleccionar CSV de estudiantes.
2. Ejecutar `Crear estructura` en modo simulacion y luego real.
3. Subir documentos comunes si corresponde.
4. Usar envio individual cuando el documento es para un caso puntual.
5. Ejecutar `Anadir historial` para vincular anos anteriores.

## 5) Video corto de uso (pendiente)

Espacio reservado para incorporar un video de YouTube con demostracion basica.

- Enlace: `PENDIENTE`
- Insertar aqui cuando este publicado.

## 6) Errores comunes y solucion

- `no existe ...`: revisar ruta base y permisos.
- CSV invalido: verificar encabezados (`apellido`, `nombre`, etc.).
- resultado inesperado: volver a correr en modo `Simular` y revisar salida.
- rutas largas en Windows/Drive: mantener nombres cortos y ordenados.

## 7) Recordatorio operativo

La herramienta busca reducir trabajo manual y errores:

- estructura consistente por estudiante,
- carga masiva controlada,
- envios puntuales a docente o alumno,
- historial trazable por ano.
