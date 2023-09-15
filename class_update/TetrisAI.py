class TetrisAI:
    @staticmethod
    def get_best_move(game_blocks):
        best_move = None
        best_score = -float('inf')

        current_block = game_blocks.select_Block
        game_field = game_blocks.field
        block_size = game_blocks.block_size

        for rotation in range(4):
            for col in range(len(game_field[0]) - len(current_block[0]) + 1):
                row = 0
                while not TetrisAI.collision(game_field, current_block, row, col):
                    row += 1
                row -= 1

                # Simulate placing the block and calculate the score
                temp_field = [row[:] for row in game_field]
                TetrisAI.place_block(temp_field, current_block, row, col)
                score = TetrisAI.calculate_score(temp_field)

                if score > best_score:
                    best_score = score
                    best_move = (rotation, col)

            # Rotate the block for the next iteration
            current_block = TetrisAI.rotate_block(current_block)

        # Choose the best move based on the rotation and column
        rotation, col = best_move
        if rotation != 0:
            return 'rotate'
        elif col < game_blocks.current_col:
            return 'move_left'
        elif col > game_blocks.current_col:
            return 'move_right'
        else:
            return 'move_down'

    @staticmethod
    def collision(field, block, row, col):
        for r, row_value in enumerate(block):
            for c, cell in enumerate(row_value):
                if cell and (field[row + r][col + c] != 0 or
                             row + r >= len(field) or col + c < 0 or col + c >= len(field[0])):
                    return True
        return False

    @staticmethod
    def place_block(field, block, row, col):
        for r, row_value in enumerate(block):
            for c, cell in enumerate(row_value):
                if cell:
                    field[row + r][col + c] = 1

    @staticmethod
    def calculate_score(field):
        # Implement your scoring logic here
        # This is a simplified example, you can consider factors like lines cleared, holes, height, etc.
        score = 0
        return score

    @staticmethod
    def rotate_block(block):
        # Implement block rotation logic here
        # This is a simplified example, consider the block's rotation rules in your game
        return block  # No rotation in this example
