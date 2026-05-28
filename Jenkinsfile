pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --break-system-packages -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --tb=short -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS - Tous les tests sont passés.'
        }
        failure {
            echo 'FAILURE - Des tests ont échoué.'
        }
    }
}
