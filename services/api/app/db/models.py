from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    github_id = Column(String, unique=True, index=True)
    login = Column(String, index=True)
    email = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

class GitHubToken(Base):
    __tablename__ = 'github_tokens'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    encrypted_token = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    last_used = Column(DateTime, nullable=True)

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, primary_key=True)
    repo_id = Column(String, unique=True, index=True)
    owner = Column(String)
    name = Column(String)
    branch = Column(String, default='main')
    indexed_at = Column(DateTime, server_default=func.now())
    chunks_count = Column(Integer, default=0)
    user_id = Column(Integer, index=True)

class AuditLog(Base):
    __tablename__ = 'audit_logs'
    id = Column(Integer, primary_key=True)
    event = Column(String, index=True)
    user_id = Column(Integer, nullable=True)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

Base.metadata.create_all(bind=engine)  # dev auto-create; use Alembic in prod