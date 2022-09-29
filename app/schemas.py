from pydantic import BaseModel


class TodoTaskModel(BaseModel):
    slug: str
    title: str
    description: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "slug": "test-task", 
                "title": "Test task", 
                "description": "Just some test task",
                "status": "In progress"
            }
        }