import pyfiglet

def list_figlet_styles():
    """Returns a list of all available figlet fonts."""
    return pyfiglet.FigletFont.getFonts()  

def generate_ascii_art(text, style):
    """Generates ASCII art using pyfiglet."""
    return pyfiglet.Figlet(font=style).renderText(text)

# Get all available figlet styles
figlet_styles = list_figlet_styles()

# Display the styles with numbers
print(f"\nAvailable Figlet Styles ({len(figlet_styles)} styles):")
for i, style in enumerate(figlet_styles, 1):
    print(f"{i}. {style}")

# User selects a style by number
try:
    style_number = int(input("\nEnter the number of your preferred style: "))
    if 1 <= style_number <= len(figlet_styles):
        chosen_style = figlet_styles[style_number - 1]
        text = input("Enter text for ASCII art: ")
        print(generate_ascii_art(text, chosen_style))
    else:
        print("Invalid number chosen. Please run the script again.")
except ValueError:
    print("Invalid input. Please enter a number.")
