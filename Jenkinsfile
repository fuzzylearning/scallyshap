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
        
    }

}