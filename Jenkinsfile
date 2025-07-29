pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
        PATH = "${HOME}/.local/bin:${env.PATH}"
        PYTHONPATH = "${HOME}/.local/lib/python3.10/site-packages"
    }

    stages {
        stage('Install Netmiko') {
            steps {
                sh '''
                    curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py
                    python3 get-pip.py --user
                    pip3 install --user netmiko
                '''
            }
        }

        stage('Validate Script') {
            steps {
                sh "python3 -m py_compile ${SCRIPT}"
            }
        }

        stage('Run Netmiko Script') {
            steps {
                sh "python3 ${SCRIPT}"
            }
        }

        stage('Post Check') {
            steps {
                echo "Pipeline completed. Devices configured."
            }
        }
    }
}
