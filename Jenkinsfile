pipeline {
    agent {label 'agent-eg'}
    stages {
       
        stage('Building') {
            steps {
                // sh 'docker build -t test_test_test .'
                sh """
                docker-compose build
                docker-compose up -d
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
      post {
      always {
          sh "docker-compose down || true"
      }

    }
}
