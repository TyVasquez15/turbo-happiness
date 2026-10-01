import mathematics.whoami as math_whoami
import mathematics.numbers.whoami as numbers_whoami
import mathematics.numbers.series as series
import mathematics.numbers.simple as simple
import mathematics.geometry.whoami as geometry_whoami
import mathematics.geometry.circle as circle
import mathematics.geometry.rectangle as rectangle
import mathematics.geometry.cube as cube


print("===== MATHEMATICS =====")
print(math_whoami.getname())

print("\n===== NUMBERS =====")
print(numbers_whoami.getname())

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Sum:", series.sum(list=numbers))
print("Average:", series.average(list=numbers))

print("\n===== SIMPLE =====")
print("Addition:", simple.addition(left=10, right=5))
print("Subtraction:", simple.subtraction(left=10, right=5))
print("Multiplication:", simple.multiplication(left=10, right=5))
print("Division:", simple.division(left=10, right=5))

print("\n===== GEOMETRY =====")
print(geometry_whoami.getname())

print("\nCircle")
print("Circumference:", circle.circumference(radius=5))
print("Area:", circle.area(radius=5))

print("\nRectangle")
print("Perimeter:", rectangle.perimeter(length=10, width=5))
print("Area:", rectangle.area(length=10, width=5))

print("\nCube")
print("Surface Area:", cube.surface_area(side=4))
print("Volume:", cube.volume(side=4))