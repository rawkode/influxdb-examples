CLEAR=\033[0m
WHITEB=\033[1;37m

up:
	@echo -e "$(WHITEB)Preparing Cluster$(CLEAR)"
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
	@echo -e "$(WHITEB)Installing Helm$(CLEAR)"
	@helm init --wait
	@echo -e "$(WHITEB)Installing Consul (via Helm)$(CLEAR)"
	@helm upgrade --install consul stable/consul
	@echo -e "$(WHITEB)Installing Prometheus Exporters$(CLEAR)"
	@kubectl apply -f prometheus/exporters

clean:
	@kubectl delete -f . --recursive
	@helm ls | tail -n +2 | awk '{print $1}' | xargs helm delete --purge || true

init:
	minikube start --vm-driver=kvm2

purge:
	minikube delete
