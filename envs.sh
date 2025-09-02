#!/usr/bin/env bash

# PostgreSQL connection settings
export postgres_user="username"
export postgres_pass="password"
export postgres_host_reader="database"
export postgres_host_writer="database"
export postgres_port="5432"
export postgres_dbname="postgis"

# Optional extra settings for test environment
export stac_fastapi_title="stac-fastapi-test"
export stac_fastapi_description="STAC FastAPI test instance"
export stac_fastapi_version="0.1"
export stac_fastapi_landing_id="stac-fastapi"
export app_host="0.0.0.0"
export app_port="8080"
export reload="True"
export enable_response_models="False"
export enable_direct_response="False"
export openapi_url="/api"
export docs_url="/api.html"
export root_path=""
