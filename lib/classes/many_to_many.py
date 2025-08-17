class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("name must not be empty")
        self._name = name.strip()

    @property
    def name(self):
        return self._name  

    def articles(self):
        arts = [article for article in Article.all if article.author == self]
        return arts if arts else None

    def magazines(self):
        arts = self.articles()
        if not arts:
            return None
        return list({article.magazine for article in arts})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list({mag.category for mag in mags})


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be a string")
        if len(value.strip()) == 0:
            raise ValueError("category must not be empty")
        self._category = value

    def articles(self):
        arts = [article for article in Article.all if article.magazine == self]
        return arts if arts else None

    def contributors(self):
        arts = self.articles()
        if not arts:
            return None
        return list({article.author for article in arts})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None
        authors = [article.author for article in arts]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None
