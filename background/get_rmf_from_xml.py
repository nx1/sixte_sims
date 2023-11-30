import os
import xml.etree.ElementTree as et

def get_enviroment_variable(name):
    var = os.environ.get(name)
    if var is None:
        raise ValueError(f'The {var} environment variable is not set.')
    return var

if __name__ == "__main__":
    SIXTE = get_enviroment_variable('SIXTE')
    
    xml=f'{SIXTE}/share/sixte/instruments/athena-wfi/wfi_w_filter_B4C/ld_wfi_ff_large.xml'
    
    tree = et.parse(xml)
    print(xml)    
    for i in tree.getroot():
        print('')
        print(i.tag)
        print('='*len(i.tag))
        for j in i:
            print(f'{j.tag:<24} : {j.attrib}')
    
