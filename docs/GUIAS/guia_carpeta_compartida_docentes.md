# Guia docente de uso de la carpeta compartida

Ultima actualizacion: 2026-05-14

## Objetivo

Explicar de forma simple como acceder, usar y cuidar la carpeta compartida institucional desde Linux o Windows.

## Para que sirve esta carpeta

La carpeta compartida permite guardar y consultar materiales de trabajo institucional sin depender del celular personal de cada docente.

Se puede usar para:

- documentos institucionales,
- fotos o videos seleccionados de actividades relevantes,
- materiales pedagogicos de uso comun,
- archivos de trabajo que convenga conservar en la institucion.

## Antes de empezar

- Estar conectado a la red de la institucion.
- Solicitar las credenciales al referente TIC.
- Tener en cuenta que no todas las carpetas son de uso docente.

Para solicitar credenciales:

- escribir por WhatsApp al referente TIC dentro del grupo institucional de sede,
- o escribir a `guillermoneculqueo@gmail.com`.

Mas adelante, el canal previsto sera `tic@escuelaespecial.com`.

## Guias en video

- [Guia actualizada Windows](https://youtu.be/l5bieCmHfjA)
- [Guia Linux - Ubuntu](https://youtu.be/YHuS4O7o2Io)
- [Guia Windows](https://youtu.be/_uidaaKAnvQ)

## Direccion de acceso dentro de la institucion

- Linux: `smb://192.168.0.102/compartido`
- Windows: `\\192.168.0.102\compartido`

## Acceso desde Linux

Ejemplo pensado para GNOME Archivos o exploradores compatibles con `smb://`:

1. Abrir `Archivos`.
2. Ir a `Otras ubicaciones`.
3. Escribir `smb://192.168.0.102/compartido`.
4. Presionar `Conectar`.
5. Ingresar el usuario y la contrasena entregados por TIC.

Si el equipo Linux no tiene herramientas SMB instaladas, primero ejecutar:

```bash
sudo apt update
sudo apt install -y smbclient cifs-utils
```

Prueba rapida por terminal:

```bash
smbclient //srv-ee23/compartido -U secretaria
```

Montaje manual en Linux (opcional):

```bash
sudo mkdir -p /mnt/compartido
sudo mount -t cifs //srv-ee23/compartido /mnt/compartido -o username=secretaria,uid=$(id -u),gid=$(id -g),iocharset=utf8
```

Para desmontar:

```bash
sudo umount /mnt/compartido
```

## Acceso desde Windows

1. Abrir el `Explorador de archivos`.
2. Escribir `\\192.168.0.102\compartido` en la barra de direcciones.
3. Presionar `Enter`.
4. Ingresar el usuario y la contrasena entregados por TIC cuando el sistema lo solicite.

Nota: Windows ya trae cliente SMB incorporado, no hace falta instalar Samba Client para uso habitual.

Si Windows insiste con una credencial vieja, abrir `CMD` y ejecutar:

```bat
net use * /delete /y
```

## Que carpetas va a ver un docente

Dentro del recurso compartido pueden verse carpetas como:

- `00-publico`
- `01-docentes`
- `02-secretaria`
- `03-direccion`
- `04-equipo-tecnico`
- `99-archivo`

Un docente comun puede ver la estructura general, pero normalmente trabajara sobre:

- `00-publico`
- `01-docentes`

La carpeta `99-archivo` esta reservada para personal autorizado (`direccion`, `tecnico` y `tic`).

## Primer paso recomendado dentro de `01-docentes`

Al ingresar por primera vez, cada docente deberia crear una carpeta propia con su nombre en formato simple.

Ejemplo:

- `maria_jose`
- `juan_perez`
- `ana_garcia`

Dentro de esa carpeta puede guardar su material de trabajo institucional.

## Uso recomendado de `00-publico`

La carpeta `00-publico` sirve para materiales que realmente tenga sentido compartir con otros miembros de la institucion.

Ejemplos:

- modelos de notas,
- planillas utiles,
- materiales didacticos comunes,
- documentos institucionales de consulta frecuente.

## Normas de convivencia basicas

- No borrar archivos de otras personas.
- No modificar carpetas ajenas sin acuerdo previo.
- No usar nombres confusos para las carpetas.
- No subir material innecesario o repetido.
- Mantener orden minimo dentro de la propia carpeta.

Aunque todos los docentes de sede puedan compartir el espacio `01-docentes`, se espera un uso responsable y respetuoso.

## Que conviene subir

- documentos de trabajo institucional,
- materiales pedagogicos utiles,
- evidencias seleccionadas de actividades importantes,
- archivos que deban conservarse para consulta posterior.

## Que no conviene subir

- fotos borrosas,
- muchas fotos casi iguales,
- videos sin valor institucional claro,
- archivos duplicados,
- material personal ajeno a la escuela,
- descargas innecesarias o copias de seguridad masivas del celular.

## Ejemplo practico con fotos de un acto

Si en un acto se sacaron 50 fotos, no hace falta subir las 50.

Se recomienda:

1. borrar las fotos borrosas,
2. elegir las mejores,
3. evitar subir muchas imagenes repetidas,
4. conservar solo el material que realmente represente la actividad.

Si el material ya fue publicado en un canal institucional como Facebook y no hace falta archivarlo nuevamente, evaluar si realmente corresponde guardarlo tambien en el servidor.

## Acceso remoto

El acceso remoto no esta habilitado de forma general para todas las personas.

Si alguien lo necesita por una razon concreta, debe solicitarlo al referente TIC.

En esos casos se indicara instalar `Tailscale` y compartir el enlace o identificador necesario para autorizar el equipo.

## Posible mejora futura

Si un docente hace buen uso del recurso y realmente necesita un espacio mas privado, se podra evaluar la creacion de:

- un usuario individual,
- un directorio personal no compartido con el resto.

## Video tutorial

Si preferis ver el procedimiento completo antes de hacerlo, tenes estos tutoriales:

- Windows (conexion, inicio de sesion y uso de usuarios SMB): https://youtu.be/_uidaaKAnvQ
- Linux (configuracion de carpeta compartida Samba en equipo local y conexion al servidor institucional): https://youtu.be/YHuS4O7o2Io

## Referencias

- [Servidor de archivos institucional EEE23](../INFRAESTRUCTURA/servidor_archivos_eee23.md)
- [Politica de uso de carpeta compartida - borrador](../NORMATIVA/politica_uso_carpeta_compartida_borrador.md)
