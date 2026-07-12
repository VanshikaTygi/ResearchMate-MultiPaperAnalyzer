from utils.llm import generate_answer


def generate_research_innovation(all_papers):

    combined_context = ""

    for paper in all_papers:
        combined_context += f"""
    Title: {paper["title"]}

    Summary:
    {paper["summary"]}

    -----------------------------------------
    """

    question = f"""
    Analyze the following research paper summaries.

    If there is only ONE paper:
    Provide:
    1. Research Gaps
    2. Current Limitations
    3. Possible Improvements
    4. Novel Research Ideas
    5. Future Research Directions
    6. Practical Applications

    If there are MULTIPLE papers:
    Provide:
    1. Common Research Gaps
    2. Shared Limitations
    3. Opportunities to Combine the Methods
    4. Novel Hybrid Research Idea
    5. Suggested Future Experiments
    6. Potential Research Project Proposal
    7. Practical Real-World Applications

    Give the answer in a well-structured research innovation report.
    """

    innovation_report = generate_answer(
        question,
        combined_context
    )

    return innovation_report