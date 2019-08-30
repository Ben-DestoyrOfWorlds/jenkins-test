pipeline {
    agent none
    stages {
      stage('Initialize') {
          steps {
          sh 'ls -la'
          }
        }
        stage('Test') {
        post {
            always {
                echo 'This ran'
            }
            success {
            echo 'This worked'
            }
            failure {
                echo 'This didnt work'
            }
            changed {
                echo "Change"
            }
        }
        }
    }
}
