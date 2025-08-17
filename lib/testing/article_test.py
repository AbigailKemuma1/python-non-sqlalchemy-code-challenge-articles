class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must not be empty")
        self._name = name

    @property
    def name(self):
        return self._name  # read-only, cannot change

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Magazine category must be a string")
        if len(category) == 0:
            raise ValueError("Magazine category cannot be empty")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        """Return all Article instances in this magazine"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique Authors who have written for this magazine"""
        return list({article.author for article in self.articles()})

    def article_titles(self):
        """Return list of titles of all articles in this magazine"""
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        """Return authors who have written more than 2 articles in this magazine"""
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]


class Article:
    all = []  # single source of truth

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine instance")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("title must be a string between 5 and 50 characters")

        self._author = author
        self._magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
