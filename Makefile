.PHONY: upgrade-install

upgrade-install:
	@helm upgrade --install -n prometheus -f kube_prom_stack/values.yaml --version 66.2.1 prometheus prometheus-community/kube-prometheus-stack