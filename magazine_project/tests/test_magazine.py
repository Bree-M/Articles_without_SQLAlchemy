from lib.models.magazine import Magazine

def test_magazine_creation():
    mag = Magazine("Tech", "Tech Category")
    mag.save()
    assert mag.id is not None
