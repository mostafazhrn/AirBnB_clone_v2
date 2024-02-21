#!/usr/bin/python3
"""This module shall defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import os


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    def __init__(self, *args, **kwargs):
        """This shall init user class"""
        super().__init__(*args, **kwargs)
