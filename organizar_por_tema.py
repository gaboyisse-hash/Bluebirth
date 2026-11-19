#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Organiza el árbol de trabajo por tema mediante copias, sin alterar el origen.

Uso:
  python organizar_por_tema.py                         # simulación
  python organizar_por_tema.py --copiar                # copia junto al origen
  python organizar_por_tema.py RUTA --copiar           # origen explícito
  python organizar_por_tema.py RUTA --destino SALIDA --copiar
"""

import argparse
import collections
import hashlib
import os
import re
import shutil
import sys

RAIZ_DEFAULT = os.path.dirname(os.path.abspath(__file__))

CATEGORIAS = [
    ("00_OBRA_Y_EDICIONES", "El libro, ediciones integradas y obra canónica"),
    ("01_FILOSOFIA_Y_PENSAMIENTO", "Ontología, lenguaje, libertad, silencio, cábala y vínculo"),
    ("02_FISICA_COSMOLOGIA_Y_ATOMO", "Cosmología, humo, EEL, átomo, luz y tiempo"),
    ("03_ANTROPOLOGIA_CONSCIENCIA_Y_SER", "Consciencia, cuerpo, ser, sombra, caduceo y Maturana"),
    ("04_INVESTIGACION_Y_METODO", "Homologación, dictámenes, verificaciones y auditorías"),
    ("05_BLUE_BIRD_RED_LUCY", "Moneda BB, red Lucy, economía y componentes Aura"),
    ("06_MUSICA_TIEMPO_Y_DANZA", "Música, economía musical, escucha y percepción temporal"),
    ("07_CHARLAS_DIALOGOS_E_INFORMATIVOS", "Charlas, diálogos y documentos informativos"),
    ("08_AUDITORIA_TECNICA_Y_LOGS", "Logcat, conexiones, inventarios y herramientas técnicas"),
    ("09_IDENTIDAD_Y_MARCO_PERSONAL", "Identidad, periodos y manifiesto personal"),
    ("99_SIN_UBICAR", "Pendiente de clasificación manual"),
]

# Cada categoría 05 se mantiene separada para conservar el contexto de la red.
R = []
def reg(pattern, category):
    R.append((re.compile(pattern), category))

# Obra y ediciones.
reg(r"^\./(La_Danza_del_Colibri_Tratado_Unificado\.md|colibri_edicion_integrada\.md|EL_LIBRO_DEL_COLIBRI_edicion_integrada\.docx)$", "00_OBRA_Y_EDICIONES")
reg(r"^\./(SEGMENTO_INDEPENDIENTE|dolly_docs/|tanda4/07_obra_canonica|tanda3/(arquitectura|colibro)\.|docs2/(danza_colibri|geometria_relacional)\.)", "00_OBRA_Y_EDICIONES")

# Filosofía y pensamiento.
reg(r"(lenguaje_(liora|modelo)|lenguaje_como_modelo|liora_geometrica|amor_estructura|LIBERTAD_CORRELACIONAL|paradoja_libertad|CABALA_Y_EL_ARBOL|cabala_desde_el_silencio|conceptualizacion_silencio|GLOSARIO_DE_CONCEPTOS|ECONOMIA_DE_DAs|economia_cosmica_delta_as)", "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"^\./docs/change_word", "01_FILOSOFIA_Y_PENSAMIENTO")

# Física, cosmología y átomo.
reg(r"(AGUJEROS_NEGROS|agujero_negro|ruedo|RUEDO|[Hh]umo|HUMO|eel|EEL|atalogo|diagrama_temporal|DIAGRAMA_TEMPORAL|modelo_atomo|analisis_modelo_atomo)", "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"^\./tanda3/(ckp_v2|math_flush|id_colores)\.|^\./aportes_movimiento_del_universo\.md$", "02_FISICA_COSMOLOGIA_Y_ATOMO")

# Antropología, consciencia y ser.
reg(r"^\./blue_bird_docs/postulado_maya/|[Cc]aduceo|KUNDALINI|PENSAMIENTO_CUERPO|ciencia_pensamiento_silencio|SOMBRA|defectos_de_personalidad|aura_retorno", "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"^\./maturana_guia\.md$", "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")

# Investigación y método.
reg(r"^\./(analogo_conceptual_v1|comparacion_v1_v2|v3_meta|v4)/|^\./revision_2026-09-22/|HOMOLOGACI|^\./(corpus_review_silencio_del_colibri|auditoria_corpus_dolly|distincion_participacion_liora)\.md$|^\./AGRUPACION_DOCUMENTOS\.md$", "04_INVESTIGACION_Y_METODO")
reg(r"^\./blue_bird_docs/(CRONOLOGIA_y_historicidad|PRECEDENCIA_y_sincronia|ESCALERA_de_correcciones)\.md$|^\./blue_bird_docs/(analisis_precedencia|caminar_indice|prueba_azar_sin_input|prueba_repetir_la_cinta)\.py$|^\./blue_bird_docs/precedencia_resultados\.json$", "04_INVESTIGACION_Y_METODO")

# Contexto de red Blue Bird / Red Lucy.
reg(r"^\./blue_bird_docs/(0[1-6]_|integrar/|marco/|banxico/)", "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"^\./tanda4/(0[1-6]_|02_)", "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"(?i)(BB_CLOSURE|reciclaje_cancelacion_deuda|blockchain_bb|bb_pasarelas|fiat_paridades|CODIGO_COMPLETO_CONSTRUCTO_VALOR_BB|table_)", "05_BLUE_BIRD_RED_LUCY|05b_Valor_moneda_y_economia")
reg(r"^\./blue_bird_docs/(modelo_valor/|simulador/)", "05_BLUE_BIRD_RED_LUCY|05b_Valor_moneda_y_economia")
reg(r"(?i)(nodo_maestro_bb|nodo_web_bb|blue_bird_docs/red/|red_multinivel|cordon|topologia)", "05_BLUE_BIRD_RED_LUCY|05c_Red_topologia_cordon_escala")
reg(r"(?i)(BLUEBIRD\.HTML|Génesis_BB|genesis|firmar genesis|Simulador-Red-Blue-Bird|simulador_red_blue_bird|bb.?birth.?aura|blue_bird_docs/(interfaz|artefactos)|logcat_audit/drive/(doc_|v24_))", "05_BLUE_BIRD_RED_LUCY|05d_Interfaz_y_artefactos")
reg(r"(?i)(agencia_cambio_aura|aura_agencia_autonoma|aura_servidor_completo|consolidacion_intercambio_aura|multivectorial_ck_t|organismos_biologia_i3v|organismos_vivos_aura|participacion_usuarios_aura|sistema_coherencia|usuarios_aura|blue_bird_docs/codigo/|original_bb\.txt)", "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")

# Música, tiempo y danza.
reg(r"QUE_ES_LA_MUSICA|ECONOMIA_BASE_MUSICAL|^\./blue_bird_docs/catalogo_red/|^\./docs/(tiempo_vive|time_issue_aura)|^\./docs2/timecepcion", "06_MUSICA_TIEMPO_Y_DANZA")

# Charlas e informativos.
reg(r"Chat con Dola|chat_dola|^\./tanda3/|^\./docs/(dialogos_aura|neutrino|reflexion)|^\./docs2/sophi_bisho|Texto compartido|The_Coiled_Serpent|threaht speculation|Aura proyecci", "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")

# Auditoría técnica.
reg(r"^\./logcat_audit/logcat_diagnostico\.txt$|^\./logcat_audit/(informe_auditoria|ficha_blue_bird|CHANGELOG|REDACCION|segundo)|^\./logcat_audit/drive/(inventario|_descarga_meta)|^\./(analisis_conexiones\.md|conexiones_clasificadas\.csv|log_conexiones_original\.csv|clasificar_log\.py|organizar_drive_v[23]\.gs|inventario_drive_solo\.gs)$|(?i)cloudflared", "08_AUDITORIA_TECNICA_Y_LOGS")

# Identidad.
reg(r"^\./mapa_identidades_y_periodos\.md$|^\./docs/manifiesto|Mi_Identidad_Gabriel", "09_IDENTIDAD_Y_MARCO_PERSONAL")

# Material de entrada de Drive: se conserva el desglose de red y artefactos.
reg(r"^\./logcat_audit/drive/descarga/\d+__code_[^/]*\.(py|c|sh|json|csv|txt)$", "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")
reg(r"^\./logcat_audit/drive/descarga/\d+__code_[^/]*\.html$", "05_BLUE_BIRD_RED_LUCY|05d_Interfaz_y_artefactos")
reg(r"^\./logcat_audit/drive/descarga/\d+__Obra_Canonica", "00_OBRA_Y_EDICIONES")
reg(r"^\./logcat_audit/drive/descarga/\d+__(Radio|README)", "99_SIN_UBICAR")


def es_ignorado(nombre, ruta, script_actual):
    return (nombre == script_actual or nombre == "organizar_por_tema.py" or
            nombre.startswith(".") or nombre.endswith((".pyc", ".pyo")) or
            "__pycache__" in ruta)


def recolectar(raiz, destino):
    salida = []
    destino = os.path.abspath(destino)
    script_actual = os.path.basename(__file__)
    for base, dirs, files in os.walk(raiz):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git") and
                   not d.startswith(".") and
                   os.path.abspath(os.path.join(base, d)) != destino]
        for nombre in files:
            ruta = os.path.relpath(os.path.join(base, nombre), raiz).replace(os.sep, "/")
            ruta = "./" + ruta
            if not es_ignorado(nombre, ruta, script_actual):
                salida.append(ruta)
    return sorted(salida)


def clasificar(ruta):
    for expresion, categoria in R:
        if expresion.search(ruta):
            return categoria
    return "99_SIN_UBICAR"


def main():
    parser = argparse.ArgumentParser(description="Clasifica por tema y construye una vista por copia.")
    parser.add_argument("origen", nargs="?", help="Carpeta origen; por defecto, donde reside el script")
    parser.add_argument("--copiar", action="store_true", help="Construye la vista organizada")
    parser.add_argument("--destino", help="Destino; por defecto <origen>/ORGANIZADO_POR_TEMA")
    args = parser.parse_args()

    raiz = os.path.abspath(args.origen) if args.origen else RAIZ_DEFAULT
    destino = os.path.abspath(args.destino) if args.destino else os.path.join(raiz, "ORGANIZADO_POR_TEMA")
    if not os.path.isdir(raiz):
        print(f"Error: la carpeta origen no existe: {raiz}", file=sys.stderr)
        return 1

    archivos = recolectar(raiz, destino)
    asignacion = collections.defaultdict(list)
    for ruta in archivos:
        asignacion[clasificar(ruta)].append(ruta)

    print(f"Carpeta origen:  {raiz}\nCarpeta destino: {destino}\n")
    print(f"Archivos considerados (sin cachés ni archivos ocultos): {len(archivos)}\n")
    for categoria, descripcion in CATEGORIAS:
        claves = [k for k in asignacion if k == categoria or k.startswith(categoria + "|")]
        total = sum(len(asignacion[k]) for k in claves)
        print(f"{categoria:38s} {total:4d}   {descripcion}")
        for clave in sorted(claves):
            if "|" in clave:
                print(f"    └─ {clave.split('|', 1)[1]:38s} {len(asignacion[clave]):4d}")

    pendientes = asignacion.get("99_SIN_UBICAR", [])
    if pendientes:
        print(f"\nPENDIENTES DE CLASIFICAR A MANO ({len(pendientes)}):")
        for ruta in pendientes:
            print("   ", ruta)

    if not args.copiar:
        print("\n[simulación] no se copió nada. Ejecuta con --copiar para construir la vista.")
        return 0

    vistos = set()
    copiados = omitidos = 0
    for clave, rutas in sorted(asignacion.items()):
        if "|" in clave:
            base, subcategoria = clave.split("|", 1)
            carpeta = os.path.join(destino, base, subcategoria)
        else:
            carpeta = os.path.join(destino, clave)
        os.makedirs(carpeta, exist_ok=True)
        for relativa in rutas:
            origen = os.path.join(raiz, relativa[2:])
            with open(origen, "rb") as archivo:
                digest = hashlib.md5(archivo.read()).hexdigest()
            if digest in vistos:
                omitidos += 1
                continue
            vistos.add(digest)
            nombre = os.path.basename(origen)
            raiz_nombre, extension = os.path.splitext(nombre)
            salida = os.path.join(carpeta, nombre)
            contador = 2
            while os.path.exists(salida):
                salida = os.path.join(carpeta, f"{raiz_nombre}__{contador}{extension}")
                contador += 1
            shutil.copy2(origen, salida)
            copiados += 1

    print(f"\nCopiados: {copiados} · omitidos por duplicado exacto: {omitidos}")
    print(f"Vista organizada: {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
