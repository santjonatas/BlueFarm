import requests

class ForDevsService:
    def validar_cpf(self, cpf):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        url = 'https://www.4devs.com.br/ferramentas_online.php'

        data = {
            'acao': 'validar_cpf',
            'txt_cpf': cpf,
        }

        try:
            response = requests.post(url, headers=headers, data=data)
            response.raise_for_status() 

            return response.text

        except requests.exceptions.RequestException as e:
            return f'Erro na requisição: {e}'
