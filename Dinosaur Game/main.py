print('You are in a dark cave, searching for treasure.')
print('You are armed with a sword and a shield.')
print('You see a large dragon blocking your path!')

action = input('What will you do? (Attack/Run)')

if action == 'Attack':
    print('You swing your sword at the dragon!')
    print('The dragon breathes fire at you!')
    print('You raise your shield to block the flames!')
    print('You have been burned by the dragon!')
    print('You fight bravely, but are defeated by the dragon.')
elif action == 'Run':
    print('You turn and run away from the dragon!')
    print('The dragon breathes fire at you as you flee!')
    print('You escape the cave, but without any treasure.')
else:
    print('Invalid action!')