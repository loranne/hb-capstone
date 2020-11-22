######### GOOD THINGS TO KNOW TO TEST DB###############

# dropdb ptremix
# createdb ptremix

# db.create_all()

# Run functions from seed file. 


#######TRIED TO WRITE UNITTEST##########################
import unittest
import pytest
from crud import add_injury_to_exercise
import server
import model
import tempfile
import os

@pytest.fixture
def client():
    db_fd, server.app.config['DATABASE'] = tempfile.mkstemp()
    server.app.config['TESTING'] = True

    with server.app.test_client() as client:
        # with server.app.app_context():
        #     server.init_db()
        yield client

    os.close(db_fd)
    os.unlink(server.app.config['DATABASE'])

@pytest.mark.usefixtures("client")
class CrudTest(unittest.TestCase):

    def setUp(self):
        # app = create_app()
        # self.app = create_app(TestConfig)
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        # db.create_all()

        pass

    def tearDown(self):
        # db.session.remove()
        # db.drop_all()
        # self.app_context.pop()

        pass

    def test_add_ex_to_injury(self):

        exercise = model.Exercise.query.get(exercise_id)
        injury = model.InjuryType.query.get(injury_type_id)

        exercise.injuries.append(injury)

        model.db.session.commit()

        assert injury.exercises != []
        
    def test_method2(self):
        assert True
