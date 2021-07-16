import logging
import os

import boto3

client = boto3.client("pinpoint")


def lambda_handler(event, context):
    interest = event["interest"]
    product_name = event["product_name"]
    product_link = event["product_link"]
    segmentid = event["SegmentId"]  # TODO: var not used, can we remove?
    global log_level  # TODO: undefined at module level, can we remove?
    log_level = str(os.environ.get("LOG_LEVEL")).upper()
    if log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        log_level = "ERROR"
    logging.getLogger().setLevel(log_level)
    logging.info(event)

    try:
        response = client.get_segment(
            ApplicationId=os.environ.get("PINPOINT_PROJECT_ID"),
            SegmentId=event["SegmentId"],
        )
        segment_id = response["SegmentResponse"]["Id"]
        segment_status = "COMPLETED"
        db_logging_status = "SEGMENT_SUCCESS"
        logging.info(response)
    except Exception as e:
        print(e)
        segment_id = "NA"
        segment_status = "INVALID"
        db_logging_status = "SEGMENT_FAILED"

    return {
        "SegmentId": segment_id,
        "SegmentStatus": segment_status,
        "product_name": product_name,
        "interest": interest,
        "product_link": product_link,
        "db_logging_status": db_logging_status,
    }
