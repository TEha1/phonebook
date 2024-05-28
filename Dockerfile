FROM python:3.10-slim

WORKDIR /app

# Install PostgreSQL client libraries
RUN apt-get update && apt-get install -y gcc python3-dev libpq-dev

COPY requirements.txt requirements.txt
COPY .env.example .env
RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
