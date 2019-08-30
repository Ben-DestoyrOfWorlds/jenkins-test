node {
    stage('Initialize') {
        sh 'ls -la'
    }
    stage('Test') {
        sh 'echo test'   
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
