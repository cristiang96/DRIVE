pipeline {
    agent {label 'agent-eg'}
    stages {
        stage('Example Build') {
            steps {
                sh """
                // docker build -t test_test_test .
                sudo docker-compose build"
                sudo docker-compose up -d"
                """
                echo 'Hello, Maven'
            }
        }
        stage('Example Test') {
            steps {
                echo 'Hello, JDK'
            }
        }
    }
}
