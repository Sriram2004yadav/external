pipeline{
    agent any
    tools {
        maven 'Maven3.8.4'
        jdk 'JDK11'
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
        stahge('build') {
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
