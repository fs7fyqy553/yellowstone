Try at https://main.d1xjk6ynccgx64.amplifyapp.com/

An application made to calculate the term at the nth position of the Yellowstone sequence, described at https://rosettacode.org/wiki/Yellowstone_sequence.

The calculation is done using AWS Lambda and results are displayed to the users of the webpage; sequences calculated in the process are memoised using DynamoDB for faster calculation later. Please see ./lambda/nth_calculator for the algorithm (in algorithm.py) and the Lambda function (in app.py), both of which are written in Python 3.

While the Lambda configuration is done in this repository, configuration for DynamoDB, API Gateway, IAM and Amplify (which is simply used to host the webpage) is done in the AWS Management Console.