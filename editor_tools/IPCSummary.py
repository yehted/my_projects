import pandas as pd
import argparse
import os.path

class IPCSummary(object):
    """This is a tool that helps the QA process for IPC stories.

    The main function presents the user with a command line menu interface
    where the user can select various paragraphs of the IPC story to
    investigate.
    """

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

    def metadata(self, meta_data=['ClientName', 'PortfolioID', 'PortfolioTotalReturn',
            'EndDate', 'BenchmarkName', 'BenchmarkTotalReturn',
            'SelectionEffect', 'AllocationEffect', 'InteractionEffect',
            'TotalEffect']):
        """Paragraph 1

        This function prints the information in meta.csv in a readable format.
        The desired columns to print are defined in meta_data
        """
        return self.META[meta_data].transpose()

    def absolute_performance_by_sector(self):
        """Paragraph 2

        This function summarizes the absolute performance of the fund,
        sorting sectors by PortfolioContribution.
        """

        sectors = self.SECTOR[pd.isnull(self.SECTOR['Industry'])]
        no_cash_sectors = sectors[
        	~sectors.Sector.isin(['[Cash]', 'Cash'])]
        positive_pf_weight = no_cash_sectors[
        	no_cash_sectors['PortfolioAvgWeight'] > 0]
        sector_gains = positive_pf_weight[
        	positive_pf_weight['PortfolioContribution'] > 0]
        sorted_sectors = sectors.sort(
        	'PortfolioContribution', ascending=False).reset_index(drop=False)

        result = {
            'sectors': len(sectors),
            'sectors_with_positive_weight': len(positive_pf_weight),
            'sectors_with_gains': len(sector_gains),
            'sectors_by_contribution': sorted_sectors[['Sector', 'PortfolioContribution', 'PortfolioAvgWeight']]
        }
        return result

    def relative_performance(self, region=False, ascending=False, number=3,
            columns_to_print=['TotalEffect', 'SelectionEffect', 'AllocationEffect']):
        """Paragraph 3

        This function prints the top 3 companies of the top 3 industries of the
        top 3 sectors. If the ascending tag is set to True, this function
        will print the bottom 3 companies of the bottom 3 industries of the
        bottom 3 sectors

        columns_to_print specifies a list of which columns to display. The
        default is just TotalEffect, SelectionEffect, and AllocationEffect
        """

        if region:
            if self.REGION is None:
                raise KeyError('This fund does not have region.csv')
            base = self.REGION
            self.header1 = 'Region'
            self.header2 = 'Country'
        else:
            base = self.SECTOR
            self.header1 = 'Sector'
            self.header2 = 'Industry'

        result = {}

        # Top sectors/regions
        sectors = base[pd.isnull(base[self.header2])]
        total_effect_sectors = sectors.sort('TotalEffect', ascending=ascending).reset_index(drop=False)
        result['header1'] = total_effect_sectors[[self.header1] + columns_to_print]

        top_industries = {}
        result['header2'] = []
        result['companies'] = {}

        # Top industries/countries in sector/region
        for sect in total_effect_sectors[self.header1].head(number):
            temp = base[base[self.header1].isin([sect])]
            temp = temp[~pd.isnull(temp[self.header2])]
            top_industries[sect] = temp[pd.isnull(temp['Company'])].sort('TotalEffect',
                ascending=ascending)
            result['header2'].append(top_industries[sect][[self.header2] + columns_to_print].head(number))

            # Top companies in industry/country
            result['companies'][sect] = []
            for industry in top_industries[sect][self.header2].head(number):
                temp2 = base[base[self.header2].isin([industry])]
                temp2 = temp2[~pd.isnull(temp2['Company'])]
                top_companies = temp2.sort('TotalEffect', ascending=ascending)
                result['companies'][sect].append(top_companies[['Company'] + columns_to_print].head(number))

        return result

    def absolute_performance_by_company(self, number=5):
        """Paragraph 4

        This function prints the top 5 and bottom 5 performing companies
        by PortfolioContribution. The default number of 5 can be changed by
        changing the optional argument, number
        """

        companies = self.SECTOR[~pd.isnull(self.SECTOR['Company'])].sort('PortfolioContribution',
                ascending=False)

        result = {
            'top': companies[['Company', 'Sector', 'PortfolioContribution']].head(number),
            'bottom': companies[['Company', 'Sector', 'PortfolioContribution']].tail(number)
        }
        return result

    def bought_sold_positions(self):
        """Paragraph 5

        This function prints the companies that were bought and sold during the
        period. For positions bought, it checks the PortfolioEndWeight and
        PortfolioAvgWeight. For positions sold, it checks PortfolioEndWeight
        and PortfolioAvgWeight"""

        columns_to_print = ['Sector', 'PortfolioAvgWeight', 'PortfolioEndWeight',
            'PortfolioContribution']
        companies = self.SECTOR[~pd.isnull(self.SECTOR['Company'])]

        # Sold positions
        sold_companies = companies[companies['PortfolioAvgWeight'] > 0]
        sold_companies = sold_companies[sold_companies['PortfolioAvgWeight'] > sold_companies['PortfolioEndWeight']]
        sold_companies['Difference'] = sold_companies['PortfolioAvgWeight'] - sold_companies['PortfolioEndWeight']
        sold_companies = sold_companies.sort('PortfolioContribution', ascending=True)

        # Bought positions
        bought_companies = companies[companies['PortfolioEndWeight'] > 0]
        bought_companies = bought_companies[bought_companies['PortfolioEndWeight'] > bought_companies['PortfolioAvgWeight']]
        bought_companies['Difference'] = bought_companies['PortfolioEndWeight'] - bought_companies['PortfolioAvgWeight']
        bought_companies = bought_companies.sort('Difference', ascending=False)

        result = {
            'sold_companies': sold_companies[['Company'] + columns_to_print].head(5),
            'bought_companies': bought_companies[['Company'] + columns_to_print].head(5)
        }
        return result


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

    columns_to_print = ['TotalEffect', 'SelectionEffect', 'AllocationEffect',
        'InteractionEffect']# 'PortfolioAvgWeight', 'BenchmarkAvgWeight',
        # 'PortfolioEndWeight', 'BenchmarkEndWeight']

    A = IPCSummary(args.fund)

    def print_options():
        print 'IPC QA tool'
        print '-----------------------------------------------------'
        print '1: Meta data'
        print '2: Absolute performance by sector'
        print '3: Relative performance (sector->industry->company)'
        print '4: Absolute performance by company'
        print '5: Bought/sold positions'

    print_options()
    select_msg = 'Select paragraph to print (q to quit, ? for options): '
    selection = raw_input(select_msg)
    print

    while selection != 'q':
        if selection == '1':
            print 'Paragraph 1: Meta-data'
            print '----------------------------------------------'
            print A.metadata()
            print
        elif selection == '2':
            res = A.absolute_performance_by_sector()
            print 'Paragraph 2: Absolute performance by sector'
            print '----------------------------------------------'
            print 'Total number of sectors: ', res['sectors']
            print 'Sectors with positive portfolio average weight: ', res['sectors_with_positive_weight']
            print 'Of the above, number with gains: ', res['sectors_with_gains']
            print
            print 'List sorted by PortfolioContribution: '
            print res['sectors_by_contribution']
            print
        elif selection == '3':
            region = raw_input('Region? 0=no, 1=yes: ')
            ascending = raw_input('Top? 0=no, 1=yes: ')
            valid = {'0', '1'}
            if not (region in valid and ascending in valid):
                print 'Invalid selection'
                continue
            res = A.relative_performance(region=int(region), ascending=not int(ascending))

            print 'Paragraph 3'
            print '----------------------------------------------'
            print '{} by TotalEffect: {}'.format(A.header1, 'Ascending' if ascending else 'Descending')
            print res['header1']
            print '----------------------------------------------'
            for i, item1 in enumerate(res['header1'][A.header1].head(3)):
                print 'Top {} in {}: {}'.format(A.header2, A.header1, item1)
                print res['header2'][i]
                print '----------------------------------------------'

                for j, item2 in enumerate(res['companies'][item1]):
                    print 'Top companies in {SECTOR}: {sect}, {INDUSTRY}: {indus}'.format(SECTOR=A.header1,
                    INDUSTRY=A.header2, sect=item1, indus=res['header2'][i][A.header2].iloc[j])
                    print res['companies'][item1][j]
                    print
                print '----------------------------------------------'
            print
        elif selection == '4':
            res = A.absolute_performance_by_company()
            print 'Paragraph 4: Companies by PortfolioContribution'
            print '----------------------------------------------'
            print 'Best companies'
            print res['top']
            print
            print 'Worst companies'
            print res['bottom']
            print
        elif selection == '5':
            res = A.bought_sold_positions()
            print 'Paragraph 5: Bought/sold positions'
            print '----------------------------------------------'
            print 'Sold positions'
            print res['sold_companies']
            print
            print 'Bought positions'
            print res['bought_companies']
            print
        elif selection == '?':
            print_options()
        else:
            print 'Invalid selection'
        selection = raw_input(select_msg)
        print

    return A

if __name__ == '__main__':
    A = main()
