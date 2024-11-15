# Car Price Prediction

## Instruções para Buildar e Rodar o Container Docker

### Pré-requisitos

Certifique-se de que você tem o Docker instalado em sua máquina. Você pode baixar e instalar o Docker a partir do [site oficial](https://www.docker.com/get-started).

### Buildando o Container

Para buildar o container Docker, navegue até o diretório onde o arquivo `Dockerfile` está localizado e execute o seguinte comando:

```sh
docker build -t car-price-prediction .
```

### Rodando o Container

Após buildar o container, você pode rodá-lo com o seguinte comando:

```sh
docker run -p 8501:8501 car-price-prediction
```

Isso irá iniciar o container e mapear a porta 8501 do container para a porta 8501 da sua máquina local. Agora você pode acessar o aplicativo de previsão de preços de carros através do endereço `http://localhost:8501`.

### Observações

- Certifique-se de que a porta 8501 está disponível e não está sendo usada por outro serviço.
- Para parar o container, você pode usar o comando `docker stop <container_id>`.

Aproveite o uso do aplicativo de previsão de preços de carros!
