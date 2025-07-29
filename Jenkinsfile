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
