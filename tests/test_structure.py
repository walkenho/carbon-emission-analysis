import numpy as np
import pandas as pd
import pytest

from emissionsanalysis.data.make_dataset import EmissionsData
from emissionsanalysis.data.structure import Ship


def test_emissionsdata_raises_AssertionError_for_technical_efficiency():
    df = pd.DataFrame({Ship.efficiency_value: [0, -1, np.nan]})

    with pytest.raises(AssertionError):
        EmissionsData(df)._assert_technical_efficiency_is_not_negative()


def test_emissionsdata_raises_AssertionError_for_multiple_imo_occurences_per_year():
    df = pd.DataFrame({Ship.year: [2001, 2001], Ship.imo: [1, 1]})

    with pytest.raises(AssertionError):
        EmissionsData(df)._assert_entries_are_unique()
