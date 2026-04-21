# 🏫 EE N°23 - Organización de Google Workspace (CEE26)

<div style="position: sticky; top: 12px; z-index: 1000;">
  <a href="../README.md" style="display:inline-block; padding:8px 12px; background:#f5f5f5; border:1px solid #ccc; border-radius:8px; text-decoration:none;">
    ← Volver a Normativa
  </a>
</div>

---

## 📌 Objetivo

Documentar la estructura organizativa implementada en Google Workspace para la institución **EE N°23**, incluyendo:

* Unidades organizativas (OU)
* Grupos de comunicación
* Criterios de diseño
* Buenas prácticas
* Políticas de seguridad

Este documento permite:

* Mantener consistencia en la gestión
* Facilitar la incorporación de nuevos usuarios
* Centralizar servicios institucionales
* Mejorar la comunicación interna

---

# 🧩 Estructura General

## 🏢 Unidades Organizativas (OU)

Cada usuario pertenece a **una única unidad organizativa**, la cual define:

* Políticas de seguridad
* Accesos a servicios
* Configuraciones específicas

### 📂 OU creadas

* `Alumnos`
* `Docentes`
* `Equipo_Directivo`
* `Equipo_Tecnico`
* `Secretaría`
* `Servicios_Generales`
* `TIC`

---

## 👥 Grupos de comunicación

Los grupos permiten enviar correos a múltiples usuarios de forma centralizada.

### 📬 Grupos creados

| Grupo               | Correo                                                                              | Uso                          |
| ------------------- | ----------------------------------------------------------------------------------- | ---------------------------- |
| Alumnos             | [alumnos@escuelaespecial23.com](mailto:alumnos@escuelaespecial23.com)               | Comunicación con estudiantes |
| Docentes            | [docentes@escuelaespecial23.com](mailto:docentes@escuelaespecial23.com)             | Comunicación pedagógica      |
| Equipo Directivo    | [direccion@escuelaespecial23.com](mailto:direccion@escuelaespecial23.com)           | Gestión institucional        |
| Secretaría          | [secretaria@escuelaespecial23.com](mailto:secretaria@escuelaespecial23.com)         | Administración               |
| Equipo Técnico      | [equipo.tecnico@escuelaespecial23.com](mailto:equipo.tecnico@escuelaespecial23.com) | Acompañamiento educativo     |
| Servicios Generales | [servicios.psa@escuelaespecial23.com](mailto:servicios.psa@escuelaespecial23.com)   | Personal de apoyo            |
| TIC                 | [tic.soporte@escuelaespecial23.com](mailto:tic.soporte@escuelaespecial23.com)       | Soporte técnico              |
| Contacto General    | [contacto@escuelaespecial23.com](mailto:contacto@escuelaespecial23.com)             | Contacto externo             |

---

# 🧠 Criterios de diseño

## 🔹 Separación de responsabilidades

Se diferenciaron:

* Usuarios → identidad individual
* Grupos → comunicación
* OU → políticas

---

## 🔹 Centralización

Todos los servicios institucionales deben:

* Usar cuentas institucionales
* No depender de cuentas personales

Ejemplo:

* ❌ Firebase con Gmail personal
* ✅ Firebase con cuenta institucional

---

## 🔹 Escalabilidad

La estructura permite:

* Agregar nuevos usuarios fácilmente
* Incorporar nuevas áreas
* Automatizar procesos a futuro

---

# 💬 Modelo de comunicación

## 🟢 Google Chat

Uso:

* Comunicación rápida
* Coordinación diaria
* Consultas internas

Ejemplo:

> “No me funciona el proyector”

---

## 📧 Gmail

Uso:

* Comunicaciones formales
* Avisos institucionales
* Documentación

Ejemplo:

> “Se informa que…”

---

## 🎥 Google Meet

Uso:

* Reuniones virtuales
* Clases
* Coordinación remota

---

# 🔐 Políticas de seguridad

## ⚠️ Importancia

Se implementan políticas mínimas debido a incidentes previos de seguridad (robo de cuentas, uso indebido de datos personales).

---

## 🔑 Requisitos de contraseña

Todas las cuentas deben cumplir:

* Mínimo 8 caracteres (recomendado 10+)
* Al menos:

  * 1 mayúscula
  * 1 minúscula
  * 1 número
  * 1 símbolo

### ✅ Ejemplo válido

```
Escuela23!
```

### ❌ Ejemplo inválido

```
12345678
```

---

## 🔄 Cambio obligatorio de contraseña

Al crear un usuario:

* Se debe forzar cambio de contraseña en el primer inicio de sesión

---

## 🚫 Buenas prácticas obligatorias

* No compartir contraseñas
* No usar cuentas personales para tareas institucionales
* No reutilizar contraseñas
* No guardar contraseñas en papel visible

---

## 🛑 Recomendaciones adicionales

* Activar verificación en dos pasos (2FA) en cuentas críticas
* Usar contraseñas únicas por servicio
* Capacitar al personal en seguridad básica

---

# 👤 Gestión de usuarios

## 📌 Al crear un usuario

1. Asignar a una OU correspondiente
2. Añadir a uno o más grupos
3. Forzar cambio de contraseña
4. Informar buenas prácticas

---

## 🔄 Ejemplo

Usuario: docente nuevo

* OU → `Docentes`
* Grupo → `docentes@`
* Acceso → Gmail, Drive, Chat, Meet

---

# 🚀 Futuro / Próximos pasos

* Migración de servicios externos (Firebase, Cloudinary, etc.)
* Implementación de backups
* Automatización con scripts
* Desarrollo de sitio web institucional
* Creación de espacios en Google Chat por área

---

# 📌 Notas finales

Esta estructura fue diseñada para:

* Ordenar la institución digitalmente
* Mejorar la comunicación
* Aumentar la seguridad
* Reducir dependencia de cuentas personales

---

**Responsable TIC:**
Guillermo Neculqueo
EE N°23 - Ingeniero Jacobacci

---
