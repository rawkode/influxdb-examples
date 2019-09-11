import jenkins

server = jenkins.Jenkins('http://localhost:8080')
print(server.jobs_count())

my_job = server.get_job_config('Test')

def create_jenkins_jobs(number):
    job_names = ["Test" + str(x) for x in range(number)]
    [server.create_job(job, my_job) for job in job_names]
    [server.enable_job(job) for job in job_names]
    [server.build_job(job) for job in job_names]
    

def disable_jenkins_jobs(number):
    job_names = ["Test" + str(x) for x in range(number)]
    [server.disable_job(job) for job in job_names]