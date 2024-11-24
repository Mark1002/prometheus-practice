.PHONY: prom-install redis-install

prom-install:
	@helm upgrade --install -n prometheus -f kube_prom_stack/values.yaml --version 66.2.1 prometheus prometheus-community/kube-prometheus-stack

redis-install:
	@helm upgrade --install -n redis -f redis/values.yaml --version 20.3.0 redis oci://registry-1.docker.io/bitnamicharts/redis