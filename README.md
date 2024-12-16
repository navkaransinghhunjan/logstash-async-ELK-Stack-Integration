# Description
The logstash-async project is an implementation of the ELK Stack (Elasticsearch, Logstash, and Kibana) designed to facilitate asynchronous logging in Python applications using FastAPI. This project showcases how to effectively collect, process, and visualize log data in real-time, making it an essential tool for developers looking to monitor their applications and gain insights into system performance.
With this setup, you can send logs from your FastAPI application to Logstash, which then forwards them to Elasticsearch for storage and analysis. Kibana provides a powerful interface for visualizing and querying the log data, enabling users to create dashboards and perform complex searches.
# Features
 * Asynchronous Logging: Utilizes logstash-async for non-blocking log transmission.
 * Real-time Data Processing: Logs are processed in real-time through Logstash.
 * Powerful Visualization: Leverage Kibana to create visualizations and dashboards from your log data.
 * Health Monitoring: Includes a health check endpoint in FastAPI to monitor application status.
 * Dockerized Environment: Easily deploy the entire stack using Docker and Docker Compose.
# Getting Started
## Prerequisites
* Docker and Docker Compose installed on your machine.
* Basic knowledge of Python and FastAPI.
  
## Installation
1. Clone this repository:
```bash
git clone https://github.com/navkaransinghhunjan/logstash-async-ELK-Stack-Integration.git
cd logstash-async-ELK-Stack-Integration
```
2.  Build and start the ELK stack:
```bash
docker-compose up --build
```
3. Access Kibana at http://localhost:5601 to visualize your logs.
## Configuration
* Logstash configuration is found in logstash/logstash.conf. Modify this file to adjust input sources or output destinations as needed.
* FastAPI application can be customized in main.py. Adjust logging settings or endpoints as required.
## Usage
Once the stack is running, you can send logs from your FastAPI application. The application will log requests and responses asynchronously to Logstash, which will then forward them to Elasticsearch for indexing.
## Health Check
You can verify if the FastAPI application is running correctly by accessing:
```text
http://localhost:8000/healthcheck
```
