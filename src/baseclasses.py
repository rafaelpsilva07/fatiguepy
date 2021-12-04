import yaml
import os

class Material():

    def __init__(self, name):
        self.name = name
        self.sigma_0 = None
        self.sigma_u = None
        self.gamma = None


    def get_material_properties(self):
        '''set material properties values '''
        dir = os.path.dirname(__file__)
        material_source = os.path.join(dir, 'database/materials.yaml')

        with open(material_source, 'r') as materials_database:
            materials = yaml.load(materials_database, Loader=yaml.FullLoader)

        self.sigma_0 = materials[self.name]['sigma_0']
        self.sigma_u = materials[self.name]['sigma_u']
        self.gamma = materials[self.name]['gamma']

        return None



if __name__ == '__main__':

    dir = os.path.dirname(__file__)
    material_source = os.path.join(dir, 'database/materials.yaml')
    with open(material_source, 'r') as materials_database:
        material = yaml.load(materials_database, Loader=yaml.FullLoader)
        materials_database.close()
    
    print(material)
    dir = os.path.dirname(__file__)
    material = os.path.join(dir, 'materials.yaml')
    print(material)

    mat = Material('SAE 4130 St, Norm')
    mat.get_material_properties()
    print(mat.sigma_0)