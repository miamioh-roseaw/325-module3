pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
    }

    stages {
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
