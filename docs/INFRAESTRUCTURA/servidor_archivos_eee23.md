# Servidor de archivos institucional EEE23

Ultima actualizacion: 2026-05-08

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
- En una etapa posterior se podran crear usuarios individuales y directorios privados para casos justificados

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

## Referencias recomendadas

- [Guia docente de carpeta compartida](../GUIAS/guia_carpeta_compartida_docentes.md)
- [Politica de uso de carpeta compartida - borrador](../NORMATIVA/politica_uso_carpeta_compartida_borrador.md)
