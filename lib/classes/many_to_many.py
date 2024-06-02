class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._title = title
        self.author = author
        self.magazine = magazine
        self.validate_title(title)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    def validate_title(self, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

class Author:
    def __init__(self, name):
        self._name = name
        self.articles_list = []
        self.validate_name(name)

    @property
    def name(self):
        return self._name

    def validate_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self.articles_list.append(article)
        return article

    def articles(self):
        return self.articles_list

    def magazines(self):
        return list({article.magazine for article in self.articles_list})

    def topic_areas(self):
        return list({article.magazine.category for article in self.articles_list}) if self.articles_list else None

class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.articles_list = []
        self.validate_name(name)
        self.validate_category(category)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self._name = value

    def validate_name(self, name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self.validate_category(value)
        self._category = value

    def validate_category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return self.articles_list

    def add_article(self, author, title):
        article = Article(author, self, title)
        self.articles_list.append(article)
        return article

    def contributors(self):
        return list({article.author for article in self.articles_list})

    def article_titles(self):
        return [article.title for article in self.articles_list] if self.articles_list else None

    def contributing_authors(self):
        authors_count = {}
        for article in self.articles_list:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        return [author for author, count in authors_count.items() if count > 2] if self.articles_list else None
