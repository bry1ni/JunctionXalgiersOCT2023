import openai

openai.api_key = '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'


def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def generate_questions_with_gpt(text):
    prompt = f"Generate multiple-choice questions and answers based on the following text:\n{text}\n\nQuestion:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()


text_content = read_text_from_file('course.txt')

if text_content is not None:
    generated_questions = generate_questions_with_gpt(text_content)
    print("Generated Questions:")
    print(generated_questions)
