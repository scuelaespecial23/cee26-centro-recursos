# Procedimiento de restauracion del backup INCLUSION_2026

## 1. Objetivo

Este procedimiento permite recuperar archivos del backup del servidor `srv-ee23` sin trabajar directamente sobre la informacion productiva hasta haber revisado la copia restaurada.

El backup se encuentra en:

```text
/srv/backups/google-drive/inclusion_2026/
```

La estructura es:

```text
current/                 Copia vigente del origen
history/YYYY-MM-DD/      Versiones anteriores movidas en esa ejecucion
```

## 2. Como funciona el backup

La tarea se ejecuta diariamente a las `02:30` mediante `rclone sync` con `--backup-dir`.

- `current` representa la copia mas reciente disponible.
- `history/YYYY-MM-DD` contiene las versiones anteriores de archivos que fueron reemplazados o eliminados durante la ejecucion de ese dia.
- Un directorio de `history` no es una copia completa del sistema.
- Un archivo eliminado del origen no desaparece inmediatamente: su ultima version respaldada queda en el `history` de la ejecucion que detecto la eliminacion.
- La retencion documentada es de 60 dias.

Importante: si alguien elimina o modifica un archivo hoy por la tarde, antes de la proxima ejecucion de las `02:30`, probablemente la version correcta todavia este en `current`. Si el cambio ya fue procesado por el backup, hay que buscar la version anterior en `history`.

## 3. Reglas de seguridad

1. No restaurar directamente sobre `/srv/compartido` sin revisar antes el archivo recuperado.
2. Extraer primero en una carpeta local de prueba.
3. Confirmar la ruta exacta y el nombre exacto del archivo.
4. No usar `rclone sync` para restaurar: podria eliminar o reemplazar archivos no deseados.
5. No pegar contrasenas en comandos ni en este documento.
6. La contrasena solicitada por `sudo` es la de `admin23`, no la de Samba del usuario `tic`.
7. Al terminar una transferencia, limpiar la variable de entorno:

```zsh
unset SUDO_PASSWORD
```

## 4. Preparar la carpeta local de trabajo

En la PC local:

```zsh
mkdir -p "$HOME/prueba-backup"
```

Se recomienda conservar una carpeta diferente para cada caso, por ejemplo:

```zsh
mkdir -p "$HOME/prueba-backup/caso-docente-2026-10-15"
```

## 5. Autenticacion correcta desde Zsh

Para transferencias sin crear un archivo temporal pesado en el servidor, se envia la contrasena a `sudo` por la entrada estandar.

En `zsh`, la sintaxis correcta para leerla sin mostrarla es:

```zsh
read -r -s 'SUDO_PASSWORD?Clave sudo de admin23: '
printf '\n'
```

No usar `read -p`: esa opcion no funciona igual en `zsh`.

Se puede verificar la autenticacion antes de transferir archivos:

```zsh
printf '%s\n' "$SUDO_PASSWORD" |
  ssh admin23@srv-ee23 'sudo -S -p "" id'
```

El resultado esperado contiene:

```text
uid=0(root)
```

## 6. Restaurar la copia vigente (`current`)

Usar este caso cuando:

- el archivo fue eliminado o modificado despues de la ultima ejecucion del backup;
- se necesita la copia mas reciente completa;
- no se necesita una version historica anterior.

Crear una carpeta local aislada:

```zsh
mkdir -p "$HOME/prueba-backup/current"
```

Transferir directamente `current`:

```zsh
printf '%s\n' "$SUDO_PASSWORD" |
  ssh admin23@srv-ee23 \
    'sudo -S -p "" tar -C /srv/backups/google-drive/inclusion_2026 -cf - current' |
  tar --no-same-owner -C "$HOME/prueba-backup" -xf -
```

Verificar el resultado:

```zsh
du -sh "$HOME/prueba-backup/current"
find "$HOME/prueba-backup/current" -type f | wc -l
find "$HOME/prueba-backup/current" -type f | head
```

## 7. Traer un incremental de una fecha

Usar este procedimiento para revisar versiones anteriores movidas en una ejecucion concreta.

Ejemplo: `2026-10-15`.

Primero, en el servidor, revisar el tamaño y la cantidad de archivos:

```bash
sudo du -sh /srv/backups/google-drive/inclusion_2026/history/2026-10-15
sudo find /srv/backups/google-drive/inclusion_2026/history/2026-10-15 -type f | wc -l
```

En la PC local:

```zsh
mkdir -p "$HOME/prueba-backup/history-2026-10-15"
```

Transferir solo ese historico, sin crear un `.tar` en el servidor:

```zsh
printf '%s\n' "$SUDO_PASSWORD" |
  ssh admin23@srv-ee23 \
    'sudo -S -p "" tar -C /srv/backups/google-drive/inclusion_2026/history/2026-10-15 -cf - INCLUSION' |
  tar --no-same-owner -C "$HOME/prueba-backup/history-2026-10-15" -xf -
```

Listar los archivos recuperados:

```zsh
find "$HOME/prueba-backup/history-2026-10-15" -type f -print
```

## 8. Caso: un docente elimino un archivo por la tarde

### 8.1. Si la eliminacion ocurrio despues de las 02:30

La ejecucion del backup todavia no proceso la eliminacion. Buscar el archivo en:

```text
current/
```

Traer `current` completo o solo la ruta requerida a una carpeta de prueba.

### 8.2. Si la eliminacion ocurrio antes de las 02:30 y el backup ya se ejecuto

Buscar el archivo en el `history` de la fecha de ejecucion que detecto la eliminacion. Por ejemplo:

```text
history/2026-10-15/INCLUSION/...
```

Para localizarlo en todos los historicos, desde el servidor:

```bash
sudo find /srv/backups/google-drive/inclusion_2026/history \
  -type f -iname '*parte-del-nombre*' -print
```

Luego transferir el historico de la fecha correspondiente y revisar el archivo localmente.

## 9. Caso: un docente modifico un archivo y necesita la version anterior

1. Registrar la ruta completa del archivo.
2. Confirmar la hora aproximada de la modificacion.
3. Revisar si la modificacion ocurrio antes o despues de las `02:30`.
4. Si ocurrio despues de las `02:30`, usar `current`.
5. Si ocurrio antes de las `02:30`, buscar la version anterior en el `history` de esa ejecucion.
6. Extraer el archivo a una carpeta local de prueba.
7. Comparar el contenido con el archivo actual.
8. Pedir confirmacion antes de reemplazar la version productiva.

Para comparar dos archivos en la PC:

```bash
sha256sum archivo-actual archivo-recuperado
```

Para documentos Office o PDF, abrir ambas copias y confirmar visualmente el contenido, no solo el hash.

## 10. Caso: se elimino una carpeta completa

No asumir que un directorio de `history` contiene la carpeta completa. Puede contener solo los archivos que cambiaron o fueron eliminados en esa ejecucion.

Procedimiento:

1. Identificar la fecha en la que el backup detecto la eliminacion.
2. Buscar la carpeta en todos los historicos:

```bash
sudo find /srv/backups/google-drive/inclusion_2026/history \
  -type d -path '*parte-de-la-ruta*' -print
```

3. Traer el historico de la fecha a una carpeta local.
4. Revisar si estan todos los archivos necesarios.
5. Si faltan archivos que no cambiaron ese dia, completar la revision usando `current`.
6. No reconstruir la carpeta automaticamente sin comparar primero los contenidos.

## 11. Caso: recuperar varios archivos de una misma fecha

Si se conoce la fecha y se necesita todo `INCLUSION` de ese historico:

```zsh
mkdir -p "$HOME/prueba-backup/revision-2026-10-15"

printf '%s\n' "$SUDO_PASSWORD" |
  ssh admin23@srv-ee23 \
    'sudo -S -p "" tar -C /srv/backups/google-drive/inclusion_2026/history/2026-10-15 -cf - INCLUSION' |
  tar --no-same-owner -C "$HOME/prueba-backup/revision-2026-10-15" -xf -
```

Para traer solamente una ruta especifica, reemplazar `INCLUSION` por la ruta relativa exacta:

```zsh
printf '%s\n' "$SUDO_PASSWORD" |
  ssh admin23@srv-ee23 \
    'sudo -S -p "" tar -C /srv/backups/google-drive/inclusion_2026/history/2026-10-15 -cf - -- INCLUSION/comallo/nivel_primario/escuela_n_73' |
  tar --no-same-owner -C "$HOME/prueba-backup/revision-2026-10-15" -xf -
```

## 12. Restaurar en el servidor despues de revisar

La restauracion productiva debe hacerse solo despues de validar la copia local y confirmar la ruta destino.

### 12.1. Preparar una copia de seguridad del archivo actual

En el servidor, como `root`, cambiar las variables por la ruta real:

```bash
TARGET='/srv/compartido/ruta/al/archivo'
STAMP=$(date +%F-%H%M%S)
cp -a -- "$TARGET" "$TARGET.pre-restauracion-$STAMP"
```

### 12.2. Subir el archivo validado a una zona de staging

Desde la PC:

```bash
scp '/ruta/local/archivo-validado' admin23@srv-ee23:/home/admin23/
```

### 12.3. Copiarlo a produccion

En el servidor, como `root`:

```bash
cp -a -- /home/admin23/archivo-validado '/srv/compartido/ruta/al/archivo'
chown --reference='/srv/compartido/ruta/al/archivo.pre-restauracion-FECHA' \
  '/srv/compartido/ruta/al/archivo'
chmod --reference='/srv/compartido/ruta/al/archivo.pre-restauracion-FECHA' \
  '/srv/compartido/ruta/al/archivo'
```

Verificar propietario y permisos:

```bash
ls -l '/srv/compartido/ruta/al/archivo'
```

No eliminar inmediatamente la copia `.pre-restauracion-*`. Conservarla hasta confirmar que el usuario recupero la informacion correctamente.

## 13. Restaurar una carpeta completa en produccion

Para carpetas, es mas seguro restaurar primero en una carpeta staging del servidor, comparar y luego copiar los archivos aprobados.

No ejecutar directamente:

```bash
rclone sync ...
```

ni copiar una carpeta historica completa sobre produccion sin revisar, porque el historico puede ser solamente un delta.

## 14. Verificar que el backup se ejecuto correctamente

En el servidor:

```bash
sudo tail -n 100 /var/log/backup-inclusion.log
```

Buscar especialmente:

```text
Checks: ... / ..., 100%
Elapsed time: ...
```

Revisar errores:

```bash
sudo grep -Ein 'error|failed|fatal|panic' /var/log/backup-inclusion.log | tail -n 50
```

Los avisos `Duplicate object found in source - ignoring` no necesariamente detienen la ejecucion, pero deben registrarse y revisarse porque indican objetos duplicados en el origen.

## 15. Verificar las fechas disponibles

```bash
sudo ls -1dt /srv/backups/google-drive/inclusion_2026/history/*
```

Para conocer el tamaño de cada historico:

```bash
sudo du -sh /srv/backups/google-drive/inclusion_2026/history/*
```

## 16. Limitacion importante: restauracion a un punto exacto del tiempo

El esquema actual no genera snapshots completos diarios. Genera:

```text
current + deltas historicos
```

Por eso no se debe afirmar que `history/2026-10-15` representa todo el servidor tal como estaba el 15 de octubre. Representa solamente los archivos antiguos movidos durante la ejecucion de esa fecha.

Para recuperar un archivo puntual, este esquema es adecuado. Para reconstruir toda la estructura en un punto exacto del tiempo, hay que combinar `current` con los deltas posteriores en orden inverso y resolver eliminaciones, reemplazos y renombres. Ese procedimiento debe probarse antes en una copia aislada.

Si se necesita restauracion completa por fecha de forma sencilla, conviene cambiar el diseño a snapshots completos con hard links o utilizar una herramienta con historial de versiones integrado.

## 17. Registro de cada restauracion

Registrar como minimo:

```text
Fecha y hora:
Solicitante:
Usuario o area:
Ruta original:
Fecha del history utilizado:
Motivo:
Archivos recuperados:
Destino de prueba:
Destino productivo, si correspondio:
Persona que verifico:
Resultado:
```

Al finalizar cualquier transferencia desde la PC:

```zsh
unset SUDO_PASSWORD
```
