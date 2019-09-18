up:
	@docker-compose up -d
	@echo "Jenkins Password is ..."
	@docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

down:
	@docker-compose down -v
