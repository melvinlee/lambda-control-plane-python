# AWS-Py-Control-Plane

FaaS control plane to start/stop EC2 and set autoscaling instance size. See `serverless.yml` example how to hook up event trigger for each function.

## Setup

1. ***Install serverless framework via npm:***

    ```npm install -g serverless```

2. ***Set-up your AWS Provider Credentials***

## Deploy

In order to deploy the function simply run

    serverless deploy

The expected result should be similar to:

    Serverless: Packaging service...
    Serverless: Creating Stack...
    Serverless: Checking Stack create progress...
    .....
    Serverless: Stack create finished...
    Serverless: Uploading CloudFormation file to S3...
    Serverless: Uploading artifacts...
    Serverless: Uploading service .zip file to S3 (1.1 KB)...
    Serverless: Validating template...
    Serverless: Updating Stack...
    Serverless: Checking Stack update progress...
    ..................................................................
    Serverless: Stack update finished...
    Service Information
    service: py-control-plane
    stage: pro
    region: ap-southeast-1
    api keys:
    None
    endpoints:
    None
    functions:
    ec2start: py-control-plane-pro-ec2start
    ec2stop: py-control-plane-pro-ec2stop

## Usage

You can now invoke each of the Lambdas directly and print their log statements via

    serverless invoke -f ec2stop -l

The expected result should be similar to:

    {
        "message": "Success"
    }
    --------------------------------------------------------------------
    START RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b Version: $LATEST
    Receive event: {}
    Filters: [{'Name': 'tag:AutoStop', 'Values': ['Yes', 'YES', 'true']}, {'Name': 'instance-state-name', 'Values': ['running']}]
    RunningInstance: ['i-0f5dd561fdec382d7', 'i-0d912a68c42ff4c83', 'i-03fc4e9e3b80d464b', 'i-0a580e2601fc73fa5', 'i-01d47cf36bd757795', 'i-03287ddca76d7b8be', 'i-009814c9ecff25cc6']
    END RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b
    REPORT RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b  Duration: 1101.61 ms    Billed Duration: 1200 ms        Memory Size: 128 MB Max Memory Used: 43 MB

You can also tail the function Logs

    serverless logs -f ec2stop -t

The expected result should be similar to:

    START RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b Version: $LATEST
    Receive event: {}
    Filters: [{'Name': 'tag:AutoStop', 'Values': ['Yes', 'YES', 'true']}, {'Name': 'instance-state-name', 'Values': ['running']}]
    RunningInstance: ['i-0f5dd561fdec382d7', 'i-0d912a68c42ff4c83', 'i-03fc4e9e3b80d464b', 'i-0a580e2601fc73fa5', 'i-01d47cf36bd757795', 'i-03287ddca76d7b8be', 'i-009814c9ecff25cc6']
    END RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b
    REPORT RequestId: 480343e4-5264-11e7-ba6e-cf514b863e2b  Duration: 1101.61 ms    Billed Duration: 1200 ms        Memory Size: 128 MB Max Memory Used: 43 MB