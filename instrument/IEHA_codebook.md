# Codebook — IEH-A

Versión 1.0 · 2026-06 · CC BY 4.0. Define la codificación, la puntuación y el cruce diagnóstico. Núcleo común (no se altera sin acuerdo del comité directivo).

## Codificación de los ítems IEH-A

Cada ítem se codifica por el **grado de contracción** de la conducta:

| Respuesta | Código | Significado |
|---|---|---|
| `Igual` | 0 | Sin cambio |
| `Cambié el horario` | 1 | Reorganización (la práctica persiste, desplazada) |
| `Lo hago menos` | 2 | Reducción |
| `Lo abandoné` | 3 | Cese |
| `No aplica` | NA | Excluir del cálculo (la práctica no existe en el hogar) |

Cada ítem lleva además su **razón verbatim** (texto), usada para la **atribución** (acústica vs. no acústica) y para la codificación temática posterior.

## Puntuación del índice

- **Por dimensión** (OC, PR, CU): media de los ítems válidos (no-NA) de la dimensión, en escala 0–3.
- **IEH-A global:** **suma observada / suma máxima posible** sobre los ítems válidos (normalizado 0–1). Reportar también el **número de ítems válidos** (denominador) por la prevalencia de `No aplica`.
- **Punto de corte "IEH-A alto":** se **calibra empíricamente** en la fase de verificación (no se fija a priori; tentativo ≥ 0.40 en el agregado, sujeto a los datos multi-sitio).

> La puntuación final del índice **no se calcula en campo**; es post-aplicación.

## Atribución (acústica vs. otras causas)

A partir de la razón verbatim, cada cambio se clasifica como: `acústica` · `no-acústica` · `mixta` · `sin-razón`. Solo la contracción con atribución acústica o mixta cuenta como **erosión por ruido**; la no-acústica se conserva como control.

## Cruce con escalas clínicas: los cuatro perfiles

Dicotomizando IEH-A (alto/bajo, según corte calibrado) y el estado clínico (PSQI/PSS-10 normal/alterado):

| Perfil | PSQI / PSS-10 | IEH-A | Interpretación |
|---|---|---|---|
| 1 | Normal | Bajo | Habitar acústico preservado |
| 2 | Alterado | Alto | Daño clínico convergente con erosión (caso "esperado") |
| **3** | **Normal** | **Alto** | **Habitante funcional con mundo práctico contraído (foco de interés)** |
| 4 | Alterado | Bajo | Daño clínico sin erosión del habitar (otras causas) |

El **Perfil 3** es la contribución diferencial del instrumento: identifica a quienes las escalas estándar declaran funcionales pero cuyo mundo práctico se ha contraído. Su existencia y caracterización empírica, y su **independencia estadística** respecto de PSQI/PSS-10, son el objeto central de la validación multi-sitio (ver [pre-registro](../preregistration/multisite_validation_protocol.md)).

## Variables mínimas a reportar

Ver la [plantilla de datos](../data/data_template.csv) y el [diccionario](../data/data_dictionary.md).
