import requests
import argparse
import concurrent.futures

def test_url(url, dir):
    test_url = url+"/"+dir
    try:
        r = requests.get(test_url)
        if r.status_code == 200:
            print("[*] Encontrado: ", test_url)
    except:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BruteEvolve1.0 - Teste de diretórios")
    parser.add_argument("url", help="URL do site ou aplicação web")
    parser.add_argument("wordlist", help="Caminho para a wordlist de diretórios ocultos")
    parser.add_argument("-s", "--silent", action="store_true", help="Modo silencioso")
    parser.add_argument("-t", "--threads", type=int, default=1, help="Número de threads")
    args = parser.parse_args()

    url = args.url
    wordlist = args.wordlist
    silent = args.silent
    threads = args.threads

    if not silent:
        print("[*] Iniciando a varredura em", url)
        print("[*] Usando a wordlist", wordlist)
        print("[*] Usando", threads, "threads")

    with open(wordlist, "r") as f:
        dirs = f.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for dir in dirs:
            futures.append(executor.submit(test_url, url, dir))
        
        for future in concurrent.futures.as_completed(futures):
            pass

    if not silent:
        print("[*] Varredura concluída")
