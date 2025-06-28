
import argparse

def summarize_text(text, num_sentences=3):
    sentences = text.split('.')
    summarized_sentences = sentences[:num_sentences]
    return '.'.join(summarized_sentences).strip() + '.'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple MCP text summarizer tool.")
    parser.add_argument("--text", type=str, required=True, help="The text to summarize.")
    parser.add_argument("--num_sentences", type=int, default=3, help="Number of sentences to include in the summary.")
    args = parser.parse_args()

    summary = summarize_text(args.text, args.num_sentences)
    print(summary)
