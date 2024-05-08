from pydantic import BaseModel, Field

class StandardResponse(BaseModel):
    isSuccess: bool
    code: str
    message: str
    data: dict = Field(default={})

# 예를 들어 SQL 쿼리 결과를 반환할 때 사용할 수 있는 데이터 모델을 추가 정의할 수 있습니다.
class SQLResponseData(BaseModel):
    sql: str
