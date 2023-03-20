from enum import Enum
import pandas as pd

class Ship(str, Enum):
    imo = "ship_imo_number"
    year = "ship_reporting_period"
    name = "ship_name"
    type = "ship_ship_type"
    shipname = "ship_name"
    efficiency_type = "ship_technical_efficiency_type"
    efficiency_value = "ship_technical_efficiency_value"

    def __str__(self) -> str:  # makes enum values duck-type to strings
        return str.__str__(self)


class AnnualReport(str, Enum):
    co2_per_dwt_distance = "annual_monitoring_results_annual_average_fuel_consumption_per_transport_work_(dwt)_[g_/_dwt_carried_·_n_miles]"
    co2_per_distance = (
        "annual_monitoring_results_annual_average_co₂_emissions_per_distance_[g_co₂_/_n_mile]"
    )
    fuel_per_distance = (
        "annual_monitoring_results_annual_average_fuel_consumption_per_distance_[kg_/_n_mile]"
    )
    fuel_total = "annual_monitoring_results_total_fuel_consumption_[m_tonnes]"
    dwt_carried = "annual_monitoring_results_annual_average_dwt_carried"
    distance_total = "annual_monitoring_results_total_distance[n_mile]"
    distance_total_imputed_mean = "annual_monitoring_results_total_distance[n_mile]_imputed_mean"
    distance_total_imputed_median = (
        "annual_monitoring_results_total_distance[n_mile]_imputed_median"
    )

    def __str__(
        self,
    ) -> str:  # makes enum values duck-type to strings, needed for graphs
        return str.__str__(self)


class EmissionsData:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def test_data_quality(self) -> None:
        self._assert_entries_are_unique()
        self._assert_technical_efficiency_is_not_negative()

    def _assert_entries_are_unique(self) -> None:
        # TODO: convert to logging
        print("\nChecking if all IMO entries are unique")
        assert (
            len(self.data.groupby([Ship.imo, Ship.year], as_index=False).size().query("size > 1"))
            == 0
        )
        print("- OK")

    def _assert_technical_efficiency_is_not_negative(self) -> None:
        # TODO: convert to logging
        print("\nChecking if all efficiency values are non-negativ.")
        assert len(self.data[self.data[Ship.efficiency_value].fillna(0) < 0]) == 0
        print("- OK")

