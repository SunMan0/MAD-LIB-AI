import openai

# Replace with your OpenAI API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_story_prompt(user_input):
    # Generate a prompt for the AI to understand the user's story request
    prompt = f"Generate a story about {user_input}. The story should be in a Mad Lib style. Here's the story:"
    return prompt

def get_mad_lib_question(story, user_input):
    # Generate a Mad Lib question based on the user's story request
    # You can create a predefined set of Mad Lib questions or generate them dynamically.
    # For example:
    mad_lib_question = f"Give me a {user_input} that you find in the story."
    return mad_lib_question

def generate_mad_lib_story(user_input):
    # Generate a Mad Lib-style story
    prompt = generate_story_prompt(user_input)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200  # Adjust this based on the desired story length
    )
    story = response.choices[0].text.strip()
    
    # Get the Mad Lib question
    mad_lib_question = get_mad_lib_question(story, user_input)
    
    return story, mad_lib_question

# Main loop
while True:
    user_input = input("Describe a story you want: ")
    story, mad_lib_question = generate_mad_lib_story(user_input)
    
    print("Story:")
    print(story)
    
    user_answer = input(mad_lib_question + " ")
    
    # Replace the Mad Lib placeholder in the story with the user's answer
    story = story.replace(f'[{user_input}]', user_answer)
    
    print("Your Mad Lib Story:")
    print(story)
    
    continue_playing = input("Do you want to create another story (yes/no)? ")
    if continue_playing.lower() != "yes":
        break
