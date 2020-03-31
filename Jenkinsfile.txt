node {  
    stage('Build') { 
        environment {
            PATH = "$PATH:/usr/local/bin"
        }
            sshagent(['ec2new']) {
			    def gitClone = 'git clone https://github.com/irahulgulati/newsapi.git'
				def changeDir = 'cd newsapi/'
				def dockerRun = 'docker-compose up' 
				sh "ssh -o StrictHostKeyChecking=no ec2-user@172.31.17.1 '${gitClone} && ${changeDir} && ${dockerRun}'"
			}
	}
}
