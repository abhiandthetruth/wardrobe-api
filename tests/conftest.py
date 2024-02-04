from dotenv import dotenv_values
from pymongo import MongoClient
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app as application
import mongomock


@pytest.fixture
def app() -> FastAPI:
    application.dependency_overrides = {}
    application.mongodb_client = mongomock.MongoClient()
    application.database = mongomock.MongoClient().get_database("test_db")
    return application


@pytest.fixture
def client(app) -> TestClient:
    return TestClient(app)
