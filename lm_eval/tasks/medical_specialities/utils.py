def doc_to_text(doc) -> str:
    """
    Question: <question>
    Choices:
    A. <choice1>
    B. <choice2>
    C. <choice3>
    D. <choice4>
    Answer:
    """
    choices = [doc["op1-fa"], doc["op2-fa"], doc["op3-fa"], doc["op4-fa"]]
    option_choices = {'A': choices[0], 'B': choices[1], 'C': choices[2], 'D': choices[3]}

    prompt = "Question: " + doc["question-fa"][:-1] + "\nChoices:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Answer:"
    return prompt


def doc_to_target(doc) -> int:
    return int(doc["cop"])-1
