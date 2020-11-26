######### GOOD THINGS TO KNOW TO TEST DB###############

# dropdb ptremix
# createdb ptremix

# db.create_all()

# Run functions from seed file. 

# Make a routine:

r1 = Routine(user_id=1, duration=10, date_created=datetime.now())
db.session.add(r1)

# Make some injury-exercise relationships:

def add_injury_to_exercises(injury_type_id, exercise_ids):
    injury = InjuryType.query.get(injury_type_id)
    for ex_id in exercise_ids:
        exercise = Exercise.query.get(ex_id)
        exercise.injuries.append(injury)
    db.session.commit()        


# add all exercises to an injury

add_injury_to_exercises(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# get exercises by injury ID
def get_exercises_by_injury(injury_id):

    ex_by_inj = InjuryType.query.get(injury_id).exercises
    return ex_by_inj

# get most recent routine by user (where user_id = 1)
query = Routine.query.order_by(Routine.date_created.desc()).filter(Routine.user_id==1).first()


db.session.commit()


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
