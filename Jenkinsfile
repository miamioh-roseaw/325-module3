pipeline {
       agent any
       environment {
       SCRIPT = 'configure_all_devices.py'
       }
       stages {
       //stage('Checkout') {
       //       steps {
       //     git 'https://github.com/miamioh-roseaw/325-module2.git'
       //       }
       //}
       //stage('Validate Script') {
       //       steps {
       //     sh "python3 -m py_compile ${SCRIPT}"
       //       }
       //}
       stage('Install Dependencies') {
            steps {
                sh '''
                    which python3 || sudo apt-get install -y python3
                    which pip3 || sudo apt-get install -y python3-pip
                    pip3 install --upgrade pip
                    pip3 install netmiko
                '''
            }
       }
       stage('Run Netmiko Script') {
              steps {
            sh "python3 ${SCRIPT}"
              }
       }
       //stage('Post Check') {
       //       steps {
       //     sh 'echo "Pipeline completed. Devices configured."'
       //       }
       //}
}
}
