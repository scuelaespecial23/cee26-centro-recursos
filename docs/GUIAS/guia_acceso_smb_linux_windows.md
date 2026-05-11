# Guia rapida de acceso SMB (Linux y Windows)

Ultima actualizacion: 2026-05-10

## Objetivo

Dejar una referencia corta para conectarse al recurso compartido `compartido` del servidor `srv-ee23`.

## Datos de conexion

- Servidor: `srv-ee23`
- IP local: `192.168.0.102`
- Recurso: `compartido`
- Ruta de red: `//srv-ee23/compartido` o `//192.168.0.102/compartido`

## Linux

Instalar cliente SMB:

```bash
sudo apt update
sudo apt install -y smbclient cifs-utils
```

Prueba por terminal:

```bash
smbclient //srv-ee23/compartido -U secretaria
```

Montar como carpeta local:

```bash
sudo mkdir -p /mnt/compartido
sudo mount -t cifs //srv-ee23/compartido /mnt/compartido -o username=secretaria,uid=$(id -u),gid=$(id -g),iocharset=utf8
```

Desmontar:

```bash
sudo umount /mnt/compartido
```

## Windows

No hace falta instalar Samba Client. Windows ya trae cliente SMB.

Conexion desde Explorador:

1. Abrir `Explorador de archivos`.
2. Escribir `\\srv-ee23\compartido`.
3. Si no resuelve nombre, usar `\\192.168.0.102\compartido`.
4. Ingresar usuario y contrasena entregados por TIC.

Limpiar credenciales en cache (si toma una clave vieja):

```bat
net use * /delete /y
```

Mapeo como unidad (opcional):

```bat
net use Z: \\srv-ee23\compartido /user:secretaria *
```

Quitar unidad mapeada:

```bat
net use Z: /delete
```

## Permisos esperados

- `00-publico`: uso compartido general.
- `01-docentes`: uso docente.
- `02-secretaria`: uso secretaria.
- `03-direccion`: uso direccion.
- `04-equipo-tecnico`: uso tecnico.
- `99-archivo`: acceso solo para `direccion`, `tecnico` y `tic`.

## Referencias

- [Guia docente de uso de la carpeta compartida](./guia_carpeta_compartida_docentes.md)
- [Servidor de archivos institucional EEE23](../INFRAESTRUCTURA/servidor_archivos_eee23.md)
