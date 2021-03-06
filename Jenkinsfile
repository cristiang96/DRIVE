pipeline {
    
    agent {label 'agent-eg'}
    
    environment {
        BUILD_NUMBER = "0.3"
        PROJECT_PREFIX = "TASK-SCHED"
        PROJECT_IMAGE = "${env.PROJECT_PREFIX}:${env.BUILD_NUMBER}"
        PROJECT_CONTAINER = "${env.PROJECT_PREFIX}-${env.BUILD_NUMBER}"
        IMAGE_NAME = "testing123"
        PACKAGE_MONGO = "mongodb"
        PACKAGE_REDIS = "redis-server"
        NEXUS_IP_PORT = "10.28.108.180:8123"
    }
    
    stages {
        stage("Prepare Environment") {
            steps {
                sh """sudo apt-get update
                    sudo apt-get -y install python3.8
                    sudo apt-get -y install python3-pip
                    sudo apt-get -y install python3-virtualenv
                    python3 -m venv \$WORKSPACE/venv
                    source \$WORKSPACE/venv/bin/activate
                    pip3 install -r requirements.dev.txt
                    pip3 install tox
                    pip3 install wheel
                    sudo apt-get -y install tox
                        
                    PKG_OK=\$(dpkg-query -W --showformat='\${Status}\\n' \${PACKAGE_MONGO}|grep "install ok installed")
                    echo Checking for \${PACKAGE_MONGO}: \${PKG_OK}
                    if [ "" = "\${PKG_OK}" ]; then
                        echo "Not found: \${PACKAGE_MONGO}... Setting up \${PACKAGE_MONGO}."
                        sudo apt-get --y install \${PACKAGE_MONGO} 
                    fi 
                    PKG_OK=\$(dpkg-query -W --showformat='\${Status}\\n' \${PACKAGE_REDIS}|grep "install ok installed")
                    echo Checking for \${PACKAGE_REDIS}: \${PKG_OK}
                    if [ "" = "\${PKG_OK}" ]; then
                        echo "Not found: \${PACKAGE_REDIS}... Setting up \${PACKAGE_REDIS}."
                        sudo apt-get --y install \${PACKAGE_REDIS} 
                    fi  """
            }
        }
        stage('UnitTests') {
            steps {
                sh """source \$WORKSPACE/venv/bin/activate
                      tox -vvv """
            }
        }
        /*
        stage('Static code analysis') {
            steps {
                script {
                    // SonarQube Scanner Installation name = sonarqube-scanner-at
                    // Get the directory path where SonarQube Scanner
                    def scannerHome = tool 'sonarqube-scanner-at'
                    // SonarQube Server name = sonarqube-automation
                    withSonarQubeEnv('sonarqube-automation') {
                    // Set parameters to the sonar-scanner binary and run it
                        sh """${scannerHome}/bin/sonar-scanner \
                        -Dsonar.projectName=$PROJECT_PREFIX \
                        -Dsonar.projectKey=$PROJECT_PREFIX \
                        -Dsonar.sources=."""
                    }
                }
             }
        }
        
        stage("Building with Docker") {
            steps {
                // sh 'docker build -t test_test_test .'
                sh """
                docker-compose build """
                // sh "docker-compose up -d"
            }
        }
        
        stage('Promote Image') {
            steps{
                script {
                        withCredentials([usernamePassword(
                          credentialsId: 'nexus_eg_credentials',
                          usernameVariable: 'USERNAME',
                          passwordVariable: 'PASSWORD'
                        )]) {

                          sh """
                            docker login -u $USERNAME -p $PASSWORD \${NEXUS_IP_PORT}
                            docker tag \${IMAGE_NAME}:\${BUILD_NUMBER} \${NEXUS_IP_PORT}/app:latest
                            docker push \${NEXUS_IP_PORT}/app:latest
                          """
                        }
                    }
                }
            }
    */
    }
    post {
        always {
            echo "DONE!!!"
            // sh "docker-compose down || true"
            }
        }
}
