import re


class ExtratorUrl:

    def __init__(self, url):
        self.__url = self._sanitiza_url(url)
        self._valida_url()

    def _sanitiza_url(self, url):
        if type(url == str):
            return url.strip()
        else:
            return ""

    def _valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

        padrao_url = re.compile('(http(s)?://)?(www.)?alura.com(.br)?/')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida!")

    def buscar_parametro(self, parametro):
        if parametro not in self.parametros:
            raise ValueError("O parâmetro nao está presente na URL!")

        indice_parametro = self.parametros.find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.parametros.find('&', indice_valor)
        if indice_e_comercial == -1:
            return self.parametros[indice_valor]
        else:
            return self.parametros[indice_valor:indice_e_comercial]

    def __str__(self):
        return f'URL completa: {self.url} ' \
               f'\nURL base: {self.base} ' \
               f'\nURL parâmetros: {self.parametros} ' \
               f'\nTamanho URL: {len(self)}'

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    @property
    def url(self):
        return self.__url

    @property
    def base(self):
        if '?' not in self.url:
            return self.__url
        else:
            posicao_interrogacao = self.url.find('?')
            return self.url[:posicao_interrogacao]

    @property
    def parametros(self):
        if '?' not in self.url:
            return ""
        else:
            posicao_interrogacao = self.url.find('?')
            return self.url[posicao_interrogacao + 1:]


url_alura = ExtratorUrl("https://alura.com.br/search?query=python&theme=dark")
url_alura2 = ExtratorUrl("https://alura.com.br/search?query=python&theme=dark")
print(url_alura, end="\n\n")
print(f'Parametros da URL: {url_alura.parametros}')
print(f'Valor do parametro "query" na URL: {url_alura.buscar_parametro("query")}')
print(f'Verificando igualdade de dois objetos: {url_alura == url_alura2}')
