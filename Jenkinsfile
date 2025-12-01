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
                bat "python calculator.py"
            }
        }
        stage('Archive') {
            steps {
                Archive
            }
        }
    }
}