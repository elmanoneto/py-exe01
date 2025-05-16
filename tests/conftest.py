import pytest
import sqlite3
from example01.db import create_table

@pytest.fixture
def connect_db():
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    yield conn
    conn.close()
