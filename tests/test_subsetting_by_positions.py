#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.subsetting_by_positions import main, subsetting_by_positions


class SubsettingByPositions(unittest.TestCase):

    def test_shape_and_columns(self):
        df = subsetting_by_positions()
        self.assertEqual(
            df.shape, (10, 2), msg="The returned DataFrame had wrong shape!"
        )
        np.testing.assert_array_equal(
            df.columns, ["Title", "Artist"], err_msg="Incorrect column names"
        )

    def test_called(self):
        with patch(
            "src.subsetting_by_positions.subsetting_by_positions",
            wraps=subsetting_by_positions,
        ) as psbp, patch(
            "src.subsetting_by_positions.pd.read_csv", wraps=pd.read_csv
        ) as prc:
            main()
            psbp.assert_called()
            prc.assert_called()


if __name__ == "__main__":
    unittest.main()
