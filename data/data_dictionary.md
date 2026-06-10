# Diccionario de datos — plantilla armonizada IEH-A

Versión 1.0 · 2026-06 · CC BY 4.0. Una fila = un informante. Datos **anonimizados**: ningún campo permite reidentificación. Ver [`data_template.csv`](data_template.csv).

| Campo | Tipo | Valores / formato | Descripción |
|---|---|---|---|
| `site_id` | texto | p. ej. `MX01`, `BR01` | Identificador del sitio/equipo participante. |
| `respondent_id` | texto | `E0NN` | Código de informante disociado del nombre (el vínculo, si existe, permanece **solo** en el sitio). |
| `country` | texto | ISO-3166 alfa-2 (`MX`, `BR`, `ES`, `PE`…) | País del sitio. |
| `city` | texto | libre | Ciudad/localidad. |
| `context_label` | texto | `S-<contexto>-<etiqueta>` | Código de sub-zona/contexto (anonimizado, sin domicilios). |
| `dominant_source` | texto | `corredor_vehicular` · `infraestructura_institucional` · `vida_nocturna` · `mixto` · `otro` | Fuente sonora dominante del sector. |
| `application_date` | fecha | `YYYY-MM-DD` | Fecha de aplicación. |
| `mode` | texto | `assisted` · `think_aloud` | Modalidad de aplicación. |
| `age_range` | texto | `18-29` · `30-44` · `45-59` · `60+` | Rango de edad (no edad exacta). |
| `gender` | texto | `F` · `M` · `X` · `NR` | Género autoreportado (`X` otro, `NR` no responde). |
| `residence_months` | entero | meses | Tiempo de residencia en el domicilio (≥ 6 para inclusión). |
| `OC1`…`OC4` | entero/NA | `0`·`1`·`2`·`3`·`NA` | Ítems de Contracción de ocupaciones (codificación en [codebook](../instrument/IEHA_codebook.md)). |
| `PR1`…`PR4` | entero/NA | `0`·`1`·`2`·`3`·`NA` | Ítems de Deterioro de proyecciones. |
| `CU1`…`CU4` | entero/NA | `0`·`1`·`2`·`3`·`NA` | Ítems de Simplificación del cuidado. |
| `<item>_attr` | texto | `acustica` · `no-acustica` · `mixta` · `sin-razon` · (vacío si `Igual`/`NA`) | Atribución del cambio, derivada de la razón verbatim. |
| `PSQI_global` | entero/NA | 0–21 | Puntaje global PSQI (si se aplicó). |
| `PSS10_total` | entero/NA | 0–40 | Puntaje total PSS-10 (si se aplicó). |
| `IEHA_OC`,`IEHA_PR`,`IEHA_CU` | decimal | 0–3 | Media por dimensión sobre ítems válidos. |
| `IEHA_global` | decimal | 0–1 | Suma observada / máxima posible (normalizado). |
| `n_valid_items` | entero | 0–12 | Ítems válidos (no-NA) usados en el cálculo. |
| `profile` | entero/NA | `1`·`2`·`3`·`4`·`NA` | Perfil del cruce IEH-A × clínicas (NA si no hay escalas clínicas). |
| `instrument_version` | texto | `v0.1` · `v0.2` … | Versión del instrumento aplicada. |
| `protocol_deviations` | texto | libre | Desviaciones del protocolo común. |
| `notes` | texto | libre | Observaciones del sitio. |

## Reglas

- **No** se comparten: nombre, dirección exacta, coordenadas de domicilio, audio, ni cualquier dato reidentificable.
- Los **textos verbatim completos** no van en esta plantilla agregada; se conservan en el sitio y se aportan, si procede, en un archivo separado **ya anonimizado** y bajo acuerdo del comité.
- Acompañar el envío con una **nota de sitio** (contexto, fuente dominante, n, fechas, modalidad, adaptaciones, desviaciones).
