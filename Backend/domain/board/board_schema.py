from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# 새 게시글 Class
class NewPost(BaseModel):
  writer: str
  title: str
  content: Optional[str] = None

# 게시글 리스트
class PostList(BaseModel):
  no: int
  writer: str
  title: str
  date: datetime

# 게시글
class Post(BaseModel):
  no: int
  writer: str
  title: str
  content: Optional[str] = None
  date: datetime

# 게시글 수정
class UpdatePost(BaseModel):
  no: int
  title: str
  content: Optional[str] = None