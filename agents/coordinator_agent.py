# ==========================================================
# COORDINATOR AGENT
# Rule-based intent router — NO LLM call happens here.
# Reads the user's question as plain text and decides which
# specialist agent(s) should handle it, based on keyword
# matching. Order of the if/elif chain matters: more specific
# combined-intent rules must come BEFORE the general single-
# intent rules, or they'll never be reached.
# ==========================================================


ANALYSIS_KEYWORDS = ["summary", "summarize", "summarise", "analysis", "analyze",
                     "analyse", "method", "methodology", "dataset", "results",
                     "paper overview", "overview"]
QA_KEYWORDS = ["what", "why", "how", "when", "who", "explain", "describe",
               "meaning", "stand", "brief"]
COMPARISON_KEYWORDS = ["compare", "difference", "similarity", "better", "versus", "vs"]
INNOVATION_KEYWORDS = ["research gap", "future work", "improvement", "innovation", "limitations"]


def route_query(user_query):
    """
    Detects the user's intent and returns
    which AI agent(s) should handle the request.
    """

    query = user_query.lower()


    # ---- Combined-intent rule ----
    # Catches queries that need two agents at once, e.g.
    # "compare these papers and suggest future improvements".
    # If this block were placed after the single-word checks
    # below, the "compare" keyword would already have matched
    # the Comparison-only rule and this block would never run.

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


    # ---- Single-intent: Analysis ----

    # ==========================
    # Research Analysis
    # ==========================
    elif any(word in query for word in ANALYSIS_KEYWORDS):
        
        return {
            "agents": ["Research Analysis Agent"],
            "keys": ["analysis"]
        }

    # ---- Single-intent: Q&A ----
    # NOTE: this is checked before generic "compare"/"gap"
    # keywords, so a question like "what is the difference..."
    # will match "what" here rather than falling through to
    # the Comparison rule below. Keep this ordering in mind
    # if you add new keywords.

    # ==========================
    # Research Q&A
    # ==========================
    elif any(word in query for word in QA_KEYWORDS):
        
        return {
            "agents": ["Research Q&A Agent"],
            "keys": ["qa"]
        }

    # ---- Single-intent: Comparison ----

    # ==========================
    # Comparison
    # ==========================
    elif any(word in query for word in COMPARISON_KEYWORDS):

        return {
            "agents": ["Comparative Intelligence Agent"],
            "keys": ["comparison"]
        }

    # ---- Single-intent: Innovation ----

    # ==========================
    # Innovation
    # ==========================
    elif any(word in query for word in INNOVATION_KEYWORDS):

        return {
            "agents": ["Research Innovation Agent"],
            "keys": ["innovation"]
        }

    # ---- Fallback ----
    # If nothing matched, default to Analysis rather than
    # showing an error — a paper summary is a safe, useful
    # default response for almost any unrecognized question.

    # ==========================
    # Default
    # ==========================
    else:

        return {
            "agents": ["Research Analysis Agent"],
            "keys": ["analysis"]
        }