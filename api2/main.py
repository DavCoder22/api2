from fastapi import FastAPI
import openai


# Configurar la conexión a Azure Cosmos DB
client = MongoClient("<connection_string>")
db = client["mydatabase"]
collection = db["inverted_texts"]

# Crear una instancia de la aplicación FastAPI
app = FastAPI()

# Definir una ruta POST para invertir el texto y guardarlo en Azure Cosmos DB


# Ejecutar la aplicación

