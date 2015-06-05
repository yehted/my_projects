import pandas as pd
import argparse
import os.path
import json

from ns_data_performance import top_entities as top

class IPCSummary(object):
    def __init__(self, fund_symbol):
        self.load_files(fund_symbol)

    def load_files(self, fund_symbol):
        """Load files into data frames

        This function looks in the current directory/data/<Fund Symbol/
        for sector.csv and meta.csv
        """

        local_path = os.path.dirname(os.path.realpath(__file__))
        meta_file = os.path.join(local_path, 'data/', fund_symbol, 'meta.csv')
        sector_file = os.path.join(local_path, 'data/', fund_symbol, 'sector.csv')
        region_file = os.path.join(local_path, 'data/', fund_symbol, 'region.csv')
        try:
            self.META = pd.read_csv(meta_file)
            self.SECTOR = pd.read_csv(sector_file)
        except IOError:
            raise

        try:
            self.REGION = pd.read_csv(region_file)
        except IOError:
            self.REGION = None

def main():
    """Main function that runs from command line

    Takes one parameter, the fund symbol, which corresponds to the location of
    the sector and meta data files. Function returns the dataframes associated
    with the files for debugging in interactive mode.
    """
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    parser = argparse.ArgumentParser()
    parser.add_argument("fund", help='Fund symbol')
    args = parser.parse_args()

    A = IPCSummary(args.fund)

    hierarchy = ['Sector', 'Industry', 'Company']
    metric = 'PortfolioContribution'

    result = top.top_values(df=A.SECTOR, hierarchy=hierarchy, metric=metric,
        limit=3)

    # print result
    with open('output.json', 'w') as f:
        # json.dump(result, f)
        f.write(str(result))

    return A

if __name__ == '__main__':
    A = main()