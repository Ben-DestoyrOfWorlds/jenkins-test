pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
    post {
        always {
            echo 'This ran'
        }
        success {
          echo 'This worked'
        }
        failure {
            echo 'This didn't work'
        }
        changed {
            echo "Change"
        }
    }
}
