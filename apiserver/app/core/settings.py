import logging
import os
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = os.getenv('APP_NAME', 'my-app')
    app_version: str = os.getenv('APP_VERSION', '0.0.1')

    app_description: str

    log_level: str = os.getenv('LOG_LEVEL', 'DEBUG')


settings = Settings(
    app_description=(Path(__file__).parent.parent /
                     'static/docs.md').read_text(encoding='utf-8')
)

# configure project-specific logger
logging.basicConfig(
    level=settings.log_level,
    format=
    '%(asctime)s - %(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s'
)
