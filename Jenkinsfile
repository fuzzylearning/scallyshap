pipeline {
    agent none


    stages {
        stage("publish-pypi") {
            agent {
                    docker { image 'python' }
                }
            steps {
                    script {
                            withCredentials([
                            usernamePassword(credentialsId: 'twine-login-info',
                            usernameVariable: 'username',
                            passwordVariable: 'password')
                                            ]) {

                                                sh 'rm -rf dist'
                                                sh 'sudo -H pip3 install setuptools '
                                                sh 'sudo -H pip3 install pip install twine '
                                                sh 'sudo -H python setup.py sdist'
                                                sh 'sudo -H twine upload dist/* -u=${username} -p=${password}'

                                                }
                            }
            
                }
        }

        // stage("Download-data-build-test"){

        //     agent {
        //         dockerfile true
        //     }

        //     steps {

        //                 sh 'echo hi from docker 2'
        //                 sh './run.sh'


        //     }

        // }

        
        
    }

}