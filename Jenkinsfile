pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
		sh 'pip install pytest'
                sh 'pytest Docker/app.py'
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
            echo 'This didnt work'
        }
        changed {
            echo "Change"
        }
    }
}
