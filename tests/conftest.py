import pytest
from app import create_app
from app.extensions.database import db
from app.models.category import CategoryModel
from app.models.topic import TopicModel
from app.models.user import UserModel
from app.models.comment import CommentModel
from app.utils.auth import make_hash
from app.extensions.config import TestingConfig


@pytest.fixture(scope='module')
def app():
    app = create_app(config_class=TestingConfig)
    with app.app_context():
        yield app


@pytest.fixture(scope='module')
def client(app):
    return app.test_client()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='module')
def test_user(init_database):
    user = UserModel(email="test@example.com", username="test", password=make_hash("password"))
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture(scope="module")
def test_category(init_database):
    category = CategoryModel(title="test category")
    db.session.add(category)
    db.session.commit()
    return category


@pytest.fixture(scope="module")
def test_topic(init_database, test_user, test_category):
    topic = TopicModel(
        title="test topic",
        body="body of test topic",
        user_id=test_user.id,
        category_id=test_category.id
    )
    db.session.add(topic)
    db.session.commit()
    return topic


@pytest.fixture(scope="module")
def test_comment(init_database, test_user, test_topic):
    comment = CommentModel(
        body="body of test topic",
        user_id=test_user.id,
        topic_id=test_topic.id
    )
    db.session.add(comment)
    db.session.commit()
    return comment
