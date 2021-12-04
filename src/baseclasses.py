import yaml

class Material():

    def __init__(self, name):
        self.name = name


    @staticmethod
    def get_property(self):
        pass
        #material_source = './materials.yaml'
        #with open(material_source, 'r'):


if __name__ == '__main__':

    material_source = 'D:/repositories/fatiguepy/src/database/materials.yaml'
    with open(material_source, 'r') as materials_database:
        material = yaml.load(materials_database, Loader=yaml.FullLoader)

    print(materials_database)