from utils.vector_store import search_vector_store
from utils.llm import generate_answer


def research_qa_agent(
        question,
        vector_store,
        embedding_model,
        chunks
):

    # Step 1: Retrieve relevant research content
    relevant_chunks = search_vector_store(
        question,
        vector_store,
        embedding_model,
        chunks
    )


    # Step 2: Combine retrieved chunks
    context = "\n\n".join(relevant_chunks)


    # Step 3: Generate final AI answer
    answer = generate_answer(
        question,
        context
    )


    return answer