from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILENAME = 'status_summary_{now_format}.csv'
NUMBER_NAME = r'PEP\s(?P<number>\d+)\W+(?P<name>.+)$'
STATUS_XPATH = '//*[contains(text(), "Status")]'
NEXT_SIBLING = '//following-sibling::node()[{}]/text()'.format('2')
