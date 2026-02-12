# -*- coding: utf-8 -*-

{
    'name' : 'Real Estate Management',
    'version' : '19.0.1.0.0',
    'summary': 'Manage Real Estate Properties, Agents, and Sales',
    'description': """
        This module provides functionalities to manage real estate properties,
        agents, clients, and sales processes efficiently.
    """,
    'depends' : ['base', 'contacts'],
    'data' : [
        'security/ir.model.access.csv',
        'wizard/real_estate_property_sold_to_wizard.xml',
        'views/real_estate_property_type.xml',
        'views/real_estate_form.xml',
        'views/real_estate_view.xml',
        'views/real_estate_menu.xml',
    ],
    'author' : 'Ariel Recto - Innovato Solutions',
    'installable': True,
    'application': True,
    'sequence': -1,
    'category': 'Real Estate',
}