# Use a imagem base do Python
FROM python:3.9

# Defina o diretório de trabalho no container
WORKDIR /car-price-prediction

# Copie os arquivos de requisitos para o container
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o conteúdo do projeto para o diretório de trabalho
COPY . .

# Exponha a porta que o Streamlit usa
EXPOSE 8501

# Comando para rodar o aplicativo
CMD ["streamlit", "run", "app/index.py", "--server.port=8501", "--server.address=0.0.0.0"]