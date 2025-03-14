# Usa una imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8000 para la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "icard.wsgi:application", "--bind", "0.0.0.0:8000"]
