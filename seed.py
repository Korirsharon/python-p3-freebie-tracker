#!/usr/bin/env python3

# Script goes here!
from models import Company, Dev, Freebie, session

def seed_database():
    # Clear existing data
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    
    # Create companies
    safaricom = Company(name="Safaricom", founding_year=1998)
    deloitte = Company(name="Deloitte", founding_year=1994)
    microsoft = Company(name="Microsoft", founding_year=1975)
    
    # Create devs
    sharon = Dev(name="Sharon")
    faith = Dev(name="Faith")
    charlie = Dev(name="Charlie")
    
    # Create freebies
    freebies = [
        Freebie(item_name="T-shirt", value=20, dev=sharon, company=safaricom),
        Freebie(item_name="Stickers", value=5, dev=sharon, company=deloitte),
        Freebie(item_name="Water Bottle", value=15, dev=faith, company=safaricom),
        Freebie(item_name="Laptop", value=1200, dev=charlie, company=microsoft),
        Freebie(item_name="USB Drive", value=10, dev=faith, company=microsoft)
    ]
    
    session.add_all([safaricom, deloitte, microsoft, sharon, faith, charlie] + freebies)
    session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()