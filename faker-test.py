# Testing out Faker module

from faker import Faker
# could also do import faker

# allows me to do things like call faker_data.name, etc. to create records/pull fake info
# use faker_data.seed() to seed database? use faker_data.seed(5678) to make sure I'm getting
# the same data every time
faker_data = Faker()

