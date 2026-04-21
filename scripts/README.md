# CEE26 Inclusion - Programa descargable

<div style="position: sticky; top: 12px; z-index: 1000;">
  <a href="../README.md" style="display:inline-block; padding:8px 12px; background:#f5f5f5; border:1px solid #ccc; border-radius:8px; text-decoration:none;">
    ← Volver a Normativa
  </a>
</div>

---

Esta carpeta ya no contiene solo scripts: ahora incluye el programa
CEE26 Inclusion para docentes, con instaladores para Windows y Linux (Debian),
y su documentacion de uso.

## Contenido

- `automatiza_inclusion/`
  - `cee26-inclusion_0.2.0_amd64.deb` (instalador Linux Debian/Ubuntu)
  - `cee26_inclusion_0.2.0_linux_amd64.tar.gz` (paquete Linux portable)
  - `cee26_inclusion_linux` (binario Linux)
  - `CEE26_Inclusion_windows.exe` (ejecutable Windows)
  - `CEE26_Inclusion_0.2.0_windows.zip` (paquete comprimido Windows)
  - `GUIA_USO_INCLUSION_V2.md` (guia docente actualizada)

## Instalacion rapida

No es necesario tener Python instalado para usar los ejecutables publicados.

### Linux Debian/Ubuntu

```bash
sudo dpkg -i scripts/automatiza_inclusion/cee26-inclusion_0.2.0_amd64.deb
```

Si faltan dependencias:

```bash
sudo apt-get -f install
```

### Windows

- Opcion 1: ejecutar `scripts/automatiza_inclusion/CEE26_Inclusion_windows.exe`
- Opcion 2: descomprimir `scripts/automatiza_inclusion/CEE26_Inclusion_0.2.0_windows.zip`

Nota: en Windows no hace falta instalar Python para estas opciones.

## Guia de uso

- [Abrir guia para docentes](./automatiza_inclusion/GUIA_USO_INCLUSION_V2.md)
