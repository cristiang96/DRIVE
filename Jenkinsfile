pipeline {
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
