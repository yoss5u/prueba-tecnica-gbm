"""
The minimum_jumps function calcualte wich is the minimum of jumps to reach x value in the OX-axis

The arg is the number to reach

return:
    if the value is is greater than or equal to 106 return False, in other case return a integer value that indicates the minimum of jumps
"""
def minimum_jumps(x):
    if x >= 106:
        return False
    steps = 0
    while steps * (steps + 1) < 2 * x: # if the steps is less than the double of the value is the minium of the steps
        steps += 1

    if steps * (steps + 1) // 2 == x + 1: # checks if the steps really reach the x value in other way add a step
        steps += 1

    return steps

def main():
    number_of_cases = int(input("How many cases do you want to try?: "))
    for _ in range(number_of_cases):
        value = int(input("Enter the value you want to reach: "))
        result = minimum_jumps(value)
        print(f'The minimum number of jumps for this case is: {result}')
    

if __name__ == "__main__":
    main()