pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
    }

    stage('Debug Python') {
    steps {
        sh '''
            which python3
            python3 -m site
            python3 -c "import sys; print(sys.path)"
            python3 -c "import netmiko; print(netmiko.__file__)"
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
