pipeline {
    agent none


    stages {
        
        stage("Download-data"){

            agent {
                docker{
                    image 'ubuntu'
                }
            }

            steps {

                sh 'apt-get install -y gnumeric'

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