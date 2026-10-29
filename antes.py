class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        self.__nome = nome
        self.__idade = idade


    def mostrar_idade(self) -> int:
        return self.__idade



p + Pessoa("Teste", 100)
print("qual era a idade da pessoa?")
# print(p.__idade)
print(p.mostrar_idade())