# prometheus-practice
This is a repo that used to practice prometheus & Grafana.

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