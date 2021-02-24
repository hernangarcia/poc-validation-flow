import json
import logging
import os

import boto3
from aws_lambda_powertools import Metrics, Logger, Tracer

logger = Logger()
tracer = Tracer()
metrics = Metrics()

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):
    
    logger.info("Hello from function " + context.function_name)
    
    return {"filtersChecked" : True}
