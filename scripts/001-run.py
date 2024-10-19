import os

from openai import AzureOpenAI
from pydantic import BaseModel, ValidationError
from typing import List, Optional

ENDPOINT_V2024_05_13 = os.getenv("AZURE_OPENAI_GPT4O_V2024_05_13_ENDPOINT")
KEY_V2024_05_13 = os.getenv("AZURE_OPENAI_GPT4O_V2024_05_13_KEY")

ENDPOINT_V2024_08_06 = os.getenv("AZURE_OPENAI_GPT4O_V2024_08_06_ENDPOINT")
KEY_V2024_08_06 = os.getenv("AZURE_OPENAI_GPT4O_V2024_08_06_KEY")

# Azure OpenAI API の設定
client_v2024_05_13 = AzureOpenAI(
  azure_endpoint=ENDPOINT_V2024_05_13,
  api_key=KEY_V2024_05_13,
  api_version="2024-08-01-preview"
)
client_v2024_08_06 = AzureOpenAI(
  azure_endpoint=ENDPOINT_V2024_08_06,
  api_key=KEY_V2024_08_06,
  api_version="2024-08-01-preview"
)
clients = [
    client_v2024_05_13,
    client_v2024_08_06,
]

# Pydantic モデルの定義
class Person(BaseModel):
    name: str
    age: Optional[int]
    email: Optional[str]

class ResponseModel(BaseModel):
    people: List[Person]

# Azure OpenAI API にリクエストを送信して結果を取得する関数
def get_openai_response(
    client: AzureOpenAI,
    messages: list[dict],
) -> str:
    response = client.beta.chat.completions.parse(
        model="<ignored>",
        messages=messages,
    )
    print(response.usage)
    print(response.usage.prompt_tokens)
    print(response.usage.completion_tokens)
    print(response.usage.total_tokens)
    return response.choices[0].message.content

def get_openai_response_with_format(
    client: AzureOpenAI,
    messages: list[dict],
    response_format: BaseModel | None = None,
) -> str:
    response = client.beta.chat.completions.parse(
        model="<ignored>",
        messages=messages,
        response_format=response_format,
    )
    print(response.usage)
    print(response.usage.prompt_tokens)
    print(response.usage.completion_tokens)
    print(response.usage.total_tokens)
    return response.choices[0].message.content

# 出力を Pydantic モデルに変換する関数
def parse_response_to_model(response_text: str) -> str | None:
    try:
        # Pydantic モデルにデータを解析してマッピング
        structured_response = ResponseModel.model_validate_json(response_text)
        return structured_response
    except ValidationError as e:
        print("Validation Error:", e)
        return None

# メイン処理
if __name__ == "__main__":
    version_to_client = {
        "v2024-05-13": client_v2024_05_13,
        "v2024-08-06": client_v2024_08_06,
    }
        
    prompt = """
    Please provide the following information in structured JSON format:
    - A list of people with their name, age (optional), and email (optional).
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ]

    print(f"# RUN ON: v2024-05-13")
    # Azure OpenAI からの出力を取得
    response_text = get_openai_response(
        client=client_v2024_05_13,
        messages=messages,
    )
    print("## Raw Response:")
    print(f"TYPE: {type(response_text)}")
    print(response_text)
    print()    

    print(f"# RUN ON: v2024-08-06")
    # Azure OpenAI からの出力を取得
    response_text = get_openai_response_with_format(
        client=client_v2024_08_06,
        messages=messages,
        response_format=ResponseModel,
    )
    print("## Raw Response:")
    print(f"TYPE: {type(response_text)}")
    print(response_text)

    # 出力を Pydantic モデルに変換
    parsed_output = parse_response_to_model(response_text)
    print("## parsed output")
    print(f"TYPE: {type(parsed_output)}")
    print(parsed_output)
    print(parsed_output.model_dump_json(indent=4))
