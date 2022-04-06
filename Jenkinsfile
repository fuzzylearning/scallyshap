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
                                                sh 'python -m build'
                                                sh 'pip install pip install twine'
                                                sh 'twine upload dist/* -u=${username} -p=${password}'

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