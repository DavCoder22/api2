from fastapi import FastAPI
from pymongo import MongoClient

# Configurar la conexión a Azure Cosmos DB
client = MongoClient("<connection_string>")
db = client["mydatabase"]
collection = db["inverted_texts"]

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta POST para invertir el texto y guardarlo en Azure Cosmos DB
@app.post("/invert")
def invert_text(data: dict):
    text = data.get("text", "")  # Obtener el valor del campo "text" del diccionario (si no existe, usar una cadena vacía)
    inverted_text = text[::-1]  # Invertir el texto

    # Guardar el texto invertido en Azure Cosmos DB
    document = {"text": inverted_text}
    result = collection.insert_one(document)
    document_id = str(result.inserted_id)

    return {"inverted_text": inverted_text, "document_id": document_id}

# Ejecutar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
