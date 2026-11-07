from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv

load_dotenv()


def pick_llm(level: str):

    if level.lower() == "low":
        # Query Curation
        llm = ChatOpenRouter(
            model="openrouter/free",
            temperature=0
        )

    elif level.lower() == "medium":
        # SQL Generation
        llm = ChatOpenRouter(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            temperature=0
        )

    elif level.lower() == "high":
        # Result Representation
        llm = ChatOpenRouter(
            model="nvidia/nemotron-3-ultra-550b-a55b:free",
            temperature=0
        )

    elif level.lower() == "claude":
        llm = ChatOpenRouter(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        temperature=0
        )

    else:
        raise ValueError(f"Unsupported level: {level}")

    return llm


if __name__ == "__main__":
    # Example usage of the pick_llm function
    llm_obj = pick_llm("claude")

    response = llm_obj.invoke(
        "Write an sql query to join two tables with name A and B on the column id and select all columns from both tables"
    )

    print(response.content)
