from director import Director
from concretebuilder1 import Concretebuilder1

director = Director()
builder = Concretebuilder1()

director.builder = builder

print("\nobiekt minimalny")
director.build_minimal_version()
builder.product.list_parts()

print("\nobiekt pełny")
director.build_full_version()
builder.product.list_parts()

print("\nobiekt specjalny (AC)")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
