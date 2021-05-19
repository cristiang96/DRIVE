pipeline {
    agent {label 'agent-eg'}
    environment {
        BUILD_NUMBER = "0.9"
        PROJECT_PREFIX = "TASK-SCHED"
        PROJECT_IMAGE = "${env.PROJECT_PREFIX}:${env.BUILD_NUMBER}"
        PROJECT_CONTAINER = "${env.PROJECT_PREFIX}-${env.BUILD_NUMBER}"
    }
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
