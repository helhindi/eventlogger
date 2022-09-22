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

Create a GCS bucket for TF state and initialise it:
```
  gsutil mb -l [REGION] gs://[BUCKET_NAME]
  terraform init -backend-config=bucket=[BUCKET_NAME] -backend-config=project=[GOOGLE_PROJECT]
```

#### Initialise Terraform GCP vars:
```
  export TF_VAR_project="$(gcloud config list --format 'value(core.project)')"
  export TF_VAR_region="europe-west2"
```
**Note:** Verify the vars by running:
```
  echo TF_VAR_region=$TF_VAR_region&&echo TF_VAR_project=$TF_VAR_project
```

Also, enter your `gcp_project_id` and `gcp_location` in the `/terraform.tfvars` file.

Now specify an administrative account `user=admin` and set a random password:
```
  export TF_VAR_user="admin"
  export TF_VAR_password="m8XBWryuWEJ238ew"
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
Once the infrastructure is deployed; authenticate and connect to your cluster via `kubectl` and deploy your code using:
```
  skaffold run (or 'skaffold dev' if you want to see code changes deployed immediately)
```

## Testing:
Now to test the `flask` web service; run:
```
  curl localhost:8080/test
```
To test the `postgres` db; run:
```
  curl localhost:8080/test_db
```
