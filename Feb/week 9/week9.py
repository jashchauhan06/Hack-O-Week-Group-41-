# Week 9: Multi-channel Deployment Mockup
# Plan and prototype how the chatbot would behave on web and WhatsApp

class ChatbotChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.message_format = self._get_format()
    
    def _get_format(self):
        """Define message format for each channel"""
        formats = {
            'web': {
                'max_length': 1000,
                'supports_html': True,
                'supports_buttons': True,
                'supports_images': True
            },
            'whatsapp': {
                'max_length': 4096,
                'supports_html': False,
                'supports_buttons': True,
                'supports_images': True
            },
            'console': {
                'max_length': None,
                'supports_html': False,
                'supports_buttons': False,
                'supports_images': False
            }
        }
        return formats.get(self.channel_name, formats['console'])
    
    def format_message(self, message, buttons=None):
        """Format message according to channel capabilities"""
        formatted = f"[{self.channel_name.upper()}]\n"
        
        # Truncate if needed
        if self.message_format['max_length']:
            message = message[:self.message_format['max_length']]
        
        # Add HTML formatting if supported
        if self.message_format['supports_html']:
            formatted += f"<div class='bot-message'>{message}</div>\n"
        else:
            formatted += f"{message}\n"
        
        # Add buttons if supported
        if buttons and self.message_format['supports_buttons']:
            formatted += "\nQuick Actions:\n"
            for i, btn in enumerate(buttons, 1):
                formatted += f"  [{i}] {btn}\n"
        
        return formatted
    
    def send_message(self, message, buttons=None):
        """Simulate sending message on channel"""
        formatted = self.format_message(message, buttons)
        print(formatted)
        return {'status': 'sent', 'channel': self.channel_name}

class MultiChannelBot:
    def __init__(self):
        self.channels = {
            'web': ChatbotChannel('web'),
            'whatsapp': ChatbotChannel('whatsapp'),
            'console': ChatbotChannel('console')
        }
    
    def process_query(self, query, channel='console'):
        """Process query and respond on specified channel"""
        # Simple response logic
        response = f"You asked: '{query}'\n\nHere's the information you requested..."
        
        # Channel-specific buttons
        buttons = ['Check Exam Schedule', 'View Fees', 'Contact Support']
        
        # Send via appropriate channel
        if channel in self.channels:
            return self.channels[channel].send_message(response, buttons)
        else:
            return {'status': 'error', 'message': 'Unknown channel'}

def deploy_multichannel():
    """Interactive multi-channel deployment"""
    bot = MultiChannelBot()
    
    print("=" * 60)
    print("Multi-channel Deployment Mockup - Week 9")
    print("=" * 60)
    print("\nThis bot simulates deployment across different channels.")
    print("Available channels: web, whatsapp, console")
    print("Type 'exit' or 'quit' to stop.")
    print("Type 'channel <name>' to switch channels (e.g., 'channel web')\n")
    
    current_channel = 'console'
    print(f"Current channel: {current_channel.upper()}\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['exit', 'quit']:
            print("\nThank you for using the Multi-channel bot!")
            break
        
        if user_input.lower().startswith('channel '):
            new_channel = user_input.split(' ', 1)[1].lower()
            if new_channel in bot.channels:
                current_channel = new_channel
                print(f"\n[Switched to {current_channel.upper()} channel]\n")
            else:
                print(f"\n[Unknown channel. Available: web, whatsapp, console]\n")
            continue
        
        if not user_input:
            continue
        
        result = bot.process_query(user_input, current_channel)
        print()

if __name__ == "__main__":
    deploy_multichannel()
