from lib.models.article import Article

def test_article_creation():
    article = Article("Test Article", 1, 1)
    article.save()
    assert article.id is not None
