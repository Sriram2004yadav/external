pipeline{
    agent any
    tools {
        maven 'Maven3'
        jdk 'JDK1'
    }
    stages {
        stage('pull') {
            steps {
                checkout scm
            }
        }
        stage('test') {
            steps {
                maven clean test
                javac Calculator.java
                java Calculator
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.jar', fingerprint: true
            }
        }
    }
}
