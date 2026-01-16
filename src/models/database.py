from pydantic import BaseModel, Field


class BaseConnection(BaseModel):
    connection_string: str = Field(..., description="The connection string")
    database_name: str = Field(..., description="The name of the database")
