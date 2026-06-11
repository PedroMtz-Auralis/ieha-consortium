# Handoff de producción — Video explainer IEH-A (Auralis / ElevenLabs)

> Documento listo para pasar al pipeline de Auralis (Átomico/BAWI). Contiene el **guion de narración para ElevenLabs**, el **storyboard escena por escena**, la **lista de assets** y la **dirección de voz**. Idioma primario **español (MX)**; al final, notas para versión en inglés. Duración objetivo **~2:30**.

## 0. Ficha

| | |
|---|---|
| **Objetivo** | Que un investigador de acústica/urbanismo entienda el IEH-A en 2 minutos y quiera sumarse al consorcio. |
| **Audiencia** | Comunidad iberoamericana de acústica (FIA 2026) + difusión abierta. |
| **Tono** | Experto cercano, claro y directo (voz Auralis Lab); sereno, no alarmista. |
| **Salida** | YouTube (canal Auralis) + embebido en el repo. 1080p, subtítulos ES (y EN). |
| **CTA** | `github.com/PedroMtz-Auralis/ieha-consortium` + QR. |
| **Licencia** | CC BY 4.0; arte e ilustraciones (viñetas P2) con crédito Auralis Lab. |

## 1. Dirección de voz (ElevenLabs)

- **Voz:** femenina o masculina cálida, registro experto-cercano (alineada a la voz de marca Auralis: "dominio técnico sin jerga"). Modelo **multilingüe v2** (buena prosodia en español).
- **Ajustes sugeridos:** *Stability* ~50–60 (consistente pero con vida), *Similarity* ~75, *Style* bajo-medio. Ritmo pausado.
- **Pronunciación del acrónimo:** la **primera** vez decir el nombre completo —"el Índice de Erosión del Habitar Acústico"— y a partir de ahí **"el índice"**. **No** leer "IEH-A" como sigla (se mangonea en TTS). En pantalla sí aparece "IEH-A".
- **Pausas:** los puntos y las rayas (—) marcan respiración; los puntos suspensivos (…) crean una pausa más larga. Respetar el segmentado por escena.

## 2. Guion + storyboard (escena por escena)

> Para ElevenLabs: copia el bloque **NARRACIÓN** de cada escena (el texto entre comillas) como un segmento. El resto es para edición/montaje.

---

**ESC 1 — El gancho (0:00–0:22)**
- **NARRACIÓN:** "Imagina a alguien que duerme bien. Que no se dice estresado. Que, si le preguntas, te responde que ya se acostumbró al ruido… y, sin embargo, dejó de usar su patio. Selló sus ventanas. Ya no recibe visitas. Y piensa en mudarse."
- **VISUAL:** Viñeta 1 (Perfil 3: persona en calma, interior, ventana sellada, patio vacío afuera, arcos de sonido). Zoom lento.
- **TEXTO EN PANTALLA:** —(ninguno; dejar respirar la imagen)

**ESC 2 — La brecha (0:22–0:48)**
- **NARRACIÓN:** "La investigación del ruido urbano mira por dos ventanas. Una, la clínica: el sueño, el estrés. Otra, el paisaje sonoro: la calidad del entorno que se percibe. Entre las dos queda una zona ciega. La de esta persona: las escalas la declaran funcional, pero su mundo se ha encogido en silencio."
- **VISUAL:** Split conceptual (dos "ventanas"/logos abstractos) → transición a Viñeta 2 (habituación + huellas de erosión).
- **TEXTO EN PANTALLA:** "clínica" / "paisaje sonoro" → "la zona ciega"

**ESC 3 — El constructo (0:48–1:10)**
- **NARRACIÓN:** "A eso lo llamamos la contracción del mundo práctico. Y se puede medir. El Índice de Erosión del Habitar Acústico registra qué actividades se abandonaron, qué planes se alteraron, qué cuidados se simplificaron… por conducta, no por autoevaluación. Doce preguntas. Tres dimensiones."
- **VISUAL:** Viñeta 3 (cuidado que se reorganiza) → tarjeta limpia con las 3 dimensiones (Ocupaciones · Proyecciones · Cuidado).
- **TEXTO EN PANTALLA:** "IEH-A" · "Ocupaciones · Proyecciones · Cuidado" · "conducta, no autoevaluación"

**ESC 4 — El Perfil 3 (1:10–1:35)**
- **NARRACIÓN:** "Cruzado con las escalas clínicas, el índice define cuatro perfiles. El que importa es el tercero: clínicamente sano, pero con el habitar erosionado. Es la población que nadie está contando."
- **VISUAL:** Fig. de ortogonalidad (P3) — animar la aparición del cluster verde arriba-izquierda. Resaltar "Perfil 3".
- **TEXTO EN PANTALLA:** "Perfil 3 — clínicamente sano · habitar erosionado"

**ESC 5 — Por qué una red (1:35–2:02)**
- **NARRACIÓN:** "Pero qué cuenta como habitar, como cuidado, como vida cotidiana… cambia con la cultura y el territorio. Por eso este índice no se valida desde un solo lugar. Proponemos aplicarlo en muchas ciudades, con un mismo protocolo, para responder una pregunta de fondo: ¿mide lo mismo en poblaciones distintas?"
- **VISUAL:** Viñeta 4 (hero: corredor que contrae el habitar) → mapa con varias ciudades encendiéndose → Fig. de invarianza (P3).
- **TEXTO EN PANTALLA:** "¿mide lo mismo en contextos distintos?" · "validación distribuida"

**ESC 6 — La invitación / CTA (2:02–2:30)**
- **NARRACIÓN:** "El instrumento, su protocolo y sus materiales son abiertos. Cada equipo trabaja con su propia aprobación ética; quien aplica el protocolo y aporta datos, co-firma la validación. Si estudias el ruido en tu ciudad, esta es tu invitación. Te esperamos."
- **VISUAL:** Tarjeta final: logo Auralis Lab + URL del repo + **QR** grande. Créditos coordinación.
- **TEXTO EN PANTALLA:** "github.com/PedroMtz-Auralis/ieha-consortium" · "CC BY 4.0 · ética per-sitio · co-autoría por contribución" · "P. Martínez Cisneros · E. Sánchez Flores · Auralis Lab"

---

## 3. Lista de assets

| Asset | Origen |
|---|---|
| Viñetas 1–4 (y 5 opcional) | Generadas con `outreach/vignette_image_prompts.md` (motor de imágenes) |
| Figuras P3 (ortogonalidad, invarianza) | `outreach/projected_outcomes/figures/` |
| Logo Auralis Lab | `_brand_assets/` (Drive `01_Identidad`) |
| QR al repo | Generar apuntando a `https://github.com/PedroMtz-Auralis/ieha-consortium` |
| Música | Lecho instrumental sobrio, bajo, sin percusión agresiva (tono Átomico) |
| Tipografía en pantalla | Montserrat (títulos) + Noto Sans (cuerpo) — marca Auralis |
| Paleta | Morado `#432B63`, gris `#3A3A3A`, azul-grisáceo `#A0B4C8` |

## 4. Notas de cumplimiento (no negociables)

- Las viñetas se rotulan, en pantalla o créditos: **"Ilustración conceptual. No representa participantes reales."**
- Las figuras P3 conservan el rótulo **"ILUSTRATIVO · datos sintéticos"** en pantalla.
- Encuadre de **estudio de dos investigadores** (Auralis Lab); **sin** mención de tesis/doctorado ni de aval institucional; **sin** afirmar aprobación ética inexistente.

## 5. Versión en inglés

Regrabar la narración con la traducción EN (mismo arco). El one-pager (`outreach/one_pager_IEHA.md`) ya trae el texto base EN para derivar el guion. Subtítulos EN en la versión ES.
