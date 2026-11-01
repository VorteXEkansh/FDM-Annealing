"""Readable scientific notation for both Word and ReportLab manuscript markup."""
def number(value, precision=3):
    text = f'{float(value):.{precision}g}'
    if 'e' in text:
        mantissa, exponent = text.split('e')
        text = f'{mantissa} × 10<sup>{int(exponent)}</sup>'
    return text.replace('-', '−')
