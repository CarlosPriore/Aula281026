class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
      self.__nome = nome
      self.__idade = idade


    @property
    def nome(self) -> str:
        """Getter: acesso ao __nome"""
        return self.__nome

    @property
    def idade(self) -> int:
        """Getter: acesso a __idade"""
        print("Passou no getter de idade")
        return self.__idade

    @idade.setter
    def idade(self, valor:int) -> None:
        """Setter: muda o valor de __idade"""
        print("Passou no setter de idade")

        if valor < 0:
            raise TypeError("Idade impossivel")

        if valor > 100:
             raise TypeError("Voce esta mentindo")




p = Pessoa("teste novo", 100)
print("Qual sera a idade dessa pessoa?")
print(p.idade)
p.idade = 50
print("Qual sera a idade dessa pessoa?")
print(p.idade)