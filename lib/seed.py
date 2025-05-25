from database import Base, engine, session
from models import Dev, Company, Freebie

# Reset database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Seed data
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

company1 = Company(name="OpenAI", founding_year=2015)
company2 = Company(name="GitHub", founding_year=2008)

session.add_all([dev1, dev2, company1, company2])
session.commit()

freebie1 = Freebie(item_name="T-shirt", value=15, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker", value=5, dev=dev2, company=company1)
freebie3 = Freebie(item_name="Mug", value=20, dev=dev1, company=company2)

session.add_all([freebie1, freebie2, freebie3])
session.commit()
