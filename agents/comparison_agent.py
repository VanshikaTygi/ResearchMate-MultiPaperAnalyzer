from utils.llm import generate_answer


def compare_research_papers(papers, user_query=None):
    """
    papers: List of dictionaries
    Each dictionary contains:
    {
        "title": "...",
        "filename": "...",
        "summary": "..."
    }

    user_query:
        None  -> Automatic comparison
        String -> User-specific comparison question
    """

    comparison_context = ""

    for index, paper in enumerate(papers, start=1):

        comparison_context += (
            f"\n\nPaper {index}\n"
            f"Title: {paper['title']}\n"
            f"File: {paper['filename']}\n\n"
            f"{paper['summary']}\n"
        )

    if user_query is None:

        question = """
    Compare the following research papers.

    Provide a detailed comparison including:

    1. Research Objective
    2. Proposed Method
    3. Methodology
    4. Key Contributions
    5. Advantages
    6. Limitations
    7. Best Use Case
    8. Which paper is the most innovative and why?
    9. Overall Recommendation

    Present the comparison in a clean markdown table wherever appropriate.

    Finish with a short conclusion.
    """

    else:

        question = f"""
    You are comparing multiple research papers.

    Using only the provided research summaries,

    answer the following comparison question.

    Question:

    {user_query}

    Give a detailed comparison and explain your reasoning.
    """
        
    comparison = generate_answer(
    question,
    comparison_context
)

    return comparison