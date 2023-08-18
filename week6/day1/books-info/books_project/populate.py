import requests
from datetime import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')
import django

# Set up Django environment
django.setup()

from books.models import Book

def populate_books(search_term):
    API_ENDPOINT = 'https://www.googleapis.com/books/v1/volumes?q={}'
    response = requests.get(API_ENDPOINT.format(search_term))

    if response.status_code == 200:
        books_data = response.json().get('items', [])

        for entry in books_data:
            volume_info = entry.get('volumeInfo', {})
            title = volume_info.get('title', '')
            author = ', '.join(volume_info.get('authors', []))
            description = volume_info.get('description', '')
            page_count = volume_info.get('pageCount', 0)
            categories = ', '.join(volume_info.get('categories', []))
            thumbnail_url = volume_info.get('imageLinks', {}).get('thumbnail', '')

            # Convert published date to a datetime object
            published_date_str = volume_info.get('publishedDate', '')
            try:
                # Handle different date formats
                if '-' in published_date_str:
                    published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()
                else:
                    published_date = datetime.strptime(published_date_str, '%Y').date()
            except ValueError:
                published_date = None

            # Create the Book object
            Book.objects.create(
                title=title,
                author=author,
                published_date=published_date,
                description=description,
                page_count=page_count,
                categories=categories,
                thumbnail_url=thumbnail_url
            )

if __name__ == '__main__':
    search_terms = ["python", "django"]
    for term in search_terms:
        populate_books(term)
        print(f"Books related to '{term}' have been added.")
