import argparse
import pandas as pd
import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    """Parse the input XML file and extract the relevant data"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    prefix = 'webNLG'
    rows = []
    for entry in root.findall('./entries/entry'):
        input_text = [otriple.text for otriple in entry.findall('./modifiedtripleset/mtriple')]
        target_text = [lex.find('./text').text for lex in entry.findall('./lex')]
        rows.append([prefix, input_text, target_text])
    return rows

def save_csv(output_file, rows):
    """Save the extracted data as a CSV file"""
    df = pd.DataFrame(rows, columns=['prefix', 'input_text', 'target_text'])
    df.to_csv(output_file, index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an XML file to a CSV file')
    parser.add_argument('input_file', type=str, help='Path to the input XML file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    args = parser.parse_args()
    rows = parse_xml(args.input_file)
    save_csv(args.output_file, rows)
