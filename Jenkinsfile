pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
        VENV = 'venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Validate Script') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python -m py_compile ${SCRIPT}
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python ${SCRIPT}
                '''
            }
        }

        stage('Post Check') {
            steps {
                echo 'Pipeline completed. Devices configured.'
            }
        }
    }
}
