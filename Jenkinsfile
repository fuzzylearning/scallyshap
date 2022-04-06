pipeline {
    agent none


    stages {
        stage("publish-pypi") {
            agent any
            steps {
                step {
                    script {
                            withCredentials([
                            usernamePassword(credentialsId: 'twine-login-info',
                            usernameVariable: 'username',
                            passwordVariable: 'password')
                                            ]) {
                                                print 'username=' + username + 'password=' + password
                                                print 'username.collect { it }=' + username.collect { it }
                                                print 'password.collect { it }=' + password.collect { it }
                                                }
                            }
                     }
            
                }

        stage("Download-data-build-test"){

            agent {
                dockerfile true
            }

            steps {

                step {
                        sh 'echo hi from docker 2'
                        sh './run.sh'

                }

            }

        }

        
        
    }

}