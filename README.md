Try at https://main.dkdq6lguvybor.amplifyapp.com/

A simple application made to calculate a term at the nth position in the Yellowstone sequence, described at https://rosettacode.org/wiki/Yellowstone_sequence.

The calculation is done using AWS Lambda and results are currently stored in a DynamoDB database, as well as displayed to the user of the webpage.

While the Lambda configuration is done in this repository, configuration for DynamoDB, API Gateway, IAM and Amplify (which is simply used to host the webpage) is done in the AWS Management Console.

The algorithm in lambda/nth_calculator/algorithm.py is working but must be optimised. Thus far, however, it utilises dynamic programming. Moreover, memoisation must be implemented, in which the lambda function simply returns a Yellowstone integer from the DynamoDB database if it has already been calculated.