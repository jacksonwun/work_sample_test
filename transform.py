import json, os, pandas as pd
from dataclasses import dataclass
import time
import numpy as np
import csv

@dataclass
class Dataitem:
    input_1: str
    input_2: str
    target: str

    def run(self):
        if self.target[-3:] == 'csv':
            self.output_csv()
        else:
            self.output_json()

    def read_1(self) -> pd.DataFrame():
        """ read the input 1"""
        if self.input_1[-3:] == 'csv':
            df = pd.read_csv(self.input_1)
            return df
        elif self.input_1[-4:] == 'json':
            df = pd.read_json(self.input_1)
            return df
        else:
            raise FileNotFoundError()

    def read_2(self) -> pd.DataFrame():
        """ read the input 2"""
        if self.input_2[-3:] == 'csv':
            df = pd.read_csv(self.input_2)
            return df
        elif self.input_2[-4:] == 'json':
            df = pd.read_json(self.input_2)
            return df
        else:
            raise FileNotFoundError()

    def transform(self) -> pd.DataFrame():
        """ Transform from json to csv """
        df1 = self.read_1()
        df2 = self.read_2()

        ## Merge and group them to one df
        df3 = pd.merge(df1, df2, left_on='|uuid|', right_on='|group_id|')
        df3["|uuid|"] = df3["|uuid|_y"]
        df3 = df3.drop(columns=['|uuid|_x', "|uuid|_y", "|group_id|"])

        ## Use to_formatted_json to transform the data
        df4 = self.to_formatted_json(df3)
        return df4

    def to_formatted_json(self, df: pd.DataFrame()) -> list():
        """ Merge row to the standard format """
        result = []
        for _, row in df.iterrows():
            output_dict = {}

            output_dict[row['|uuid|'][1:-1] + '_title'] = {'string': row['|title|'][1:-1]}
            output_dict[row['|uuid|'][1:-1]  + '_description'] = {'string': row['|description|'][1:-1], 'context': row['|group|'][1:-1]}

            result.append(output_dict)
        return result

    def output_json(self):
        """ Output to a json """
        output = self.transform()
        with open(self.target, 'w') as f:
            json.dump(output, f)

    def output_csv(self):
        """ Output to a csv """
        output_list = self.transform()
        with open(self.target, 'w') as f:
            write = csv.writer(f)
            write.writerows(output_list)

if __name__ == "__main__":
    # dataitem = Dataitem('groups.csv', 'items.csv', 'output.json')
    # dataitem.from_csv_to_json()
    dataitem = Dataitem('groups.json', 'items.json', 'output.csv')
    dataitem.run()