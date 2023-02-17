#!/usr/bin/python3
import os
import markdown

# Constants for templates and output folder
TEMPLATE_DIR = "templates"
OUTPUT_DIR = "output"

# Load templates
with open(os.path.join(TEMPLATE_DIR, "base.html")) as f:
    base_template = f.read()
with open(os.path.join(TEMPLATE_DIR, "home.html")) as f:
    home_template = f.read()
with open(os.path.join(TEMPLATE_DIR, "article.html")) as f:
    article_template = f.read()
with open(os.path.join(TEMPLATE_DIR, "404.html")) as f:
    error_404_template = f.read()


def generate_article(filename):
    with open(filename) as f:
        content = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(content)

    # Replace template placeholders with actual content
    html = article_template.replace("{{content}}", html)
    html = base_template.replace("{{content}}", html)

    # Write output to file
    output_filename = os.path.join(OUTPUT_DIR, os.path.splitext(os.path.basename(filename))[0] + ".html")
    with open(output_filename, "w") as f:
        f.write(html)


def generate_homepage():
    # Replace template placeholders with actual content
    html = home_template
    html = base_template.replace("{{content}}", html)

    # Write output to file
    output_filename = os.path.join(OUTPUT_DIR, "index.html")
    with open(output_filename, "w") as f:
        f.write(html)


def generate_404():
    # Replace template placeholders with actual content
    html = error_404_template
    html = base_template.replace("{{content}}", html)

    # Write output to file
    output_filename = os.path.join(OUTPUT_DIR, "404.html")
    with open(output_filename, "w") as f:
        f.write(html)


if __name__ == "__main__":
    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Generate articles
    articles_dir = "articles"
    for filename in os.listdir(articles_dir):
        generate_article(os.path.join(articles_dir, filename))

    # Generate homepage and error pages
    generate_homepage()
    generate_404()
