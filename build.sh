#!/bin/bash

POM_FILE_PATH="./pom.xml"
ARTIFACT_NAME="cloud-1.0-SNAPSHOT.jar"
ARTIFACT_PATH="./target/$ARTIFACT_NAME"

COS_BUCKET_NAME="chrisdemo-1253970226"
COS_REMOTE_PATH="scf_release/$ARTIFACT_NAME"

rm -rf "./target"
mvn package -f $POM_FILE_PATH