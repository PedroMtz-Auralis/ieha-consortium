# Pre-registro — Validación distribuida multi-sitio del IEH-A

Versión 1.0 · 2026-06 · CC BY 4.0. Plan pre-registrado del estudio de validación coordinado por el Consorcio IEH-A. Se versiona en el repositorio; cualquier enmienda queda fechada y trazable.

## 1. Objetivo y preguntas

**Objetivo:** establecer las propiedades de medición del IEH-A a través de contextos territoriales diversos y caracterizar empíricamente sus perfiles diagnósticos.

**Preguntas:**
- **P1 (invarianza de medición).** ¿El IEH-A mide el mismo constructo en poblaciones de origen y contexto distintos? (invarianza configural, métrica y escalar entre sitios).
- **P2 (Perfil 3).** ¿Existe y es caracterizable el Perfil 3 —clínica normal con IEH-A alto—? ¿Es **estadísticamente independiente** de los instrumentos clínicos (PSQI, PSS-10)?
- **P3 (estructura).** ¿Se sostiene la estructura de tres dimensiones (OC, PR, CU) entre sitios?

## 2. Diseño

Estudio **observacional, transversal, multi-sitio**, tipo **ensayo inter-territorial (*round-robin*)**: un protocolo común aplicado por equipos independientes en contextos distintos, con datos armonizados. Cada sitio gestiona su propia ética (modelo per-sitio, [ETHICS.md](../ETHICS.md)).

## 3. Participantes y muestreo

- **Inclusión:** residentes mayores de edad con ≥ 6 meses en el domicilio, en sectores con régimen acústico sostenido.
- **Estratificación:** por **fuente sonora dominante** (no solo proximidad a vía) y por **rango de edad**, con captación en franjas horarias diversas.
- **Tamaño:** orientativo **N ≥ 150 por sitio** para contribuir a las pruebas de invarianza (sitios menores se integran como exploratorios). El N total se determina por el número de sitios.

## 4. Variables

- **IEH-A:** 12 ítems (OC, PR, CU), formato categorial + atribución verbatim → puntuación por dimensión y global ([codebook](../instrument/IEHA_codebook.md)).
- **Clínicas (cuando el sitio las incluya):** PSQI global, PSS-10 total (versiones validadas locales).
- **Contexto:** fuente dominante, edad, género, tiempo de residencia.

## 5. Plan analítico (pre-especificado)

1. **Descriptivos** por sitio y agregados; prevalencia de `No aplica` por ítem.
2. **Estructura y fiabilidad:** análisis factorial confirmatorio (3 factores correlacionados) + consistencia interna por dimensión (ordinal α/ω). Ajuste por la naturaleza ordinal de los ítems (estimador WLSMV o equivalente).
3. **Invarianza de medición** entre sitios: secuencia **configural → métrica → escalar**, con criterios pre-especificados (p. ej. ΔCFI ≤ 0.010, ΔRMSEA ≤ 0.015). Identificación de ítems no invariantes (candidatos a "específicos del contexto").
4. **Perfiles:** dicotomización de IEH-A (corte calibrado empíricamente sobre el agregado) × estado clínico; tabla de contingencia de los cuatro perfiles por sitio.
5. **P2 — Perfil 3 / independencia:** prueba de que la varianza del IEH-A **no es redundante** con PSQI/PSS-10 (correlaciones; varianza incremental del IEH-A sobre las clínicas en modelos jerárquicos; existencia de una celda Perfil 3 no vacía y estadísticamente distinguible). Controles: edad, tiempo de residencia, fuente dominante.
6. **Atribución:** proporción de erosión con atribución acústica/mixta vs. no-acústica.

## 6. Resultados primarios

- Grado de invarianza alcanzado (configural/métrica/escalar) e ítems no invariantes.
- Existencia, tamaño y caracterización del Perfil 3 y su independencia de las clínicas.
- Recomendaciones de refinamiento del instrumento (v0.3) basadas en la evidencia multi-sitio.

## 7. Gobernanza de datos y reporte

- Datos armonizados y anonimizados por sitio → conjunto *pooled* gobernado por el comité directivo ([GOVERNANCE.md](../GOVERNANCE.md) §5).
- Depósito abierto del conjunto agregado (con DOI) tras la publicación principal.
- Autoría según [AUTHORSHIP.md](../AUTHORSHIP.md). En el reporte se declaran las aprobaciones éticas **por sitio**.

## 8. Enmiendas

Cualquier cambio al plan se registra como nueva versión fechada de este documento, con la justificación, **antes** de los análisis afectados.
