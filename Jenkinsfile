pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
        PIP_BIN = "${HOME}/.local/bin"
    }

    stages {
        stage('Install Netmiko') {
            steps {
                sh '''
                    python3 -m pip install --upgrade --user pip
                    python3 -m pip install --user netmiko
                '''
            }
        }

        stage('Validate Script') {
            steps {
                sh '''
                    export PATH=$PIP_BIN:$PATH
                    python3 -m py_compile ${SCRIPT}
                '''
            }
        }

        stage('Run Script') {
            steps {
                sh '''
                    export PATH=$PIP_BIN:$PATH
                    python3 ${SCRIPT}
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
