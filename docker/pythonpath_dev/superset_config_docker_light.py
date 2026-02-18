# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Configuration for docker-compose-light.yml - disables Redis and uses minimal services

# Import all settings from the main config first
from flask_caching.backends.filesystemcache import FileSystemCache
from superset_config import *  # noqa: F403

# Override caching to use simple in-memory cache instead of Redis
RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

CACHE_CONFIG = {
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_light_",
}
DATA_CACHE_CONFIG = CACHE_CONFIG
THUMBNAIL_CACHE_CONFIG = CACHE_CONFIG


# Disable Celery entirely for lightweight mode
CELERY_CONFIG = None  # type: ignore[assignment,misc]
#
#
# # Custom configuration for enabling Dashboard embed
# SESSION_COOKIE_SAMESITE = None
# ENABLE_PROXY_FIX = True
# PUBLIC_ROLE_LIKE_GAMMA = True
# WTF_CSRF_ENABLED = False
# FEATURE_FLAGS = {
#   "EMBEDDED_SUPERSET": True
# }
# TALISMAN_ENABLED = False
# ENABLE_CORS = True
# HTTP_HEADERS={"X-Frame-Options":"ALLOWALL"}
# #SQLALCHEMY_DATABASE_URI = 'mysql://superset:superset@3.111.209.150:3306/shiprelax_uat_3_mar_2023'
# SECRET_KEY='TyPUbdt+hr05jzZIsXg1201R8Q4QiEKQK0oDu233GOdGFpJTYLYzGLaM'
# GUEST_TOKEN_JWT_EXP_SECONDS = 2592000
# CORS_OPTIONS = {
#  'supports_credentials': True,
#  'allow_headers': ['*'],
#  'resources':['*'],
#  'origins': ['http://localhost:8088', 'http://localhost:8888']
# }

