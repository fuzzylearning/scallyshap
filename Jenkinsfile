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

                sh 'echo hi from docker'
                sh 'echo hi from docker 2'



            }

        }
        
    }

}