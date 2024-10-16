def game(factory: UnitFactory):
    warrior = factory.create_warrior()
    mage = factory.create_mage()
    
    print(warrior.attack())
    print(mage.attack())

# Użycie różnych rodów
print("Stark House:")
game(StarkFactory())

print("\nLannister House:")
game(LannisterFactory())

print("\nTargaryen House:")
game(TargaryenFactory())
