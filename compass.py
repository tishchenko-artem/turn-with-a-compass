def direction(facing: str, turn: int) -> str:
    compass = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    try:
        if turn > 1800 or turn < -1800:
            raise ValueError

        return compass[(compass.index(facing) + turn // 45) % 8]

    except ValueError:
        print("Turn cannot be more than 1800 or less than -1800 degrees")
