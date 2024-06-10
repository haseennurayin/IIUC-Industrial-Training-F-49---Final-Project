from sqlalchemy.orm import Session
from . import models, schemas

def get_news(db: Session, news_id: int):
    result = db.query(models.News).filter(models.News.id == news_id).first()
    return result

def get_news_list(db: Session, skip: int = 0, limit: int = 10):
    query = db.query(models.News).offset(skip).limit(limit)
    news_list = query.all()
    return news_list

def get_or_create_category(db: Session, name: str, description: str):
    category = db.query(models.Category).filter(models.Category.name == name).first()
    if not category:
        category = models.Category(name=name, description=description)
        db.add(category)
        db.commit()
        db.refresh(category)
    return category

def get_or_create_reporter(db: Session, name: str, email: str):
    reporter = db.query(models.Reporter).filter(models.Reporter.name == name).first()
    if not reporter:
        reporter = models.Reporter(name=name, email=email)
        db.add(reporter)
        db.commit()
        db.refresh(reporter)
    return reporter

def get_or_create_publisher(db: Session, name: str, website: str):
    publisher = db.query(models.Publisher).filter(models.Publisher.name == name).first()
    if not publisher:
        publisher = models.Publisher(name=name, website=website)
        db.add(publisher)
        db.commit()
        db.refresh(publisher)
    return publisher

def get_news_existance(db: Session, news_title: str):
    existing_news = db.query(models.News).filter(models.News.title == news_title).first()
    return existing_news

def create_image(db: Session, news_id: int, url: str):
    db_image = models.Image(news_id=news_id, url=url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def create_news(db: Session, news: schemas.NewsCreate):
    category = get_or_create_category(db, news.news_category, f"{news.news_category} description")
    reporter = get_or_create_reporter(db, news.news_reporter, f"{news.news_reporter}@gmail.com")
    publisher = get_or_create_publisher(db, news.news_publisher, f"https://{news.publisher_website}")
    
    existing_news = get_news_existance(db, news_title=news.title)
    if existing_news:
        return existing_news

    db_news = models.News(
        title=news.title,
        datetime=news.datetime,
        body=news.body,
        link=news.link,
        category_id=category.id,
        reporter_id=reporter.id,
        publisher_id=publisher.id
    )
    db.add(db_news)
    db.commit()
    db.refresh(db_news)

    for image_url in news.images:
        create_image(db, news_id=db_news.id, url=image_url)

    return db_news
