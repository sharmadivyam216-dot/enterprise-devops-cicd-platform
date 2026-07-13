pipeline {
    agent any

    environment {
        IMAGE_NAME = "divyamsh1316/enterprise-devops-app"
    }

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r app/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                cd app
                pytest
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:latest ./app
                docker tag $IMAGE_NAME:latest $IMAGE_NAME:${BUILD_NUMBER}
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                    docker push $IMAGE_NAME:latest
                    docker push $IMAGE_NAME:${BUILD_NUMBER}

                    docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Docker image successfully pushed to Docker Hub!'
        }

        failure {
            echo '❌ Pipeline failed.'
        }
    }
}