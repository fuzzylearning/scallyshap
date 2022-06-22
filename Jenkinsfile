 // pipeline {
 //    agent none


//     stages {
//         stage("publish-pypi") {
//             agent {
//                     docker { image 'python' }
//                 }
//             steps {
//                     script {
//                             withCredentials([
//                             usernamePassword(credentialsId: 'twine-login-info',
//                             usernameVariable: 'username',
//                             passwordVariable: 'password')
//                                             ]) {

//                                                 sh 'rm -rf dist'
//                                                 sh ' pip3 install setuptools '
//                                                 sh 'pip3 install pip install twine '
//                                                 sh 'python setup.py sdist'
//                                                 sh ' twine upload dist/* -u=${username} -p=${password}'

//                                                 }
//                             }
            
//                 }
//         }

//         stage("Download-data-build-test"){

//             agent {
//                 dockerfile true
//             }

//             steps {

//                         sh 'echo hi from docker 2'
//                         sh './run.sh'


//             }

//         }

//         post {
//         // Clean after build

//         always {
//             cleanWs(cleanWhenNotBuilt: false,
//                     deleteDirs: true,
//                     disableDeferredWipeout: true,
//                     notFailBuild: true,
//                     patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
//                                [pattern: '.propsfile', type: 'EXCLUDE']])
//         }
//     }
        

//     }

    

// }


pipeline {
    // withCredentials([
    //                          usernamePassword(credentialsId: 'twine-login-info',
    //                          usernameVariable: 'username',
    //                          passwordVariable: 'password')
    //                                          ]) 

    agent any

    stages {

        // stage("Download-data-build-test"){

        //      agent {
        //          dockerfile true
        //      }

        //      steps {

        //                 sh 'docker image successfully installed from root of project :)'
        //                 sh 'run tests !'
        //                 sh './run.sh'


        //      }

         
        
stage("publish-pypi") {
                 
             steps {

                                                 sh '''
                                                 docker version
                                                 docker info
                                                 docker build -f Dockerfile.publish .
                                                 '''

                                                 //sh 'python3 --version'
                                                 // sh '/usr/local/bin/python3 -m pip install --upgrade pip'
                                                 // sh 'python3 -m  pip install  twine --user'
                                                 //sh '/usr/local/bin/python3 setup.py sdist'
                                                 //sh '''#!/bin/bash
                                                //    sudo apt-get install -y twine
                                                 //   '''
                                                 
                                                 // sh 'twine upload dist/* -u=${username} -p=${password}'

            
                 }
            }
    
}

}

