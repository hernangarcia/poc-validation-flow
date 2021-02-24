# Setup Information

## Using AWS SAM

Deploy the source from you local development environment. Please note, this requires the following environment setup.

<details>
<summary><strong>Deploy from Source(expand for details)</strong></summary><p>

### Requirements

* [aws-cli](https://aws.amazon.com/cli/) already configured with Administrator permissions.
* [sam-cli](https://github.com/awslabs/aws-sam-cli) AWS SAM CLI tool for local development and testing of Serverless applications
* [Docker installed](https://www.docker.com/community-edition)
* [Python 3.7 or greater](https://realpython.com/installing-python/)

<br/>
<details>
<summary><strong>Installing SAM CLI</strong></summary><p>

**Brew for Mac and Linux**

You can install SAM CLI using brew, a popular package manager for installing the packages you need. Installation is as simple as:

```shell
brew tap aws/tap
brew install aws-sam-cli
```

> **NOTE:** On a Mac you use [Homebrew](https://brew.sh/), and on Linux you use [Linuxbrew](http://linuxbrew.sh/) (a fork of the Homebrew package manager).

**MSI for Windows**

You can now download an MSI to install SAM CLI on Windows. Get the MSI you need here:

* [64-bit](https://github.com/awslabs/aws-sam-cli/releases/download/v0.6.2/AWS_SAM_CLI_64_PY3.msi)
* [32-bit](https://github.com/awslabs/aws-sam-cli/releases/download/v0.6.2/AWS_SAM_CLI_32_PY3.msi)

</p></details>

<br/>

### Clone the repository

```shell
https://github.com/hernangarcia/poc-validation-flow
```

### Building

You can issue the following command in a shell to build the project:

```shell
sam build --use-container
```

### Deploy

We will use the AWS SAM CLI to deploy.

```shell
sam deploy --guided
```

## Testing

