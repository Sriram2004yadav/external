pipeline{
    agent any

    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                bat "python calculator.py"
            }
        }
        stage('archive') {
            steps {
                Archive
            }
        }
    }
}
