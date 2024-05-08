from fastapi import FastAPI

from models.response_model import SQLResponseData, StandardResponse
from models.user_query import UserQuery
from schema import schema
from context import context

app = FastAPI()

# api_key = os.environ.get('GPT_SERVER_KEY')
# client = OpenAI(api_key=api_key)

@app.post("/sheet/make-sql")
async def make_sql(user_query: UserQuery):

    prompt = f"""  
    User Query: {user_query.question}
    """

    system_context = context.format(schema=schema, attribute_names=user_query.attributes_names)

    print(system_context)
    # try:
    #     response = client.chat.completions.create(
    #         model="gpt-4-turbo",
    #         messages=[
    #             {"role": "system", "content": system_context},
    #             {"role": "user", "content": prompt}
    #         ],
    #         temperature=0.1
    #     )
    #
    #     # 응답 메시지 추출
    #     result = response['choices'][0]['message']['content']

        # data = SQLResponseData(sql=result)
        # return StandardResponse(isSuccess=True, code="200", message="Success", data=data.dict())
    # except Exception as e:
    #     return StandardResponse(isSuccess=False, code="500", message=str(e), data={})
