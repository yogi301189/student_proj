pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yogi301189/student_proj.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t student-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop student-app || true
                docker rm student-app || true
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 80:5000 --name student-app student-app'
            }
        }
    }
}
