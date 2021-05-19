node {
  checkout scm
  environment {
        PATH = "$PATH:/usr/local/bin/docker-compose"
    }
    stages {
        stage("Building") {
            steps {
                sh "docker-compose up"
                echo "CREATED"
            }
        }
    }
}
