import os
import shutil
from unittest import TestCase

from fastapi.testclient import TestClient

from main import app


class TestApp(TestCase):
    def setUp(self):
        super().setUp()

        self.client = TestClient(app)
        self.TEST_DIR = "test/fixtures/tmp/"
        copy_and_overwrite("test/fixtures/data/", self.TEST_DIR)
        copy_and_overwrite(
            "test/fixtures/status/", os.path.join(self.TEST_DIR, "status")
        )
        self.pdf_sha = "3febb2bed8865945e7fddc99efd791887bb7e14f"

    def tearDown(self):
        shutil.rmtree(self.TEST_DIR)

    def test_root(self):
        response = self.client.get("/")
        assert response.status_code == 204
