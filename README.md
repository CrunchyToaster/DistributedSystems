# DistributedSystems
This Repository contains a full-stack web-application for the Distributed Systems course. 

It consists of a NuxtJS frontend and a Django backend using a PostgreSQL database for storage.

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Prerequisites](#prerequisites)  
3. [Docker Images](#docker-images)
4. [Quickstart](#quickstart)  
   - [Docker](#docker)  
   - [Kubernetes](#kubernetes)  
5. [API](#api)  
   - [Base URL](#base-url)  
   - [Endpoints](#endpoints)  
6. [12 Factors](#12-factors) 

## Project Overview
- **Frontend**: Nuxt.js  
- **Backend**: Django+ Django REST Framework  
- **Database**: PostgreSQL via Docker

## Docker Images
Backend: 
```bash
ghcr.io/crunchytoaster/crunchytoaster-web:latest
```

Frontend:
```bash
ghcr.io/crunchytoaster/crunchytoaster-nuxt:latest
```

## Quickstart

### Docker
Run:
```bash
docker-compose up --build
```

```bash
docker compose run web python manage.py migrate
```

### Kubernetes
Make sure kind is installed and a cluster has been created before running these commands:
```bash
kubectl apply -f k8s/
```

```bash
kubectl port-forward svc/nuxt 3000:3000
```

```bash
kubectl port-forward svc/web 8000:8000
```

## API

#### Base URL:
`<backend-url>/items`

#### Endpoints:
| Method | Path | Description |
| ------ | --- | ---|
| GET    | `/items/` | List all items|
| POST | `/items/` |  Create or Update item by name |
| PUT | `/items/{id}/`|Update item by ID|
| DELETE | `/items/{id}/` | Delete an item by ID |

## 12 Factors
This project aligns with the 12 Factor App methodology to ensure portability, scalability and maintainability:

### I. Codebase
> One codebase tracked in revision control, many deploys

All Code is in a single repository

### II. Dependencies
> Explicitly declare and isolate dependencies

All dependencies are declared in `requirements.txt` and `package.json` 

### III. Config
> Store config in the environment

Environment specific settings are passes via environment variables

### IV. Backing Services
> Treat backing services as attached resources

Postgres runs as an attached service in Docker or Kubernetes

### V. Build, Release, Run
> Strictly separate build and run stages

Docker Compose and Kubernetes manifests separate build and run stages

### VI. Processes
> Execute the app as one or more stateless processes

The app runs as stateless processes managed by Docker or Kubernetes

### VII. Port Binding
> Export services via port binding

Backend running on port `8000` frontend on `3000`

### VIII. Concurrency
> Scale out via the process model

Multiple replicas or containers suppord scaling

### IX. Disposability
> Maximize robustness with fast startup and graceful shutdown

Fast startup and graceful shutdown

### X. Dev/prod Parity
> Keep development, staging, and production as similar as possible

Docker Compose and Kubernetes simulate production in development

### XI. Logs
> Treat logs as event streams

Logs are written to stdout for centralized collection

### XII. Admin Processes
> Run admin/management tasks as one-off processes

One-off management commands run via `python manage.py <command>`
