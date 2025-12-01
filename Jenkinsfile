pipeline{
    agent any

    stages {
        stage('pull') {
            steps {
                checkout scm
            }
        }
        stage('test') {
            steps {
                bat 'python calculator.py'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'calculator.py', fingerprint: true
            }
        }
    }
}
