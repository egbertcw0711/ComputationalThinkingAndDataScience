from ps2 import RectangularRoom, Position, Robot

import random
random.seed(0)

def test_RectRoom():
	my_room = RectangularRoom(2,2)
	assert my_room.getNumCleanedTiles() == 0, "getNumCleanedTiles method got wrong answer"
	assert my_room.isTileCleaned(1,0) == False, "It should be Flase but return True"
	my_room.cleanTileAtPosition(Position(1.1,0.1))
	assert my_room.isTileCleaned(1,0) == True, "It should be True but return False"
	assert my_room.getNumCleanedTiles() == 1, "getNumCleanedTiles method got wrong answer"

	assert my_room.getNumTiles() == 4, "getNumTiles method got wrong ansewer"
	
	for _ in range(10):
		my_room.cleanTileAtPosition(Position(1.1,0.1))
		assert my_room.getNumCleanedTiles() == 1, "getNumCleanedTiles method got wrong answer"

	print(my_room.getRandomPosition())
	print(my_room.getRandomPosition())

	assert my_room.isPositionInRoom(Position(0.5,0.5)) == True, "isPositionInRoom method got wrong answer"
	assert my_room.isPositionInRoom(Position(3,3)) == False, "isPositionInRoom method got wrong answer"

	print("RectangularRoom Class Test PASS!")

def test_Robot():
	"""
	Attention: the Robot is an abstract class
	"""
	room = RectangularRoom(5,5)
	robot = Robot(room, 1.0)
	print(robot.getRobotPosition())
	print(robot.getRobotDirection())

	robot.setRobotDirection(128)
	assert robot.getRobotDirection() == 128,\
	"getRobotDirection method got wrong result"

	robot.setRobotPosition(Position(3.5,4.5))
	# print(robot.getRobotPosition())
	# print(Position(3.5,4.5))
	assert robot.getRobotPosition().getX() == 3.5 and\
	robot.getRobotPosition().getY() == 4.5,\
	"getRobotPosition method got wrong result"

	print("Robot Class Test PASS!")



print("Testing RectangularRoom Class ... ")
test_RectRoom()

print("\nTesting Robot Class ... ")
test_Robot()