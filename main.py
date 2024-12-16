# pylint: disable=missing-module-docstring,missing-function-docstring
from os import environ
import random
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, Response
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import LogstashFormatter


logger = logging.getLogger("fastapi-logstash")
logger.setLevel(logging.INFO)

# Specify a database path for log persistence or set it to None
logstash_handler = AsynchronousLogstashHandler(
    host=environ.get("LOGSTASH_HOST", "logstash"),
    port=int(environ.get("LOGSTASH_PORT", 5959)),
    database_path='/tmp/logstash.db'  # Specify a valid path here
)

logstash_handler.setFormatter(LogstashFormatter())
logger.addHandler(logstash_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
logger.addHandler(stream_handler)

app = FastAPI()

status_dict = {
    200: "OK - Everything is fine.",
    201: "Created - Your resource was successfully created.",
    301: "Moved Permanently - The resource has moved to a new URL.",
    403: "Forbidden - You do not have permission to access this resource.",
    404: "Not Found - The requested resource could not be found.",
    503: "Service Unavailable - The server is not ready to handle the request.",
}


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("Request: %s %s", request.method, request.url.path)
    response = await call_next(request)
    logger.info("Response: %d", response.status_code)
    return response


@app.get("/")
async def get_random_status():
    status_code = random.choice(list(status_dict.keys()))
    message = status_dict[status_code]
    return JSONResponse(content={"message": message}, status_code=status_code)


@app.get("/healthcheck")
async def healthcheck():
    return JSONResponse(content={"status": "healthy"}, status_code=200)
