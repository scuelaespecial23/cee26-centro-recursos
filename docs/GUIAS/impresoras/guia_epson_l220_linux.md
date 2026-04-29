# Guia paso a paso para Epson L220 en Linux

Ultima actualizacion: 2026-04-29

## Objetivo

Dejar documentado el procedimiento completo para instalar, configurar y probar una impresora Epson L220 en Linux, usando los drivers oficiales de Epson.

## Resultado esperado

Al finalizar la guia, la impresora debe:

- ser detectada por el sistema,
- quedar agregada como impresora disponible,
- imprimir una pagina de prueba correctamente,
- permitir tareas de mantenimiento desde la utilidad de Epson.

## Enlace oficial de descarga

Descargar los archivos oficiales desde:

- Centro de descargas Epson para Linux: `https://download-center.epson.com/softwares/?device_id=L220+Series&region=AR&os=DEBX64&language=es`

## Archivos necesarios

En Linux se recomienda descargar e instalar estos dos paquetes:

1. `Epson Inkjet Printer Driver (ESC/P) for Linux`
2. `Epson Printer Utility for Linux`

## Importante antes de empezar

- Conectar la impresora por cable USB.
- Encender la impresora.
- Verificar que tenga papel y tinta.
- Si ya hubo intentos fallidos previos, conviene eliminar configuraciones viejas de la impresora antes de volver a agregarla.

## Paso 1. Descargar los drivers

1. Abrir el enlace oficial de Epson para Linux.
2. Confirmar que el sistema operativo seleccionado sea `Linux Deb (x64)`.
3. Descargar:
   - `Epson Printer Utility for Linux`
   - `Epson Inkjet Printer Driver (ESC/P) for Linux`
4. Guardar ambos archivos en `Descargas`.

## Paso 2. Instalar la utilidad de Epson

Desde una terminal, ejecutar:

```bash
cd ~/Descargas
sudo dpkg -i epson-printer-utility_*.deb
```

Esta utilidad no reemplaza al driver principal. Sirve para mantenimiento y limpieza de cabezales.

## Paso 3. Instalar el driver de impresion

Desde la misma terminal, ejecutar:

```bash
cd ~/Descargas
sudo dpkg -i epson-inkjet-printer-*.deb
sudo apt -f install
```

En una instalacion verificada para Epson L220, el paquete descargado fue:

```bash
epson-inkjet-printer-201401w_1.0.1-1_amd64.deb
```

## Paso 4. Verificar que Linux detecte la impresora

Con la impresora conectada por USB, ejecutar:

```bash
lsusb
```

Deberia aparecer una linea similar a esta:

```bash
Seiko Epson Corp. EPSON L220 Series
```

Tambien se puede verificar el URI disponible con:

```bash
lpinfo -v
```

En la prueba realizada, el sistema detecto la impresora asi:

```bash
usb://EPSON/L220%20Series?serial=5647514B3236393067&interface=1
```

## Paso 5. Agregar la impresora en CUPS

Si la impresora todavia no aparece en `Configuracion > Impresoras`, se puede agregar manualmente desde terminal.

Ejemplo funcional:

```bash
sudo lpadmin -p Epson-L220 -E -v 'usb://EPSON/L220%20Series?serial=5647514B3236393067&interface=1' -P '/opt/epson-inkjet-printer-201401w/ppds/Epson/Epson-L220_Series-epson-driver.ppd.gz'
sudo lpoptions -d Epson-L220
```

Notas:

- `-p Epson-L220` define el nombre de la impresora en el sistema.
- `-v` indica el dispositivo USB detectado.
- `-P` apunta al archivo PPD del modelo L220 instalado por el driver oficial.

## Paso 6. Revisar si la cola fue creada correctamente

Ejecutar:

```bash
lpstat -t
```

La impresora ya deberia aparecer listada como destino disponible.

## Paso 7. Imprimir una pagina de prueba

Para probar la impresion desde terminal:

```bash
lp -d Epson-L220 /usr/share/cups/data/testprint
```

Tambien se puede hacer desde:

1. `Configuracion`
2. `Impresoras`
3. Seleccionar `Epson-L220`
4. `Imprimir pagina de prueba`

## Paso 8. Si la hoja sale en blanco

Si la impresora es detectada pero la hoja sale completamente en blanco, revisar en este orden:

1. Confirmar que el driver correcto de Epson fue instalado.
2. Confirmar que la impresora fue agregada con el PPD `Epson-L220_Series` y no con uno generico.
3. Revisar niveles de tinta.
4. Ejecutar limpieza de cabezales.

## Paso 9. Limpieza de cabezales en Linux

Abrir la utilidad de Epson:

```bash
epson-printer-utility
```

Si no abre, probar:

```bash
/usr/bin/epson-printer-utility
```

Luego:

1. Seleccionar la impresora Epson L220.
2. Ejecutar `Nozzle Check`.
3. Si la impresion sale cortada o con lineas faltantes, ejecutar `Head Cleaning`.
4. Imprimir otra prueba.
5. Repetir `Head Cleaning` una o dos veces mas solo si hace falta.

## Recomendaciones para limpieza

- No hacer muchas limpiezas seguidas porque consumen tinta.
- Si despues de 2 o 3 limpiezas sigue mal, dejar descansar la impresora entre 20 y 30 minutos.
- Si estuvo mucho tiempo sin uso, puede requerir una limpieza mas profunda.

## Capturas sugeridas para anexar a la wiki

Si se desea enriquecer esta guia con imagenes, conviene sumar capturas de:

- la pagina oficial de Epson donde aparecen los dos paquetes para Linux,
- la pantalla de instalacion o descarga,
- la configuracion final de la impresora en el sistema.

## Resumen corto del procedimiento validado

El procedimiento que funciono correctamente fue:

1. Descargar la utilidad de Epson.
2. Descargar el driver `ESC/P` para Linux.
3. Instalar ambos paquetes.
4. Conectar nuevamente la impresora.
5. Crear la impresora con el driver especifico de Epson L220.
6. Imprimir pagina de prueba.
7. Usar `Head Cleaning` si la impresion sale entrecortada.

## Referencias

- Epson Download Center L220 Linux: `https://download-center.epson.com/softwares/?device_id=L220+Series&region=AR&os=DEBX64&language=es`
- Sitio de soporte general Epson Argentina: `https://epson.com.ar/Soporte/Impresoras/sh/s1`
