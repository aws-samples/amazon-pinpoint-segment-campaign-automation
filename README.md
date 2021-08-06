## Amazon Pinpoint Segment Campaign Automation

[![Publish Version](https://github.com/aws-samples/amazon-pinpoint-segment-campaign-automation/workflows/Publish%20Version/badge.svg)](https://github.com/aws-samples/amazon-pinpoint-segment-campaign-automation/actions)
[![Unit Tests](https://github.com/aws-samples/amazon-pinpoint-segment-campaign-automation/workflows/Unit%20Tests/badge.svg)](https://github.com/aws-samples/amazon-pinpoint-segment-campaign-automation/actions)

#### Introduction

This repository contains a solution for automating the process of capturing your customers’ interests in a product category so you can tailor your marketing messages. It uses a series of AWS services including Amazon Pinpoint, AWS Step Functions, AWS Lambda, Amazon DynamoDB and Amazon Simple Notification Service (SNS).

An AWS CloudFormation template will deploy an AWS Step Functions with a series of Lambdas, one Amazon DynamoDB table and three SNS topics. For a successful deployment, you will need to provide an existing Amazon Pinpoint project as well as a validated email address from where you can send emails from.

This repository is part of a blog in which a step by step implementation guide can be found.

#### Architecture

This solution uses:
* [Amazon Pinpoint](https://aws.amazon.com/pinpoint/) to send email campaigns and store customer data
* [AWS Step Functions](https://aws.amazon.com/step-functions/) to orchestrate the automation of Amazon Pinpoint activities
* [AWS Lambda](https://aws.amazon.com/lambda/) to perform calls to Amazon Pinpoint and process data
* [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) as a target database to store all logs from this solution
* [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) as a way to emit messages depending the outcome of each AWS Step Functions execution

An overview of the architecture is below:

 [![Architecture Diagram](https://github.com/aws-samples/amazon-pinpoint-segment-campaign-automation/blob/pavlosik-patch-1/docs/Architecture%20Diagram.png)]


### Usage

#### Prerequisites

To deploy the solution, you will require an AWS account. If you don’t already have an AWS account,
create one at <https://aws.amazon.com> by following the on-screen instructions.
Your access to the AWS account must have IAM permissions to launch AWS CloudFormation templates that create IAM roles.

#### Deployment

The application is deployed as an [AWS CloudFormation](https://aws.amazon.com/cloudformation) template.

> **Note**
You are responsible for the cost of the AWS services used while running this sample deployment. There is no additional
cost for using this sample. For full details, see the pricing pages for each AWS service you will be using in this sample. Prices are subject to change.

1. Deploy the latest CloudFormation template by following the link below for your preferred AWS region:

|Region|Launch Template|
|------|---------------|
|**US East (N. Virginia)** (us-east-1) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-us-east-1/amazon-pinpoint-segment-campaign-automation/latest/main.template)|
|**US West (Oregon)** (us-west-2) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-us-west-2/amazon-pinpoint-segment-campaign-automation/latest/main.template)|
|**EU (Ireland)** (eu-west-1) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-1#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-eu-west-1/amazon-pinpoint-segment-campaign-automation/latest/main.template)|
|**EU (London)** (eu-west-2) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-west-2#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-eu-west-2/amazon-pinpoint-segment-campaign-automation/latest/main.template)|
|**EU (Frankfurt)** (eu-central-1) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-eu-central-1/amazon-pinpoint-segment-campaign-automation/latest/main.template)|
|**AP (Sydney)** (ap-southeast-2) | [![Launch CloudFormation Stack](docs/deploy-to-aws.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-southeast-2#/stacks/new?stackName=pinpoint-campaign-automation&templateURL=https://s3.amazonaws.com/solution-builders-ap-southeast-2/amazon-pinpoint-segment-campaign-automation/latest/main.template)|

2. If prompted, login using your AWS account credentials.
1. You should see a screen titled "*Create Stack*" at the "*Specify template*" step. The fields specifying the CloudFormation
   template are pre-populated. Click the *Next* button at the bottom of the page.
1. On the "*Specify stack details*" screen you may customize the following parameters of the CloudFormation stack:

|Parameter label|Default|Description|
|---------------|-------|-----------|
|PinpointProjectId|`required`|Amazon Pinpoint Project ID.|
|EmailFromAddress|`required`|Type the email that you would like the campaign email to be sent from. This email address needs to be validated first.|
|ResourceTags|MyApp|Tag resources, which can help you identify and categorize them.|
|Environment|DEV|The type of environment to tag your infrastructure with.|

When completed, click *Next*
1. [Configure stack options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-add-tags.html) if desired, then click *Next*.
1. On the review screen, you must check the boxes for:
    * "*I acknowledge that AWS CloudFormation might create IAM resources*"
    * "*I acknowledge that AWS CloudFormation might create IAM resources with custom names*"
    * "*I acknowledge that AWS CloudFormation might require the following capability: CAPABILITY_AUTO_EXPAND*"

   These are required to allow CloudFormation to create a Role to grant access to the resources needed by the stack and name the resources in a dynamic way.
1. Click *Create Stack*
1. Wait for the CloudFormation stack to launch. Completion is indicated when the "Stack status" is "*CREATE_COMPLETE*".
    * You can monitor the stack creation progress in the "Events" tab.

### Clean up

To remove the stack:

1. Open the AWS CloudFormation Console.
1. Click the *pinpoint-campaign-automation* project, right-click and select "*Delete Stack*".
1. Your stack will take some time to be deleted. You can track its progress in the "Events" tab.
1. When it is done, the status will change from "DELETE_IN_PROGRESS" to "DELETE_COMPLETE". It will then disappear from the list.
1. Locate the S3 bucket and delete it manually.

## Local Development
See [Local Development](docs/LOCAL_DEVELOPMENT.md) guide to get a copy of the project up and running on your local machine for development and testing purposes.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
