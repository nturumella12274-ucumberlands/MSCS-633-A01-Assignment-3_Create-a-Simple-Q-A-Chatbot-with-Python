from chatbot import chatbot

def chat():
    """
    Runs the TerminalBot chat interface.
    
    The user can interact with the chatbot by typing messages.
    Type 'exit' to quit the chat.
    """
    # Print welcome message with instructions
    print("Welcome to TerminalBot! Type 'exit' to quit.\n")
    
    # Start the chat loop
    while True:
        try:
            # Prompt user for input
            user_input = input("user: ")
            
            # Check if the user wants to exit, ignoring case and whitespace
            if user_input.lower().strip() == 'exit':
                print("bot: Goodbye!")
                break
            
            # Generate and display the bot's response
            response = chatbot.get_response(user_input)
            print(f"bot: {response}\n")
        
        except (KeyboardInterrupt, EOFError):
            # Handle graceful exit on Ctrl+C or EOF
            print("\nbot: Goodbye!")
            break
        
        except Exception as e:
            # Handle errors from response generation
            print(f"bot: Sorry, I encountered an error: {e}\n")

# Run the chat function if this script is executed directly
if __name__ == "__main__":
    chat()
