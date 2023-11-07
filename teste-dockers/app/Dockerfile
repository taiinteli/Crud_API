# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho
WORKDIR /app

# Copie o código-fonte do aplicativo para o contêiner
COPY . .

# Instale as dependências do aplicativo
RUN pip install -r requirements.txt

# Exponha a porta que o aplicativo Flask usará
EXPOSE 80

# Inicie o aplicativo Flask
CMD ["python", "app.py"]
