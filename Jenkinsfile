pipeline {
    agent any

    environment {
        SCRIPT = 'configure_all_devices.py'
        PATH = "${HOME}/.local/bin:${env.PATH}"
        PYTHONPATH = "${HOME}/.local/lib/python3.10/site-packages"
    }

    stages {
        stage('Install pip and Netmiko') {
            steps {
                sh '''
                    # Ensure pip is available
                    if ! command -v pip3 > /dev/null; then
                        echo "[INFO] Bootstrapping pip..."
                        if command -v wget > /dev/null; then
                            wget https://bootstrap.pypa.io/get-pip.py -O get-pip.py
                        else
                            echo "ERROR: wget not found. Install wget or manually place get-pip.py."
                            exit 1
                        fi
                        python3 get-pip.py --user
                    fi
                    
                    # Upgrade pip and install netmiko
                    ~/.local/bin/pip3 install --user --upgrade pip
                    ~/.local/bin/pip3 install --user netmiko
                '''
            }
        }

        stage('Run Netmiko Script') {
            environment {
                CISCO_CREDS = credentials('cisco-ssh-creds') // Jenkins credential ID
            }
            steps {
                sh '''
                    echo "[INFO] Running Netmiko configuration script..."
                    export CISCO_CREDS_USR="${CISCO_CREDS_USR}"
                    export CISCO_CREDS_PSW="${CISCO_CREDS_PSW}"

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

    post {
        always {
            echo "[INFO] Archiving logs..."
            archiveArtifacts artifacts: 'netmiko.log', allowEmptyArchive: true
        }
    }
}
