pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'sudo apt-get update && apt-get upgrade -y'
                sh 'sudo apt-get install python'
                sh 'python --version && whoami'
		sh 'pip --cache-dir /home/ubuntu/.cache install pytest'
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
