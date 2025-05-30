from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def debug():
    """Interactive debugging session."""
    print("Debugging Session")
    print("1. All Authors:")
    for author in [Author.find_by_id(i) for i in range(1, 4)]:
        if author:
            print(f"ID: {author.id}, Name: {author.name}")

    print("\n2. All Magazines:")
    for mag in Magazine.find_by_category("Technology") + Magazine.find_by_category("News"):
        print(f"ID: {mag.id}, Name: {mag.name}, Category: {mag.category}")

    print("\n3. Articles by Author 1:")
    author = Author.find_by_id(1)
    for article in author.articles():
        print(f"Title: {article.title}, Magazine ID: {article.magazine_id}")

    print("\n4. Top Publisher:")
    top = Magazine.top_publisher()
    if top:
        print(f"Top Magazine: {top.name}, Category: {top.category}")

    print("\n5. Most Prolific Author:")
    prolific = Article.most_prolific_author()
    if prolific:
        print(f"Most Prolific Author: {prolific.name}")

if __name__ == "__main__":
    debug()