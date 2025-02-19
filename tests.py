import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 1
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_3(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_4(self):
        num_cols = 0
        num_rows = 10
        # m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertRaises(ValueError, Maze, 0, 0, num_rows, num_cols, 10, 10)

    def test_maze_create_cells_5(self):
        num_cols = 0
        num_rows = 0
        # m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertRaises(ValueError, Maze, 0, 0, num_rows, num_cols, 10, 10)

    def test_maze_create_cells_6(self):
        num_cols = 1000
        num_rows = 1000
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_entrance_and_exit_removal(self):
        num_cols = 5
        num_rows = 4
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        # m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()