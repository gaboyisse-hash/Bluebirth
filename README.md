# Blue Bird
Red BlueBird - No cómputo, solo existo

## Organizar archivos por tema

El script `organizar_por_tema.py` crea una vista organizada **por copia**; no mueve ni elimina los archivos originales. Primero ejecuta la simulación para revisar la clasificación:

```bash
python3 organizar_por_tema.py
```

Cuando estés conforme con el listado, genera las copias con:

```bash
python3 organizar_por_tema.py --copiar
```

La vista se crea en `ORGANIZADO_POR_TEMA/`. Los archivos sin una regla definida quedan en `99_SIN_UBICAR` para revisión manual. El script omite cachés y duplicados exactos.
