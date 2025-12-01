pipeline{
    agent any
    tools {
        maven 'Maven3'
        jdk 'JDK17'
    }
    stages {
        stage('pull') {
            steps {
                checkout scm
            }
        }
        stage('test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('build') {
            steps {
                sh 'mvn package'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.jar', fingerprint: true
            }
        }
    }
}
