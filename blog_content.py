import random
from sqlalchemy.orm import sessionmaker
from faker import Factory
from user import engine, User, UserInfo, Category, Article, Tag

faker = Factory.create()
Session = sessionmaker(bind=engine)
session = Session()

faker_users = [User(
    username = faker.name(),
    password = faker.word(),
    email = faker.email(),
    ) for i in range(10)]
session.add_all(faker_users)

faker_categories = [Category(name=faker.word()) for i in range(5)]
session.add_all(faker_categories)

faker_tags = [Tag(name=faker.word()) for i in range(20)]
session.add_all(faker_tags)

for i in range(100):
    article = Article(
            title = faker.sentence(),
            content = ' '.join(faker.sentences(nb=random.randint(10,20))),
            author=random.choice(faker_users),
            categories=random.choice(faker_categories)
            )

    for tag in random.sample(faker_tags, random.randint(2,5)):
        article.tags.append(tag)
    session.add(article)

session.commit()
