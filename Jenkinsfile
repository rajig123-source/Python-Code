pipeline{
  agent any
  environment{
    APP_URL='http://127.0.0.1:5001'
  }
  stages{
    stage{'Checkout'}{
      steps{
        echo 'Fetching Project from Github'
        checkout scm
      }
    }
    stage('Install Dependencies'}{
      steps{
        but 'python -m pip install -r Requirement.txt'
      }
    }
    stage('Start Flask Application'}{
      steps{
        bat 'start "FlaskApp" /B puthon app.py'
      }
    }
    stage('Execcute API Test'){
      steps {
        bat 'python -m  robot test_2.robot'
        )
      }

          
  
