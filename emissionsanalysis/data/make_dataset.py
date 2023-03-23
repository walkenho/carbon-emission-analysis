import pathlib

import numpy as np
import pandas as pd

from emissionsanalysis.data.structure import AnnualReport, EmissionsData, Ship


class DataLoader:
    # TODO: Tidy
    def _load_df_from_file(filename: pathlib.PosixPath) -> pd.DataFrame:
        df = pd.read_excel(filename, header=[0, 2], engine="openpyxl")
        df.columns = [c.replace(" ", "_").lower() for c in df.columns.map("_".join)]

        df[[Ship.efficiency_type, Ship.efficiency_value]] = df[
            "ship_technical_efficiency"
        ].str.extract(r"(.*) \((.*) gCO₂\/t·nm\)")

        df = df.astype({Ship.efficiency_value: float, Ship.year: str})

        # data cleaning
        df[AnnualReport.co2_per_dwt_distance] = df[
            AnnualReport.co2_per_dwt_distance
        ].replace("Division by zero!", np.nan)

        df[AnnualReport.co2_per_mass_distance] = df[
            AnnualReport.co2_per_mass_distance
        ].replace("Division by zero!", np.nan)

        df[AnnualReport.fuel_per_distance] = df[AnnualReport.fuel_per_distance].replace(
            "Division by zero!", np.nan
        )

        # convert co2 per distance to from kg to g for consistency with other variables
        df[AnnualReport.co2_per_distance] = (
            df[
                "annual_monitoring_results_annual_average_co₂_emissions_per_distance_[kg_co₂_/_n_mile]"
            ]
            * 1000
        )

        # brute force "Division by zero!Division by zero!..." replacement
        df[AnnualReport.co2_per_distance] = pd.to_numeric(df[
            AnnualReport.co2_per_distance
        ], errors='coerce')

        df = df.drop(
            columns=[
                "annual_monitoring_results_annual_average_co₂_emissions_per_distance_[kg_co₂_/_n_mile]",
            ],
            axis=1,
        )

        # add dwt carried for Q3
        df["annual_monitoring_results_annual_average_dwt_carried"] = (
            df[AnnualReport.co2_per_distance] / df[AnnualReport.co2_per_dwt_distance]
        )

        df["annual_monitoring_results_annual_average_mass_carried"] = (
            df[AnnualReport.co2_per_distance] / df[AnnualReport.co2_per_mass_distance]
        )

        # add distances for Q4
        df[AnnualReport.distance_total] = (
            df[AnnualReport.fuel_total] / df[AnnualReport.fuel_per_distance]
        )

        df[AnnualReport.distance_total_imputed_mean] = df[
            AnnualReport.distance_total
        ].fillna(df.groupby(Ship.imo)[AnnualReport.distance_total].transform("mean"))

        df[AnnualReport.distance_total_imputed_median] = df[
            AnnualReport.distance_total
        ].fillna(df.groupby(Ship.imo)[AnnualReport.distance_total].transform("median"))

        print(f"Loaded {filename} containing {df.shape[0]} entries")
        return df

    def load_folder(folder: pathlib.PosixPath) -> EmissionsData:
        filenames = list(folder.glob("*.xlsx"))
        print(f"Processing {len(filenames)} files.")

        return EmissionsData(
            data=pd.concat(
                [DataLoader._load_df_from_file(filename) for filename in filenames]
            )
        )
