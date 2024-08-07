def get_input(prompt):
    """Prompt the user for input and return the input."""
    return input(prompt)

def get_story_choice():
    """Prompt the user to choose a story type and return the choice."""
    print("Choose a story type:")
    print("1. Fantasy")
    print("2. Sci-Fi")
    print("3. Horror/Thriller")
    choice = input("Enter the number of your choice: ")
    return choice

def main():
    # Define the parts of speech needed for each story type
    prompts = {
        "common": {
            "noun": "Enter a noun: ",
            "verb": "Enter a verb: ",
            "adjective": "Enter an adjective: ",
            "adverb": "Enter an adverb: ",
            "place": "Enter a place: ",
            "number": "Enter a number: ",
            "color": "Enter a color: "
        },
        "fantasy": {
            "animal": "Enter an animal: ",
            "food": "Enter a type of food: ",
            "emotion": "Enter an emotion: "
        },
        "sci-fi": {
            "planet": "Enter a planet name: ",
            "tech": "Enter a piece of futuristic technology: ",
            "alien": "Enter an alien species: "
        },
        "horror": {
            "scary_thing": "Enter something scary: ",
            "sound": "Enter a type of scary sound: ",
            "creature": "Enter a type of creepy creature: "
        }
    }

    # Define the story templates
    stories = {
        "1": (
            "In a distant {place}, there lived a {adjective} {animal} named {noun}. "
            "{noun} loved to {verb} {adverb}, dreaming of adventure. One sunny afternoon, "
            "{noun} discovered a {color} {food} that granted {number} wishes. Filled with {emotion}, "
            "{noun} wished for a world where everyone could {verb} freely. As the wishes came true, "
            "{place} turned into a land of {emotion} and joy. People traveled from far and wide to see the "
            "magical {animal} and the {color} {food} that made it all possible. From then on, {noun} and the "
            "residents of {place} lived happily ever after."
        ),
        "2": (
            "In the year 3000, on the planet {planet}, a {adjective} scientist named {noun} was working on a groundbreaking project. "
            "Using a revolutionary {tech}, {noun} managed to {verb} {adverb}. During the experiment, {noun} encountered a friendly "
            "{alien} who offered to share the secrets of the universe. Together, they built a {color} spaceship and set off on a journey to explore "
            "{number} different galaxies. The journey was filled with awe and excitement, and {noun} and the {alien} made discoveries that "
            "changed the course of history. The universe would never be the same thanks to the {adjective} scientist named {noun}."
        ),
        "3": (
            "One eerie night in {place}, a group of friends decided to explore a {adjective} mansion. As they ventured inside, they heard a "
            "{sound} echoing through the halls. Trembling with fear, {noun} led the way. They stumbled upon a {color} door, behind which lay "
            "a room filled with {scary_thing}. Suddenly, a {creature} appeared, causing everyone to {verb} {adverb}. They needed to find {number} "
            "keys to escape. With each key found, the mansion grew more {adjective}, and the {creature} became more menacing. In the end, {noun} "
            "and the friends managed to escape, promising never to return to the {adjective} mansion."
        )
    }

    story_choice = get_story_choice()

    # Map numeric choices to the corresponding story keys
    story_keys = {
        "1": "fantasy",
        "2": "sci-fi",
        "3": "horror"
    }

    # Determine the required inputs based on the story choice
    if story_choice in stories:
        story_key = story_keys[story_choice]
        required_prompts = {**prompts["common"], **prompts[story_key]}

        # Collect inputs from the user
        user_inputs = {}
        for key, prompt in required_prompts.items():
            user_inputs[key] = get_input(prompt)

        # Generate the story by replacing placeholders with user inputs
        story = stories[story_choice].format(**user_inputs)

        # Display the generated story
        print("\nHere's your story:")
        print(story)
    else:
        print("Invalid choice. Please restart the program and choose a valid story type.")

if __name__ == "__main__":
    main()
