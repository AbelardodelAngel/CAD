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
