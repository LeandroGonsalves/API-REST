# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt e instale as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o resto dos arquivos da sua aplicação para o contêiner
COPY . .

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=main.py

# Exponha a porta em que a sua aplicação estará ouvindo
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
