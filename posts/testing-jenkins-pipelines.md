<!-- 
.. title: Testing Jenkins pipeline
.. slug: testing-jenkins-pipeline
.. date: 2017-07-30 14:18:08 UTC+02:00
.. tags: testing, pipelines, draft
.. category: 
.. link: 
.. description: 
.. type: text
-->

Based on our experience, you are correct that to meaningfully test the changes you need to have them at least somewhere where Jenkins will be able to pull them, preferably in a branch in the same repository you configured as the pipeline-library source.

We have been fine with this so far, because on github which we use, you can reference PR's to a repository as if they already were branches on that repository, i.e. I have @Library('fh-pipeline-library@pr/40') _ on top of my Jenkinsfile in my PR [1] which then references the PR to our pipeline library [2]

To do this we first run into two problems in our configuration of the pipeline library, but after we set "Load implicitly" configuration to be disabled and "Allow default version to be overridden" to be enabled this started working fine.

If you needed more flexibility, you could use the explicit library step, i.e. when I was experimenting with it, I managed to load my library directly, despite the annotation:

```
@Library('fh-pipeline-library@master') _
library identifier: 'fh-pipeline-library2@openshift_utils', retriever: modernSCM([$class: 'GitSCMSource', credentialsId: '', excludes: '', id: '4eefd1a5-6ae6-49bf-8819-26e669e14c7f', ignoreOnPushNotifications: false, includes: '*', rawRefSpecs: '+refs/heads/*:refs/remotes/origin/*', remote: 'https://github.com/AdamSaleh/fh-pipeline-library.git', remoteName: 'openshift_utils'])
```

But the code is quite ugly, and I don't think I would be able to produce it without the snippet generator. 

But if you really need to avoid comiting to your primary repository, this seems to be a way.

On the other hand, only way to test changes I haven't pushed anywhere yet, seems to be with unit testing [3], and we are experimenting on adding something like that to our pipeline-library, but we are not sure if it would be worth it.

Adam

[1] https://github.com/feedhenry/fh-mbaas/pull/51/files#diff-58231b16fdee45a03a4ee3cf94a9f2c3R4
[2] https://github.com/feedhenry/fh-pipeline-library/pull/40
[3] https://github.com/macg33zr/pipelineUnit
