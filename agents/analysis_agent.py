from utils.llm import generate_answer


def analyze_research_paper(chunks):

    # Select important sections from the whole research paper

    selected_chunks = (
        chunks[:5] +
        chunks[len(chunks)//2 : len(chunks)//2 + 5] +
        chunks[-5:]
    )

    # Combine paper content
    context = "\n\n".join(selected_chunks)

    question = """
    Analyze this research paper and provide:

    1. Main Research Problem
    2. Proposed Solution / Approach
    3. Methodology Used
    4. Key Contributions
    5. Advantages
    6. Limitations
    7. Future Research Directions

    Give the answer in a structured research review format.
    """

    analysis = generate_answer(
        question,
        context
    )

    analysis += (
        "\n\n---\n**📌 Source:** Beginning, middle, and concluding sections of the paper."
    )

    return analysis