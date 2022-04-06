pipeline {
    agent none


    stages {
        
        stage("Download-data-build-test"){

            agent {
                dockerfile true
            }

            steps {

                sh 'echo hi from docker 2'
                sh './run.sh'

            }

        }
        
    }

}