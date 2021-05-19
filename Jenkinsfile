node {
  checkout scm
  environment {
        PATH = "$PATH:/usr/local/bin/docker-compose"
    }

        stage("Building") {
          echo "$PATH"
                sh "docker-compose up"
                echo "CREATED"
     
        }
    
}
