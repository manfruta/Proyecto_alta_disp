#imagen
FROM python:3.8

#donde va a trabajar
WORKDIR /Servidor
# Copiar archivos necesarios   todo lo de la carpeta dockerfile(pc)/al contenedor
COPY . .

# Instalar dependencias de Python
RUN pip install -r requirements.txt

# Ejecutar script
CMD ["python", "app.py"]
