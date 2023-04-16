# BruteEvolve1.0

BruteEvolve1.0 é uma ferramenta de teste de diretórios para sites ou aplicações web. Ela utiliza uma lista de diretórios ocultos e faz uma varredura em uma URL especificada para encontrar diretórios ocultos.

## Como usar

Para usar a ferramenta, você precisa ter o Python 3.x instalado em sua máquina. Em seguida, execute o seguinte comando em um terminal:


### Argumentos

- `URL`: a URL do site ou aplicação web que você deseja varrer.
- `wordlist`: o caminho para o arquivo de wordlist de diretórios ocultos que você deseja utilizar.
- `-s` ou `--silent`: opcional, define o modo silencioso, sem saída no terminal.
- `-t` ou `--threads`: opcional, define o número de threads a serem utilizados na varredura.

## Exemplo

Para varrer um site com a URL `http://example.com` utilizando a wordlist `wordlist.txt` com 4 threads, você executaria o seguinte comando:

python BruteEvolve1.0.py <URL> <wordlist> [-s] [-t <threads>]
  # usando threads
  python BruteEvolve1.0.py http://example.com wordlist.txt -t 4
  
## Observação

Esta é uma ferramenta de teste de diretórios e não deve ser utilizada para fins maliciosos. O uso indevido desta ferramenta pode ser ilegal. Use por sua conta e risco.
#Feito por um amante de CTFS
