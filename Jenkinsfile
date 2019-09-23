pipeline {
  agent { dockerfile true }
  stages {
    stage('Test') {
      steps {
        sh 'python --version && pwd && ls -la'
        sh 'pyflakes Docker/app.py'
        sh 'echo tesssssssst'
        sh 'python Docker/test.py'
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
