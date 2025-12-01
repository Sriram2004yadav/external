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
                mvn clean test
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
