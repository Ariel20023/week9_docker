# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume
fastapi-db

### Create the volume
```bash
docker volume create fastapi-db

```

### Seed the volume (via Docker Desktop)

```bash
import "C:\Users\ariel\Downloads\shopping_list (1) (1).tar"

```

## Server 1

### Build the image
```bash
docker build -t shopping-server1:v1 . 

```

### Run the container
```bash
docker run -p 8000:8000 -v fastapi-db:/app/data shopping-server1:v1

```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 . 

```

### Run the container

```bash
docker run -p 8000:8000 -v fastapi-db:/app/data shopping-server2:v1

```

