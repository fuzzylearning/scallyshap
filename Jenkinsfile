pipeline {
    agent none


    stages {
        
        stage("Download-data"){

            agent {
                docker{
                    image 'debian'
                }
            }

            steps {

                sh 'su -'
                sh 'echo hi from docker 2'
                sh "adduser --disabled-password --gecos '' user"
                sh 'apt-get update -y'



            }

        }
        
    }

}