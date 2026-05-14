# Plantilla de alta de usuario (Servidor CEE23)

Ultima actualizacion: 2026-05-14

## Objetivo

Contar con un mensaje reutilizable para informar a cada persona su acceso al servidor de archivos institucional.

## Plantilla reutilizable (correo)

```text
Asunto: Acceso a servidor compartido CEE23

Hola [NOMBRE],

Ya creamos tu acceso al servidor de archivos institucional.

Tus datos de acceso:
- Usuario: [USUARIO]
- Contrasena temporal: [PASSWORD_TEMPORAL]
- Area: [AREA]
- Carpeta personal: [RUTA_PERSONAL]

Importante (conexion en la institucion):
1) Debes conectarte a la red WiFi: REPETIDOR SECRETARIA
2) Esa red esta conectada directamente al servidor actualmente.
3) Por ahora, el acceso esta habilitado en modo local (dentro de la institucion).

Como acceder:
- Windows:
  - Abre el Explorador de archivos.
  - En la barra de direccion escribe: \\srv-ee23\compartido
  - Ingresa tu usuario y contrasena.
- Si no abre por nombre:
  - Prueba: \\192.168.0.102\compartido

Estructura general de carpetas compartidas:
- 00-publico
- 01-docentes
- 02-secretaria
- 03-direccion
- 04-equipo-tecnico
- 99-archivo

Tu carpeta personal dentro del area:
- [RUTA_PERSONAL]
(Esta carpeta es privada: solo tu puedes ver/modificar su contenido).

Cambio de contrasena:
- Al primer ingreso, solicita cambio de contrasena al equipo TIC.
- Para evitar desajustes, TIC actualiza ambas credenciales del usuario (Linux y Samba) dejando la misma clave.
- Si necesitas ayuda, te apoyamos en la institucion.

Guias y tutoriales (Wiki de apoyo):
https://github.com/scuelaespecial23/cee26-centro-recursos

Acceso remoto (solo si es estrictamente necesario):
- Se habilita caso a caso con apoyo del area TIC.
- Requiere configuracion asistida (Tailscale).
- Si lo necesitas, debes solicitar ayuda presencial para dejarlo operativo.

Saludos,
[TU_NOMBRE / EQUIPO TIC]
```

## Ejemplos rapidos

### Secretaria

- Usuario: `marite`
- Area: `secretaria`
- Carpeta personal: `/srv/compartido/02-secretaria/marite`

### Docentes

- Usuario: `karina-loncon`
- Area: `docentes`
- Carpeta personal: `/srv/compartido/01-docentes/karina-loncon`

## Nota operativa

Gestion de contrasenas (uso interno TIC):

```bash
sudo passwd <usuario>
sudo smbpasswd <usuario>
```

Antes de enviar el mensaje, validar en servidor:

```bash
id <usuario>
sudo pdbedit -L | grep <usuario>
sudo ls -ld /srv/compartido/<carpeta_area>/<usuario>
```
