# Manifiesto e Índice: Vista Organizada por Tema

**Fecha de generación:** 2026-11-19  
**Origen:** `C:\Bluebird`  
**Destino de la vista:** `C:\Bluebird\ORGANIZADO_POR_TEMA`  
**Total de archivos copiados:** 25  
**Duplicados omitidos:** 1 (`nodo_web_bb (2).py`)

## 1. Resumen por Categoría

| Categoría / Subcategoría | Archivos | Descripción |
|---|---:|---|
| `05_BLUE_BIRD_RED_LUCY` | 24 | Moneda BB, red Lucy, ecosistema financiero, simuladores y artefactos |
| ├─ `05b_Valor_moneda_y_economia` | 4 | Modelo de valor de la BB, paridades, simulaciones económicas, tablas |
| ├─ `05c_Red_topologia_cordon_escala` | 3 | Nodos de red, topología, código de sincronización y conectividad |
| ├─ `05d_Interfaz_y_artefactos` | 6 | Interfaces HTML, simuladores web interactivos y artefactos de génesis |
| └─ `05e_Codigo_y_simuladores` | 10 | Módulos Aura, agentes autónomos, biología de organismos y servidores |
| `08_AUDITORIA_TECNICA_Y_LOGS` | 1 | Binarios de conectividad, túneles y herramientas técnicas |
| `99_SIN_UBICAR` | 1 | Documentación y notas generales pendientes de asignación específica |

## 2. Inventario Detallado de Archivos

### `05_BLUE_BIRD_RED_LUCY / 05b_Valor_moneda_y_economia`

Modelo de valor de la BB, paridades, balances contables y blockchain.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `BB_CLOSURE_V9_CORE.canonical.json` | 235 B | .json | Parámetros canónicos de cierre del núcleo V9 |
| `bb_pasarelas_fiat_paridades.py` | 13.11 KB | .py | Lógica de pasarelas fiat, tipos de cambio y paridades |
| `bb_v8_reciclaje_cancelacion_deuda.json` | 3.18 KB | .json | Reglas y registros de reciclaje / cancelación de deuda V8 |
| `blockchain_bb.json` | 3.59 MB | .json | Libro mayor / cadena de bloques del ecosistema Blue Bird |

### `05_BLUE_BIRD_RED_LUCY / 05c_Red_topologia_cordon_escala`

Nodos distribuidores, interfaces de red y topología del cordón sináptico.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `nodo_maestro_bb.py` | 4.56 KB | .py | Servidor y orquestador del nodo maestro Blue Bird |
| `nodo_web_bb.py` | 17.07 KB | .py | Implementación del nodo cliente / pasarela web Blue Bird |
| `nodo_web_bb (1).py` | 0 B | .py | Archivo de nodo web complementario / marcador |

> El duplicado exacto `nodo_web_bb (2).py` fue omitido automáticamente durante la copia para evitar redundancia de almacenamiento.

### `05_BLUE_BIRD_RED_LUCY / 05d_Interfaz_y_artefactos`

Artefactos interactivos, visualizadores HTML y componentes de arranque.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `bb birth aura. js` | 3.40 KB | .js | Script de inicialización y nacimiento de la entidad Aura |
| `BLUEBIRD.HTML` | 6.58 KB | .html | Interfaz visual principal Blue Bird |
| `firmar genesis.html` | 4.52 KB | .html | Artefacto web para firma y validación del bloque génesis |
| `Génesis_BB.html` | 1.94 KB | .html | Documento de especificación visual del Génesis Blue Bird |
| `simulador_red_blue_bird(1).html` | 21.06 KB | .html | Simulador interactivo de la red de nodos en navegador |
| `Simulador-Red-Blue-Bird-ACTIVO.html` | 18.65 KB | .html | Simulador operativo en tiempo real de la topología Blue Bird |

### `05_BLUE_BIRD_RED_LUCY / 05e_Codigo_y_simuladores`

Módulos de backend, agentes autónomos, biología sintética de organismos y coherencia.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `agencia_cambio_aura.py` | 9.77 KB | .py | Lógica de la agencia de cambio y conversiones Aura |
| `aura_agencia_autonoma.py` | 22.16 KB | .py | Agente autónomo de toma de decisiones y arbitraje |
| `aura_servidor_completo.py` | 15.42 KB | .py | Servidor backend monolítico de la red Aura |
| `consolidacion_intercambio_aura.py` | 14.55 KB | .py | Motor de liquidación y consolidación de transacciones |
| `multivectorial_ck_t.py` | 6.23 KB | .py | Modelo matemático multivectorial tiempo/estado (`ck,t`) |
| `organismos_biologia_i3v.py` | 14.86 KB | .py | Lógica de simulación biológica digital (`i3v`) |
| `organismos_vivos_aura.py` | 15.95 KB | .py | Entidades dinámicas y modelado de vida artificial en red |
| `participacion_usuarios_aura.py` | 7.96 KB | .py | Métricas de involucramiento y reputación de usuarios |
| `sistema_coherencia_v5_robust.py` | 44.34 KB | .py | Motor de coherencia y verificación de consenso V5 |
| `usuarios_aura.json` | 2.98 KB | .json | Base de datos / estado inicial de cuentas de usuario |

### `08_AUDITORIA_TECNICA_Y_LOGS`

Herramientas operativas, binarios y auditoría.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `cloudflared.exe.exe` | 52.77 MB | .exe | Binario de Cloudflare Tunnel para publicación de endpoints |

### `99_SIN_UBICAR`

Archivos genéricos o informativos pendientes de integración manual.

| Archivo | Tamaño | Extensión | Propósito |
|---|---:|---|---|
| `README.txt` | 640 B | .txt | Documento de instrucciones / notas iniciales |

## 3. Principios de Integridad Aplicados

- **Inmutabilidad del origen:** Ningún archivo de `C:\Bluebird` fue renombrado, movido o modificado.
- **Deduplicación por hash:** Identificación basada en MD5 que previene copias redundantes con nombres idénticos o distintos.
- **Manejo de colisiones:** En caso de coexistir archivos con el mismo nombre y diferente contenido, se aplican sufijos secuenciales (`__2`, `__3`, etc.).
