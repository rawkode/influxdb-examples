CLEAR=\033[0m
WHITEB=\033[1;37m

up:
	@echo -e "$(WHITEB)Preparing Cluster$(CLEAR)"
	@bash -c "eval $(minkube docker-env); docker image build -t telegraf:master -f ./nodes/Dockerfile --build-arg VERSION_PREFIX="" --build-arg VERSION=master ./nodes"
	@kubectl apply -f setup/namespaces.yaml
	@kubectl apply -f setup
	@echo -e "$(WHITEB)Installing InfluxDB$(CLEAR)"
	@kubectl apply -f influxdb
	@echo -e "$(WHITEB)Installing Control Plane Monitoring$(CLEAR)"
	@kubectl apply -f control-plane
	@echo -e "$(WHITEB)Installing Node Monitoring$(CLEAR)"
	@kubectl apply -f nodes
	@echo -e "$(WHITEB)Installing Prometheus Monitoring$(CLEAR)"
	@kubectl apply -f prometheus
	@echo -e "$(WHITEB)Add deprecated "stable" Helm repo$(CLEAR)"
	@helm repo add stable https://kubernetes-charts.storage.googleapis.com
	@echo -e "$(WHITEB)Installing Consul (via Helm)$(CLEAR)"
	@helm upgrade --install consul stable/consul
	@echo -e "$(WHITEB)Installing Prometheus Exporters$(CLEAR)"
	@kubectl apply -f prometheus/exporters
	@echo -e "$(WHITEB) Deploying GitOps Bundle$(CLEAR)"
	@kubectl apply -f gitops-alerting/kubernetes
	@echo -e "$(WHITEB) If you have the InfluxDB v2 CLI locally, you can run: $(CLEAR)"
	@echo "INFLUX_TOKEN=secret-token INFLUX_ORG=InfluxData influx pkg -f ./gitops-alerting/influxdb/resources.yaml"
	@echo "Otherwise, please create the alerting task manually."

clean:
	@kubectl delete -f . --recursive
	@helm ls | tail -n +2 | awk '{print $1}' | xargs helm delete --purge || true

init:
	minikube start --vm-driver=kvm2

purge:
	minikube delete
