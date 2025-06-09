from lib.models.author import Author

def test_author_creation():
    author = Author("Test Author")
    author.save()
    assert author.id is not None