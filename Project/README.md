## Compose Electricity Provider Application

### Use with Docker Environments

You can open this sample with Docker Desktop version 4.12 or later.


### Django application Electricity Provider in Development

Project structure:
```
.
├── docker-compose.yaml
├── .env 
├── electricity-provider
    ├── Dockerfile
    ├── requirements.txt
    ├── manage.py
    ├── init.sh
    ├── .env
    └── main
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
        

```

[_docker-compose.yaml_](docker-compose.yaml)
```
version: '3'
services:
  electricity-provider: 
    build: ./electricity-provider
    container_name: electricity-provider
    ports: 
      - '8000:8000'
    volumes:
      - ./electricity-provider:/app
    environment:
       WEB_DOCUMENT_ROOT: /app/electricity-provider
    networks:
      internal:
        ipv4_address: 10.0.1.60
    depends_on:
      - postgres_db
    links:
    - postgres_db
    
  postgres_db:
      image: postgres:16.0-alpine
      container_name: postgres_db
      hostname: postgres_db
      volumes:
        - postgres_data:/var/lib/postgresql/data
      environment:
        - POSTGRES_DB=${SQL_NAME}
        - POSTGRES_USER=${SQL_USER}
        - POSTGRES_PASSWORD=${SQL_PASSWORD}  
      ports:
        - '5432:5432'
      networks:
        internal:
          ipv4_address: 10.0.1.70

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin
    depends_on:
      - postgres_db
    ports:
      - 5555:80
    environment:
      - PGADMIN_DEFAULT_EMAIL=${PGADMIN_DEFAULT_EMAIL}
      - PGADMIN_DEFAULT_PASSWORD=${PGADMIN_DEFAULT_PASSWORD}
    restart: unless-stopped
    volumes:
        - postgres_data:/var/lib/postgresql/data
    networks:
      internal:
        ipv4_address: 10.0.1.80

volumes:
  postgres_data:
    driver: local


networks:
  internal:
    driver: bridge
    ipam: 
      config: 
        - subnet: 10.0.1.0/24

```

## Login-Data

Go to .env Directory

