 Import chatbot and trainer classes
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot(
    'TerminalBot',
    read_only=True,  # No learning after training
    logic_adapters=['chatterbot.logic.BestMatch']  # Use best match for responses
)

# Set up trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# Train on English corpus
try:
    print("Training TerminalBot...")
    trainer.train("chatterbot.corpus.english")
    print("Training done!")
except Exception as e:
    print(f"Training failed: {e}")
