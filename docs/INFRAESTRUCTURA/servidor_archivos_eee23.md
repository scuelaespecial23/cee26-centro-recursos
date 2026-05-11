# Servidor de archivos institucional EEE23

Ultima actualizacion: 2026-05-11

## Objetivo

Dejar documentado el estado actual del servidor de archivos institucional, su forma de acceso, criterios de soporte y lineamientos basicos para futuras ampliaciones.

## Resumen operativo

- Nombre del servidor: `srv-ee23`
- Servicio principal de archivos: `Samba`
- Recurso compartido principal: `compartido`
- Ruta real del recurso: `/srv/compartido`
- IP local fija del servidor: `192.168.0.102`
- Acceso local por Linux: `smb://192.168.0.102/compartido`
- Acceso local por Windows: `\\192.168.0.102\compartido`
- Acceso remoto tecnico validado por Tailscale: `smb://100.66.31.17/compartido`

## Estado de red

- Sistema operativo instalado: `Ubuntu 24.04.4 LTS`
- La interfaz `enp21s0` quedo fijada con IP estatica `192.168.0.102/24`
- Gateway actual: `192.168.0.1`
- El servidor ya fue probado con conectividad saliente correcta a Internet
- La IP local fue fijada en el servidor porque no hay acceso administrativo al router principal del ISP

## Estructura actual del recurso compartido

Carpetas creadas dentro de `/srv/compartido`:

- `00-publico`
- `01-docentes`
- `02-secretaria`
- `03-direccion`
- `04-equipo-tecnico`
- `99-archivo`

## Usuarios y alcance previsto

- Los docentes de sede acceden con credenciales compartidas por el referente TIC
- Un docente comun puede ver la estructura general del recurso, pero solo debe trabajar en los espacios autorizados
- Para uso cotidiano docente, el trabajo principal se realiza en `00-publico` y `01-docentes`
- Se creo el usuario tecnico transversal `tic` para soporte operativo con acceso a todas las carpetas de trabajo
- En una etapa posterior se podran crear usuarios individuales y directorios privados para casos justificados

## Permisos vigentes por carpeta

- `00-publico`: compartida para trabajo comun.
- `01-docentes`: uso docente.
- `02-secretaria`: uso secretaria.
- `03-direccion`: uso direccion.
- `04-equipo-tecnico`: uso tecnico.
- `99-archivo`: acceso restringido a `direccion`, `tecnico` y `tic` mediante grupo `grp_archivo`.

## Estado de validacion (2026-05-10)

- Servicio `smbd` activo y funcionando.
- Usuarios Samba validados: `docentes`, `secretaria`, `direccion`, `tecnico`, `tic`.
- Prueba real de acceso:
  - `secretaria` no puede entrar a `99-archivo` (`NT_STATUS_ACCESS_DENIED`).
  - `direccion` puede acceder a `99-archivo`.
  - `tic` puede acceder y crear/borrar carpeta de prueba en `99-archivo`.

## Soporte y solicitud de acceso

Canales vigentes para solicitar acceso o soporte:

- mensaje directo por WhatsApp dentro del grupo institucional de sede,
- correo personal del referente TIC: `guillermoneculqueo@gmail.com`

Canal previsto a futuro:

- correo institucional TIC: `tic@escuelaespecial.com`

## Acceso remoto excepcional

El acceso remoto al servidor no es automatico ni general para todo el personal.

Se contempla solo para casos puntuales que realmente lo necesiten y siempre con autorizacion del referente TIC.

Procedimiento general previsto:

1. La persona solicita acceso remoto por WhatsApp o por correo.
2. Se le indica instalar `Tailscale` en su equipo.
3. La persona comparte el enlace o identificador generado por Tailscale para autorizar el equipo.
4. El referente TIC agrega ese equipo a la red de Tailscale.
5. Una vez autorizado, se informa la forma correcta de acceso al servidor.

## Expansion prevista

Si el uso del servidor resulta sostenido y ordenado, se podra evaluar:

- crear usuarios personales,
- asignar directorios privados no compartidos con otros usuarios,
- ampliar documentacion y tutoriales,
- definir criterios mas finos de permisos por perfil.

## Backup externo de informacion critica

Ademas del servidor local con RAID1, se implemento backup externo de Google Drive para informacion critica de inclusion.

- Origen: carpeta `INCLUSIÓN_2026` de la cuenta Gmail institucional actual.
- Destino local: `/srv/backups/google-drive/inclusion_2026/current`.
- Historico de cambios y borrados: `/srv/backups/google-drive/inclusion_2026/history/AAAA-MM-DD`.
- Frecuencia: diaria (cron 02:30).
- Retencion del historico: 60 dias.

## Referencias recomendadas

- [Guia docente de carpeta compartida](../GUIAS/guia_carpeta_compartida_docentes.md)
- [Guia rapida de acceso SMB (Linux y Windows)](../GUIAS/guia_acceso_smb_linux_windows.md)
- [Backup operativo de Google Drive - INCLUSIÓN_2026](./backup_google_drive_inclusion_2026.md)
- [Politica de uso de carpeta compartida - borrador](../NORMATIVA/politica_uso_carpeta_compartida_borrador.md)
