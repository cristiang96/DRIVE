pipeline {
  environment {
        PATH = "$PATH:/usr/local/bin/docker-compose"
    }
  agent any
    stages {
        stage("Building") {
            steps {
                sh "docker-compose up"
                echo "CREATED"
            }
        }
    }
}
