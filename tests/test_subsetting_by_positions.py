#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.subsetting_by_positions import main, subsetting_by_positions


class SubsettingByPositions(unittest.TestCase):

    def test_returns_a_dataframe(self):
        df = subsetting_by_positions()
        self.assertIsInstance(
            df,
            pd.DataFrame,
            msg="subsetting_by_positions() must return a pandas DataFrame, "
            "not %r." % (type(df),),
        )

    def test_shape(self):
        df = subsetting_by_positions()
        self.assertEqual(
            df.shape,
            (10, 2),
            msg="The returned DataFrame should have shape (10, 2): the top "
            "10 chart positions and the 2 selected columns. Got %r."
            % (df.shape,),
        )

    def test_columns(self):
        df = subsetting_by_positions()
        np.testing.assert_array_equal(
            df.columns,
            ["Title", "Artist"],
            err_msg="The DataFrame's columns should be exactly ['Title', "
            "'Artist'] in that order. Got %r." % (list(df.columns),),
        )

    def test_index_is_the_top_10_positions(self):
        df = subsetting_by_positions()
        np.testing.assert_array_equal(
            df.index,
            list(range(1, 11)),
            err_msg="The index should be the chart positions 1 through 10, "
            "in order. Got %r." % (list(df.index),),
        )

    def test_first_and_last_rows(self):
        df = subsetting_by_positions()
        self.assertEqual(
            (df.loc[1, "Title"], df.loc[1, "Artist"]),
            ("I WANT TO HOLD YOUR HAND", "THE BEATLES"),
            msg="Position 1 should be ('I WANT TO HOLD YOUR HAND', 'THE "
            "BEATLES'). Got %r."
            % ((df.loc[1, "Title"], df.loc[1, "Artist"]),),
        )
        self.assertEqual(
            (df.loc[10, "Title"], df.loc[10, "Artist"]),
            ("DON'T TALK TO HIM", "CLIFF RICHARD"),
            msg="Position 10 should be (\"DON'T TALK TO HIM\", 'CLIFF "
            "RICHARD'). Got %r."
            % ((df.loc[10, "Title"], df.loc[10, "Artist"]),),
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
