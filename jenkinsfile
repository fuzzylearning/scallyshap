pipeline {
    agent any

    tools {

        pip
        mvn

    }

    stages {
        
        stage("build"){

            steps {

                echo 'building scallyshap appication...'

            }

        }
        stage("test"){

            steps {
                echo 'testing scallyshap appication...'
                
            }

    
        stage("deploy"){

            steps {
                echo 'deploying scallyshap appication...'
                
            }

        }
    }

    post{
        always {

        }
        success {

        }
        failure {

        }
    }
}