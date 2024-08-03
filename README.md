# EmpowerU Certificate Generation Microservice

## Overview

The EmpowerU Certificate Generation Microservice handles requests for generating and sending completion certificates. This service is implemented as an AWS Lambda function using Python.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Usage](#usage)
- [Examples](#examples)
- [Todo](#todo)
- [License](#license)

## Features

- Receives requests for certificate generation
- Generates completion certificates for users
- Sends generated certificates via email

## Technologies

- AWS Lambda
- Python
- AWS SQS (for triggering the function)

## Usage

The microservice uses an SQS queue as a trigger. When a message is published to the queue, the Lambda function is triggered, generating a certificate and sending it to the student's email.


## Examples

For examples of generated certificates, please refer to the [examples](./examples/) folder in the repository.

## TODO

- [ ] Implement CI/CD to automate deploy
- [ ] Implement functionality to pre-generate certificates and store them in S3 for faster retrieval when requested by students

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/WiliamMelo01/EmpoweruCertificateMicroserviceLambda/blob/main/LICENSE) file for details.
