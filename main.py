import os
import subprocess
from config import *
from filldata import data


class BotTemplate:

    def __init__(self, foldername='NewBot', utils=True, gitpack=False) -> None:
        self.name = foldername
        self.utils = utils
        self.pack = gitpack
        

    def create_template(self):
        os.makedirs(f'{self.name}')
        
        self.create_main()
        self.create_config()
        self.create_utils()
        self.create_menu()
        self.create_data()
        self.create_venv()

        if self.pack:
            self.create_license()
            self.create_readme()

    def create_main(self):
        with open(f'{self.name}/main.py', 'w') as main:
            main.write(main_text)
            main.flush()
            main.close()

    def create_config(self):
        with open(f'{self.name}/config.py', 'w') as config:
            config.write(config_text)
            config.close()

    def create_utils(self):
        if self.utils == True:
            os.makedirs(f'{self.name}/utils')
            with open(f'{self.name}/utils/__init__.py', 'w') as initial:
                initial.write(initial_text)
                initial.close()

            with open(f'{self.name}/utils/states.py', 'w') as state:
                state.write(state_text)
                state.close()

    def create_menu(self):
        os.makedirs(f'{self.name}/menu')
        with open(f'{self.name}/menu/base_model.py', 'w') as base_m:
            base_m.write(base_model_text)
            base_m.close()

        with open(f'{self.name}/menu/mainkb.py', 'w') as main_kb:
            main_kb.write(main_kb_text)
            main_kb.close()

    def create_data(self):
        os.makedirs(f'{self.name}/data')
        with open(f'{self.name}/data/base_creation.py', 'w') as db:
            db.write('#Your Database Here')
            db.close()

    def create_venv(self):
        os.makedirs(f'{self.name}/venv')
        subprocess.run(['python', '-m', 'venv', f'{self.name}/venv'])

    def create_license(self):
        with open(f'{self.name}/LICENSE.txt', 'w') as lic:
            lic.write(license_text)
            lic.close()

    def create_readme(self):
        with open(f'{self.name}/README.md', 'w') as rm:
            rm.write(readme_text)
            rm.close()


bot = BotTemplate(data['botname'], data['utils'], data['gitpack'])
bot.create_template()
