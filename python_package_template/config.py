from pydantic import BaseModel, Field


class Config(BaseModel):
    name: str = Field(default="World", description="The name to greet")

    model_config = {"title": "Hello World Config"}

