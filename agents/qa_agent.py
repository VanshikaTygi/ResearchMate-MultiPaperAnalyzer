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

    print(f"Top K Selected: {top_k}")
    

    # Step 1: Retrieve relevant research content
    relevant_chunks = search_vector_store(
        question,
        vector_store,
        embedding_model,
        chunks,
        top_k=top_k
    )

    print("=" * 80)
    print(f"Question: {question}")
    print(f"Total Retrieved Chunks: {len(relevant_chunks)}")

    for i, chunk in enumerate(relevant_chunks):
        print("=" * 60)
        print(f"Chunk {i+1}")
        print(chunk[:800])


    # Step 2: Combine retrieved chunks
    context = "\n\n".join(relevant_chunks)

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


    return answer