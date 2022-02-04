pipeline { 
    agent any { 
    stages {
        stage('Example Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Nilakshi23/test2.git'
            }
		stage('Checkout code') {
            steps {
                checkout scm
                               }
                   }
                 }
                }
         }
} 