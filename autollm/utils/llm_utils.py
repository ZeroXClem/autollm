from autollm.utils.templates import QUERY_PROMPT_TEMPLATE, SYSTEM_PROMPT
from autollm.utils.llm_utils import *


def set_default_prompt_template():
    """
    Sets the default prompt templates for the query engine.

    Returns:
        SystemPrompt (str): The default system prompt for the query engine.
        QueryPromptTemplate: The default query prompt template for the query engine.
    """

    return SYSTEM_PROMPT, QUERY_PROMPT_TEMPLATE
