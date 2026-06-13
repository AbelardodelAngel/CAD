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

* # 🛠️ Módulo 1: Entorno de Ejecución e Infraestructura de Cómputo

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





