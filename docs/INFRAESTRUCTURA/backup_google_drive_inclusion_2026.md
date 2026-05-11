# Backup operativo de Google Drive (`INCLUSIÓN_2026`)

Ultima actualizacion: 2026-05-11

## Objetivo

Documentar el respaldo automatico diario de la carpeta `INCLUSIÓN_2026` de Google Drive hacia el servidor institucional `srv-ee23`.

## Alcance actual

- Cuenta origen: Gmail institucional en uso actual (no Workspace todavia).
- Carpeta origen: `INCLUSIÓN_2026`.
- No se respalda toda la unidad de Drive en esta etapa.
- Este esquema es transitorio hasta la migracion a Google Workspace for Education.

## Por que se hace backup si hay RAID1

RAID1 no reemplaza backup.

- RAID1 protege ante falla de un disco fisico.
- No protege ante borrado accidental, sobrescritura, ransomware o errores de sincronizacion.
- El backup permite recuperar versiones y archivos eliminados.

## Esquema implementado

- Herramienta: `rclone`.
- Modo: `sync` incremental diario con historico por fecha (`--backup-dir`).
- Destino actual: `/srv/backups/google-drive/inclusion_2026/current`.
- Historico de cambios y borrados: `/srv/backups/google-drive/inclusion_2026/history/AAAA-MM-DD`.
- Retencion del historico: `60 dias`.
- Log principal: `/var/log/backup-inclusion.log`.

## Automatizacion (cron de root)

Crontab configurado:

```cron
30 2 * * * FECHA=$(date +\%F) && /usr/bin/rclone --config /home/admin23/.config/rclone/rclone.conf sync "gdrive_ee23:INCLUSIÓN_2026" "/srv/backups/google-drive/inclusion_2026/current" --backup-dir="/srv/backups/google-drive/inclusion_2026/history/$FECHA" --create-empty-src-dirs --log-file=/var/log/backup-inclusion.log --log-level INFO
45 2 * * * /usr/bin/find /srv/backups/google-drive/inclusion_2026/history -mindepth 1 -maxdepth 1 -type d -mtime +60 -exec rm -rf {} \;
```

## Verificacion operativa

Comandos utiles de control:

```bash
sudo crontab -l
sudo tail -n 80 /var/log/backup-inclusion.log
sudo ls -la /srv/backups/google-drive/inclusion_2026/current
sudo ls -la /srv/backups/google-drive/inclusion_2026/history
```

## Restauracion basica de archivo

1. Buscar el archivo en `history/AAAA-MM-DD/...`.
2. Copiarlo al destino de recuperacion.
3. Verificar que abre correctamente.
4. Registrar fecha, archivo restaurado y motivo.

Ejemplo:

```bash
sudo cp "/srv/backups/google-drive/inclusion_2026/history/2026-05-11/INCLUSION/.../archivo.docx" "/tmp/archivo_recuperado.docx"
```

## Consideraciones de seguridad

- No compartir tokens ni archivos de configuracion de `rclone`.
- Mantener permisos restringidos sobre `/srv/backups/google-drive`.
- Revisar periodicamente que siga vigente la autorizacion OAuth del remote.

## Plan futuro

Cuando se habilite Google Workspace for Education:

- migrar documentos al esquema institucional definitivo,
- redisenar politica de backup para todo el dominio,
- evaluar baja de este backup transitorio.
