# DocuMind-API
A system for notes
=======
# 🚀 DocuMind API

Backend desarrollado con **FastAPI** que utiliza Inteligencia Artificial (**Google Gemini 2.0**) para analizar y resumir documentos PDF.

## ✨ Características
- Extracción de texto de PDFs mediante `PyPDF2`.
- Integración con modelos generativos de última generación.
- Documentación automática con Swagger UI.
- Arquitectura limpia y escalable.

## 🛠️ Instalación
1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Configurar tu `.env` con tu `GEMINI_API_KEY`.

## 🚀 Uso
Ejecutar el servidor:
```bash
uvicorn app.main:app --reload

