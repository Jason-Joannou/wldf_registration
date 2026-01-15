from pydantic_settings import BaseSettings, SettingsConfigDict, NoDecode
from pydantic import Field, field_validator
import json
from typing import Dict, Annotated
from pathlib import Path
from typing import List

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    google_service_account_email: str = Field(..., min_length=1)
    registration_template_folder_name: str = Field(..., min_length=1)
    google_service_account_credentials: Annotated[Dict[str, str], NoDecode] = Field(..., min_length=1)

    @field_validator("google_service_account_credentials", mode="before")
    @classmethod
    def load_credentials_from_file(cls, v) -> Dict:
        """Load JSON from file path or parse JSON string"""
        if isinstance(v, str):
            if not v or not v.strip():
                raise ValueError("google_service_account cannot be empty")
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                file_path = Path(v)
                if file_path.exists():
                    with open(file_path, 'r') as f:
                        return json.load(f)
                raise ValueError(f"Invalid JSON or file not found: {v}")
        return v