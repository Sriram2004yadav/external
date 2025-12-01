pipepline{
    agent any

    stages {
        stage('pull') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                bat 'python -m py_compile calculator.py'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'calculator.py', fingerprint: true
            }
        }
    }
}
