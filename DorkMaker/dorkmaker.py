import time

def generate_dorks(text: str, dork_file: str) -> list[str]:
    with open(dork_file, 'r') as file:
        dorks = [line.strip() for line in file if line.strip()]

    result = [word + dork for word in text.split() for dork in dorks]

    return result


if __name__ == '__main__':
    text_input = input("Enter the text: ")
    dork_file = "dork.txt"  # Update with your dork file path
    
    # Start the loading animation
    print("Generating dorks...", end='', flush=True)
    for i in range(10):
        time.sleep(0.2)
        print(".", end='', flush=True)
    print()
    
    result = generate_dorks(text_input, dork_file)
    
    with open("dorklist.txt", 'w', encoding='utf-8') as file:
        file.write('\n'.join(result))
    print(f"Generated {len(result)} dorks have been saved in dorklist.txt file.")
