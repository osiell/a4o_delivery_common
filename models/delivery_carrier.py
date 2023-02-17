# This file is part of an Adiczion's Module.
# The COPYRIGHT and LICENSE files at the top level of this repository
# contains the full copyright notices and license terms.
from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    sender_id = fields.Many2one('res.partner', 'Sender',
        default=lambda self: self.env.company.partner_id,
        help="Select the partner that will be used as sender when requesting "
        "a label from the carrier.")
    country_origin_id = fields.Many2one('res.country',
        string='Default Country of Origin', ondelete='restrict',
        help="Country of origin of the default product (if not indicated on "
        "the product) used in CN22/CN23.\n"
        "Beware! it is preferable to use Odoo's intrastat modules or a module "
        "from a partner to add this information to each product.")

    @api.model
    def cron_get_sending_package_status(self):
        """Cron called regularly to check the status of the shipment."""
        self.get_sending_package_status()

    @api.model
    def get_sending_package_status(self):
        delivery_types = set(self.search([]).mapped('delivery_type'))
        for delivery_type in delivery_types:
            _logger.debug("[get_sending_package_status] Delivery type: "
                "%s", delivery_type)
            method = getattr(
                self, '%s_get_sending_package_status' % delivery_type, None)
            if method:
                method()
