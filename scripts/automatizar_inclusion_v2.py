#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
import unicodedata
from pathlib import Path


PENDIENTE_DEFINIR = "pendiente_definir"

CARPETA_ADMIN = "_administracion"
CARPETA_PLANTILLAS = "_plantillas_docentes"
CARPETA_MODELO_ESTUDIANTE = "_plantilla_carpeta_estudiante"

ARCHIVOS_PLANTILLA = [
    ("Informe Diagnostico.docx", "informe_diagnostico.docx"),
    ("Informe Diagnóstico.docx", "informe_diagnostico.docx"),
    ("modelo_ppi_2026.odt", "modelo_ppi_2026.odt"),
    ("ppi_2026.odt", "ppi_2026.odt"),
]

ARCHIVOS_ESTUDIANTE = [
    ("modelo_ppi_2026.odt", ["modelo_ppi_2026.odt"]),
    (
        "Informe Diagnóstico.docx",
        ["Informe Diagnóstico.docx", "Informe Diagnostico.docx"],
    ),
]

NIVELES_MAPA = {
    "primera_infancia_0_2": "primera_infancia_0_2",
    "primera_infancia_0_a_2": "primera_infancia_0_2",
    "nivel_primario": "nivel_primario",
    "nivel_inicial": "nivel_inicial",
    "nivel_secundario": "nivel_secundario",
    "jovenes_y_adultos": "jovenes_y_adultos",
    "educacion_temprana": "educacion_temprana",
    PENDIENTE_DEFINIR: PENDIENTE_DEFINIR,
}

LOCALIDADES_INVALIDAS_A_PENDIENTE = {
    "sede",
    "sede_escuela_especial_23",
    "escuela_especial_23",
    "domicilio",
    "domiciliaria",
    "visita_domiciliaria",
    "visitas_domiciliarias",
}


def normalizar_slug(texto: str) -> str:
    valor = unicodedata.normalize("NFKD", texto.strip().lower())
    valor = "".join(c for c in valor if not unicodedata.combining(c))
    salida = []
    for c in valor:
        if c.isalnum():
            salida.append(c)
        else:
            salida.append("_")
    limpio = "".join(salida)
    while "__" in limpio:
        limpio = limpio.replace("__", "_")
    return limpio.strip("_")


def crear_directorio(path: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] mkdir -p {path}")
        return
    path.mkdir(parents=True, exist_ok=True)


def copiar_archivo(origen: Path, destino: Path, dry_run: bool) -> None:
    if dry_run:
        print(f"[dry-run] cp {origen} {destino}")
        return
    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origen, destino)


def copiar_archivo_si_no_existe(origen: Path, destino: Path, dry_run: bool) -> None:
    if destino.exists():
        return
    copiar_archivo(origen, destino, dry_run)


def buscar_primero_existente(base_dir: Path, candidatos: list[str]) -> Path | None:
    for nombre in candidatos:
        ruta = base_dir / nombre
        if ruta.exists():
            return ruta
    return None


def construir_base_anio(inclusion_root: Path, anio: str, dry_run: bool) -> Path:
    inclusion_anio = inclusion_root / anio
    crear_directorio(inclusion_anio, dry_run)
    return inclusion_anio


def construir_base_inclusion(base_dir: Path, anio: str, dry_run: bool) -> Path:
    inclusion = base_dir / "inclusion"

    crear_directorio(inclusion / CARPETA_PLANTILLAS, dry_run)

    construir_base_anio(inclusion, anio, dry_run)

    return inclusion


def crear_estructura_admin(inclusion: Path, anio: str, dry_run: bool) -> None:
    crear_directorio(inclusion / CARPETA_ADMIN / anio, dry_run)


def crear_estructura_plantilla_modelo(
    inclusion: Path,
    anio: str,
    dry_run: bool,
) -> None:

    plantilla = (
        inclusion / CARPETA_MODELO_ESTUDIANTE / "ESTUDIANTE_APELLIDO_NOMBRE" / anio
    )
    crear_directorio(plantilla / "01_documentacion_estudiante", dry_run)
    crear_directorio(plantilla / "02_docentes" / "DOCENTE_APELLIDO_NOMBRE", dry_run)
    crear_directorio(plantilla / "03_actas_y_seguimiento", dry_run)


def copiar_plantillas(
    base_dir: Path,
    inclusion_dir: Path,
    anio: str,
    dry_run: bool,
    incluir_modelo_docente: bool,
) -> None:
    destino_plantillas = inclusion_dir / CARPETA_PLANTILLAS
    destino_modelo_docente = None
    if incluir_modelo_docente:
        destino_modelo_docente = (
            inclusion_dir
            / CARPETA_MODELO_ESTUDIANTE
            / "ESTUDIANTE_APELLIDO_NOMBRE"
            / anio
            / "02_docentes"
            / "DOCENTE_APELLIDO_NOMBRE"
        )

    encontrados = {}
    for origen_nombre, destino_nombre in ARCHIVOS_PLANTILLA:
        origen = base_dir / origen_nombre
        if origen.exists() and destino_nombre not in encontrados:
            encontrados[destino_nombre] = origen

    for destino_nombre, origen in encontrados.items():
        copiar_archivo(origen, destino_plantillas / destino_nombre, dry_run)
        if destino_modelo_docente is not None:
            copiar_archivo(origen, destino_modelo_docente / destino_nombre, dry_run)


def parsear_lista(valor: str, separador: str) -> list[str]:
    if not valor:
        return []
    return [v.strip() for v in valor.split(separador) if v.strip()]


def canonicalizar_localidad_slug(localidad: str) -> str:
    slug = normalizar_slug(localidad)
    if not slug:
        return PENDIENTE_DEFINIR
    if slug in LOCALIDADES_INVALIDAS_A_PENDIENTE:
        return PENDIENTE_DEFINIR
    return slug


def canonicalizar_institucion_slug(institucion: str) -> str:
    slug = normalizar_slug(institucion)
    if not slug:
        return PENDIENTE_DEFINIR
    if slug == PENDIENTE_DEFINIR:
        return PENDIENTE_DEFINIR

    patron_escuela_numero = re.match(r"^esc(?:uela)?(?:_n)?_(\d+)$", slug)
    if patron_escuela_numero:
        return f"escuela_n_{patron_escuela_numero.group(1)}"

    patron_jardin_infantil_numero = re.match(
        r"^(?:jardin|escuela)_infantil_(?:n_)?(\d+)$",
        slug,
    )
    if patron_jardin_infantil_numero:
        return f"escuela_infantil_n_{patron_jardin_infantil_numero.group(1)}"

    patron_jardin_numero = re.match(r"^jardin(?:_n)?_(\d+)$", slug)
    if patron_jardin_numero:
        return f"jardin_n_{patron_jardin_numero.group(1)}"

    patron_esrn = re.match(r"^esrn(?:_n)?_(\d+)$", slug)
    if patron_esrn:
        return f"esrn_n_{patron_esrn.group(1)}"

    patron_cet = re.match(r"^cet(?:_n)?_(\d+)$", slug)
    if patron_cet:
        return f"cet_n_{patron_cet.group(1)}"

    patron_cens = re.match(r"^cens(?:_n)?_(\d+)$", slug)
    if patron_cens:
        return f"cens_n_{patron_cens.group(1)}"

    patron_eeba = re.match(r"^eeba(?:_n)?_(\d+)$", slug)
    if patron_eeba:
        return f"eeba_n_{patron_eeba.group(1)}"

    return slug


def canonicalizar_nivel_slug(nivel: str) -> str:
    slug = normalizar_slug(nivel)
    if not slug:
        return PENDIENTE_DEFINIR
    return NIVELES_MAPA.get(slug, slug)


def construir_ruta_base_estudiante(
    inclusion_anio_dir: Path,
    localidad: str,
    institucion: str,
    nivel: str,
    estudiante: str,
) -> Path:
    localidad_slug = canonicalizar_localidad_slug(localidad)
    nivel_slug = canonicalizar_nivel_slug(nivel)
    institucion_slug = canonicalizar_institucion_slug(institucion)
    estudiante_slug = normalizar_slug(estudiante)

    return (
        inclusion_anio_dir
        / localidad_slug
        / nivel_slug
        / institucion_slug
        / estudiante_slug
    )


def crear_carpeta_estudiante(
    inclusion_anio_dir: Path,
    localidad: str,
    institucion: str,
    nivel: str,
    estudiante: str,
    docentes: list[str],
    dry_run: bool,
) -> None:
    base = construir_ruta_base_estudiante(
        inclusion_anio_dir=inclusion_anio_dir,
        localidad=localidad,
        institucion=institucion,
        nivel=nivel,
        estudiante=estudiante,
    )

    crear_directorio(base / "01_documentacion_estudiante", dry_run)
    crear_directorio(base / "03_actas_y_seguimiento", dry_run)
    if not docentes:
        crear_directorio(base / "02_docentes", dry_run)
        return

    for docente in docentes:
        crear_directorio(base / "02_docentes" / normalizar_slug(docente), dry_run)


def copiar_plantillas_en_estudiante(
    base_dir: Path,
    inclusion_anio_dir: Path,
    localidad: str,
    institucion: str,
    nivel: str,
    estudiante: str,
    dry_run: bool,
) -> None:
    destino_base = construir_ruta_base_estudiante(
        inclusion_anio_dir=inclusion_anio_dir,
        localidad=localidad,
        institucion=institucion,
        nivel=nivel,
        estudiante=estudiante,
    )
    crear_directorio(destino_base, dry_run)

    for destino_nombre, origenes in ARCHIVOS_ESTUDIANTE:
        origen = buscar_primero_existente(base_dir, origenes)
        if origen is None:
            continue
        copiar_archivo_si_no_existe(origen, destino_base / destino_nombre, dry_run)


def crear_desde_csv(
    base_dir: Path,
    inclusion_root: Path,
    csv_path: Path,
    anio_default: str,
    separador_lista: str,
    dry_run: bool,
) -> None:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        requeridas = {"apellido", "nombre", "localidad", "institucion", "nivel"}
        faltantes = [c for c in requeridas if c not in (reader.fieldnames or [])]
        if faltantes:
            raise ValueError(
                "CSV invalido. Faltan columnas: " + ", ".join(sorted(faltantes))
            )

        inclusion_anio_dir = construir_base_anio(inclusion_root, anio_default, dry_run)
        for fila in reader:
            apellido = (fila.get("apellido") or "").strip()
            nombre = (fila.get("nombre") or "").strip()
            if not apellido or not nombre:
                continue

            estudiante = f"{apellido}_{nombre}"
            localidad = (fila.get("localidad") or "").strip()
            institucion = (fila.get("institucion") or "").strip()
            nivel = (fila.get("nivel") or "").strip()
            docentes = parsear_lista(fila.get("docentes", ""), separador_lista)

            crear_carpeta_estudiante(
                inclusion_anio_dir=inclusion_anio_dir,
                localidad=localidad,
                institucion=institucion,
                nivel=nivel,
                estudiante=estudiante,
                docentes=docentes,
                dry_run=dry_run,
            )
            copiar_plantillas_en_estudiante(
                base_dir=base_dir,
                inclusion_anio_dir=inclusion_anio_dir,
                localidad=localidad,
                institucion=institucion,
                nivel=nivel,
                estudiante=estudiante,
                dry_run=dry_run,
            )


def listar_carpetas_estudiantes(inclusion_anio_dir: Path) -> list[Path]:
    carpetas = {
        p.parent
        for p in inclusion_anio_dir.rglob("01_documentacion_estudiante")
        if p.is_dir() and p.parent.is_dir()
    }
    return sorted(carpetas)


def replicar_documentos_comunes(
    inclusion_anio_dir: Path,
    docs_replicar_dir: Path,
    dry_run: bool,
) -> tuple[int, int]:
    archivos = sorted([p for p in docs_replicar_dir.iterdir() if p.is_file()])
    if not archivos:
        return (0, 0)

    estudiantes = listar_carpetas_estudiantes(inclusion_anio_dir)
    if not estudiantes:
        return (0, len(archivos))

    copiados = 0
    for carpeta_estudiante in estudiantes:
        destino_doc = carpeta_estudiante / "01_documentacion_estudiante"
        crear_directorio(destino_doc, dry_run)
        for archivo in archivos:
            destino = destino_doc / archivo.name
            existia = destino.exists()
            copiar_archivo_si_no_existe(archivo, destino, dry_run)
            if not existia:
                copiados += 1

    return (copiados, len(archivos) * len(estudiantes))


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Automatiza la estructura de directorios para Inclusion (v2.0).",
    )
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Directorio base donde se crea la carpeta inclusion.",
    )
    parser.add_argument(
        "--anio",
        default="2026",
        help="Ano lectivo base para la plantilla.",
    )
    parser.add_argument(
        "--students-csv",
        help="CSV opcional para crear carpetas de estudiantes.",
    )
    parser.add_argument(
        "--docs-replicar-todos",
        help=(
            "Carpeta con archivos comunes para copiar en "
            "01_documentacion_estudiante de todos los estudiantes del anio."
        ),
    )
    parser.add_argument(
        "--separador-lista",
        default=";",
        help="Separador para la columna docentes del CSV.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Muestra acciones sin crear ni copiar archivos.",
    )
    parser.add_argument(
        "--crear-admin",
        action="store_true",
        help="Crea carpeta _administracion/<anio> (opcional).",
    )
    parser.add_argument(
        "--crear-plantilla-modelo",
        action="store_true",
        help=(
            "Crea _plantilla_carpeta_estudiante y copia plantillas en "
            "02_docentes/DOCENTE_APELLIDO_NOMBRE (opcional)."
        ),
    )
    return parser


def main() -> int:
    parser = construir_parser()
    args = parser.parse_args()
    base_dir = Path(args.base_dir).resolve()

    if not base_dir.exists():
        print(f"Error: no existe el directorio base: {base_dir}", file=sys.stderr)
        return 1

    if not args.students_csv and not args.docs_replicar_todos:
        parser.print_help()
        return 1

    inclusion_root = base_dir / "inclusion"
    if args.students_csv:
        inclusion_root = construir_base_inclusion(base_dir, args.anio, args.dry_run)
        if args.crear_admin:
            crear_estructura_admin(inclusion_root, args.anio, args.dry_run)
        if args.crear_plantilla_modelo:
            crear_estructura_plantilla_modelo(inclusion_root, args.anio, args.dry_run)
        copiar_plantillas(
            base_dir,
            inclusion_root,
            args.anio,
            args.dry_run,
            incluir_modelo_docente=args.crear_plantilla_modelo,
        )

    if args.students_csv:
        csv_path = Path(args.students_csv).resolve()
        if not csv_path.exists():
            print(f"Error: no existe el CSV: {csv_path}", file=sys.stderr)
            return 1
        crear_desde_csv(
            base_dir=base_dir,
            inclusion_root=inclusion_root,
            csv_path=csv_path,
            anio_default=args.anio,
            separador_lista=args.separador_lista,
            dry_run=args.dry_run,
        )

    if args.docs_replicar_todos:
        docs_replicar_dir = Path(args.docs_replicar_todos).resolve()
        if not docs_replicar_dir.exists() or not docs_replicar_dir.is_dir():
            print(
                (
                    "Error: no existe la carpeta de docs a replicar: "
                    f"{docs_replicar_dir}"
                ),
                file=sys.stderr,
            )
            return 1

        inclusion_anio_dir = inclusion_root / args.anio
        if not inclusion_anio_dir.exists():
            print(
                (
                    "Error: no existe la carpeta del anio en inclusion: "
                    f"{inclusion_anio_dir}"
                ),
                file=sys.stderr,
            )
            return 1

        copiados, posibles = replicar_documentos_comunes(
            inclusion_anio_dir=inclusion_anio_dir,
            docs_replicar_dir=docs_replicar_dir,
            dry_run=args.dry_run,
        )
        print(
            "Documentos comunes replicados: "
            f"{copiados} archivo(s) nuevos sobre {posibles} destino(s) posibles."
        )

    print("Proceso finalizado (v2.0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
