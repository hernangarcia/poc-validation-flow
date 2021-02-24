import json
import logging
import os
import base64

import boto3
from aws_lambda_powertools import Metrics, Logger, Tracer
from aws_lambda_powertools.metrics import MetricUnit

logger = Logger()
tracer = Tracer()
metrics = Metrics()

logger.info("Getting SFN ARN from env var")
stateMachineArn = os.environ['STATE_MACHINE_ARN']

logger.info("Initializing SFN client")
stepFunctionClient = boto3.client('stepfunctions')

class StreamProcessingException(Exception):
    def __init__(self, message=None, details=None):
        self.message = message or "Event processing failed"
        self.details = details or {}

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):
    #TODO: improve with Powertools
    #event: KinesisStreamEvent = KinesisStreamEvent(event)
    try:
        for record in event['Records']:
            recordPayload = base64.b64decode(record["kinesis"]["data"]).decode('utf8')
            
            response = stepFunctionClient.start_execution(
                stateMachineArn = stateMachineArn,
                input=recordPayload
            )
            logger.info("stepFunctionClient.start_execution: " + str(response))
            return json.dumps(response, default=str)
    except StreamProcessingException as err:
        metrics.add_metric(name="FailedEventProcessing", unit=MetricUnit.Count, value=1)
        tracer.put_annotation("StreamConsumerFunctionStatus", "FAILED")
        logger.exception({"operation": "stream_processing"})
        raise