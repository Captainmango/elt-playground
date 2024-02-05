import os
import unittest
from unittest import mock


class BaseScriptTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.env_patcher = mock.patch.dict(os.environ, 
                                            {
                                              "SOURCE_USER": "TEST",
                                              "SOURCE_DB": "test",
                                              "SOURCE_HOST": "test",
                                              "SOURCE_PASS": "test",
                                              "SOURCE_PORT": "1234",
                                              "DEST_USER": "TEST",
                                              "DEST_DB": "test",
                                              "DEST_HOST": "test",
                                              "DEST_PASS": "test",
                                              "DEST_PORT": "1234",
                                            }
                                        )
        cls.env_patcher.start()

        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
