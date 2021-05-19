pipeline {
    agent none
    stages {
        stage('Example Build') {
            agent { docker 'redis:latest' } 
            agent { docker 'mongo:latest' } 
            steps {
                echo 'Hello, Maven'
            }
        }
        stage('Example Test') {
            agent { label 'new' } 
            steps {
                echo 'Hello, JDK'
            }
        }
    }
}
