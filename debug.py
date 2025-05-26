#!/usr/bin/env python3

from models import Company, Dev, Freebie, session

def test_models():
    print("=== TESTING COMPANY METHODS ===")
    
    oldest = Company.oldest_company()
    print(f"Oldest company: {oldest.name} (founded {oldest.founding_year})")  
    
    
    safaricom = session.query(Company).filter_by(name="Safaricom").first()
    print(f"\nSafaricom's freebies:")
    for freebie in safaricom.freebies:
        print(f"- {freebie.print_details()}")
    
    print(f"\nDevs who got Safaricom freebies:")
    for dev in safaricom.devs:
        print(f"- {dev.name}")

    print("\n=== TESTING DEV METHODS ===")
    sharon = session.query(Dev).filter_by(name="Sharon").first()
    print(f"\nSharon's freebies:")
    for freebie in sharon.freebies:
        print(f"- {freebie.item_name} (${freebie.value}) from {freebie.company.name}")
    
    print(f"\nDoes Sharon have a T-shirt? {sharon.received_one('T-shirt')}")  
    print(f"Does Sharon have a Laptop? {sharon.received_one('Laptop')}")    
    
    
    faith = session.query(Dev).filter_by(name="Faith").first()
    sharon_freebie = sharon.freebies[0]
    print(f"\nBefore give_away: {sharon_freebie.print_details()}")
    sharon.give_away(faith, sharon_freebie)
    print(f"After give_away: {sharon_freebie.print_details()}")  

    print("\n=== TESTING FREEBIE METHODS ===")
    laptop = session.query(Freebie).filter_by(item_name="Laptop").first()
    print(laptop.print_details())  

if __name__ == '__main__':
    test_models()
    session.commit()  