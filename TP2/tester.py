import re

def markdown_to_html(markdown):
    # Lista numerada
    html = re.sub(r'^(\d+\.)\s+(.*)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    html = f'<ol>\n{html}</ol>'
    return html

def main():
    markdown = ""
    print("Insira o texto Markdown (insira 'fim' em uma nova linha para terminar):")
    while True:
        line = input()
        if line.strip().lower() == "fim":
            break
        markdown += line + "\n"

    html = markdown_to_html(markdown)
    print(html)

if __name__ == '__main__':
    main()
