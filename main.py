from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from router import router
import uvicorn

app = FastAPI(swagger_ui_parameters={"docExpansion": "none"})

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        app=app, host="localhost", port=8000, log_level="debug"
    )
