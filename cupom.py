# coding: utf-8

from datetime import datetime

class Endereco:
  
  def __init__(self, logradouro, numero, complemento, bairro, municipio, 
      estado, cep):
    self.logradouro = logradouro
    self.numero = numero
    self.complemento = complemento
    self.bairro = bairro
    self.municipio = municipio
    self.estado = estado
    self.cep = cep

  def validar_campos_obrigatorios(self):

    if not self.logradouro:
        raise Exception("O campo logradouro do endereço é obrigatório")

    if not self.municipio:
        raise Exception("O campo município do endereço é obrigatório")  

    if not self.estado:
        raise Exception("O campo estado do endereço é obrigatório")
  
  def dados_endereco(self):

    self.validar_campos_obrigatorios()

    logradouro = self.logradouro + ", "

    numero = "s/n" if not self.numero or self.numero == 0 else str(self.numero)

    complemento = self.complemento if self.complemento else ""

    complemento = " " + complemento if self.complemento else complemento

    bairro = self.bairro + " - " if self.bairro else ""

    municipio = self.municipio + " - "

    cep = "CEP:" + self.cep if self.cep else ""

    return (f"""{logradouro}{numero}{complemento}
{bairro}{municipio}{self.estado}
{cep}""")

class Venda:

  def __init__(self, loja, dataHora, ccf, coo):

    self.loja = loja
    self.dataHora = dataHora
    self.ccf = ccf
    self.coo = coo

  def validar_campos_obrigatorios(self):

    if not self.loja:
      raise Exception ("Informe uma loja válida")

    if not self.dataHora:
      raise Exception ("Data e hora são obrigatórios")

    if not self.ccf:
      raise Exception ("O campo ccf é obrigatório")

    if not self.coo:
      raise Exception ("O campo coo é obrigatório")

  def dados_venda(self):

    self.validar_campos_obrigatorios()

    texto_data = self.dataHora.strftime("%d%m%Y")
    texto_hora = self.datahora.time().strftime("%H:%M:%S")
    _ccf = "CCF:" + self.ccf
    _coo = "COO:" + self.coo
    return (f"""{texto_data}{texto_hora}{_ccf}{_coo}""")

 
class Loja:
  
  def __init__(self, nome_loja, endereco, telefone, observacao, cnpj, 
      inscricao_estadual):
    self.nome_loja = nome_loja
    self.endereco = endereco
    self.telefone = telefone
    self.observacao = observacao
    self.cnpj = cnpj
    self.inscricao_estadual = inscricao_estadual
    

  def validar_campos_obrigatorios(self):

    if not self.nome_loja:
      raise Exception("O campo nome da loja é obrigatório")
 
    if not self.cnpj:
      raise Exception("O campo CNPJ da loja é obrigatório")
 
    if not self.inscricao_estadual:
      raise Exception("O campo inscrição estadual da loja é obrigatório")

  def dados_loja(self):

    self.validar_campos_obrigatorios()

    texto_endereco = self.endereco.dados_endereco()

    telefone = "Tel " + self.telefone if self.telefone else ""

    telefone = " " + telefone if self.endereco.cep and self.telefone else telefone

    observacao = self.observacao if self.observacao else ""

    cnpj = "CNPJ: " + self.cnpj

    inscricao_estadual = "IE: " + self.inscricao_estadual


    return (f"""{self.nome_loja}
{texto_endereco}{telefone}
{observacao}
{cnpj}
{inscricao_estadual}""")
     
