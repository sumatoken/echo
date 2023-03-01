from prompt_engine.chat_engine import ChatEngine, ChatEngineConfig
from prompt_engine.model_config import ModelConfig
from prompt_engine.interaction import Interaction
import openai
import os


def generatePrompt(query):
    config = ChatEngineConfig(ModelConfig(max_tokens=1024))
    description = "You are a robot capable of holding conversations with intellectual humans. You always make your answer as short as possible"
    examples = [
        Interaction("Hello", "Hey, how are you?"),
        Interaction("I am feeling okay, and you?", "I'm in my best shape!"),
        Interaction(
            "How many characters are in an average two sentences?",
            "Depending on the length of the sentences, the exact number of characters can vary. However, an average two sentences would usually be around 60-80 characters.",
        ),
        Interaction(
            "What is a quantum state?",
            "In quantum mechanics, a quantum state is a precise mathematical description of a physical system that includes both position and momentum.",
        ),
        Interaction(
            "What is Compton effect?",
            "The Compton effect, first described by Arthur Holly Compton, is the phenomenon in which an x-ray or gamma ray photon interacts with an electron, resulting in the photon's energy being partially transferred to the electron.",
        ),
        Interaction(
            "How can I generate signals exploiting the properties of operational amplifiers?",
            "Operational amplifiers (or op amps) can be used to generate various types of signals. For example, you can use the op amp to generate a sine wave by combining a non-inverting and inverting amplifier, or you can use the op amp to generate a square wave by using hysteresis.",
        ),
    ]
    chat_engine = ChatEngine(config=config, description=description, examples=examples)
    return chat_engine.build_prompt(query)


def generateResponse(prompt):
    openai.organization = "org-xwIudUz9vZhKbTbBroTcMtfP"
    openai.api_key = os.environ.get("OPENAI_KEY")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        temperature=0.7,
    )
    return response.choices[0].text
