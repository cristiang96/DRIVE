pipeline {
    agent any
    stages {
        stage('Example Build') {
            steps {
                sh """
                docker build -t test_test_test .
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
