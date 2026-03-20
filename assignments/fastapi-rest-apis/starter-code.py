"""
Building REST APIs with FastAPI
Starter code for the FastAPI REST API assignment
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI application
app = FastAPI(
    title="Todo API",
    description="A simple REST API for managing todos",
    version="1.0.0"
)

# ============================================================================
# Pydantic Models for request/response validation
# ============================================================================

class TodoBase(BaseModel):
    """Base model for todo data"""
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    """Model for creating a new todo"""
    pass


class Todo(TodoBase):
    """Model for todo response"""
    id: int

    class Config:
        from_attributes = True


# ============================================================================
# In-memory data store (for demonstration purposes)
# ============================================================================

todos_db = {
    1: {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Complete the FastAPI REST API assignment",
        "completed": False
    },
    2: {
        "id": 2,
        "title": "Build a REST API",
        "description": "Create a todo API with CRUD operations",
        "completed": False
    }
}

next_id = 3


# ============================================================================
# API Endpoints - Task 1: Basic CRUD Operations
# ============================================================================

@app.get("/todos", response_model=List[Todo], tags=["todos"])
async def get_todos():
    """
    Retrieve all todos.
    
    Returns:
        List of all todos in the system
    """
    # TODO: Implement this endpoint to return all todos
    pass


@app.get("/todos/{todo_id}", response_model=Todo, tags=["todos"])
async def get_todo(todo_id: int):
    """
    Retrieve a specific todo by ID.
    
    Args:
        todo_id: The ID of the todo to retrieve
        
    Returns:
        The requested todo
        
    Raises:
        HTTPException: If todo is not found
    """
    # TODO: Implement this endpoint to return a specific todo
    pass


@app.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED, tags=["todos"])
async def create_todo(todo: TodoCreate):
    """
    Create a new todo.
    
    Args:
        todo: The todo data to create
        
    Returns:
        The created todo with its assigned ID
    """
    # TODO: Implement this endpoint to create a new todo
    pass


@app.put("/todos/{todo_id}", response_model=Todo, tags=["todos"])
async def update_todo(todo_id: int, todo_data: TodoCreate):
    """
    Update an existing todo.
    
    Args:
        todo_id: The ID of the todo to update
        todo_data: The updated todo data
        
    Returns:
        The updated todo
        
    Raises:
        HTTPException: If todo is not found
    """
    # TODO: Implement this endpoint to update a todo
    pass


@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["todos"])
async def delete_todo(todo_id: int):
    """
    Delete a todo.
    
    Args:
        todo_id: The ID of the todo to delete
        
    Raises:
        HTTPException: If todo is not found
    """
    # TODO: Implement this endpoint to delete a todo
    pass


# ============================================================================
# API Endpoints - Task 2: Advanced Features (Optional)
# ============================================================================

@app.get("/todos/search/filter", response_model=List[Todo], tags=["todos"])
async def filter_todos(completed: Optional[bool] = None, skip: int = 0, limit: int = 10):
    """
    Filter and paginate todos.
    
    Args:
        completed: Filter by completion status (optional)
        skip: Number of todos to skip (pagination)
        limit: Maximum number of todos to return (pagination)
        
    Returns:
        Filtered and paginated list of todos
    """
    # TODO: Implement this endpoint with filtering and pagination
    pass


@app.get("/", tags=["root"])
async def root():
    """Root endpoint that returns API information"""
    return {
        "message": "Welcome to the Todo API",
        "docs_url": "/docs",
        "openapi_url": "/openapi.json"
    }


# ============================================================================
# Run the application
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
