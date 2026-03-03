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

        stage('Vérification') {
            steps {
                echo 'Vérification des fichiers...'
                sh 'ls -la'
                sh 'cat app/requirements.txt'
            }
        }

        stage('Build Docker') {
            steps {
                echo 'Construction de l image Docker...'
                sh 'docker build -t cloudpulse-app -f docker/Dockerfile app/'
            }
        }

        stage('Test') {
            steps {
                echo 'Test de l application...'
                sh 'docker run --rm cloudpulse-app python -c "import flask; print(flask.__version__)"'
            }
        }

    }

    post {
        success {
            echo 'Pipeline réussi ✅'
        }
        failure {
            echo 'Pipeline échoué ❌'
        }
    }
}