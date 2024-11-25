# prometheus-practice
This is a repo that used to practice prometheus & Grafana.

## Requirement
* Helm Chart version 3+
* Two hlem repo install
    
    1.  https://github.com/prometheus-community/helm-charts/tree/kube-prometheus-stack-66.2.1
    2. https://github.com/bitnami/charts/tree/main/bitnami/redis
* MacOS Docker Desktop kubernetes 

## Deployment
1. Kube prometheus Stack
```bash
$ make prom-install
```
2. Redis Sentinel Cluster
```bash
$ make redis-install
```
3. Start Mock data to redis app
```bash
# Start build app docker image
$ make docker-build
# Start app as a pod
$ make start-app 
```