# This file is part of an Adiczion's Module.
# The COPYRIGHT and LICENSE files at the top level of this repository
# contains the full copyright notices and license terms.
from odoo import api, models, fields, _
import logging

_logger = logging.getLogger(__name__)


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    sender_id = fields.Many2one('res.partner', 'Sender',
        default=lambda self: self.env.company.partner_id,
        help="Select the partner that will be used as sender when requesting "
        "a label from the carrier.")
