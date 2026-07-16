# ==========================================================
# RESEARCH Q&A AGENT
# The ONLY agent that performs genuine RAG (Retrieval-
# Augmented Generation): it embeds the user's question,
# searches the paper's FAISS index for the most relevant
# chunks, and feeds ONLY those chunks to the LLM — along
# with explicit chunk-number citations in the final answer.
# ==========================================================

from utils.vector_store import search_vector_store
from utils.llm import generate_answer


def research_qa_agent(
    question,
    vector_store,
    embedding_model,
    chunks,
    paper_title,
    paper_filename
):

    question_lower = question.lower()

    # Broad questions ("summarize", "explain", "overview")
    # need more context to answer well, so we widen the
    # retrieval window (top_k=10) for these. Narrow, specific
    # questions ("what dataset was used") only need top_k=3 —
    # pulling in more chunks would just add noise.

    broad_questions = [
        "explain",
        "summary",
        "summarize",
        "overview",
        "describe",
        "paper",
        "main contribution",
        "conclusion"
    ]

    top_k = 3

    if any(keyword in question_lower for keyword in broad_questions):
        top_k = min(10, len(chunks))
    

    # Step 1: Retrieve relevant research content
    relevant_chunks, relevant_indices = search_vector_store(
        question,
        vector_store,
        embedding_model,
        chunks,
        top_k=top_k
    )


    # Step 2: Combine retrieved chunks

    # Each retrieved chunk is labeled [Chunk N] so the LLM
    # can reference specific chunks in its answer, and so we
    # can show the user exactly which chunks were used
    # (the "Sources" line appended below).

    context = "\n\n".join(
        f"[Chunk {i+1}]\n{chunk}"
        for i, chunk in zip(relevant_indices, relevant_chunks)
    )


    context = f"""
    Selected Paper Title:
    {paper_title}

    Filename:
    {paper_filename}

    Research Content:
    {context}
    """


    # Step 3: Generate final AI answer
    answer = generate_answer(
        question,
        context
    )

    sources = ", ".join(f"Chunk {i+1}" for i in relevant_indices)

    # This is what makes this agent's answers verifiable —
    # unlike the Analysis/Comparison/Innovation agents, the
    # user can trace every answer back to specific chunks.
    
    answer += f"\n\n---\n**📌 Sources:** {sources} of *{paper_title}*"


    return answer