pipeline {
  agent any

  stages {
    stage("This is stage 1") {
      steps {
        git branch: 'main', url: 'https://github.com/Nilakshi23/Test.git'
      }
    }

    stage("This is stage 2") {
      steps {
        echo 'Cool stuff goes here!'
      }
    }
  }
}