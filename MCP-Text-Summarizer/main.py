from text_summarizer import summarize_text

def mcp_tool_summarize(text: str, num_sentences: int = 3) -> str:
    """
    MCP Tool to summarize a given text.

    Args:
        text (str): The input text to be summarized.
        num_sentences (int, optional): The number of sentences to include in the summary. Defaults to 3.

    Returns:
        str: The summarized text.
    """
    return summarize_text(text, num_sentences)
