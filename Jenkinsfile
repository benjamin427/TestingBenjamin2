pipeline {

    agent { docker {image 'python:3.12.1'}}

    stages {
        stage('Build') {
            steps {
                bat 'python --version'
                bat 'cd FrameworkAnalysis_2/'
                bat 'pip install -r requirements.txt'
                bat 'pytest'
            }
        }
    }
}