FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt  # '--no-cache-dir' Evita armazenar cache desnecessário

COPY . .

EXPOSE 8000

# Inicia o servidor uvicorn, e usa a porta definida em PORT(Se houver) ou 8000 como porta padrão
CMD ["sh", "-c", "exec uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]  # 'sh -c' inicia um Shell para interpretar o comando '${PORT:-8000}'
