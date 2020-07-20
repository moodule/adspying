# -*- coding: utf-8 -*-

"""
=========
Vehicules
=========

Search for vehicules in ad listings.
"""

from __future__ import division, print_function, absolute_import

from homespace.items.vehicules import VehiculeAd, VehiculeAdLoader
from homespace.spiders.leboncoin._leboncoin import LeboncoinSpider

#####################################################################
# SEARCH ARG VALUES
#####################################################################

FUEL_VALUES = []

MAKE_VALUES = list(range(1960, 2020, 1))

MILEAGE_VALUES = (
    list(range(0, 100000, 10000))
    + list(range(100000, 275000, 25000)))

PRICE_VALUES = (
    list(range(0, 1000, 250))
    + list(range(1000, 3000, 500))
    + list(range(3000, 15000, 1000))
    + list(range(15000, 30000, 2500))
    + list(range(30000, 55000, 5000)))

#####################################################################
# FILTERS
#####################################################################

VANS_FILTER = ('')

#####################################################################
# SPIDER
#####################################################################

class LeboncoinVehiculesSpider(LeboncoinSpider):
    name = 'leboncoin_vehicules'

    def __init__(self, *args, **kwargs):
        """
        """
        super(LeboncoinVehiculesSpider, self).__init__(*args, **kwargs)

        # forge a url to query leboncoin
        self._queries = {
            'default': {
                'category': '5', # utility vehicules
                'fuel': '',
                'locations': '',
                'mileage': '',
                'page': '1',
                'price': '',
                'regdate': '',
                'shippable': '1',
                'text': ''},
            'vans': {
                'category': '5', # utility vehicules
                'fuel': '',
                'locations': '',
                'mileage': '',
                'page': '1',
                'price': 'min-5000',
                'regdate': '2010-max',
                'shippable': '1',
                'text': '',
                'vehicle_is_eligible_p2p': '2'}}

        # scrape the resulting listing
        self._ad_specific_attributes_xpath = {
            'color': (
                '//div[contains(@data-qa-id, "criteria_item_vehicule_color")]'
                + '/div[2]/p[2]/text()'),
            'fuel': (
                '//div[contains(@data-qa-id, "criteria_item_fuel")]'
                + '/div[2]/p[2]/text()'),
            'gearbox': (
                '//div[contains(@data-qa-id, "criteria_item_gearbox")]'
                + '/div[2]/p[2]/text()'),
            'issuance': (
                '//div[contains(@data-qa-id, "criteria_item_issuance_date")]'
                + '/div[2]/p[2]/text()'),
            'make': (
                '//div[contains(@data-qa-id, "criteria_item_regdate")]'
                + '/div[2]/p[2]/text()'),
            'mileage': (
                '//div[contains(@data-qa-id, "criteria_item_mileage")]'
                + '/div[2]/p[2]/text()'),}

        # classes to store, clean and export the data
        self._item_class = VehiculeAd
        self._loader_class = VehiculeAdLoader
