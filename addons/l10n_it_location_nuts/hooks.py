# Copyright 2018 Simone Rubino - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging

from odoo import SUPERUSER_ID, api

_logger = logging.getLogger(__name__)


def post_init_hook(cr, registry):
    """Define Italian specific configuration in res.country."""
    env = api.Environment(cr, SUPERUSER_ID, {})
    italy = env.ref("base.it")
    _logger.info("Setting Italy NUTS configuration")
    italy.write({"state_level": 4})
