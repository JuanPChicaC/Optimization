# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 23:02:37 2021

@author: juanp
"""

from pandas import DataFrame
from numpy import log, ones, array, transpose, matmul, exp
from yfinance import Ticker
from scipy.optimize import minimize


class Portfolio():
    
    '''
    
    asset_information_dataframe : DataFrame witn information about financial assets.
    it has to contain assets names as titles of columns, datetime information as index and
    price per time of each asset in the cell
    
    index          asset1          assse2           ..........         asset-n
    
   datetime 1    price(1,1)      price(1,2)         ..........        price(1,n)
    
    ...          .........       .........          ..........        .........
    
    ...          .........       .........          ..........        .........
    
    ...          .........       .........          ..........        .........
    
  dateime n    price(m,1)      price(m,2)          ..........       price(m,n) 
    
    
    '''
    
    
    def __init__(
            self,
            asset_information_dataframe = DataFrame(),
            shortable =  False
            ):
        
        
        self.price_information = asset_information_dataframe
        
        
        err_msg = '''
            The DataFrame can´t have null values
        '''
        
        assert not self.price_information.isnull().values.any() , err_msg
        
        err_msg = '''
            for correct specification in the model, the information dataframe need
            to have more information about prices than the number of assets.
            this condition is to fulfill the random sampling asumption
        '''
        
        assert self.price_information.shape[0] > self.price_information.shape[1], err_msg
        
        err_msg = '''
            is required information at least for one asset to estimate the optimal participation
        '''
        
        assert self.price_information.shape[1] > 0, err_msg
        
        
        
        
        self.asset_names = self.price_information.columns.tolist()
        
        self.DLP_information = DataFrame()
        
        for asset in self.asset_names:
            
            self.DLP_information[asset] = self.price_information[asset].apply(
                lambda x: log(x)
                )
            
            self.DLP_information[asset] = self.DLP_information[asset].diff()
        
        self.mean_vector = self.DLP_information.mean().values
        
        self.covariance_matrix = self.DLP_information.cov().values
        
        self.ones_vector = ones(
            len(self.asset_names),
            dtype=int
            )
        
        self.number_assets = len(self.asset_names)
        
        self.initial_point = [1/self.number_assets for _ in self.asset_names]
        
        if shortable:
            self.bounds = [(-1,1) for _ in self.asset_names]        
        else:
            self.bounds = [(0,1) for _ in self.asset_names]

    def constraint(self,
                   coeffients_vector
                   ):
        coeffients_vector = array(
            [coeffients_vector]
            )
    
        sum_coefficients = matmul(
            coeffients_vector,
            transpose(
                self.ones_vector
                )
            )
        sum_coefficients = sum_coefficients[0]
        
        return sum_coefficients - 1
    
    def expected_return(self,
                        coeffients_vector
                        ):

        ln_portfolio_growth = matmul(
            coeffients_vector,
            transpose(
                self.mean_vector
                )
            )
        
        #ln_portfolio_growth = ln_portfolio_growth[0][0]
        
        portfolio_growth = exp(
            ln_portfolio_growth
            )
        
        portfolio_growth -= 1
        
        return portfolio_growth
    
    def variance_return(self,
                        coefficients_vector
                        ):
       ln_Portf_growth_var =  matmul(
           matmul(
               coefficients_vector,
               self.covariance_matrix
               ),
           transpose(
               coefficients_vector
               )
           )
       #ln_Portf_growth_var = ln_Portf_growth_var[0][0]
       
       Portf_growth_var = exp(
           ln_Portf_growth_var
           )
       
       Portf_growth_var -= 1
       
       return Portf_growth_var

    def std_return(self,
                    coefficients_vector
                    ):

        portfolio_variance = self.variance_return(
            coefficients_vector
            )        
       
        portfolio_std = (portfolio_variance + 1)**(1/2)
        
        portfolio_std -= 1
        
        return portfolio_std
        
    def objective_equation(self,
                           coefficients_vector
                           ):

        coefficients_vector = array(
            [coefficients_vector]
            )

        portfolio_growth = self.expected_return(
            coefficients_vector
            )
        
        
        portfolio_std = self.std_return(
            coefficients_vector
            )

        objective_result = portfolio_std / portfolio_growth    
        
        return objective_result[0][0]
        
    
    def optimize(self):
        if self.number_assets == 1:
             self.optimal_point = [1]
            
        else:
            self.solution = minimize(
                self.objective_equation,
                self.initial_point,
                method = 'SLSQP',
                bounds = self.bounds,
                constraints = [
                    {
                        'type':'eq',
                        'fun' : self.constraint
                        }
                    ]
                )
            
            self.optimal_point = self.solution.x.tolist()
            
        
        return self.optimal_point
        
    
class Prices_Array():
    
    '''
    
    asset_names: list of asset that wanna be consulted in yahoo finance, list like array
        
    '''
    
    
    def __init__(self,
                 asset_names = list()
                 ):
        
        self.available_periods = [
            '1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd',
            ]
        
        self.available_intervals = [
            '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'
            ]
        
        not_string_symbols = [
            str(symbol) for symbol in asset_names if type(symbol) != type('')
            ]
        
        err_msg = '''
            the symbols have to be string format inputs, so the values {} are/is not valid        
        '''
        
        assert len(not_string_symbols) == 0, err_msg.format(
            ', '.join(
                not_string_symbols
                )
            )
        
        self.asset_names = [asset.upper() for asset in asset_names]
        
        
    def generate_information(self,
            interval = '1m',
            period = '1y'
            ):
        '''
        interval: periodicity of price information for each asset
        
                the options are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        
                default: 1d
                
        period: time range of price information for each asset
        
                the options are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd
        
                default: 1y
        '''
        
        
        err_msg = '''
        
            at least one name is required to search for asset information
        
        '''
        
        assert len(self.asset_names) > 0, err_msg        

        self.interval = interval
        self.period = period
        
        err_msg = '''
        the option "{}" is not a valid {}.
        the only valid options are:
        {}
        '''
        assert self.interval in self.available_intervals, err_msg.format(
            str(self.interval),
            'interval',
            ', '.join(
                self.available_intervals
                )
            )
        
        assert self.period in self.available_periods, err_msg.format(
            str(self.period),
            'period',
            ', '.join(
                self.available_periods
                )
            )
        
        self.assets_tickers = {
            asset : Ticker(asset) 
            for asset in self.asset_names            
            }
        
        self.not_finded_assets = [
            asset for asset in self.asset_names if self.assets_tickers[asset].info['regularMarketPrice'] is None
            ]
        
        
        err_msg = '''
            the symbol(s) {} is/are not founded in Yahoo Finance,
            please double check if the sintax for each one is right
        '''
        
        assert len(self.not_finded_assets) == 0, err_msg.format(
            ', '.join(
                self.not_finded_assets
                )
            )
        
        
        self.assets_information_dict = {
            asset :  self.assets_tickers[asset].history(period = self.period) 
            for asset in self.asset_names
            }
        
        self.assets_information_df = DataFrame(
            columns = self.asset_names,
            data =  transpose(
                [
                    self.assets_information_dict[asset]['Close'].tolist() for asset in self.asset_names
                    ]
                )
            )
        
        return self.assets_information_df
        

