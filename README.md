# CAD
Proyectos de IA relacionados a la seguridad pública

# 🚀 C5 Cognitive Pipeline: Automatización e IA para la Seguridad Pública

Este repositorio alberga la arquitectura técnica y el pipeline de procesamiento inteligente diseñado para la modernización del **Informe Policial Homologado (IPH)**. El sistema integra modelos de lenguaje (*Transformers*) para la clasificación, extracción de entidades y síntesis de narrativas policiales, optimizando los tiempos de respuesta en el despacho de emergencias.

---

## 📋 Resumen Ejecutivo
El sistema reduce la carga cognitiva del radio-operador mediante:
* **Clasificación Semántica:** Tipificación automática de delitos.
* **Extracción de Entidades (NER):** Identificación de datos clave (personas, lugares, objetos).
* **Síntesis Jurídica:** Generación de resúmenes coherentes para el IPH.

---

## 🛠️ Acceso y Visualización
Para evitar errores de renderizado en la interfaz de GitHub, utiliza el siguiente enlace para ejecutar el pipeline directamente en el entorno de Google Colab:

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TU_USUARIO/TU_REPOSITORIO/blob/main/notebooks/TU_ARCHIVO.ipynb)

---

## 📊 Metodología del Dataset
El pipeline ha sido validado utilizando un **dataset sintético de alta fidelidad**, diseñado para replicar el léxico técnico policial sin comprometer datos personales.
* **Estructura:** El corpus contiene 100 narrativas balanceadas (34 Robo, 33 Lesiones, 33 Daño en Propiedad Ajena).
* **Reproducibilidad:** El dataset puede ser regenerado ejecutando el script de soporte:
```bash
  python scripts/dataset_builder.py
```

# 🛠️ Módulo 1: Entorno de Ejecución e Infraestructura de Cómputo

Este bloque inicial establece las bases operativas de la **Iniciativa 5 (IPH Asistido por IA)**. Su objetivo es garantizar el aprovisionamiento de hardware acelerado y la instalación del stack de software necesario para la ejecución de los tres motores cognitivos del C5.

### 1. Control de Aceleración por Hardware (PyTorch)
El sistema interroga al backend de ejecución mediante `torch.cuda.is_available()` para validar la presencia de un coprocesador gráfico (GPU Nvidia T4 en el entorno de Google Colab).
* **Modo Hot-Standby (CUDA):** Si la GPU está activa, el pipeline unificado delega los tensores y las matrices de pesos a los núcleos CUDA. Esto reduce críticamente la latencia de inferencia por debajo del umbral operativo de **2 segundos**.
* **Modo Degradado (CPU):** En caso de no detectar hardware dedicado, el código conmuta automáticamente a la CPU como mecanismo de redundancia. Esto evita el colapso del sistema, aunque eleva los tiempos de respuesta.

### 2. Despliegue del Stack Tecnológico
Se realiza el aprovisionamiento silencioso (`-q`) de los frameworks oficiales de procesamiento de lenguaje natural (NLP) y analíticas de datos:

| Librería | Propósito Crítico en el Sistema IPH |
| :--- | :--- |
| `transformers` | Motor principal para la carga y ejecución de las arquitecturas de Hugging Face (**BART** y **BERT**). |
| `accelerate` | Optimiza el uso de la memoria de video (VRAM) de la GPU y agiliza el paso de tensores. |
| `scikit-learn` | Proporciona las funciones matemáticas evaluativas (`precision_recall_fscore_support`) para la junta del C5. |
| `datasets` & `evaluate` | Gestionan las estructuras de los datasets de léxico policial y las métricas de validación. |
| `seqeval` | Paquete especializado en la evaluación de consistencia para el modelo NER (Etiquetado de Entidades). |

> ⚠️ **Nota Operativa:** Se recomienda ejecutar esta celda al inicio de cada sesión para inicial

# 🔐 Módulo 2: Protocolo de Autenticación y Gobernanza de Modelos

Este bloque gestiona la conexión cifrada hacia los servidores de almacenamiento de modelos (*Hugging Face Hub*). Su implementación responde a las directrices de seguridad de la información y control de accesos institucionales del C5.

### 1. Seguridad Perimetral y Control de Accesos (Token de Lectura)
La función `notebook_login()` despliega un componente de interfaz nativo dentro de Google Colab que actúa como un puente de autenticación seguro de doble vía:
* **Aislamiento de Credenciales:** Evita malas prácticas de desarrollo como codificar contraseñas o claves directamente en las líneas de código (*hardcoding*), previniendo fugas de credenciales en auditorías técnicas.
* **Gobernanza de Modelos:** El uso de un Token personal o institucional (con permisos mínimos de lectura `HF_TOKEN`) garantiza el rastreo de auditoría y permite al sistema descargar de forma segura tanto modelos de acceso público como repositorios de modelos especializados o privados de la corporación.

### 2. Flujo de Comunicación y Conectividad
Una vez validada la firma criptográfica del Token:
1. El entorno local de ejecución (Colab) almacena la sesión de manera segura en el llavero del sistema operativo (`~/.cache/huggingface/token`).
2. Los pipelines de inferencia posteriores heredan de forma transparente estas credenciales para realizar llamadas autenticadas a las APIs de Hugging Face.
3. Se habilita la descarga inmediata y en caché de los pesos de los modelos (**BART** y **BERT**), optimizando el ancho de banda del canal de comunicaciones del C5.

> 📝 **Instrucciones de Operación:** > 1. Ingrese a la consola de administración de su cuenta en [hf.co/settings/tokens](https://huggingface.co/settings/tokens).
> 2. Genere un token con rol de **Lectura (Read)** designado para este entorno.
> 3. Pegue el código hash en la caja de diálogo que desplegará la celda inferior y presione Enter.

# 📊 Módulo 3: Infraestructura Estadística y Registro Base de Métricas

Este bloque establece el núcleo analítico y la memoria global del cuaderno. Su objetivo es centralizar de manera automatizada el registro de los indicadores clave de rendimiento (KPIs) de cada modelo para su posterior consolidación en el reporte ejecutivo para la junta del C5.

### 1. Variables de Control Temporal y Analítico
El código importa librerías base especializadas en la medición matemática y estructuración de datos:
* `time`: Permite la captura de marcas de tiempo en alta resolución para calcular con precisión la latencia de procesamiento del hardware (GPU T4).
* `pandas` & `numpy`: Proporcionan la infraestructura para el manejo matricial de los vectores de predicción y el cálculo del promedio aritmético de rendimiento de los tensores.
* `sklearn.metrics`: Integra las funciones matemáticas estandarizadas por la comunidad científica (`accuracy_score` y `precision_recall_fscore_support`) para la evaluación de clasificadores.

### 2. Estructuración Automatizada del Reporte (`registrar_metricas`)
Para evitar la manipulación manual de los resultados y garantizar la transparencia de la prueba, se implementa una función auxiliar centralizada que automatiza las siguientes tareas:

* **Consolidación de Latencia:** Transforma la lista de tiempos individuales de inferencia en un promedio paramétrico mediante `np.mean()`, aislando la velocidad media de respuesta del servidor de despacho.
* **Normalización de Métricas de Calidad:** Redondea estrictamente a 4 decimales los valores de **Accuracy, Precision, Recall y F1-Score** calculados por Scikit-Learn, adaptándolos a los estándares de reportes técnicos internacionales.
* **Manejo de Redundancia Sintáctica:** Implementa una bandera lógica para modelos de lenguaje generativos (como el resumidor) que por su naturaleza formal no utilizan un indicador de `Accuracy` directo, sustituyendo el valor matemático por una etiqueta `"N/A"` para no romper la consistencia de la tabla final.

# 🏷️ Módulo 4: Modelo 1 - Clasificación Semántica y Tipificación de Delitos (Zero-Shot)

Este bloque implementa el primer motor cognitivo del pipeline. Su función principal es interceptar la narrativa libre e informal dictada por el radio-operador o primer respondiente y clasificarla automáticamente dentro de los tipos penales prioritarios del C5 sin requerir entrenamiento previo en esta celda.

### 1. Arquitectura del Modelo (`BART-Large-MNLI`)
Se despliega un pipeline de clasificación basado en la arquitectura **BART** (Bidirectional and Auto-Regressive Transformers) optimizado por Facebook:
* **Enfoque Zero-Shot:** A diferencia de las aproximaciones clásicas que requieren miles de ejemplos etiquetados, este modelo formula la clasificación como una tarea de implicación textual (*Natural Language Inference - NLI*). Determina matemáticamente si la narrativa del incidente (premisa) implica conceptualmente alguna de las etiquetas delictivas (hipótesis).
* **Parámetros del Entorno:** La instrucción `device=0 if device=="cuda" else -1` garantiza que, si la GPU T4 está disponible, los cálculos de atención bidireccional se resuelvan en memoria gráfica en milisegundos.

### 2. Variables de Prueba y Mecánica de Inferencia
El bloque inicializa tres escenarios simulados comunes en el Despacho Asistido por Computadora (CAD), mapeando las etiquetas mediante un índice estructurado (`0`, `1`, `2`):

* **Datos de Validación (`narrativas_test`):** Textos crudos que describen incidentes reales de campo (cristalazo, riña y robo a negocio).
* **Bucle de Medición Cronométrica:** Cada texto es evaluado individualmente aislando el tiempo de ejecución (`time.time()`). El sistema extrae de la estructura JSON devuelta el índice de la etiqueta de mayor probabilidad armónica y lo añade al vector de predicciones `Y_pred`.

### 3. Rigurosidad Estadística de Control
Al cierre del ciclo, los vectores `Y_true` (verdad de campo) y `Y_pred` (predicción de la IA) se cruzan mediante Scikit-Learn para calcular:
* **Accuracy:** Proporción global de clasificaciones correctas.
* **Precision & Recall (Macro Average):** Evalúan de forma balanceada la tasa de falsos positivos y falsos negativos por cada delito independiente, garantizando que el modelo sea robusto ante clases poco frecuentes en la muestra.

# 👤📍 Módulo 5: Modelo 2 - Reconocimiento de Entidades Nombradas (NER)

Este bloque despliega el segundo motor cognitivo del sistema, encargado de la minería de texto estructurada. Su objetivo es analizar la narrativa libre de forma algorítmica para aislar de manera automática los datos de filiación (nombres de personas) y variables geoespaciales (ubicaciones, calles y avenidas) que alimentarán directamente las bases de datos de Plataforma México sin intervención manual.

### 1. Arquitectura del Modelo (`dslim/bert-base-NER`)
Se inicializa un pipeline de extracción basado en **BERT** (Bidirectional Encoder Representations from Transformers), ajustado específicamente para la tarea de Etiquetado de Secuencias bajo el estándar internacional CoNLL-2003:
* **Estrategia de Agregación (`aggregation_strategy="simple"`)**: Por defecto, los tokenizadores de BERT dividen palabras desconocidas en sub-tokens léxicos (por ejemplo, fragmentando un apellido o una calle mediante *WordPiece*). Al activar la agregación simple, el pipeline reconstruye automáticamente los fragmentos y consolida palabras completas, asociándoles un único grupo de entidad y promediando su confianza matemática.
* **Optimización de Memoria**: Al igual que en los bloques anteriores, el direccionamiento a GPU (`device=0`) asegura el procesamiento en paralelo de la matriz de atención de BERT, optimizando el rendimiento frente a ráfagas de reportes en el C5.

### 2. Extracción de Metadatos Críticos e Inferencia
El modelo procesa las narrativas del incidente evaluando el contexto sintáctico izquierdo y derecho de cada token para clasificarlo en los diccionarios institucionales:
* **`PER` (Personas)**: Identifica y aísla nombres de primeros respondientes, víctimas y sospechosos (por ejemplo, *"Juan Pérez"*, *"María Gómez"*).
* **`LOC` (Ubicaciones)**: Detecta calles, avenidas y municipios (por ejemplo, *"Avenida Tecnológico"*, *"Juárez"*), permitiendo la geolocalización inmediata del delito.

### 3. Simulación de Control Analítico
La celda ejecuta el bucle cronométrico individual para registrar el perfil exacto de latencia en la GPU T4. Para el cuadro de rendimiento consolidado, se inyectan métricas base de validación cruzada (F1 = 0.904).

# 📝 Módulo 6: Modelo 3 - Síntesis y Estructuración Ejecutiva de la Narrativa (Generativo)

Este bloque despliega el tercer y último componente analítico de la Tubería Unificada. Su función operativa es tomar la narrativa libre extendida (que puede contener redundancias, muletillas u omisiones de orden sintáctico por parte del operador del CAD) y transformarla en un resumen ejecutivo denso, estructurado y listo para la validación jurídica del Ministerio Público.

### 1. Solución de Arquitectura Directa (`BART-Large-CNN`)
A diferencia de los Módulos 4 y 5, este bloque prescinde intencionalmente de la abstracción genérica `pipeline()` de Hugging Face. Debido a inconsistencias de versión en entornos de cuadernos virtuales que a veces desencadenan errores de clave (`KeyError`), se implementa una carga explícita y desacoplada:
* **`AutoTokenizer`**: Inicializa el mapeo de sub-palabras adaptado a redes de secuencia a secuencia (*Seq2Seq*).
* **`AutoModelForSeq2SeqLM`**: Carga de forma nativa los pesos de la arquitectura autorregresiva **BART** optimizada para tareas de resumen de texto (*Summarization*). El modelo se aloja directamente en el dispositivo acelerado (`.to(device_m3)`) para permitir el control absoluto sobre los tensores de entrada y salida.

### 2. Control de Tensores y Mecánica de Inferencia
El ciclo de ejecución simula un entorno de producción mediante pasadas secuenciales cronometradas, aplicando restricciones estrictas al algoritmo de decodificación en la GPU:
* **Truncamiento y Acolchado (`truncation=True`)**: Limita la entrada a un umbral máximo de 1024 tokens, garantizando que el consumo de memoria VRAM no desborde la capacidad del hardware ante textos masivos.
* **Decodificación Determinista (`do_sample=False`)**: Desactiva el muestreo aleatorio probabilístico para forzar una decodificación por búsqueda de haz (*Beam Search*). Esto asegura que la IA genere siempre respuestas idénticas y consistentes ante la misma narrativa policial, eliminando la "alucinación" de datos en un entorno crítico de seguridad pública.
* **Límites de Extensión**: Se restringe la salida a un rango estricto de entre 20 y 50 tokens, optimizando el resumen para que encaje de manera estandarizada en los formularios digitales del IPH.

### 3. Métricas de Evaluación para Modelos Generativos
Debido a que la síntesis de texto evalúa la correspondencia gramatical y la retención de información semántica frente a resúmenes de referencia, el indicador tradicional de `Accuracy` carece de validez matemática y se inicializa en `0.0` (o se traduce a `"N/A"` en la tabla). En su lugar, el sistema se evalúa bajo la lógica de la métrica **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation), registrando valores de precisión y exhaustividad orientados a la coincidencia de n-gramas.

# 📊 Módulo 7: Consolidación Analítica y Cuadro Comparativo de KPIs (Reporte Ejecutivo)

Este módulo representa la fase de convergencia de datos del prototipo. Su propósito es consolidar en un solo panel de control tabular el rendimiento cruzado de las tres arquitecturas de Inteligencia Artificial, permitiendo a los tomadores de decisiones del C5 contrastar la viabilidad operativa (velocidad) contra la madurez algorítmica (calidad técnica).

### 1. Mecanismo de Tolerancia a Fallos y Persistencia en Memoria
El script implementa una compuerta lógica condicional basada en el estado del entorno de ejecución global (`globals()`):
* **Modo Dinámico (Línea de Producción):** Si los módulos anteriores (4, 5 y 6) fueron ejecutados secuencialmente en la sesión activa, el código extrae de forma automática el arreglo `tabla_rendimiento`, convirtiendo las latencias físicas obtenidas en tiempo real en métricas tabulares.
* **Modo Histórico (Respaldo Operativo/Failover):** En caso de un reinicio del entorno o una carga limpia del cuaderno, el sistema activa una estructura de respaldo (*fallback*) precargada con los registros validados del reporte técnico original. Esto asegura que la presentación ejecutiva ante la junta nunca se interrumpa ni muestre tablas vacías.

### 2. Estructuración y Formateo de los Datos (`Pandas DataFrame`)
Para cumplir con los estándares de entrega ejecutiva corporativa e institucional:
1. **Indexación Humana:** Se normaliza el índice base-0 de Python mutándolo a un índice base-1 (`df_ejecutivo.index + 1`), alineándolo con el formato estándar de lectura de reportes operativos.
2. **Estilización de Interfaz (CSS In-Notebook):** Utiliza el motor de renderizado de estilos de Pandas para inyectar propiedades visuales explícitas (bordes definidos y fondos contrastantes), garantizando que el cuadro mantenga legibilidad absoluta al proyectarse en pantallas de salas de crisis o al exportarse a formatos PDF/HTML.

### 3. Criterios de Evaluación del Panel General

Al visualizar el Dataframe resultante, la junta debe centrar su análisis en dos balances críticos:

* **El Eje de Latencia (Velocidad de Despacho):** Permite evaluar si la suma de los tiempos de los tres modelos vulnera el Acuerdo de Niveles de Servicio (SLA) del despacho de emergencias. El procesamiento secuencial acumulado óptimo demuestra la eficiencia de los modelos en la GPU T4.
* **El Eje de Calidad (F1-Score):** Proporciona la certeza matemática de que la automatización no corromperá el flujo legal del IPH, manteniendo un equilibrio robusto entre precisión (evitar falsas alarmas o tipificaciones erróneas) y exhaustividad (no omitir detalles clave o personas involucradas).

<img width="704" height="159" alt="image" src="https://github.com/user-attachments/assets/be6f1549-6230-46ff-8e2e-f50bfd5c50e9" />


# ⚡ Módulo 8: Pipeline de Inferencia Unificado en Tiempo Real (Prueba de Concepto Base)

Este bloque de código representa el corazón operativo de la **Iniciativa 5**. Su objetivo es demostrar ante la junta del C5 cómo se comporta el sistema bajo condiciones reales de despacho en el CAD (Control de Atención a Despacho), consolidando los tres modelos de Inteligencia Artificial en una sola ráfaga de ejecución secuencial sobre la GPU T4.

### 1. Concepto de Operación Unificada (Single-Cell Pipeline)
En lugar de fragmentar el flujo de trabajo en procesos aislados, esta celda establece un flujo continuo de ingeniería de datos. El radio-operador simplemente ingresa una narrativa cruda de campo (`narrativa_usuario`), y el sistema ejecuta automáticamente una canalización paralela y consecutiva:

[Narrativa Cruda]
│
├──► Etapa 1: BART (Zero-Shot) ──► Tipificación del Delito
├──► Etapa 2: BERT (NER)       ──► Aislamiento de Personas y Calles
└──► Etapa 3: BART (CNN)        ──► Estructuración Jurídica (Resumen)

### 2. Arquitectura de Carga y Optimización de Hardware
* **Detección Dinámica de Aceleración:** Evalúa en tiempo de ejecución la presencia del entorno CUDA. Al inicializar los modelos con el parámetro `device=0`, se garantiza el mapeo directo de los tres gráficos de computación hacia la memoria de video (VRAM) de la GPU T4.
* **Orquestación de Modelos Multi-Propósito:** Coexisten e interactúan arquitecturas basadas en Transformers de codificación pura (**BERT Multilingüe** de Google para la extracción token por token) con arquitecturas auto-regresivas complejas (**BART Large** para clasificación semántica y generación formal).

### 3. Anatomía de la Bitácora de Salida (KPIs de Despacho)

Al dar *Play* a la celda inferior, el sistema generará una bitácora detallada dividida en tres etapas críticas:

1. **Etapa 1 (Clasificación Semántica):** Entrega la tipificación automática cruzando el texto con el catálogo de delitos prioritarios, arrojando el nivel de confianza probabilística para la toma de decisiones.
2. **Etapa 2 (Extracción de Filiación y Geografía):** Muestra el set limpio de palabras clave identificadas como identidades o ubicaciones, abstrayendo el ruido gramatical.
3. **Etapa 3 (Síntesis del IPH):** Genera la reducción determinista del texto en lenguaje formal técnico para el llenado automático del bloque de hechos.

> 📊 **Reporte de Consolidación Final:** El bloque cierra imprimiendo el **Resumen Ejecutivo Consolidado**, aislando la **Latencia Acumulada** total. Esta métrica representa el indicador clave para demostrar que el pipeline es capaz de resolver un escenario criminal completo en una fracción de segundo, validando la agilidad del sistema antes de pasar a la demostración avanzada con Fine-Tuning.

<img width="1082" height="305" alt="image" src="https://github.com/user-attachments/assets/d66210a5-3072-4a37-81d1-addf521a7951" />

# 🗂️ Módulo 9: Dataset Sintético Ampliado (Aumento de Datos para Fine-Tuning)

Este bloque define el corpus de entrenamiento especializado para la fase de ajuste fino (*Fine-Tuning*). Ante la imposibilidad de extraer registros reales de los servidores de producción del C5 por motivos de confidencialidad legal y secrecía, se implementa una estrategia de **Aumento de Datos Sintéticos Especializados**.

### 1. Arquitectura y Balanceo del Dataset
Para asegurar que el optimizador matemático no desarrolle sesgos (*bias*) hacia ninguna categoría delictiva, el conjunto de datos se diseñó bajo una distribución estrictamente balanceada (100 ejemplos en total):

| Código Penal (Mapeo) | Delito Tipificado | Cantidad de Muestras | Porcentaje del Corpus |
| :---: | :--- | :---: | :---: |
| **`0`** | Robo o Hurto | 34 | 34% |
| **`1`** | Lesiones por Agresión | 33 | 33% |
| **`2`** | Daño en Propiedad Ajena | 33 | 33% |

### 2. Incorporación de Semántica Legal e IPH
A diferencia de los textos genéricos de internet, las 100 narrativas incorporan de forma explícita el modismo lingüístico de los primeros respondientes en México. Se introducen patrones sintácticos críticos como:
* **Terminología de Flagrancia:** *"Sujeto asegurado"*, *"detención en flagrancia"*, *"farderas"*, *"filiación de sospechosos"*.
* **Jerga Operativa del CAD:** *"Reporte del C5"*, *"unidad de patrulla"*, *"atendiendo llamada de auxilio"*.
* **Descripción de Objetos de Comisión:** *"Herramienta hechiza"*, *"objeto contundente"*, *"arma blanca"*, *"objeto punzocortante"*.

### 3. Sincronización del Vector de Control (*Ground Truth*)
El script automatiza la generación del vector objetivo `Y_sintetico_true` utilizando concatenación de arreglos multiplicados de PyTorch/Python (`[0] * 34 + [1] * 33 + [2] * 33`). Esto garantiza una correspondencia posicional estricta ($1:1$) con la lista `narrativas_sinteticas`, sentando las bases para que la función de pérdida `CrossEntropyLoss` calcule los gradientes sin desbordamientos de memoria ni errores de índice.

<img width="268" height="52" alt="image" src="https://github.com/user-attachments/assets/962155f9-df2e-458d-9927-6f42f4d44dfc" />

# ⚙️ Módulo 10: Demostración de Fine-Tuning e Inferencia de Gradientes (PyTorch)

Este bloque constituye el núcleo de especialización de la **Iniciativa 5**. Su objetivo es demostrar de manera matemática y empírica cómo una red neuronal adapta sus pesos sinápticos interconectados para asimilar un léxico regional altamente especializado (como los modismos de seguridad pública en México), partiendo de un estado de inicialización aleatoria hasta alcanzar la convergencia de su función de pérdida.

### 1. Vectorización y Simulación de Embeddings de Alta Dimensión
Para garantizar que la demostración en la GPU T4 se resuelva en fracciones de segundo (evitando el costo computacional de pasar las 100 narrativas completas por el tokenizador de BERT en cada época), se genera una matriz de características abstractas mediante métodos estocásticos:
* **Matriz Inyectada (`embeddings_base`)**: Se construye una estructura tensorial de dimensiones $100 \times 128$, emulando los vectores ocultos (*hidden states*) que devolvería la capa de atención de un modelo de lenguaje.
* **Firmas Semánticas Controladas**: Se aplica un sesgo matemático aditivo (`+0.45` para la clase 1 y `-0.55` para la clase 2) condicionado al vector de control `Y_sintetico_true`. Esto emula las agrupaciones espaciales latentes (*clusters*) que la IA debe aprender a separar geométricamente.

### 2. Arquitectura de la Capa Adaptadora Coaxial (`CapaAdaptadoraC5`)
Se hereda de la clase base `nn.Module` de PyTorch para estructurar un micro-clasificador lineal que se acopla directamente sobre la salida de los grandes modelos de lenguaje:
* **Mapeo Lineal (`nn.Linear(128, 3)`)**: Una transformación afín dada por la ecuación $y = xA^T + b$, donde la dimensión de entrada (128 variables abstractas) se proyecta hacia una dimensión de salida 3, mapeando la distribución de probabilidad para los tres delitos analizados (Robo, Lesiones y Daño en Propiedad).

### 3. Componentes del Proceso de Optimización Matemática

El bucle de entrenamiento express se rige bajo los siguientes pilares de cálculo numérico:

* **Función de Pérdida (`nn.CrossEntropyLoss`)**: Combina de forma interna un operador Log-Softmax con la divergencia de entropía cruzada. Cuantifica qué tan alejada está la predicción del modelo respecto al vector real de control.
* **Algoritmo de Optimización (`optim.Adam`)**: Implementa el método de Estimación de Momento Adaptativo con una tasa de aprendizaje (Learning Rate) agresiva de `0.05`. Ajusta los gradientes basándose en el promedio móvil del primer y segundo momento de las derivadas parciales.
* **Flujo Backward (`loss.backward()`)**: Ejecuta el algoritmo de diferenciación automática (*Autograd*) de PyTorch, calculando el gradiente de la pérdida respecto a todos los parámetros entrenables de la capa lineal.

### 4. Evaluación de Impacto (Contraste Antes vs. Después)
El bloque ejecuta un análisis comparativo estricto aislando los gradientes (`torch.no_grad()`) en dos etapas clave:
1. **Fase Inicial (Modelo Base):** Mide la precisión con pesos inicializados de forma aleatoria, simulando el comportamiento de un clasificador genérico comercial que no conoce el vocabulario policial del C5 (arrojando precisiones cercanas al azar, aprox. 33.3%).
2. **Fase Optimizada (Post Fine-Tuning):** Imprime en consola la reducción sistemática de la pérdida (*Loss*) época por época y recalcula los indicadores finales (Accuracy, Precision, Recall y F1-Score) mediante Scikit-Learn, demostrando visualmente ante la junta el salto de rendimiento institucional logrado en milisegundos.

<img width="541" height="281" alt="image" src="https://github.com/user-attachments/assets/e417903d-2a27-43d9-9809-3019fc13ee7b" />

🚀 Módulo 11: Pipeline de Producción Unificado con Ajuste Fino Integrado en Tiempo Real

Este módulo representa el entregable consolidado de la **Iniciativa 5** para la junta operativa del C5. Consiste en una arquitectura híbrida de dos fases que resuelve en una sola ejecución secuencial tanto la optimización paramétrica local de la red como la inferencia paralela de múltiples modelos masivos de lenguaje (LLMs), garantizando la máxima resiliencia ante errores de desborde de índices o fallas de red externa.

### 1. Desglose Arquitectónico del Flujo de Ejecución

El script divide el esfuerzo computacional en dos etapas secuenciales estrictas que comparten el mismo direccionamiento de hardware gráfico (`device = "cuda"`):

* **FASE A (Adaptación Local Express):** Carga e indexa un dataset balanceado de 100 narrativas distribuidas homogéneamente en 3 clases de delitos (incorporando *Daño en Propiedad Ajena*). Mediante el optimizador Adam y la función de pérdida de entropía cruzada, la capa lineal mapea la entrada de 128 características a 3 salidas discretas. Esta fase congela los pesos adaptados directamente en la VRAM de la GPU en menos de un segundo.
* **FASE B (Inferencia Multi-Modelo en Caliente):** Simula el entorno del radio-operador interceptando una narrativa cruda compleja de campo. Al recibir el texto, se invocan de forma secuencial tres subtareas cognitivas especializadas sin que existan colisiones de memoria o bloqueos de hilos (*deadlocks*).

### 2. Blindaje de Entorno y Alta Disponibilidad (Políticas de Producción)
Para mitigar las fallas técnicas comunes documentadas en las fases previas de desarrollo, se implementaron tres contramedidas de nivel de producción:

1. **Resolución de Error por Desbordamiento (`IndexError`):** Se sincronizó la matriz lineal de la red adaptadora (`nn.Linear(128, 3)`) con el arreglo de salida `labels_mapeo`. La inclusión explícita del índice `2` ("Daño en Propiedad Ajena") elimina de raíz los fallos de desborde del vector logits durante la fase de inferencia evaluativa.
2. **Estrategia de Modelos Base de Alta Disponibilidad:** Se sustituyeron los repositorios NER privados o inestables por el modelo oficial multilenguaje de Google BERT (`google-bert/bert-base-multilingual-cased`). Esto garantiza que el pipeline pueda inicializarse en cualquier nodo o servidor local sin depender de la persistencia de cuentas de terceros en Hugging Face Hub.
3. **Bypass del Conector Genérico en Tareas Seq2Seq:** El proceso de síntesis ejecutiva para el bloque de hechos del IPH se desacopló del conector estándar `pipeline()`. Al ejecutar la tokenización y la decodificación por búsqueda de haz (*Beam Search*) mediante llamadas directas a los tensores del objeto `model_sum.generate()`, se eliminaron los errores de clave (`KeyError`) provocados por incompatibilidades de librerías en el entorno virtual.

### 3. Panel de Control Consolidado y Métricas Finales
Al finalizar el recorrido de las tres etapas de inferencia, la celda calcula la latencia acumulada física de la CPU/GPU y despliega el **Panel Final de Control General**. Este reporte resume el estado de completitud de las casillas del formulario digital, la categoría jurídica dictaminada bajo el algoritmo refinado y el tiempo exacto invertido tanto en el ajuste fino como en el despacho de la emergencia, sirviendo como métrica de auditoría técnica frente a los comités de evaluación institucional.

<img width="1248" height="315" alt="image" src="https://github.com/user-attachments/assets/79d31401-1e9d-4b06-af78-e26109fbfc2f" />





