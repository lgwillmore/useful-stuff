# How to get syntax highlighting in a JetBrains IDE

> NOTE: You might need paid versions for non intellij IDEs

[Original article describing how to do this](http://vgaidarji.me/blog/2018/07/30/working-with-jenkinsfile-in-intellij-idea/)

I am just preserving it here in case it disappears.

## Working with Jenkinsfile in Intellij IDEA
This post describes how I write/debug Jenkins Pipelines on different projects (Android, Groovy). There should be definitely other ways/environments of doing this. It’s just what’s convenient for me.

Intellij IDEA IDE
Let’s say you want to work on Jenkins Pipeline configuration on a project using IntelliJ IDEA.

- Open a project in IntelliJ IDEA
- Create Jenkinsfile in project root
    * it will be associated with Groovy language by default
    * or you can associate the file with Groovy using Associate with file type action from IDE
- Install standalone Groovy
- Add Groovy to PATH:
    * export GROOVY_HOME={path_to_groovy_folder}
    * export PATH=$PATH:$GROOVY_HOME/bin
- Configure Groovy SDK to enable autocompletion in Jenkinsfile
- Use `pipeline.gdsl` to have Pipeline syntax autocompletion in Jenkinsfile
- create `pipeline.gdsl` file from `http://{YOUR_JENKINS_ADDRESS}/job/{YOUR_PIPELINE_JOB}/pipeline-syntax/gdsl`
- place pipeline.gdsl somewhere in src folder in your project so that it’s recognized properly
- add pipeline.gdsl to .gitignore to reduce noise in the repo

Once you’ve done all these steps you’ll have autocompletion in Jenkinsfile which will help with the development of Jenkins pipelines.