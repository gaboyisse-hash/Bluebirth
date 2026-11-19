#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
organizar_por_tema.py

Clasifica el cuerpo de trabajo `project/` por TEMA, ENFOQUE Y PROPÓSITO,
y construye una vista organizada por COPIA en `ORGANIZADO_POR_TEMA/`.

Reglas de seguridad:
  - No mueve, no renombra y no borra NADA del árbol original.
  - Sólo lee del original y copia a la vista nueva.
  - Los archivos de caché (__pycache__) y los duplicados exactos no se copian.

Uso:
  python3 organizar_por_tema.py            # simulación: sólo informa
  python3 organizar_por_tema.py --copiar   # construye la vista organizada
"""

import os, re, sys, shutil, hashlib, collections

RAIZ = os.path.dirname(os.path.abspath(__file__))
DESTINO = os.path.join(RAIZ, "ORGANIZADO_POR_TEMA")

# ---------------------------------------------------------------------------
# 1. TAXONOMÍA
# ---------------------------------------------------------------------------
CATEGORIAS = [
    ("00_OBRA_Y_EDICIONES",               "El libro: tratado, ediciones integradas, partes y obra canónica"),
    ("01_FILOSOFIA_Y_PENSAMIENTO",        "Ontología, lenguaje como modelo, libertad, silencio, cábala, vínculo"),
    ("02_FISICA_COSMOLOGIA_Y_ATOMO",      "Agujeros negros, ruedo cósmico, humo y renormalización, átomo digital (EEL), luz, tiempo"),
    ("03_ANTROPOLOGIA_CONSCIENCIA_Y_SER", "Consciencia, cuerpo, ser, sombra, caduceo mexica-kundalini, regencia, Maturana"),
    ("04_INVESTIGACION_Y_METODO",         "Homologación conceptual (v1–v5), dictámenes, verificaciones, auditorías de corpus, precedencia"),
    ("05_BLUE_BIRD_RED_LUCY",             "Moneda BB, red Lucy, ecosistema financiero y su sustento legal, teórico e instrumental"),
    ("06_MUSICA_TIEMPO_Y_DANZA",          "Qué es la música, economía con base musical, catálogo de escucha, percepción del tiempo"),
    ("07_CHARLAS_DIALOGOS_E_INFORMATIVOS", "Conversaciones y charlas, y documentos informativos de consulta"),
    ("08_AUDITORIA_TECNICA_Y_LOGS",       "Logcat del teléfono, conexiones de red, herramientas de inventario de Drive"),
    ("09_IDENTIDAD_Y_MARCO_PERSONAL",     "Identidad, mapa de identidades y periodos, manifiesto personal"),
    ("99_SIN_UBICAR",                     "Pendiente de clasificar (se revisa a mano)"),
]

SUBCATEGORIAS_05 = [
    ("05a_Constitutivo_fe_y_legalidad", "Actas, constituciones, manifiestos, fe y legalidad, fechas y cronología"),
    ("05b_Valor_moneda_y_economia",     "Modelo de valor de la BB, paridades, simulaciones económicas, tablas"),
    ("05c_Red_topologia_cordon_escala", "Modelo de red sináptica: código, mediciones, cordón, escala, resultados"),
    ("05d_Interfaz_y_artefactos",       "Interfaces HTML, artefactos v2.4/v2.5, nodos, latidos, compendios, estatutos"),
    ("05e_Codigo_y_simuladores",        "Código de terceros y propio, simuladores, scripts contables"),
]

# ---------------------------------------------------------------------------
# 2. REGLAS  (primera coincidencia gana; se evalúan en orden)
#    patrón de ruta completa normalizada -> categoría
# ---------------------------------------------------------------------------
R = []
def reg(patron, cat):
    R.append((re.compile(patron), cat))

# --- 00 Obra y ediciones ---------------------------------------------------
reg(r"^\./La_Danza_del_Colibri_Tratado_Unificado\.md$", "00_OBRA_Y_EDICIONES")
reg(r"^\./colibri_edicion_integrada\.md$",              "00_OBRA_Y_EDICIONES")
reg(r"^\./EL_LIBRO_DEL_COLIBRI_edicion_integrada\.docx$","00_OBRA_Y_EDICIONES")
reg(r"^\./SEGMENTO_INDEPENDIENTE",                      "00_OBRA_Y_EDICIONES")
reg(r"^\./tanda4/07_obra_canonica",                     "00_OBRA_Y_EDICIONES")
reg(r"^\./dolly_docs/",                                 "00_OBRA_Y_EDICIONES")   # partes largas del libro
reg(r"^\./tanda3/(arquitectura|colibro)\.",             "00_OBRA_Y_EDICIONES")
reg(r"^\./docs2/(danza_colibri|geometria_relacional)\.","00_OBRA_Y_EDICIONES")

# --- 01 Filosofía y pensamiento -------------------------------------------
reg(r"lenguaje_(liora|modelo)",                         "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"lenguaje_como_modelo",                            "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"liora_geometrica",                                "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"amor_estructura",                                 "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"LIBERTAD_CORRELACIONAL|paradoja_libertad",        "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"CABALA_Y_EL_ARBOL|cabala_desde_el_silencio",      "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"conceptualizacion_silencio|GLOSARIO_DE_CONCEPTOS","01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"ECONOMIA_DE_DAs|economia_cosmica_delta_as",       "01_FILOSOFIA_Y_PENSAMIENTO")
reg(r"^\./docs/change_word",                            "01_FILOSOFIA_Y_PENSAMIENTO")

# --- 02 Física, cosmología y átomo ---------------------------------------
reg(r"AGUJEROS_NEGROS|agujero_negro",                   "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"ruedo|RUEDO",                                     "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"[Hh]umo|HUMO",                                    "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"eel|EEL",                                         "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"atalogo| diagrama_temporal|DIAGRAMA_TEMPORAL|Diagrama Temporal", "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"modelo_atomo|analisis_modelo_atomo",               "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"^\./tanda3/(ckp_v2|math_flush|id_colores)\.",      "02_FISICA_COSMOLOGIA_Y_ATOMO")
reg(r"^\./aportes_movimiento_del_universo\.md$",         "02_FISICA_COSMOLOGIA_Y_ATOMO")

# --- 03 Antropología, consciencia y ser ----------------------------------
reg(r"^\./blue_bird_docs/postulado_maya/",               "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"[Cc]aduceo|KUNDALINI",                             "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"PENSAMIENTO_CUERPO|ciencia_pensamiento_silencio",  "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"SOMBRA|defectos_de_personalidad",                  "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"aura_retorno",                                     "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")
reg(r"^\./maturana_guia\.md$",                           "03_ANTROPOLOGIA_CONSCIENCIA_Y_SER")

# --- 04 Investigación y método -------------------------------------------
reg(r"^\./(analogo_conceptual_v1|comparacion_v1_v2|v3_meta|v4)/", "04_INVESTIGACION_Y_METODO")
reg(r"^\./revision_2026-09-22/DICTAMEN",                 "04_INVESTIGACION_Y_METODO")
reg(r"^\./revision_2026-09-22/lote3/(DICTAMEN|VERIFICACION)", "04_INVESTIGACION_Y_METODO")
reg(r"^\./revision_2026-09-22/lote2/DOCUMENTOS_LIMPIOS/00_LEEME", "04_INVESTIGACION_Y_METODO")
reg(r"^\./revision_2026-09-22/DOCUMENTOS_LIMPIOS/00_LEEME", "04_INVESTIGACION_Y_METODO")
reg(r"^\./blue_bird_docs/(CRONOLOGIA_y_historicidad|PRECEDENCIA_y_sincronia|ESCALERA_de_correcciones)\.md$", "04_INVESTIGACION_Y_METODO")
reg(r"^\./blue_bird_docs/(analisis_precedencia|caminar_indice|prueba_azar_sin_input|prueba_repetir_la_cinta)\.py$", "04_INVESTIGACION_Y_METODO")
reg(r"^\./blue_bird_docs/precedencia_resultados\.json$", "04_INVESTIGACION_Y_METODO")
reg(r"^\./(corpus_review_silencio_del_colibri|auditoria_corpus_dolly|distincion_participacion_liora)\.md$", "04_INVESTIGACION_Y_METODO")
reg(r"HOMOLOGACI",                                       "04_INVESTIGACION_Y_METODO")
reg(r"^\./AGRUPACION_DOCUMENTOS\.md$",                   "04_INVESTIGACION_Y_METODO")

# --- 05 Blue Bird / Red Lucy ---------------------------------------------
reg(r"^\./blue_bird_docs/(0[1-6]_|integrar/|marco/)",    "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"^\./blue_bird_docs/(modelo_valor/|simulador/)",    "05_BLUE_BIRD_RED_LUCY|05b_Valor_moneda_y_economia")
reg(r"^\./blue_bird_docs/banxico/",                      "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"^\./blue_bird_docs/red/",                          "05_BLUE_BIRD_RED_LUCY|05c_Red_topologia_cordon_escala")
reg(r"^\./blue_bird_docs/codigo/",                       "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")
reg(r"^\./tanda4/(0[1-6]_|02_)",                         "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"^\./logcat_audit/drive/(doc_|v24_)",               "05_BLUE_BIRD_RED_LUCY|05d_Interfaz_y_artefactos")
reg(r"^\./logcat_audit/drive/original_bb\.txt$",         "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")

# --- 06 Música, tiempo y danza -------------------------------------------
reg(r"QUE_ES_LA_MUSICA|ECONOMIA_BASE_MUSICAL",           "06_MUSICA_TIEMPO_Y_DANZA")
reg(r"^\./blue_bird_docs/catalogo_red/",                 "06_MUSICA_TIEMPO_Y_DANZA")
reg(r"^\./docs/(tiempo_vive|time_issue_aura)",           "06_MUSICA_TIEMPO_Y_DANZA")
reg(r"^\./docs2/timecepcion",                            "06_MUSICA_TIEMPO_Y_DANZA")

# --- 07 Charlas, diálogos e informativos ---------------------------------
reg(r"Chat con Dola|chat_dola",                          "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"^\./tanda3/dolly_(first|comparacion)",             "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"^\./tanda3/",                                      "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"^\./docs/(dialogos_aura|neutrino|reflexion)",      "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"^\./docs2/sophi_bisho",                            "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"Texto compartido",                                 "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")
reg(r"The_Coiled_Serpent|threaht speculation|Aura proyecci", "07_CHARLAS_DIALOGOS_E_INFORMATIVOS")

# --- 08 Auditoría técnica y logs -----------------------------------------
reg(r"^\./logcat_audit/logcat_diagnostico\.txt$",        "08_AUDITORIA_TECNICA_Y_LOGS")
reg(r"^\./logcat_audit/(informe_auditoria|ficha_blue_bird|CHANGELOG|REDACCION|segundo)", "08_AUDITORIA_TECNICA_Y_LOGS")
reg(r"^\./logcat_audit/blue_bird_v2\.[45]",              "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")
reg(r"^\./logcat_audit/drive/(inventario|_descarga_meta)", "08_AUDITORIA_TECNICA_Y_LOGS")
reg(r"^\./(analisis_conexiones\.md|conexiones_clasificadas\.csv|log_conexiones_original\.csv|clasificar_log\.py)$", "08_AUDITORIA_TECNICA_Y_LOGS")
reg(r"^\./(organizar_drive_v[23]\.gs|inventario_drive_solo\.gs)$", "08_AUDITORIA_TECNICA_Y_LOGS")

# --- 09 Identidad y marco personal ---------------------------------------
reg(r"^\./mapa_identidades_y_periodos\.md$",             "09_IDENTIDAD_Y_MARCO_PERSONAL")
reg(r"^\./docs/manifiesto",                              "09_IDENTIDAD_Y_MARCO_PERSONAL")
reg(r"Mi_Identidad_Gabriel",                             "09_IDENTIDAD_Y_MARCO_PERSONAL")

# --- Material de entrada: Drive (202) ------------------------------------
#   código y datos -> 05e ; html de artefactos -> 05d ; resto se revisa aparte
reg(r"^\./logcat_audit/drive/descarga/\d+__code_[^/]*\.(py|c|sh|json|csv|txt)$", "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")
reg(r"^\./logcat_audit/drive/descarga/\d+__code_[^/]*\.html$",                   "05_BLUE_BIRD_RED_LUCY|05d_Interfaz_y_artefactos")
reg(r"^\./logcat_audit/drive/descarga/\d+__(bb_|Blue_|blue_|Blue_Birth|interfaz_|lucy_|mithos_|estatuto_|sistema_bb|compendio_bb|flujo_datos_lucy|red_multinivel|Protocolo_Blue|captall_|modelo_atomo|ruedo_cosmico)", "05_BLUE_BIRD_RED_LUCY|05d_Interfaz_y_artefactos")
reg(r"^\./logcat_audit/drive/descarga/\d+__(Documento Maestro Blue Bird|DOCUMENTO DE AUDITOR)", "05_BLUE_BIRD_RED_LUCY|05a_Constitutivo_fe_y_legalidad")
reg(r"^\./logcat_audit/drive/descarga/\d+__CODIGO_COMPLETO_CONSTRUCTO_VALOR_BB", "05_BLUE_BIRD_RED_LUCY|05b_Valor_moneda_y_economia")
reg(r"^\./logcat_audit/drive/descarga/\d+__(organismos_|participacion_usuarios|usuarios_aura|multivectorial_ck_t|sistema_coherencia|agencia_cambio_aura|aura_agencia|aura_servidor|consolidacion_intercambio|bb_pasarelas|bb_modelo)", "05_BLUE_BIRD_RED_LUCY|05e_Codigo_y_simuladores")
reg(r"^\./logcat_audit/drive/descarga/\d+__table_",      "05_BLUE_BIRD_RED_LUCY|05b_Valor_moneda_y_economia")
reg(r"^\./logcat_audit/drive/descarga/\d+__Obra_Canonica", "00_OBRA_Y_EDICIONES")
reg(r"^\./logcat_audit/drive/descarga/\d+__Radio|^\./logcat_audit/drive/descarga/\d+__README", "99_SIN_UBICAR")

# ---------------------------------------------------------------------------
# 3. RECOLECCIÓN
# ---------------------------------------------------------------------------
def es_cache(p):
    return "__pycache__" in p or p.endswith((".pyc",))

def recolectar():
    out = []
    for base, dirs, files in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in ("__pycache__", "ORGANIZADO_POR_TEMA", ".git")]
        for f in files:
            p = os.path.relpath(os.path.join(base, f), RAIZ)
            p = "./" + p.replace(os.sep, "/")
            if es_cache(p):
                continue
            out.append(p)
    return sorted(out)

def clasificar(p):
    for rx, cat in R:
        if rx.search(p):
            return cat
    return "99_SIN_UBICAR"

def main():
    archivos = recolectar()
    asignacion = collections.defaultdict(list)
    for p in archivos:
        asignacion[clasificar(p)].append(p)

    print(f"Archivos considerados (sin cachés): {len(archivos)}\n")
    for cat, desc in CATEGORIAS:
        propios = [p for p in asignacion if p == cat or p.startswith(cat + "|")]
        n = sum(len(asignacion[k]) for k in propios)
        print(f"{cat:38s} {n:4d}   {desc}")
        for k in sorted(propios):
            if "|" in k:
                print(f"    └─ {k.split('|', 1)[1]:38s} {len(asignacion[k]):4d}")
    print()
    sin = asignacion.get("99_SIN_UBICAR", [])
    if sin:
        print(f"PENDIENTES DE CLASIFICAR A MANO ({len(sin)}):")
        for p in sin:
            print("   ", p)

    if "--copiar" not in sys.argv:
        print("\n[simulación] no se copió nada. Ejecuta con --copiar para construir la vista.")
        return

    # --- copia (sin duplicados exactos) ---
    vistos, copiados, omitidos = {}, 0, 0
    for cat, sub in sorted(asignacion.items()):
        if cat == "99_SIN_UBICAR":
            destino = os.path.join(DESTINO, cat)
        elif "|" in cat:
            base, s = cat.split("|", 1)
            destino = os.path.join(DESTINO, base, s)
        else:
            destino = os.path.join(DESTINO, cat)
        os.makedirs(destino, exist_ok=True)
        for rel in sub:
            src = os.path.join(RAIZ, rel[2:])
            nombre = os.path.basename(src)
            h = hashlib.md5(open(src, "rb").read()).hexdigest()
            if h in vistos:
                omitidos += 1
                continue
            vistos[h] = rel
            dst = os.path.join(destino, nombre)
            if os.path.exists(dst):
                raiz_, ext = os.path.splitext(nombre)
                dst = os.path.join(destino, f"{raiz_}__2{ext}")
            shutil.copy2(src, dst)
            copiados += 1
    print(f"\nCopiados: {copiados} · omitidos por duplicado exacto: {omitidos}")
    print(f"Vista organizada: {DESTINO}")

if __name__ == "__main__":
    main()
