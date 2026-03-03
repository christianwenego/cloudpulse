pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Récupération du code depuis GitHub...'
                git url: 'https://github.com/christianwenego/cloudpulse.git',
                    branch: 'main'
            }
        }

        stage('Tests unitaires') {
            steps {
                echo 'Lancement des tests pytest...'
                sh '''
            cd app
            pip install -r requirements.txt -q
            pytest test.py -v
        '''
            }
        }

        stage('Build Docker') {
            steps {
                echo 'Construction de l image Docker...'
                sh 'docker build -t cloudpulse-app -f docker/Dockerfile app/'
            }
        }

        stage('Test sécurité Trivy') {
            steps {
                echo 'Scan de sécurité de l image...'
                sh '''
                    docker run --rm \
                    -v /var/run/docker.sock:/var/run/docker.sock \
                    aquasec/trivy:latest image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    cloudpulse-app
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Déploiement de l application...'
                sh '''
                    docker stop cloudpulse-api || true
                    docker rm cloudpulse-api || true
                    docker run -d \
                        --name cloudpulse-api \
                        --restart unless-stopped \
                        -p 5000:5000 \
                        cloudpulse-app
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline réussi ✅ Application déployée'
        }
        failure {
            echo 'Pipeline échoué ❌ Vérifier les logs'
        }
    }
}
