# Bitacora operativa de servidor (`srv-ee23`)

Ultima actualizacion: 2026-05-11

## Objetivo

Dejar una bitacora breve con controles diarios/semanales para soporte TIC, de modo que cualquier equipo pueda retomar rapidamente que revisar en el servidor.

## Estado inicial registrado

- Samba operativo con recurso `compartido`.
- Usuario tecnico transversal: `tic`.
- Carpeta `99-archivo` restringida a `direccion`, `tecnico` y `tic`.
- Backup automatico de `INCLUSIÓN_2026` activo por cron.

## Checklist diario (5 minutos)

1. Revisar ultimo backup:

```bash
sudo tail -n 80 /var/log/backup-inclusion.log
```

2. Confirmar que cron sigue cargado:

```bash
sudo crontab -l
```

3. Verificar estado de Samba:

```bash
systemctl is-active smbd
```

4. Verificar espacio de disco:

```bash
df -h /srv
```

## Checklist semanal (15-20 minutos)

1. Probar acceso SMB con usuario de prueba (`tic` o equivalente).
2. Restaurar 1 archivo de prueba desde `history` del backup.
3. Revisar crecimiento de `/srv/backups/google-drive/inclusion_2026`.
4. Eliminar carpetas de prueba obsoletas dentro de `compartido` si aparecen.

## Comandos de referencia rapida

Ver carpeta actual del backup:

```bash
sudo ls -la /srv/backups/google-drive/inclusion_2026/current
```

Ver historico por fechas:

```bash
sudo ls -la /srv/backups/google-drive/inclusion_2026/history
```

Ver permisos de `99-archivo`:

```bash
sudo ls -ld /srv/compartido/99-archivo
getent group grp_archivo
```

## Registro breve de cambios recientes

- 2026-05-10: alta de usuarios Samba (`docentes`, `secretaria`, `direccion`, `tecnico`).
- 2026-05-10: creacion de usuario `tic` con acceso transversal para soporte.
- 2026-05-10: restriccion de `99-archivo` via `grp_archivo`.
- 2026-05-11: backup Google Drive `INCLUSIÓN_2026` automatizado con retencion de 60 dias.

## Nota de continuidad

Cuando se migre a Google Workspace for Education, actualizar esta bitacora y revisar el esquema de backup transitorio actual.
