from fastapi.middleware.cors import CORSMiddleware
from routers.algorithms import router
from fastapi import FastAPI
import uvicorn

app = FastAPI(swagger_ui_parameters={"docExpansion": "none"})

origins = [
    "*",
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
