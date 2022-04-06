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

                sh "sudo usermod -a -G docker jenkins && apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* && apt-get install -y gnumeric"


            }

        }
        
    }

}