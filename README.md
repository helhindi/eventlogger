# eventlogger
![GitHub Actions status](https://github.com/helhindi/eventlogger/workflows/docker_lint_build_publish/badge.svg)
![Dockerhub build status](https://img.shields.io/docker/cloud/build/elhindi/flask-pg-app)

## Introduction
A sample API that allows submitting and retrieving data; as well as logging event times. The `/event` endpoint supports POST requests; while `/events` can be used to retrieve all submitted events associated to a particular api key. (further details on testing can be found at the bottom of this document under [Testing](#Testing))

**Note:** The instructions assume an OSX machine with `brew` installed.

## Getting Started

#### Clone repo & install pre-req tools:
From an OSX machine's Terminal; launch the following commands:
```
  git clone https://github.com/helhindi/eventlogger.git &&cd eventlogger
```

#### Install `brew`:
```
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
#### Install tools:
Install [`'aws-cli', 'terraform', 'skaffold'`] by running:
```
  brew bundle --verbose
```

#### Initialise `aws-cli`:
Assuming you've installed `aws-cli` (as shown above); init, authenticate and set compute zone interactively via:
```
  aws-cli init
```

Create an S3 bucket for TF state and initialise it:
```
  s3 mb -l [REGION] s3://[BUCKET_NAME]
  terraform init -backend-config=bucket=[BUCKET_NAME]
```

#### Initialise Terraform vars:
```
  export TF_VAR_region="eu-west-2"
```
**Note:** Verify the vars by running:
```
  echo TF_VAR_region=$TF_VAR_region
```

## Initialise and create:
```
  terraform init
  terraform plan
```
Once happy with the above plan output; apply using:
```
  terraform apply
```
Once the infrastructure is deployed; authenticate and connect, deploy :
```
  skaffold run (or 'skaffold dev' if you want to see code changes deployed immediately)
```

## Testing:
Now submit an event to the api:
```
curl -X POST -H "x-api-key: api-key-value" \
  -H "Content-Type: application/json" \
  -d '{"deviceId":"0000"}' \
  https://eventlogger.elhindi.org/event
```
To list all events:
```
curl -X GET \
  -H "x-api-key: api-key-value" \
  -H "Content-Type: application/json" \
  https://eventlogger.elhindi.org/events
```
