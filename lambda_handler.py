# lambda_template.py - Lambda handler template you can use as a starting point for AWS Lambda functions.
# Follows the PEP 8 style guide and some recommended practices.
import boto3
import logging
import os

# Setup logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)  # NOTE: change logging level as required (i.e. DEBUG)


# Initialize SDK clients and other shareable resources here
# e.g. s3 = boto3.client('s3')


def lambda_handler(event, context):
    logger.debug('Inside lambda_handler().')
    logger.debug('Using boto3 version: %s' % boto3.__version__)
    logger.debug('Environment: %s' % os.environ)
    logger.debug('Context: %s' % context)
    logger.debug('Event: %s' % event)

    #
    # ----- Main logic goes here -----
    #

    logger.debug('Leaving lambda_handler().')

    # Optional: return a response with some usable values; these object must be serializable by json.dumps
    body = 'Success.'
    status_code = 200
    return {
        'statusCode': status_code,
        'body': body
    }


logger.debug('Lambda function initialized.')

# Simulate a lambda execution (for local environments)
# test_event = {'key1': 'value1', 'key2': 'value2'}
# test_context = object();
# lambda_handler(test_event, test_event)
