pipeline {
  agent {node { label 'test-ci' } }
    stages {
        stage("Building") {
            steps {
                sh "docker-compose up"
                echo "CREATED"
            }
        }
    }
}
