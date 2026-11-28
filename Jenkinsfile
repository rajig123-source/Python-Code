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
    stage('Install Dependencies'){
      steps{
        but 'python -m pip install -r Requirement.txt'
      }
    }
    stage('Start Flask Application'){
      steps{
        bat '''
          cd /d "%WORKSPACE%\\Automation Simulator"
        start "FlaskApp" /B python app.py'''
      }
    }
    stage('Execcute API Test'){
      steps {
        bat'''
          cd /d "%WORKSPACE%\\Robot_APT_Project\\tests\\test_2.robot"
        python -m  robot test_2.robot'''
        )
      }
    }
}
  
