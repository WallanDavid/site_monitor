# Imagem base
FROM python:3.10-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão do Dash
EXPOSE 8050

# Comando padrão
CMD ["python", "main.py"]
