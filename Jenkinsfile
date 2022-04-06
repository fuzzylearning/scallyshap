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

                sh "adduser --disabled-password --gecos '' user && apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* && apt-get install -y gnumeric"


            }

        }
        
    }

}