import json
from bs4 import BeautifulSoup
from xml_adapter import XMLConfig

from experiment import Experiment


def main() -> None:
    with open("config.xml", encoding="utf8") as file:
        config = file.read()
    
    bs_instance = BeautifulSoup(config,'xml')
    xml_adapter = XMLConfig(bs_instance)
    
    experiment = Experiment(xml_adapter)
    experiment.run()


if __name__ == "__main__":
    main()