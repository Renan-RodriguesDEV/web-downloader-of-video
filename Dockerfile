# De onde o dockerfile pegará a imagem base
FROM python:3.12-alpine

# Pasta de trabalho principal do container
WORKDIR /app

# Arquivos copiados inicialmente para o container (geralmente os de configuração e dependências)
COPY requirements.txt requirements.txt

# Primeiro comando executado no container, instalando as dependências do projeto
# --no-cache-dir evita o cache de pacotes, economizando espaço
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto para o container
COPY . .

# Configuração para garantir que não haja timeout nas requisições
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py
ENV GUNICORN_CMD_ARGS="--timeout 120 --workers 2"

# Expondo a porta 5000, que é a porta padrão do Flask
EXPOSE 5000

# Comando para iniciar a aplicação Flask, este será executado quando o container iniciar
CMD ["python", "app.py"]