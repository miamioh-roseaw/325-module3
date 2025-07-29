pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Set Up Virtualenv') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Script in Venv') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python ${SCRIPT}
                '''
            }
        }
    }
}
