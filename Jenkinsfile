pipeline {
    agent any

    environment {
        // Adjust the Python version folder below if not 3.10
        SCRIPT = 'configure_all_devices.py'
        PATH = "${HOME}/.local/bin:${env.PATH}"
        PYTHONPATH = "${HOME}/.local/lib/python3.10/site-packages"
    }

    stages {
        stage('Install pip and Netmiko') {
            steps {
                sh '''
                    # Make sure wget exists
                    if ! command -v wget > /dev/null; then
                        echo "wget not found. Please install wget manually or update this step.";
                        exit 1
                    fi

                    # Download get-pip.py
                    wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py

                    # Install pip locally (no sudo)
                    python3 get-pip.py --user

                    # Install netmiko in user environment
                    ${HOME}/.local/bin/pip3 install --user netmiko
                '''
            }
        }

        stage('Validate Script') {
            steps {
                sh '''
                    export PATH=$HOME/.local/bin:$PATH
                    export PYTHONPATH=$HOME/.local/lib/python3.10/site-packages:$PYTHONPATH
                    python3 -m py_compile ${SCRIPT}
                '''
            }
        }

        stage('Run Netmiko Script') {
            steps {
                sh '''
                    export PATH=$HOME/.local/bin:$PATH
                    export PYTHONPATH=$HOME/.local/lib/python3.10/site-packages:$PYTHONPATH
                    python3 ${SCRIPT}
                '''
            }
        }

        stage('Post Check') {
            steps {
                echo '✅ Pipeline completed. Devices configured.'
            }
        }
    }
}
