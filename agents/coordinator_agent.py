def route_query(user_query):
    """
    Detects the user's intent and returns
    which AI agent(s) should handle the request.
    """

    query = user_query.lower()


    # ==========================
    # Combined Requests (Highest Priority)
    # ==========================
    if (
        "compare" in query and
        (
            "future" in query or
            "improvement" in query or
            "research gap" in query or
            "innovation" in query
        )
    ):
        return {
            "agents": [
                "Comparative Intelligence Agent",
                "Research Innovation Agent"
            ],
            "keys": [
                "comparison",
                "innovation"
            ]
        }

    # ==========================
    # Research Analysis
    # ==========================
    elif any(word in query for word in [
        "summary",
        "summarize",
        "summarise",
        "analysis",
        "analyze",
        "analyse",
        "method",
        "methodology",
        "dataset",
        "results",
        "paper overview",
        "overview"
    ]):
        
        return {
            "agents": ["Research Analysis Agent"],
            "keys": ["analysis"]
        }

    # ==========================
    # Research Q&A
    # ==========================
    elif any(word in query for word in [
        "what",
        "why",
        "how",
        "when",
        "who",
        "explain",
        "describe",
        "meaning",
        "stand",
        "brief"
    ]):
        
        return {
            "agents": ["Research Q&A Agent"],
            "keys": ["qa"]
        }

    # ==========================
    # Comparison
    # ==========================
    elif any(word in query for word in [
        "compare",
        "difference",
        "similarity",
        "better",
        "versus",
        "vs"
    ]):

        return {
            "agents": ["Comparative Intelligence Agent"],
            "keys": ["comparison"]
        }

    # ==========================
    # Innovation
    # ==========================
    elif any(word in query for word in [
        "research gap",
        "future work",
        "improvement",
        "innovation",
        "limitations"
    ]):

        return {
            "agents": ["Research Innovation Agent"],
            "keys": ["innovation"]
        }

    # ==========================
    # Default
    # ==========================
    else:

        return {
            "agents": ["Research Analysis Agent"],
            "keys": ["analysis"]
        }