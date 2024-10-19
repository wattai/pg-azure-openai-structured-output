# OpenAI Pydantic Sample

This is a sample project demonstrating how to use Azure OpenAI API to generate structured outputs that conform to a specific `pydantic` model. The project includes a Python script that connects to Azure OpenAI, sends a prompt, and then parses the response into a structured format using `pydantic`.

## Features

- Integration with Azure OpenAI API
- Use of `pydantic` models to structure API output
- Simple API response handling

## Prerequisites

Before you can run this project, you will need:

- Python 3.8 or later
- An Azure OpenAI resource and API key
- `setuptools` and `wheel` for packaging and dependency management

## Installation

1. Clone this repository:

   ```bash
   https://github.com/wattai/pg-azure-openai-structured-output.git
   cd pg-azure-openai-structured-output
   ```
2. Set up your environment:

   Make sure you have a Python virtual environment set up. If you don’t have one, create it as follows:

   ```bash
   pyenv install 3.12.1
   pyenv virtualenv 3.12.1 pg-azure-openai
   pyenv shell pg-azure-openai
   ```

3. Install dependencies:

Once your environment is active, install the necessary dependencies from the pyproject.toml file:

   ```bash
   pip install .
   ```

4. Set up your Azure OpenAI API credentials:

You'll need to provide your Azure OpenAI API credentials in the script (api_key, api_base, etc.) before running the project. You can find these details in the Azure portal under your OpenAI resource.

## Usage

To run the example and see the structured output:

1. Modify the script main.py and replace `<AZURE_OPENAI_GPT4O_V2024_05_13_ENDPOINT>`, `<AZURE_OPENAI_GPT4O_V2024_05_13_KEY>`, `<AZURE_OPENAI_GPT4O_V2024_08_06_ENDPOINT>`, and `<AZURE_OPENAI_GPT4O_V2024_08_06_KEY>` with your actual Azure OpenAI credentials.

2. Run the script:

   ```bash
   python scripts/001-run.py
   ```

   The script will make a call to the Azure OpenAI API, request a structured JSON response, and parse the response into a pydantic model.
