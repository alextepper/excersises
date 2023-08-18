from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Book
import json


def list_books(request):
    # Retrieve all books
    books = Book.objects.all()

    # Manually serialize the books
    books_list = []
    for book in books:
        books_list.append({
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date.strftime('%Y-%m-%d'),  # Convert date to string
            'description': book.description,
            'page_count': book.page_count,
            'categories': book.categories,
            'thumbnail_url': book.thumbnail_url,
        })

    return JsonResponse(books_list,
                        safe=False)  # 'safe' is set to False because we're passing a list instead of a dictionary


def book_detail(request, id):
    try:
        # Retrieve the book by its ID
        book = Book.objects.get(id=id)

        # Serialize the book details
        book_data = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date.strftime('%Y-%m-%d'),
            'description': book.description,
            'page_count': book.page_count,
            'categories': book.categories,
            'thumbnail_url': book.thumbnail_url,
        }

        return JsonResponse(book_data)

    except Book.DoesNotExist:
        # Return a 404 response if the book does not exist
        raise Http404("Book not found.")


@csrf_exempt  # Temporarily disable CSRF protection for demonstration. Please see notes below.
@require_POST
def create_book(request):
    # Load POST data (assuming JSON format)
    data = json.loads(request.body)

    # Validate the data (basic validation for demonstration; consider using Django Forms for more robust validation)
    if not all(k in data for k in ["title", "author", "published_date", "description", "page_count", "categories"]):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    # Create the Book object
    try:
        book = Book.objects.create(
            title=data["title"],
            author=data["author"],
            published_date=data["published_date"],
            description=data["description"],
            page_count=data["page_count"],
            categories=data["categories"],
            thumbnail_url=data.get("thumbnail_url", "")  # thumbnail_url is optional
        )
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    # Return the new book’s data
    return JsonResponse({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date.strftime('%Y-%m-%d'),
        "description": book.description,
        "page_count": book.page_count,
        "categories": book.categories,
        "thumbnail_url": book.thumbnail_url,
    })
