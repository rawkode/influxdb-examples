import hudson.plugins.git.*;

def scm = new GitSCM("https://github.com/rawkode/influxdb-examples.git")
scm.branches = [new BranchSpec("*/master")];

def flowDefinition = new org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition(scm, "./jenkins/jenkins/job/Jenkinsfile")

def parent = Jenkins.instance
def job = new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent, "Alpine Job")
job.definition = flowDefinition

parent.reload()
