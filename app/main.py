from fastapi import FastAPI, UploadFile, File, HTTPException
from app.utils.pdf_parser import extract_text_from_pdf
from app.services.ai_service import analyze_text_with_gemini
import shutil
import os

app = FastAPI(
    title="DocuMind API",
    description="API Backend para análisis de PDFs con Inteligencia Artificial"
)

@app.post("/upload", tags=["Análisis"])
async def upload_pdf(file: UploadFile = File(...)):
    # Verificación básica de extensión
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="El archivo debe ser un PDF")

    temp_path = f"temp_{file.filename}"
    
    try:
        # Guardar archivo temporalmente
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # 1. Extraer texto del PDF
        content = extract_text_from_pdf(temp_path)
        
        if not content.strip():
            raise HTTPException(status_code=400, detail="No se pudo extraer texto del PDF (¿está vacío o es solo imagen?)")

        # 2. Analizar con la nueva librería de IA
        ai_analysis = analyze_text_with_gemini(content)
        
        return {
            "status": "success",
            "filename": file.filename,
            "analysis": ai_analysis
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    
    finally:
        # Siempre borrar el archivo temporal, pase lo que pase
        if os.path.exists(temp_path):
            os.remove(temp_path)

@app.get("/", tags=["General"])
async def root():
    return {"message": "DocuMind API activa. Ve a /docs para probarla."}
