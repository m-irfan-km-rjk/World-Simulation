import random
import numpy as np

def generate_world(rows=100, cols=100):
    world = [[0 for _ in range(cols)] for _ in range(rows)]
    total_cells = rows * cols

    # Terrain IDs
    GRASS = 0
    WATER = 1
    SAND = 2
    FOREST = 3
    SWAMP = 4

    # Allocate cells among terrains (half total for patches)
    water_cells, sand_cells, forest_cells, swamp_cells = np.random.multinomial(
        total_cells // 2, [0.25, 0.25, 0.25, 0.25])

    def grow_patch(terrain_id, cells_to_fill, forbidden_ids=[]):
        attempts = 0
        while cells_to_fill > 0 and attempts < 1000:
            r = random.randint(0, rows - 1)
            c = random.randint(0, cols - 1)
            if world[r][c] != GRASS or world[r][c] in forbidden_ids:
                attempts += 1
                continue

            queue = [(r, c)]
            world[r][c] = terrain_id
            cells_to_fill -= 1

            decay = 1.0
            while queue and cells_to_fill > 0 and decay > 0.05:
                x, y = queue.pop(0)
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows and 0 <= ny < cols and
                        world[nx][ny] == GRASS and
                        world[nx][ny] not in forbidden_ids
                    ):
                        if random.random() < decay:
                            world[nx][ny] = terrain_id
                            cells_to_fill -= 1
                            queue.append((nx, ny))
                decay *= 0.98
            attempts += 1

    # Generate water first (no restrictions)
    grow_patch(WATER, water_cells)

    # Generate sand, forest, swamp avoiding water
    forbidden = [WATER]
    grow_patch(SAND, sand_cells, forbidden)
    grow_patch(FOREST, forest_cells, forbidden)
    grow_patch(SWAMP, swamp_cells, forbidden)

    return world