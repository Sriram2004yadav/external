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
                mvn clean Build
                javac Calculator.java
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.jar', fingerprint: true
            }
        }
    }
}
