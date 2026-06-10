# Gobernanza del Consorcio IEH-A

Documento vinculante para todo equipo participante. Define cómo se administra el consorcio, quién decide qué, y bajo qué condiciones se desarrolla y versiona el instrumento. Versión 1.0 · 2026-06.

## 1. Naturaleza y propósito

El Consorcio IEH-A es una **red de investigación abierta y horizontal** cuyo propósito es **validar, adaptar y mejorar** el Índice de Erosión del Habitar Acústico (IEH-A) en múltiples contextos territoriales, mediante un protocolo común aplicado de forma distribuida (ensayo inter-territorial tipo *round-robin*).

El consorcio es una iniciativa científica de sus **coordinadores fundadores** y de los **equipos participantes**; no representa ni compromete a ninguna institución, y no constituye un órgano con personalidad jurídica. Cada equipo participa a título de su propia adscripción y bajo su propia responsabilidad.

## 2. Roles

| Rol | Quién | Función |
|---|---|---|
| **Coordinación fundadora** | P. Martínez Cisneros · E. Sánchez Flores (UACJ, México) | Mantienen el protocolo común y el repositorio; convocan decisiones; consolidan el conjunto de datos *pooled*; lideran los productos de validación multi-sitio. |
| **Investigador/a principal (PI) de sitio** | Responsable de cada equipo participante | Obtiene la aprobación ética en su jurisdicción; aplica el protocolo común; entrega datos armonizados y anonimizados; participa en decisiones del consorcio. |
| **Comité directivo (steering)** | Coordinación + PIs de sitio activos | Se constituye cuando hay ≥ 3 sitios activos; decide versiones del instrumento, plan analítico y productos. |

La coordinación fundadora **rota o se amplía** por acuerdo del comité directivo a medida que la red crece.

## 3. Toma de decisiones

- **Operación cotidiana** (mantenimiento del repo, soporte a sitios): coordinación.
- **Decisiones sustantivas** (cambios al instrumento, plan analítico, política de datos, autoría de un producto): **consenso del comité directivo**; si no hay consenso, mayoría simple de PIs de sitio activos, con la posición disidente registrada.
- **Cambios a este documento de gobernanza**: requieren acuerdo del comité directivo y quedan versionados en el historial del repositorio.

Toda decisión sustantiva se registra como *issue*/acta en el repositorio (trazabilidad pública).

## 4. Versionado del instrumento

- El instrumento es un **bien común versionado**. Versión actual: **v0.1 (pre-calibrada)**.
- La **v0.2** se consolida con aportes del consorcio (rondas *think-aloud* por sitio + síntesis); a partir de v0.2 existe una **línea base compartida** que todos los sitios aplican para garantizar comparabilidad.
- Ningún sitio modifica el instrumento común por su cuenta: las **adaptaciones locales** (traducción, ajuste cultural) siguen la [guía de adaptación](instrument/translation_adaptation_guidelines.md) y se documentan; los **cambios al núcleo común** pasan por el comité directivo.

## 5. Datos

- Cada sitio es **propietario de sus datos crudos** y responsable de su resguardo conforme a la normativa de su país.
- Cada sitio comparte con el consorcio **datos armonizados y anonimizados** según la [plantilla](data/data_template.csv) y el [diccionario](data/data_dictionary.md).
- El **conjunto agregado (*pooled*)** se gobierna por el comité directivo: acceso, uso, embargo previo a publicación y depósito final (repositorio abierto con DOI tras la publicación principal).
- No se comparten datos personales identificables en ningún caso (ver [ETHICS.md](ETHICS.md)).

## 6. Productos y autoría

Los productos del consorcio (artículo de validación multi-sitio, materiales del instrumento, pre-registro) se rigen por [AUTHORSHIP.md](AUTHORSHIP.md). Regla esencial: **contribución metodológica genuina (aplicar el protocolo común + aportar datos armonizados) = co-autoría**.

## 7. Adhesión y salida

- **Adhesión:** expresión de interés → aceptación de esta gobernanza, [AUTHORSHIP.md](AUTHORSHIP.md) y [ETHICS.md](ETHICS.md) → alta como sitio.
- **Salida:** un sitio puede retirarse en cualquier momento; los datos ya aportados al *pooled* permanecen salvo objeción ética sobrevenida, en cuyo caso se acuerda su tratamiento con el comité.

## 8. Conflicto de intereses y conducta

Las decisiones se toman en función del mérito científico. Se aplica el [Código de Conducta](CODE_OF_CONDUCT.md). Disputas no resueltas se median en el comité directivo.

---

*Esta gobernanza es deliberadamente ligera: privilegia la comparabilidad del protocolo común y la equidad en la autoría, con el mínimo de estructura necesaria. Crecerá solo lo que la red necesite.*
