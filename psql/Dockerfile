FROM postgres:16.4-alpine

# Скопировать setup.sql в контейнер
COPY ./setup.sql /var/lib/postgresql/setup.sql

# Скопировать run.sh и setup.sh
COPY ./run.sh ./run.sh
COPY ./setup.sh /var/lib/postgresql/setup.sh

# Сделать скрипты исполняемыми
RUN chmod +x ./run.sh /var/lib/postgresql/setup.sh

# Команда по умолчанию (если нужно)
CMD ["./run.sh"]
