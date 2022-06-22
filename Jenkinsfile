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

        // }
        
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
                                                 sh 'pip3 install setuptools '
                                                 sh 'pip3 install pip install twine '
                                                 sh 'python setup.py sdist'
                                                 sh 'twine upload dist/* -u=${username} -p=${password}'

                                                 }
                             }
            
                 }
            }
    
}

