# ==========================================================
# RESEARCH ANALYSIS AGENT
# Produces a structured 7-point review of a SINGLE paper.
# Does not use FAISS retrieval — instead it samples fixed
# positions in the paper (start/middle/end) on the theory
# that a paper's problem statement, methodology, and
# conclusions tend to live in those regions.
# ==========================================================

from utils.llm import generate_answer


def analyze_research_paper(chunks):

    # Select important sections from the whole research paper

    # Sample beginning (problem/intro), middle (methodology/
    # results), and end (conclusion/future work) — 5 chunks
    # each, 15 total. This is a heuristic, not a guarantee:
    # very long or unusually structured papers may need a
    # different sampling strategy.

    selected_chunks = (
        chunks[:5] +
        chunks[len(chunks)//2 : len(chunks)//2 + 5] +
        chunks[-5:]
    )

    # Combine paper content
    context = "\n\n".join(selected_chunks)

    # A fixed 7-point structure so every analysis looks the
    # same regardless of paper topic — this consistency is
    # what makes the Comparison agent's job possible later
    # (it expects each paper's summary to cover the same points).
    
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