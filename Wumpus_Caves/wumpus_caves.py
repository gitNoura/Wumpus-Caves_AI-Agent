import random

num_caves = 50

for i in range(num_caves):
    # Randomly choose if x and y dimensions should be equal or not
    equal_dimensions = random.choice([True, False])
    
    if equal_dimensions:
        # If equal dimensions, choose a random size for the cave
        world_size = (random.randint(4, 5), random.randint(4, 5))
    else:
        # If unequal dimensions, choose random values for x and y dimensions
        world_size = (random.randint(4, 5), random.randint(4, 5))
        
    gold_x = random.randint(1, world_size[0])
    gold_y = random.randint(1, world_size[1])
    
    # Generate multiple pits
    num_pits = random.randint(1, 3)  # Allow up to 3 pits in a cave
    pits_condition = ''
    for _ in range(num_pits):
        pit_x = random.randint(1, world_size[0])
        pit_y = random.randint(1, world_size[1])
        pits_condition += f'(pit (x {pit_x})(y {pit_y}))\n'
    
    # Generate multiple nocaves
    num_nocaves = random.randint(1, 3)  # Allow up to 3 nocaves in a cave
    nocaves_condition = ''
    for _ in range(num_nocaves):
        nocave_x = random.randint(1, world_size[0])
        nocave_y = random.randint(1, world_size[1])
        nocaves_condition += f'(nocave (x {nocave_x})(y {nocave_y}))\n'
    
    wumpus_x = random.randint(1, world_size[0])
    wumpus_y = random.randint(1, world_size[1])
    exit_x = 1
    exit_y = 1
    agent_name = "C" + str(i + 1)
    
    with open(f'cave{i + 1}.jess', 'w') as f:
        f.write(f'(worldsize {world_size[0]} {world_size[1]})\n')
        f.write(f'(gold (x {gold_x})(y {gold_y})(amount 100))\n')
        f.write(pits_condition)
        f.write(nocaves_condition)
        f.write(f'(wumpus (x {wumpus_x})(y {wumpus_y}))\n')
        f.write(f'(exit (x {exit_x})(y {exit_y}))\n')
        f.write(f'(hunter (agent {agent_name})))\n')
        