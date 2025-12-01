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
                echo 'test stage'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'calculator.py', fingerprint: true
            }
        }
    }
}
