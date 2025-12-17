# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume
  fastapi-db

### Create the volume
 docker volume create fastapi-db
```bash

```

### Seed the volume (via Docker Desktop)
import "C:\Users\ariel\Downloads\shopping_list (1) (1).tar"

```bash

```

## Server 1

### Build the image
 docker build -t shopping-server1:v1 . 
```bash

```

### Run the container
docker run -p 8000:8000 -v fastapi-db:/app/data shopping-server1:v1
```bash

```

## Server 2

### Build the image
 docker build -t shopping-server2:v1 . 

```bash

```

### Run the container
docker run -p 8000:8000 -v fastapi-db:/app/data shopping-server2:v1

```bash

```

