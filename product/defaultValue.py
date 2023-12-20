BARCODE_TYPES = (
    (1, 'Code 128'),
    (2, 'Code 39'),
    (3, 'EAN-13'),
    (4, 'EAN-8'),
    (5, 'UPC-A'),
    (6, 'UPC-E'),
    (7, 'ITF-14'),
)
MANAGE_STOCK_CHOICES = (
    (1, 'Yes'),
    (0, 'No'),
)
ALLOW_DECIMAL = (
    (0, 'Yes'),
    (1, 'No'),
)
DURATION_TYPE = (
    (0, 'Days'),
    (1, 'Months'),
    (2, 'Years'),
)
EXPIRY_PERIOD_UNIT_CHOICES = (
    ('days', 'Days'),
    ('months', 'Months'),
)

TAX_TYPE_CHOICES = [
    (0, 'Inclusive'),
    (1, 'Exclusive'),
]

PRODUCT_TYPE_CHOICES = [
    (0, 'Single'),
    (1, 'Variable'),
]

APPLICABLE_TAX_CHOICES = [
    (0, 'Vat'),
    (1, 'SGST'),
]